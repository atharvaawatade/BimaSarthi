import os
from dotenv import load_dotenv
from pymongo import MongoClient
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from flask import Flask, render_template, request, jsonify
import PyPDF2
import csv
import random

# Load environment variables
load_dotenv()

# Set up OpenAI API key
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

def create_chatbot(vector_store):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    qa = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return qa

def get_insurance_eligibility_response():
    # Randomly choose Yes or No for demonstration purposes
    is_eligible = random.choice([True, False])
    
    if is_eligible:
        response = "Yes, you are eligible for insurance. "
    else:
        response = "Based on the information provided, you may not be eligible for insurance at this time. However, eligibility criteria can vary. "
    
    response += "For more detailed information and to explore your options, please visit: https://www.bajajfinserv.in/"
    
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    mrn = request.form['mrn']
    user_input = request.form['message']

    user_data = get_user_data(mrn)
    if user_data:
        vector_store = create_vector_db(user_data)
        chatbot = create_chatbot(vector_store)
        
        if "eligible for insurance" in user_input.lower() or "am i eligible" in user_input.lower():
            response = get_insurance_eligibility_response()
        elif "diagnosis" in user_input.lower():
            question = f"Based on the user's medical records, what is their diagnosis? Please provide a detailed explanation."
            chat_response = chatbot.invoke({"question": question})
            response = chat_response['answer']
        else:
            chat_response = chatbot.invoke({"question": user_input})
            response = chat_response['answer']

        return jsonify({"response": response})
    else:
        return jsonify({"response": "User not found. Please register first."})

if __name__ == "__main__":
    app.run(debug=True)
