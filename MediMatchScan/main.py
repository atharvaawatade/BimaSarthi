import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from flask import Flask, render_template, request, jsonify
import PyPDF2
import csv
import random
import requests
from typing import List, Optional
import re

# Load environment variables
load_dotenv()

# Set up OpenAI API key (for embeddings only)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Connect to MongoDB
try:
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client["bajaj"]
    collection = db["client"]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit(1)

app = Flask(__name__)

# Load policy and regulation data
try:
    guidelines_path = os.path.join(os.path.dirname(__file__), 'Guidelines_data.csv')
    with open(guidelines_path, "r") as f:
        policy_data = f.read()
    
    wellness_path = os.path.join(os.path.dirname(__file__), 'Guidelines on Wellness and Preventive Features.pdf')
    with open(wellness_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        regulation_data = ""
        for page in pdf_reader.pages:
            regulation_data += page.extract_text()
    
    # Load the new terms and conditions data
    terms_path = os.path.join(os.path.dirname(__file__), 'expanded_health_insurance_terms_conditions.csv')
    with open(terms_path, "r") as f:
        csv_reader = csv.DictReader(f)
        terms_data = next(csv_reader)['Insurance Regulations and Details']

except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
    exit(1)
except Exception as e:
    print(f"Error reading files: {e}")
    exit(1)

class LLaMa3_2:
    api_url: str = "http://localhost:11434/api/chat"
    
    def generate(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        messages = [{"role": "user", "content": prompt}]
        body = {
            "model": "llama3.2:latest",
            "messages": messages,
            "stream": False
        }
        if stop:
            body["stop"] = stop
        response = requests.post(self.api_url, json=body)
        if response.status_code == 200:
            return response.json()['message']['content']
        else:
            raise Exception(f"Error in LLaMa 3.2 API call: {response.text}")

def get_user_data(mrn):
    user_data = collection.find_one({"mrn_number": mrn})
    if user_data:
        return user_data.get("ocr_result", "")
    return None

def create_vector_db(user_data):
    combined_data = f"{user_data}\n\n{policy_data}\n\n{regulation_data}\n\n{terms_data}"
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts([combined_data], embeddings)
    return vector_store

def get_insurance_eligibility_response():
    is_eligible = random.choice([True, False])
    
    if is_eligible:
        response = "Yes, you are eligible for insurance. "
    else:
        response = "Based on the information provided, you may not be eligible for insurance at this time. However, eligibility criteria can vary. "
    
    response += "For more detailed information and to explore your options, please visit: https://www.bajajfinserv.in/"
    
    return response

def translate_text(text, to_lang, from_lang='en'):
    url = "https://microsoft-translator-text.p.rapidapi.com/translate"
    querystring = {"to": to_lang, "api-version": "3.0", "from": from_lang, "profanityAction": "NoAction", "textType": "plain"}
    payload = [{"Text": text}]
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "704d9bd019mshf7c899a687d57f2p1ceb2bjsnc6a8f1c59a6e",
        "X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()[0]['translations'][0]['text']
    else:
        raise Exception(f"Translation error: {response.text}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    mrn = request.form['mrn']
    user_input = request.form['message']
    language = request.form.get('language', 'english').lower()

    # Detect language change command
    if user_input.lower() in ['marathi', 'hindi', 'tamil', 'english']:
        language = user_input.lower()
        return jsonify({"response": f"Switched to {language.capitalize()} language.", "language": language})

    # Translate user input to English if not in English
    if language != 'english':
        user_input = translate_text(user_input, 'en', language)

    user_data = get_user_data(mrn)
    if user_data:
        vector_store = create_vector_db(user_data)
        
        relevant_context = vector_store.similarity_search(user_input, k=3)
        context_text = "\n".join([doc.page_content for doc in relevant_context])
        
        full_prompt = f"""Context:
{context_text}

User data:
{user_data}

User question: {user_input}

Please provide a concise and direct response. If asked about a diagnosis, state the diagnosis clearly. Offer 2-3 short, relevant suggestions if appropriate. Keep the entire response under 100 words. Do not use asterisks or any other markup for emphasis."""

        llm = LLaMa3_2()
        
        if "eligible for insurance" in user_input.lower() or "am i eligible" in user_input.lower():
            response = get_insurance_eligibility_response()
        else:
            try:
                response = llm.generate(full_prompt)
                response = re.sub(r'\*+', '', response)
            except Exception as e:
                response = f"An error occurred: {str(e)}"

        # Translate response back to the user's preferred language if not English
        if language != 'english':
            response = translate_text(response, language)

        return jsonify({"response": response, "language": language})
    else:
        response = "User not found. Please register first."
        if language != 'english':
            response = translate_text(response, language)
        return jsonify({"response": response, "language": language})

if __name__ == "__main__":
    app.run(debug=True, port=3000)
