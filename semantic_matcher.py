import os
from dotenv import load_dotenv
import google.generativeai as genai
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
genai.configure(api_key= os.getenv("GEMINI_API_KEY"))
embed_model = genai.GenerativeModel("embedding-001")

def get_embedding(text: str):
    try:
        response = genai.embed_content(
            model="models/embedding-001",
            content = text,
            task_type="retrieval_document"
        )
        return np.array(response["embedding"])
    except Exception as e:
        print(f"Error Embedding: {e}")
        return None
    
def calculate_match_score(resume_text: str, jd_text: str):
    resume_embed = get_embedding(resume_text)
    jd_embed = get_embedding(jd_text)

    if resume_embed is None or jd_embed is None:
        return None, "Error generating embeddings"
    
    score = cosine_similarity([resume_embed], [jd_embed])[0][0]
    return round(score *100,2), None
