import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

def get_resume_feedback(resume_text, jd_text = None):
    prompt = f"""

You are resume review expert.
Analyze the following resume text and provide structured feedback in three section:
1. **Bullet Point Improvements**:Rewrite unclear or weal points in a more effective, action-oriented way.

2.**Grammar and Formatting Suggestions**: Hoghlight grammar mistakes or formatting issues.

3. **Job Match Analysis**: Given This job description, identify whjat relevant skills are missing or need improvement.

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
        return response.text
    except Exception as e:
        return f"Gemini Api Error:{e}"
