# 📄 Snowwlder: AI-Powered Resume Assistant  

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)  
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-brightgreen)  
![Google Gemini](https://img.shields.io/badge/Google-Gemini-yellow)  

---

## ✨ Overview
**Snowwlder** is an AI-powered resume assistant that helps job seekers **analyze and optimize their resumes** against job descriptions.  
It uses **Google Gemini embeddings** for semantic similarity and provides **AI-generated feedback** on strengths, gaps, and missing keywords.  

---

## 🚀 Features
- ✅ **AI-Powered Feedback** on resumes  
- ✅ **Resume–JD Match Score** using embeddings + keywords  
- ✅ **Keyword Analysis** to detect missing skills  
- ✅ **Deployed on Streamlit Cloud** for instant use  

---

## 📂 Project Structure
```bash
snoww-assistant/
│── app.py                # Streamlit main app  
│── gemini_utils.py       # Gemini API utilities  
│── semantic_matcher.py   # Resume–JD similarity  
│── resume_utils.py       # Resume PDF text extraction  
│── requirements.txt      # Dependencies  
│── README.md             # Project docs  

⚡ **Installation**

Clone the repository and install dependencies:

git clone https://github.com/SUYASH2004/Snowwlder.git
cd Snowwlder
pip install -r requirements.txt

▶️ **Run the App**
streamlit run app.py

🔑 **Environment Setup**

Create a .env file in the root directory with your Google Gemini API key:

GOOGLE_API_KEY="your_api_key_here"


If using Streamlit Cloud, set the secret in:
Settings → Secrets → GOOGLE_API_KEY

📊 **Example Output**

Match Score: 0.82 / 1.0

Found Keywords: Python, Machine Learning, Data Analysis

Missing Keywords: SQL, TensorFlow

AI Feedback: Improve project descriptions, add measurable impact

Built with passion by SUYASH2004

