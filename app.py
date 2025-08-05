import streamlit as st
from resume_utils import extract_text_from_pdf
from gemini_utils import get_resume_feedback
from semantic_matcher import calculate_match_score

st.set_page_config(page_title = "Snowwlder", layout ="centered")
st.title("Snowwlder")


st.header("1. Upload Resume")
resume_file = st.file_uploader("Upload Your Resume PDF ", type = ["pdf"])

st.header("2. Provide Job Description")
jd_mode = st.radio ("Would you like to provide job Description?", ["Upload PDF", "Paste-Text"])

jd_text = ""
if jd_mode == "Upload PDF":
    jd_file = st.file_uploader("Upload Job Description PDF", type =["pdf"])
    if jd_file:
        jd_text = extract_text_from_pdf(jd_file)
elif jd_mode == "Paste-Text":
    jd_text = st.text_area("Paste Your Job Description Here", height=200)
    



if resume_file:
    resume_text = extract_text_from_pdf(resume_file)
    st.subheader("Extracted Resume Text ")
    st.text_area("Resume Content", resume_text[:3000], height=200)

if jd_mode: 

    st.subheader("Extracted JD Text")
    st.text_area("Job Desc Content", jd_text[:3000], height=200)

if resume_file and (jd_text or jd_mode == "Paste-Text"):
    if st.button("Analyze Resume with Snowwlder"):
        with st.spinner("Analyze with Gemini....."):
            feedback = get_resume_feedback(resume_text, jd_text)
            st.subheader("AI Resume Feedback")
            st.markdown(feedback)

if resume_file and jd_text:
    st.header("Resume-JD Macth Score")
    with st.spinner("Calculating Similarity...."):
        match_score, error = calculate_match_score(resume_text, jd_text)

        if error:
            st.error(error)

        else:
            st.success(f"Score: {match_score}%")
            if match_score>80:
                st.info("Excellent Score")

            elif match_score>60:
                st.info("Moderate Score")

            else:
                st.warning("Low Match, Need Improvements")

