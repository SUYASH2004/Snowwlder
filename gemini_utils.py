"""Gemini client helpers: configuration, embedding, and feedback generation."""
import os
from typing import List, Dict, Any

import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file if running locally
load_dotenv()

# Priority: Streamlit Cloud secrets > Local .env
_API_KEY = None
try:
    import streamlit as st
    _API_KEY = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
except Exception:
    _API_KEY = os.getenv("GOOGLE_API_KEY")

if not _API_KEY:
    raise RuntimeError(
        "❌ GOOGLE_API_KEY not found. "
        "Set it in a local .env file OR in Streamlit Cloud → Secrets."
    )

# Configure Gemini client
genai.configure(api_key=_API_KEY)

# Models
EMBED_MODEL = "text-embedding-004"
CHAT_MODEL = "gemini-1.5-flash"


def embed_text(text: str) -> List[float]:
    """Return embedding vector for text."""
    if not text.strip():
        return [0.0]
    resp = genai.embed_content(model=EMBED_MODEL, content=text)
    return resp.get("embedding", [])


def cosine_sim(a: List[float], b: List[float]) -> float:
    """Compute cosine similarity between two vectors."""
    import numpy as np
    va, vb = np.array(a), np.array(b)
    if va.size == 0 or vb.size == 0:
        return 0.0
    denom = (np.linalg.norm(va) * np.linalg.norm(vb))
    if denom == 0:
        return 0.0
    return float(np.dot(va, vb) / denom)


def llm_feedback(resume_text: str, jd_text: str) -> Dict[str, Any]:
    """Ask Gemini for structured resume feedback (returns JSON-like dict)."""
    model = genai.GenerativeModel(CHAT_MODEL)
    sys_msg = (
        "You are an expert resume reviewer. Given a resume and a job description, "
        "produce actionable, concise feedback. Return JSON with keys: "
        "summary, strengths, gaps, missing_keywords, improvements."
    )

    user_msg = f"""
    <resume>
    {resume_text[:18000]}
    </resume>

    <job_description>
    {jd_text[:8000]}
    </job_description>
    """

    resp = model.generate_content([{"role": "user", "parts": [sys_msg, "\n\n", user_msg]}])

    import json
    txt = resp.text or ""
    try:
        txt = txt.strip().strip("` ")
        if txt.startswith("json"):
            txt = txt[4:]
        data = json.loads(txt)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    # Fallback if JSON parsing fails
    return {
        "summary": txt[:500],
        "strengths": [],
        "gaps": [],
        "missing_keywords": [],
        "improvements": [],
    }
