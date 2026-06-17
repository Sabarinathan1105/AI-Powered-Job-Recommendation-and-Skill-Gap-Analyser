# Architecture & Workflow Diagrams

## System Architecture

```mermaid
graph TD
    A[User] -->|Upload PDF/TXT or Paste Text| B[Streamlit UI app/app.py]
    B -->|resume text| C[resume_processor.py]
    C -->|reads skill definitions| D[job_data.py 60+ roles · 8 categories]
    C --> E[clean_text]
    E --> F[extract_skills]
    E --> G[build_tfidf_vectors]
    G --> H[cosine_similarity]
    H --> I[compute_match_scores]
    F --> J[get_skill_gap]
    I --> K[Streamlit Dashboard]
    J --> K
    K --> L[Bar Chart — Top Matches]
    K --> M[Skill Gap Panel]
    K --> N[Radar Chart]
    K --> O[Industry Donut Chart]
    K --> P[Detected Skills Panel]
```

## Processing Workflow

```mermaid
flowchart LR
    A([Resume Input]) --> B[Text Extraction pdfplumber / UTF-8]
    B --> C[Text Cleaning lowercase · strip · normalise]
    C --> D[Skill Extraction regex word-boundary scan]
    C --> E[TF-IDF Vectorisation n-gram 1,2]
    E --> F[Cosine Similarity resume vs. 60+ job vectors]
    F --> G[Ranked Match Scores]
    D --> H[Skill Gap Analysis matched and missing per role]
    G --> I([Dashboard Output])
    H --> I
```

## Module Dependency

```mermaid
graph LR
    A[app/app.py] -->|imports| B[src/resume_processor.py]
    A -->|imports JOB_ROLES| C[src/job_data.py]
    B -->|imports JOB_ROLES| C
```

## Folder Structure

```
AI-Resume-Screener-and-Job-Recommender/
│
├── app/
│   └── app.py
├── src/
│   ├── resume_processor.py
│   └── job_data.py
├── assets/
│   ├── screenshots/
│   └── diagrams/
├── sample_resumes/
├── docs/
│   └── architecture.md
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
└── .gitignore
```