# This is the BRAIN of the system.
# It contains all the NLP and ML logic — parsing, vectorising, and matching.

import re
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from job_data import JOB_ROLES


# ─────────────────────────────────────────────
# STEP 1: CLEAN THE RESUME TEXT
# ─────────────────────────────────────────────
def clean_text(text: str) -> str:
    """
    Convert raw resume text into clean, lowercase tokens.

    Why? TF-IDF treats 'Python', 'PYTHON', and 'python' as different words.
    Normalising ensures they all map to the same token.
    """
    text = text.lower()                          # lowercase everything
    text = text.replace('\n', ' ')               # remove newlines
    text = re.sub(r'[^\w\s/+#.-]', ' ', text)    # keep letters, digits, / + # (for C++, C#)
    text = re.sub(r'\s+', ' ', text).strip()     # collapse multiple spaces
    return text


# ─────────────────────────────────────────────
# STEP 2: EXTRACT SKILLS FROM THE RESUME
# ─────────────────────────────────────────────
def extract_skills(resume_text: str) -> list[str]:
    """
    Scan resume text and return a list of skills it contains,
    matched against ALL skills across ALL job roles.

    How it works:
    - Build one big master list of every known skill.
    - Check if each skill appears in the resume text as a whole word.
    """
    cleaned = clean_text(resume_text)

    # Collect every unique skill from all job roles
    all_skills = set()
    for role_data in JOB_ROLES.values():
        for skill in role_data["skills"]:
            all_skills.add(skill.lower())

    found_skills = []
    for skill in all_skills:
        # \b = word boundary → prevents "r" matching "react" or "java" matching "javascript"
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, cleaned):
            found_skills.append(skill)

    return sorted(found_skills)


# ─────────────────────────────────────────────
# STEP 3: BUILD TF-IDF VECTORS
# ─────────────────────────────────────────────
def build_tfidf_vectors(resume_text: str) -> tuple:
    """
    Convert resume and all job descriptions into TF-IDF vectors.

    What is TF-IDF?
    - TF (Term Frequency): How often a word appears in a document.
    - IDF (Inverse Document Frequency): Penalises common words like "the", "and".
    - Result: Important, unique words get high scores. Common words get low scores.

    Why cosine similarity?
    - We compare the angle between two vectors, not their size.
    - So a short resume vs. a long job description is still fairly compared.
    """
    # Build job "documents": combine skills + description for each role
    job_docs = []
    job_names = []
    for role_name, role_data in JOB_ROLES.items():
        # Joining skills as text gives TF-IDF more signal
        skill_text = ' '.join(role_data["skills"])
        full_doc = skill_text + ' ' + role_data["description"]
        job_docs.append(full_doc)
        job_names.append(role_name)

    cleaned_resume = clean_text(resume_text)

    # Combine resume + all job docs into one corpus for TF-IDF to learn from
    all_docs = [cleaned_resume] + job_docs

    # n-gram range (1,2) means single words AND two-word phrases are captured
    # e.g., "machine learning" is treated as one token, not two separate ones
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(all_docs)

    # First row = resume; remaining rows = job descriptions
    resume_vector = tfidf_matrix[0]
    job_vectors = tfidf_matrix[1:]

    # Cosine similarity gives a score 0.0 (no match) → 1.0 (perfect match)
    similarity_scores = cosine_similarity(resume_vector, job_vectors)[0]

    return similarity_scores, job_names


# ─────────────────────────────────────────────
# STEP 4: COMPUTE MATCH SCORES
# ─────────────────────────────────────────────
def compute_match_scores(resume_text: str, top_n: int = 10) -> pd.DataFrame:
    """
    Return the top N job matches as a DataFrame with match percentage.
    """
    similarity_scores, job_names = build_tfidf_vectors(resume_text)

    results = []
    for i, (score, name) in enumerate(zip(similarity_scores, job_names)):
        match_pct = round(score * 100, 2)  # convert 0-1 to 0-100%
        results.append({
            "Job Role": name,
            "Match %": match_pct,
            "Category": get_category(name)
        })

    df = pd.DataFrame(results)
    df = df.sort_values("Match %", ascending=False).reset_index(drop=True)
    return df.head(top_n)


# ─────────────────────────────────────────────
# STEP 5: SKILL GAP ANALYSIS
# ─────────────────────────────────────────────
def get_skill_gap(resume_text: str, job_role: str) -> dict:
    """
    For a given job role, return:
    - matched_skills: skills in resume that match the job
    - missing_skills: skills the job requires that are NOT in the resume
    - match_percentage: percentage of required skills present
    """
    resume_skills = set(extract_skills(resume_text))

    if job_role not in JOB_ROLES:
        return {"error": f"Job role '{job_role}' not found."}

    required_skills = set(skill.lower() for skill in JOB_ROLES[job_role]["skills"])

    matched = resume_skills.intersection(required_skills)
    missing = required_skills - resume_skills

    match_pct = round(len(matched) / len(required_skills) * 100, 1) if required_skills else 0

    return {
        "job_role": job_role,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing),
        "match_percentage": match_pct,
        "total_required": len(required_skills),
        "total_matched": len(matched),
    }


# ─────────────────────────────────────────────
# HELPER: Category labels for visual grouping
# ─────────────────────────────────────────────
def get_category(role_name: str) -> str:
    categories = {
        "Data & AI": ["Data Scientist", "Machine Learning Engineer", "Data Analyst",
                      "Data Engineer", "NLP Engineer", "Computer Vision Engineer",
                      "AI/ML Research Scientist", "Business Intelligence Analyst",
                      "Healthcare Data Analyst", "Bioinformatics Scientist",
                      "Quantitative Analyst"],
        "Software Engineering": ["Software Engineer", "Backend Developer", "Frontend Developer",
                                  "Full Stack Developer", "Mobile Developer (Android)",
                                  "Mobile Developer (iOS)", "Embedded Systems Engineer",
                                  "Blockchain Developer", "QA Engineer", "Game Developer",
                                  "Robotics Engineer", "IoT Engineer"],
        "Infrastructure & Cloud": ["DevOps Engineer", "Cloud Engineer", "Site Reliability Engineer",
                                    "Network Engineer", "Database Administrator",
                                    "Systems Architect", "Cybersecurity Analyst",
                                    "Cybersecurity Engineer"],
        "Design & Product": ["UI/UX Designer", "Graphic Designer", "Product Designer",
                              "Product Manager", "Technical Writer"],
        "Management": ["Project Manager", "Scrum Master", "Operations Manager", "HR Manager"],
        "Business & Finance": ["Financial Analyst", "Accountant", "Supply Chain Analyst",
                                "Salesforce Developer", "SAP Consultant"],
        "Marketing": ["Digital Marketing Specialist", "SEO Specialist",
                       "Content Writer", "Social Media Manager"],
        "Research": ["Research Scientist"],
    }
    for category, roles in categories.items():
        if role_name in roles:
            return category
    return "Other"

# ─────────────────────────────────────────────
# HELPER: Parse PDF/TXT resume to text
# ─────────────────────────────────────────────
def extract_text_from_file(uploaded_file) -> str:
    """
    Extract raw text from an uploaded file (PDF or TXT).
    Streamlit's UploadedFile object is passed directly here.
    """
    import io
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8", errors="ignore")

    elif file_name.endswith(".pdf"):
        try:
            import pdfplumber
            with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
                text = ""
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
            return text
        except Exception as e:
            return f"ERROR reading PDF: {e}"

    else:
        return "Unsupported file format. Please upload a .txt or .pdf file."
