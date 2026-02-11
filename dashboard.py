
import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("AI Resume Analyzer & Job Matcher")

uploaded_file = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_file:
    files = {"resume": uploaded_file.getvalue()}
    response = requests.post("http://127.0.0.1:5000/analyze", files={"resume": uploaded_file})

    if response.status_code == 200:
        data = response.json()["analysis"]

        st.subheader("Job Match Results")
        for role, details in data.items():
            st.markdown(f"### {role.title()}")
            st.write("Matched Skills:", details["matched_skills"])
            st.write("Score:", details["score"])
            st.progress(details["score"] / 4)
    else:
        st.error("Error analyzing resume")
