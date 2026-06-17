# AI Resume Screener & Job Recommender

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-TF--IDF-F7931E?logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

An NLP-powered resume analysis platform that matches candidate resumes against **60+ job roles** across **8 industry categories** using TF-IDF vectorisation and cosine similarity — returning ranked job matches, skill gap reports, and interactive visualisations in real time.

---

## Table of Contents

- [About This Project](#about-this-project)
- [Key Features](#key-features)
- [Project Highlights](#project-highlights)
- [Architecture](#architecture)
- [Workflow](#workflow)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## About This Project

Manual resume screening is time-consuming and inconsistent. This project automates that initial layer of screening by applying NLP techniques to extract skills from candidate resumes, vectorise both the resume and job role descriptions using TF-IDF, and rank matches by cosine similarity.

The result is a clean, interactive Streamlit dashboard that gives candidates instant, data-driven feedback: which roles they are best suited for, which skills they already have, and exactly what they are missing for their target role.

---

## Key Features

| Feature | Description |
|---|---|
| **Resume Upload** | Accepts PDF and plain text (.txt) resumes |
| **Automated Text Extraction** | Parses PDF resumes using `pdfplumber` |
| **Skill Detection** | Scans resume against a master skill dictionary using regex word-boundary matching |
| **TF-IDF + Cosine Similarity** | Vectorises resume and 60+ job role descriptions; ranks matches by similarity score |
| **Top Job Matches** | Interactive horizontal bar chart showing ranked job recommendations |
| **Skill Gap Analysis** | Per-role breakdown of skills you have vs. skills you are missing |
| **Radar Chart** | Visual coverage comparison across your top 5 matched roles |
| **Industry Distribution** | Donut chart showing match distribution across 8 industry categories |
| **Session Persistence** | Results persist across UI interactions without re-running analysis |

---

## Project Highlights

- Processes resumes against **60+ job roles** spanning Data & AI, Software Engineering, Infrastructure & Cloud, Design & Product, Business & Finance, Marketing, Management, and Research
- Uses **n-gram range (1, 2)** in TF-IDF to capture two-word technical phrases like "machine learning" and "data pipeline"
- **Word-boundary regex matching** prevents false positives such as "r" matching "react"
- Fully **modular architecture** — NLP logic, job data, and UI are completely decoupled
- **Zero external API dependency** — no API keys or internet access required at runtime
- Deployable on Streamlit Community Cloud in under 2 minutes

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Streamlit UI (app.py)             │
│   Sidebar: Upload / Paste Resume + Settings         │
│   Main: 7 analytical sections + visualisations      │
└───────────────────┬─────────────────────────────────┘
                    │
        ┌───────────▼───────────┐
        │   resume_processor.py │  ← NLP & ML core
        │  - clean_text()       │
        │  - extract_skills()   │
        │  - build_tfidf()      │
        │  - compute_matches()  │
        │  - get_skill_gap()    │
        └───────────┬───────────┘
                    │
        ┌───────────▼───────────┐
        │      job_data.py      │  ← Skills database
        │   60+ roles × 8 cats  │
        └───────────────────────┘
```

---

## Workflow

```
Resume Input (PDF / TXT / Paste)
        │
        ▼
Text Extraction  ──►  pdfplumber (PDF) / UTF-8 decode (TXT)
        │
        ▼
Text Cleaning  ──►  lowercase, strip punctuation, collapse whitespace
        │
        ▼
Skill Extraction  ──►  regex word-boundary scan vs. master skill list
        │
        ▼
TF-IDF Vectorisation  ──►  resume + 60+ job docs → sparse matrix
        │
        ▼
Cosine Similarity  ──►  resume vector vs. each job vector → scores 0–1
        │
        ▼
Ranked Output  ──►  top N matches, skill gap, radar, pie chart
```

---

## Screenshots

### Landing Screen
![Landing](assets/screenshots/screenshot_01_landing.png)

### Summary Metrics
![Metrics](assets/screenshots/screenshot_02_metrics.png)

### Top Job Matches
![Job Matches](assets/screenshots/screenshot_03_job_matches.png)

### Skill Gap Analysis
![Skill Gap](assets/screenshots/screenshot_04_skill_gap.png)

### Radar Chart
![Radar](assets/screenshots/screenshot_05_radar.png)

### Industry Distribution
![Industry](assets/screenshots/screenshot_06_industry.png)

### Detected Skills
![Skills](assets/screenshots/screenshot_07_skills.png)

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| NLP Vectorisation | Scikit-learn (TF-IDF) |
| Similarity Scoring | Scikit-learn (Cosine Similarity) |
| PDF Parsing | pdfplumber |
| Data Manipulation | pandas, numpy |
| Visualisation | Plotly Express, Plotly Graph Objects |
| Language | Python 3.10+ |

---

## Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screener-and-Job-Recommender.git
cd AI-Resume-Screener-and-Job-Recommender

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
streamlit run app/app.py
```

---

## Project Structure

```
AI-Resume-Screener-and-Job-Recommender/
│
├── app/
│   └── app.py                  # Streamlit UI — 7 dashboard sections
│
├── src/
│   ├── resume_processor.py     # NLP core: cleaning, skill extraction, TF-IDF, scoring
│   └── job_data.py             # Job roles database: 60+ roles, skills, descriptions
│
├── assets/
│   ├── screenshots/            # UI screenshots
│   └── diagrams/               # Architecture and workflow diagrams
│
├── sample_resumes/             # Example resumes for testing
├── docs/                       # Additional documentation
│
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
└── .gitignore
```

---

## Future Enhancements

- [ ] ATS Score Calculator
- [ ] LLM-Powered Resume Feedback
- [ ] Job Portal Integration
- [ ] Multi-Resume Comparison
- [ ] Resume Builder Mode
- [ ] Export Match Report to PDF

---

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a pull request.

---
