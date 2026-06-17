All notable changes to this project are documented here.

## [1.0.0] — 2025

### Added
- Streamlit UI with 7 analytical sections
- PDF and TXT resume upload and parsing via pdfplumber
- Resume text paste as alternative input
- Skill extraction using regex word-boundary matching
- TF-IDF vectorisation with n-gram range (1, 2)
- Cosine similarity scoring against 60+ job role descriptions
- Top N job match bar chart configurable via sidebar slider
- Detailed match table with ranking and industry category
- Skill gap analysis — matched vs. missing skills per selected role
- Radar chart comparing skill coverage across top 5 matched roles
- Industry distribution donut chart across 8 categories
- Detected skills panel with colour-coded tags
- Session state persistence across Streamlit reruns
- 60+ job roles across 8 industry categories in job_data.py
- Modular architecture — UI, NLP core, and data fully decoupled

## [Unreleased]

### Planned
- .docx resume format support
- ATS score calculator
- LLM-powered resume feedback
- Unit test suite
- Job portal live feed integration