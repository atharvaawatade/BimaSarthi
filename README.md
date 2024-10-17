# BimaSarthi - AI-Powered Medical Diagnosis Extraction and Insurance and medical Assistance 🏥💡
# Hosting Link : https://bima-sarthi-home.vercel.app/
# Testing API : https://medi-match-scan.vercel.app/api/test

This example demonstrates how to send an image to the hosted API using Python's `requests` library.

```python
import requests

# Define the hosted API endpoint
url = "https://medi-match-scan.vercel.app/api/test"

# Path to the image you want to test with
image_path = "C:/Users/Asus/Desktop/apitestbimasarthi/image/sample_1.png"

# Open the image file in binary mode and send a POST request
with open(image_path, "rb") as image_file:
    files = {"image": image_file}
    response = requests.post(url, files=files)

# Print the response
try:
    print("Response:", response.json())  # Prints JSON response if available
except ValueError:
    print("Response is not in JSON format. Here is the raw response:")
    print(response.text)  # Print the raw response text if JSON decoding fails
```

![image](https://github.com/user-attachments/assets/c38eba1b-abb4-4bc2-ada7-8824663f61f7)
![image](https://github.com/user-attachments/assets/f2d51282-cce1-4331-9b32-9e840703a705)



![MediMatchBot 1](https://github.com/user-attachments/assets/e6307b89-002f-4ec1-bd1f-9fc0b3eef6ab)


## Overview
*BimaSarthi* is an AI-driven solution designed to digitize handwritten medical forms by extracting medical diagnoses specifically "provisional diagnosis"  by creating an effective Optical Character Recognition (OCR) 📝 platform based on active learning 🔄, advanced language and vision models 🧠. It also provides user assistance through an integrated chatbot 💬, simplifying interactions between patients and insurance providers for efficient and accurate claim submission.




BimaSarthi also supports regional languages  in future enhancement🌐, offers natural language summarization of diagnoses 🧠, and includes an eligibility checker ✅ that verifies whether Bajaj Finserv's healthcare policy covers the diagnosis. This solution is designed with accessibility, automation, and user-centric features, creating a seamless and intelligent experience for users and insurance companies alike.

## Key Features 🔑
- *OCR-Based Medical Diagnosis Extraction* 📝: Leverages open-source and localised OCR technology combined with LLM models to accurately extract diagnoses from handwritten medical forms.
- *Transparent Approach*: The entire system has been created using open-source and free resources.
- *Production Friendly: The entire system has been made by taking into consideration the computational costs it takes to deploy such a system.
- *Natural Language Summarization* 🧠: Simplifies complex medical diagnoses into layman's terms using Llama-3.2-3B-Instruct, improving user understanding.
- *Insurance Eligibility Checker* ✅: Automatically verifies if the extracted diagnosis is covered under the user’s healthcare plan, streamlining the claim process.
- *Chatbot Integration* 💬: Provides  assistance and recommendations related to healthcare insurance and diagnosis.

## Tech Stack 🛠
- *Database* 🗄: 
  - Vector Database(FAISS)
  - Database (MongoDB)
- *Backend* 🔧:
  - Torch, Transformers, Vision Model(Florence-2-Large-Finetuned)
  - Llama-3.2-3B-Instruct (NLP LLM)
  - Framework: Flask,FastAPI,Uvicorn,Ngrok
- *Frontend* 💻:
  - HTML/CSS, JavaScript,Typescript
  - Gradio (Interactive UI)
- *Other Tools* 🧰:
  - Pillow (Image Processing)
  - Active Learning Loop (Real-Time Feedback)
  - Multilingual Model Support (Regional Language Support)
  - Libraries: requests, base64, io
 
## OCR detection model : microsoft/Florence-2-large-ft

![WhatsApp Image 2024-09-21 at 00 02 24_7a33d654](https://github.com/user-attachments/assets/00c1e1af-6f1f-4020-976e-764456b01c18)

Output in csv format as well ( We have saved all 30 sample data in output.csv file present in MediMatchScan ) :

![image](https://github.com/user-attachments/assets/7eaae952-a1df-4084-be86-f601bfebe864)

## How BimaSarthi Works 🏥
1. *Upload Medical Form* 📄: Users upload scanned images of handwritten medical forms.
2. *OCR Extraction* 📝: The system uses OCR to extract medical diagnoses from the uploaded form.
3. *Insurance Eligibility Check & Recommendations* ✅: The system cross-references the diagnosis with the user’s healthcare plan to check claim eligibility and provide recommendations.
4. *Data Submission* 📥: The diagnosis data, along with metadata (e.g., MRN and date), is stored in a vector database for future reference and chatbot interactions.
5. *End-to-End Solution* 🔄: From form scanning to claim processing, BimaSarthi offers a seamless, fully integrated experience.

## Future Enhancements 🔮
- *AI-Powered Fraud Detection* 🚨: Implement machine learning models to detect fraudulent claims by identifying anomalies in diagnosis and insurance data.
- *Voice-Based Interaction* 🎙: Introduce voice recognition for the chatbot, enhancing accessibility through voice commands.
- *Blockchain for Data Security* 🔐: Use blockchain technology to secure and verify medical data, ensuring trust for both users and insurers.
- *Integration with Hospital Systems* 🏥: Connect to electronic health records (EHRs) for automatic diagnosis data import, reducing manual entry.
- *Multi-Language Support* 🌐: Supports regional languages like Hindi and Marathi, enhancing accessibility for a broader user base.

## Challenges & Risks ⚠
- *OCR Accuracy with Poor Handwriting* ✍: Inconsistent or poor handwriting may reduce OCR accuracy, leading to incomplete extractions.
- *Data Privacy Compliance* 🔒: Handling sensitive medical and insurance data requires strict adherence to privacy regulations and standards.
- *Integration with External Systems* 🔗: Dependence on third-party systems like insurance databases and EHRs could pose integration challenges.

## Acceptance Criteria Coverage 🎯
BimaSarthi successfully addresses all key aspects of the problem statement, including:
1. *Accurate Diagnosis Extraction*: Uses advanced OCR and deep learning models for accurate handwritten diagnosis extraction.
2. *User-Friendly Output and Editing*: Provides real-time editing and feedback options to enhance accuracy and user interaction.
3. *Insurance Eligibility Verification*: The system verifies claim eligibility by cross-referencing the diagnosis with the user's healthcare plan.
