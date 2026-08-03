import streamlit as st
from src.parser import extract_text

st.set_page_config(
    page_title="AI Referral Finder",
    layout="wide"
)

st.title("🤖 AI Referral Finder & Outreach Assistant")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

if st.button("Analyze"):

    if resume:

        resume_text = extract_text(resume)

        st.subheader("Extracted Resume Text")

        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )

    else:
        st.warning("Please upload a resume.")