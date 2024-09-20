# BimaSarthi - AI-Powered Medical Diagnosis Extraction and Insurance and medical Assistance 🏥💡
![MediMatchBot 1](https://github.com/user-attachments/assets/e6307b89-002f-4ec1-bd1f-9fc0b3eef6ab)


## Overview
*BimaSarthi* is an AI-driven solution designed to digitize handwritten medical forms by extracting medical diagnoses and streamlining insurance claim processes with recommendations. By enhancing Optical Character Recognition (OCR) 📝, active learning 🔄, and advanced AI models like GPT-3.5 🧠, BimaSarthi improves diagnosis extraction accuracy and adapts based on user feedback. It provides real-time suggestions and user assistance through an integrated chatbot 💬, simplifying interactions between patients and insurance providers for efficient and accurate claim submission.

BimaSarthi also supports regional languages 🌐, offers natural language summarization of diagnoses 🧠, and includes an eligibility checker ✅ that verifies whether the diagnosis is covered by the user’s healthcare policy. This solution is designed with accessibility, automation, and user-centric features, creating a seamless and intelligent experience for users and insurance companies alike.

## Key Features 🔑
- *OCR-Based Medical Diagnosis Extraction* 📝: Leverages OCR technology combined with AI models to accurately extract diagnoses from handwritten medical forms.
- *Real-Time Feedback Loop* 🔄: The system learns from user edits, continuously improving OCR accuracy with active learning.
- *Natural Language Summarization* 🧠: Simplifies complex medical diagnoses into layman's terms using GPT-3.5, improving user understanding.
- *Insurance Eligibility Checker* ✅: Automatically verifies if the extracted diagnosis is covered under the user’s healthcare plan, streamlining the claim process.
- *Chatbot Integration* 💬: Provides real-time assistance and recommendations related to healthcare insurance and diagnosis.

## Tech Stack 🛠
- *Database* 🗄: 
  - Vector Database (MongoDB)
- *Backend* 🔧:
  - Pytesseract (OCR)
  - Torch, Transformers (AI Models)
  - OpenAI GPT-3.5 (NLP)
  - Framework: Flask/FastAPI
- *Frontend* 💻:
  - HTML/CSS, JavaScript
  - Gradio (Interactive UI)
- *Other Tools* 🧰:
  - Pillow (Image Processing)
  - Active Learning Loop (Real-Time Feedback)
  - Multilingual Model Support (Regional Language Support)
  - Libraries: requests, base64, io
 
![GUI-Pixtral_OCR_DATAFLOW](https://github.com/user-attachments/assets/d423413a-9954-4dd9-ba91-e3b1c78c3f3c)


### Context-Aware OCR Tech Stack:
- *Large Language Model Used*: Pixtral 12B (12 Billion Parameter Multimodal Model with a 400 Million Parameter Vision Encoder)
- *API*: Hyperbolic v1 Chat Completion API

## How BimaSarthi Works 🏥
1. *Upload Medical Form* 📄: Users upload scanned images of handwritten medical forms.
2. *OCR Extraction* 📝: The system uses OCR to extract medical diagnoses from the uploaded form.
3. *Real-Time Feedback* 🔄: Users can review and edit the extracted data, with the system learning from corrections for improved accuracy.
4. *Natural Language Summarization* 🧠: Extracted diagnoses are simplified into layman’s terms using GPT-3.5 for better user understanding.
5. *Insurance Eligibility Check & Recommendations* ✅: The system cross-references the diagnosis with the user’s healthcare plan to check claim eligibility and provide recommendations.
6. *Data Submission* 📥: The diagnosis data, along with metadata (e.g., MRN and date), is stored in a vector database for future reference and chatbot interactions.
7. *End-to-End Solution* 🔄: From form scanning to claim processing, BimaSarthi offers a seamless, fully integrated experience.

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
3. *Simplified Diagnosis Explanation*: GPT-3.5 delivers a simplified summary of the medical diagnosis, aiding in user comprehension.
4. *Insurance Eligibility Verification*: The system verifies claim eligibility by cross-referencing the diagnosis with the user's healthcare plan.
