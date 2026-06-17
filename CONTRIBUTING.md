# Contributing to AI Resume Screener & Job Recommender

## How to Contribute

### 1. Fork and Clone
```bash
git clone https://github.com/YOUR_USERNAME/AI-Resume-Screener-and-Job-Recommender.git
cd AI-Resume-Screener-and-Job-Recommender
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

Use clear branch names:
- `feature/add-docx-support`
- `fix/pdf-encoding-error`
- `docs/update-architecture-diagram`

### 3. Make Your Changes
- One feature or fix per pull request
- Follow existing code style — snake_case, docstrings on all functions
- Never commit user resume files or personal data

### 4. Test Your Changes
```bash
streamlit run app/app.py
```

### 5. Submit a Pull Request
- Clear PR title and description
- Reference related issue numbers
- Include a screenshot if the change affects the UI

## Areas Where Contributions Are Welcome
- Adding new job roles to `src/job_data.py`
- Supporting additional resume formats such as `.docx`
- Improving skill extraction accuracy
- Adding unit tests under a `tests/` directory
- Writing documentation in `docs/`

## Code Standards
- Python 3.10+
- All functions must have docstrings
- Variable names in snake_case
- No hardcoded file paths
- Never commit `.env` files or API keys

## Reporting Bugs
Open a GitHub Issue with:
1. What you expected to happen
2. What actually happened
3. Steps to reproduce
4. Your Python version and OS

## Code of Conduct
This project follows the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md).