
import re
import PyPDF2

JOB_SKILLS = {
    "backend developer": ["python", "flask", "api", "sql"],
    "data analyst": ["python", "pandas", "sql", "analysis"],
    "ml engineer": ["machine learning", "tensorflow", "model"]
}

def extract_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def analyze_resume_pdf(pdf_file):
    text = extract_text(pdf_file)

    matched_roles = {}

    for role, skills in JOB_SKILLS.items():
        found = [skill for skill in skills if re.search(skill, text)]
        score = len(found)
        matched_roles[role] = {
            "matched_skills": found,
            "score": score
        }

    return {
        "analysis": matched_roles
    }
