import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

def get_resume_feedback(resume_text, jd_text=None):
    prompt = f"""
You are a resume review expert.
Analyze the following resume text and provide structured feedback in three sections:

1. **Bullet Point Improvements**: Rewrite unclear or weak points in a more effective, action-oriented way.
2. **Grammar and Formatting Suggestions**: Highlight grammar mistakes or formatting issues.
3. **Job Match Analysis**: Given this job description, identify what relevant skills are missing or need improvement.

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{jd_text if jd_text else 'N/A'}
\"\"\"

Respond in markdown format.
"""
    try:
        response = model.generate_content(prompt)

        # ✅ safer extraction instead of response.text
        if response.candidates and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text
        else:
            return "⚠️ No feedback generated. Try again with a different resume or JD."

    except Exception as e:
        return f"Gemini API Error: {e}"
