## 🌐 Live Demo

Try CareerAI:
https://careeraicapstone.streamlit.app/

## Screenshots

### Dashboard

https://github.com/durvagdalvi-coder/CareerAI/blob/main/Screenshots/App%20Interface.png

### ATS Analysis

https://github.com/durvagdalvi-coder/CareerAI/blob/main/Screenshots/App%20Interface%20With%20Skills.png

# 🚀 CareerAI

## AI-Assisted Resume Optimization Platform

CareerAI is a resume optimization application that analyzes a candidate's resume against a target job description and provides structured career insights.

The system helps users understand:

- How well their resume matches a job role
- Which skills are already aligned
- Which skills are missing
- How they can improve their application

CareerAI uses a hybrid approach combining:

- Natural Language Processing (NLP)
- Skill intelligence mapping
- Logic-based ATS analysis
- Automated career recommendations


---

# ✨ Features

## Resume & Job Input

CareerAI supports:

- PDF resume upload
- DOCX resume upload
- TXT resume upload
- Direct text input

Job descriptions can also be provided through:

- PDF
- DOCX
- TXT
- Text input


---

# 📊 Resume Analysis

CareerAI provides:

## ATS Compatibility Score

Measures resume alignment with job requirements.

## Skill Matching

Identifies:

- Skills present in the resume
- Skills required by the job

## Skill Gap Analysis

Highlights missing skills that may improve job alignment.


---

# 🎯 Role Detection

CareerAI identifies the target job profile from the job description.

Examples:

- Fashion Designer
- Software Developer
- Marketing Specialist
- Data Analyst

The system also classifies the related industry category.


---

# 💡 Career Recommendations

Based on detected skill gaps, CareerAI provides:

- Resume improvement suggestions
- Professional summary generation
- Interview preparation questions


---

# 🏗️ System Workflow



Resume + Job Description

      ↓

Document Extraction

      ↓

NLP Processing

      ↓

Skill Intelligence Engine

      ↓

Resume Matching Engine

      ↓

ATS Score + Skill Analysis

      ↓

Career Recommendations

      ↓

CareerAI Report



---

# 🧠 Architecture

CareerAI follows a modular architecture:



User Interface
(Streamlit)

    ↓

Document Processing

    ↓

NLP Layer
(spaCy)

    ↓

Skill Intelligence Engine

    ↓

Weighted Matching Engine

    ↓

Career Intelligence Layer

    ↓

Report Generation



---

# 🛠️ Technology Stack


| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Language | Python |
| Document Processing | PyPDF, python-docx |
| NLP | spaCy |
| Skill Analysis | Custom Skill Intelligence Engine |
| Matching Logic | Weighted ATS Engine |
| Output | CareerAI Report |


---

# 📂 Project Structure



CareerAI/

│
├── app.py
├── text_extractor.py
├── nlp_engine.py
├── skill_engine.py
├── matcher.py
├── role_detector.py
├── recommendations.py
├── report_generator.py
│
├── requirements.txt
└── README.md



---

# ⚙️ Installation

## 1. Clone the repository


git clone <repository-url>


## 2. Install dependencies


pip install -r requirements.txt


## 3. Install spaCy model


python -m spacy download en_core_web_sm


## 4. Run CareerAI


streamlit run app.py



---

# 📌 Example Workflow



Upload Resume

    ↓

Upload Job Description

    ↓

CareerAI Analysis

    ↓

View:

✓ ATS Score

✓ Matched Skills

✓ Skill Gaps

✓ Improvement Suggestions

✓ Professional Summary

✓ Interview Questions

    ↓

Download Report



---

# 🔒 Responsible AI Approach

CareerAI is designed as an assistance tool.

The system avoids:

- Adding false experience
- Creating fake achievements
- Misrepresenting candidate skills

Users should review all recommendations before applying them to their resumes.


---

# 🚀 Future Improvements

Possible future enhancements:

## Expanded Skill Database

Support additional industries:

- Finance
- Healthcare
- Education
- Sales
- Operations
- Engineering


## Advanced AI Integration

Future versions may include:

- More advanced language models
- Conversational career assistance
- Enhanced resume rewriting


## User Features

Future additions:

- User accounts
- Resume history
- Multiple job comparisons
- Saved analysis reports


---

# 📄 Project Summary

CareerAI demonstrates how NLP and intelligent automation can improve the resume customization process.

The project combines:

- Document processing
- Natural Language Processing
- Skill analysis
- ATS evaluation
- Career recommendations

to create a practical resume optimization platform.
