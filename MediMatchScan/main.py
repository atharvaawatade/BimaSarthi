import os
import sys
def process_folder(folder_path):
import base64
import requests
from io import BytesIO
from PIL import Image
from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import time
import uuid

app = Flask(__name__)

# MongoDB setup
mongo_client = MongoClient("mongodb+srv://atharva2021:123@cluster0.so5reec.mongodb.net/")
db = mongo_client['bajaj']
collection = db['client']

# Function to encode the image to base64
def encode_image(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    encoded_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_string

# Chat function with Pixtral and MongoDB saving
def chat_with_pixtral(base64_img, mrn_number, user_question):
    api = "https://api.hyperbolic.xyz/v1/chat/completions"
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJyZzMyNzAyNEBnbWFpbC5jb20ifQ._frFve-BYZdb0Qo6FIj6xcDcxpY-6QlC2O-ToQxBjkc"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    payload = {
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_question},  
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_img}"},
                    },
                ],
            }
        ],
        "model": "mistralai/Pixtral-12B-2409",
        "max_tokens": 2048,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    response = requests.post(api, headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        if 'choices' in response_data:
            assistant_response = response_data['choices'][0]['message']['content']
        else:
            assistant_response = "Response format is incorrect"
    else:
        assistant_response = f"API request failed: {response.status_code} - {response.text}"

    # Generate a unique ID for the request
    unique_id = str(uuid.uuid4())

    # Save the result to MongoDB with the specified format
    document = {
        'mrn_number': mrn_number,
        'ocr_result': assistant_response,
        'unique_id': unique_id,
        'got_mode': "plain texts OCR",
        'timestamp': time.time()
    }

    collection.insert_one(document)

    return assistant_response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    image = request.files['image']
    mrn_number = request.form['mrn_number']
    user_question = request.form['user_question']

    img = Image.open(image)
    base64_img = encode_image(img)

    response = chat_with_pixtral(base64_img, mrn_number, user_question)
    return jsonify({'response': response})

def main():

if len(sys.argv) != 2: print("Usage: python main.py <folder_path>")

sys.exit(1)

folder_path = sys.argv[1]

process_folder(folder_path)

if_name main()
if __name__ == '__main__':
    app.run(debug=True)
