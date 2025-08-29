❄️ Snowwlder
AI-Powered Resume Assistant

“Stop guessing. Start matching. Let AI tell you how well your resume fits the job.”

Snowwlder is an AI-driven resume analyzer that helps you land jobs faster. It compares your resume with a job description, scores the match, highlights missing skills, and gives you actionable AI feedback — all in one click.

🚀 Why Snowwlder?

🔍 Tired of resume black holes? Recruiters use Applicant Tracking Systems (ATS) that scan for keywords. Snowwlder acts like your AI recruiter — boosting your chances by showing:

✅ How well your resume matches the JD

📊 Which skills/keywords you already have

❌ Which important ones are missing

💡 Smart AI tips to improve your resume

✨ Features

📂 Upload Resume (PDF)

📝 Paste Job Description

📊 ATS Match Score (semantic + keyword-based)

🔑 Keyword Insights (found & missing skills)

🤖 Gemini AI Feedback (summary, strengths, gaps, improvements)

🌐 Deployable on Streamlit Cloud

🖼️ Sneak Peek

⚙️ Tech Stack
Layer	Tech
Frontend	Streamlit
AI Engine	Google Gemini API
Text Extraction	pypdf
Similarity	Embeddings + Cosine Similarity
Keyword Insights	Custom NLP Matching
Config	dotenv / TOML secrets
📂 Project Structure
Snowwlder/
├── app.py               # 🎨 Streamlit UI
├── gemini_utils.py      # 🤖 Gemini API helpers
├── resume_utils.py      # 📂 Resume PDF utils
├── semantic_matcher.py  # 📊 Scoring engine
├── requirements.txt     # 📦 Dependencies
└── .env.example         # 🔑 API key template

⚡ Quickstart
1️⃣ Clone repo
git clone https://github.com/SUYASH2004/Snowwlder.git
cd Snowwlder

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Set API Key

Create a .env file:

GOOGLE_API_KEY="your_api_key_here"


Or on Streamlit Cloud → Settings → Secrets:

GOOGLE_API_KEY = "your_api_key_here"

4️⃣ Run locally
streamlit run app.py

🧠 How It Works

Extract Resume (PDF) → Extracts clean text from resume.

Semantic Match → Embeds resume & JD with Gemini embeddings.

Cosine Similarity → Calculates how close they are in meaning.

Keyword Insights → Finds top keywords found & missing.

Gemini Feedback → AI provides structured review:

Summary

Strengths

Gaps

Missing Keywords

Improvements

🌟 Example Output

Match Score: 0.82 / 1.0 ✅
Keywords Found: Python, Machine Learning, SQL
Missing Keywords: Cloud, Kubernetes, CI/CD

AI Feedback:

Strengths: Strong ML background, solid Python skills

Gaps: Cloud technologies not highlighted

Improvements: Add metrics for project outcomes, emphasize teamwork

👨‍💻 Author

Suyash Rane

💼 LinkedIn

🐙 GitHub

✉️ your.email@example.com

⚡ Snowwlder: Turning resumes into job-winning tools.
