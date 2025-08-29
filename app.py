import streamlit as st

# 🔹 Page config MUST be the first Streamlit command
st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="📄",
    layout="wide"
)

# Other imports AFTER set_page_config
import json
from datetime import datetime

from resume_utils import extract_text_from_pdf, normalize_text
from semantic_matcher import compute_match
from gemini_utils import llm_feedback


# -------------------------------
# 🔹 App Header
# -------------------------------
st.title("📄 AI-Powered Resume Assistant")
st.caption("Analyze your resume against a job description. Powered by Google Gemini.")


# -------------------------------
# 🔹 Sidebar: About
# -------------------------------
with st.sidebar:
    st.header("How it works")
    st.markdown(
        "Upload a PDF resume and paste a JD. We compute semantic similarity using "
        "Gemini embeddings and show keyword coverage. Gemini also provides "
        "actionable feedback."
    )
    st.markdown("**Privacy:** Your data is processed only for this session.")


# -------------------------------
# 🔹 Inputs
# -------------------------------
uploaded = st.file_uploader(
    "Upload your resume (PDF)", type=["pdf"]
)  # UploadedFile

jd_text = st.text_area(
    "Paste the Job Description",
    height=220,
    placeholder="Paste the role, responsibilities, and required skills here…",
)

analyze = st.button("Analyze Resume ▶", type="primary", use_container_width=True)


# -------------------------------
# 🔹 Resume Analysis
# -------------------------------
if analyze:
    if not uploaded:
        st.error("⚠️ Please upload a PDF resume.")
        st.stop()
    if not jd_text or not jd_text.strip():
        st.error("⚠️ Please paste a Job Description.")
        st.stop()

    # Extract text from resume
    resume_text = extract_text_from_pdf(uploaded)
    resume_text = normalize_text(resume_text)

    # Compute similarity score (dict-based return)
    match_result = compute_match(resume_text, jd_text)

    match_score = match_result["final_score"]
    keywords_found = match_result["matched_keywords"]
    keywords_missing = match_result["missing_keywords"]

    # Get AI-powered feedback
    feedback = llm_feedback(resume_text, jd_text)

    # -------------------------------
    # 🔹 Results Display
    # -------------------------------
    st.subheader("✅ Resume–JD Match Results")
    st.metric("Match Score", f"{match_score:.2f} / 1.0")

    st.write("**Keywords Found:**", ", ".join(keywords_found) or "None")
    st.write("**Missing Keywords:**", ", ".join(keywords_missing) or "None")

    st.divider()

    st.subheader("🤖 Gemini Feedback")
    st.write("**Summary:**", feedback.get("summary", ""))

    col1, col2 = st.columns(2)
    with col1:
        st.write("**Strengths:**")
        st.write("\n".join(feedback.get("strengths", [])) or "No strengths detected.")
    with col2:
        st.write("**Gaps:**")
        st.write("\n".join(feedback.get("gaps", [])) or "No gaps detected.")

    st.write("**Missing Keywords (AI perspective):**")
    st.write(", ".join(feedback.get("missing_keywords", [])) or "None")

    st.write("**Improvements Suggested:**")
    st.write("\n".join(feedback.get("improvements", [])) or "None")
