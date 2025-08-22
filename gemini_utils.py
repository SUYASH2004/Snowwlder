import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-pro")

def get_resume_feedback(resume_text, jd_text=None):
    prompt = f"""
You are a professional resume reviewer.
Your job is to provide clear and useful resume feedback.

Please respond ONLY in the following structured format:

### Bullet Point Improvements
- Suggest improvements to unclear or weak points.

### Grammar and Formatting Suggestions
- Point out grammar mistakes or formatting issues.

### Job Match Analysis
- Compare with this job description: {jd_text if jd_text else 'N/A'}
- Highlight missing or weak skills.

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "max_output_tokens": 1024,  # ensure enough space for output
                "temperature": 0.7,         # balance creativity with focus
            }
        )

        # Debug log to see raw response in terminal
        print("DEBUG RESPONSE:", response)

        # Safe extraction
        if response.candidates and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "⚠️ No feedback generated. Try again with a different resume or JD."

    except Exception as e:
        return f"Gemini API Error: {e}"
