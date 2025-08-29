📄 Snowwlder — AI-Powered Resume Assistant

“Your AI career coach that matches resumes with job descriptions in seconds.”

Snowwlder is a Streamlit app powered by Google Gemini that helps job seekers analyze their resumes, get AI-driven feedback, and calculate resume–JD match scores using semantic embeddings.

✨ Features

📂 Upload Resume (PDF only)

📝 Paste Job Description

🤖 AI-Powered Feedback — strengths, gaps, missing keywords, improvements

📊 Match Score — semantic similarity (embeddings + keywords)

🌐 Deployed on Streamlit Cloud — runs in your browser, no installs needed

🖼️ Demo Screenshot

⚙️ Tech Stack

Streamlit
 — UI framework

Google Gemini API
 — embeddings + LLM feedback

pypdf
 — PDF text extraction

NumPy
 — cosine similarity

Python-dotenv
 — local secret management

🚀 Getting Started
1️⃣ Clone repo
git clone https://github.com/SUYASH2004/Snowwlder.git
cd Snowwlder

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your API key

Create a .env file:

GOOGLE_API_KEY="your_api_key_here"


Or in Streamlit Cloud, go to Settings → Secrets and paste:

GOOGLE_API_KEY = "your_api_key_here"

4️⃣ Run locally
streamlit run app.py

🧠 How It Works

Extract Resume → PDF text extracted via pypdf.

Embed & Compare → Both resume & JD embedded using Gemini’s text-embedding-004.

Cosine Similarity → Computes semantic similarity.

Keyword Overlap → Finds top skills/keywords matched vs missing.

LLM Feedback → Gemini gives structured feedback (summary, strengths, gaps, improvements).

📂 Project Structure
/Snowwlder
├── app.py               # Streamlit app
├── gemini_utils.py      # Gemini API helpers
├── resume_utils.py      # Resume text extraction + preprocessing
├── semantic_matcher.py  # Similarity + keyword scoring
├── requirements.txt     # Dependencies
└── .env.example         # Template env file (no secrets)

🌟 Example Output

Match Score: 0.78 / 1.0
Keywords Found: Python, Machine Learning, SQL
Missing Keywords: Kubernetes, Cloud, CI/CD

AI Feedback:

Strengths: Strong data analysis background, clear project impact

Gaps: Limited cloud experience

Improvements: Add measurable outcomes for each project

🧑‍💻 Author

Suyash Rane

💼 LinkedIn :- https://www.linkedin.com/in/suyash-rane-4aaa84258/

📧 ranesuyash2004@gmail.com

🌟 Always building AI + Web apps

⚡ Snowwlder is your personal AI recruiter — making resumes shine, one match at a time.
