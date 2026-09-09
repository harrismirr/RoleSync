# RoleSync

## Career Intelligence Platform for Skill Discovery and Role Matching

RoleSync is a career intelligence platform that analyzes a user's technical skills or resume and recommends suitable technology roles.

It combines rule-based skill coverage with TF-IDF and cosine similarity to create a hybrid role-matching system. It also identifies missing skills and generates a prioritized learning roadmap.

---

## Overview

Choosing a technology career path can be difficult when a student has multiple technical skills but does not know which roles are the best fit.

RoleSync addresses this problem by connecting:

Resume / Skills
        ↓
Skill Extraction
        ↓
Skill Normalization
        ↓
Role Matching
        ↓
Hybrid Recommendation
        ↓
Skill Gap Detection
        ↓
Career Roadmap

The goal is to transform a collection of technical skills into an actionable career direction.

---

## Key Features

### 1. Resume Intelligence

Upload a PDF resume and RoleSync automatically:

- Extracts text from the resume
- Detects recognized technical skills
- Normalizes different skill names
- Builds a structured skill profile
- Discovers related capabilities

Example:

Python → Pandas → NumPy → Data Analysis

---

### 2. Hybrid Role Recommendation

RoleSync uses two recommendation signals:

#### Rule-Based Skill Matching

Measures how many skills required by a role are already present in the user's profile.

#### TF-IDF Similarity

Uses scikit-learn's TF-IDF representation and cosine similarity to compare the user's skill profile with job skill descriptions.

The final recommendation score is:

Hybrid Score =
65% Rule-Based Skill Match
+
35% TF-IDF Similarity

This provides both interpretability and similarity-based ranking.

---

### 3. Skill Gap Analysis

For every recommended role, RoleSync identifies:

- Matched skills
- Missing skills
- Required skills
- Experience information

This helps users understand why a role is recommended and what they still need to learn.

---

### 4. Career Roadmap

Missing skills are assigned priority levels.

The roadmap categorizes skills as:

- High Priority
- Recommended
- Useful

The system also identifies the highest-priority next skill to learn.

---

### 5. Manual Skill Analysis

Users do not need to upload a resume.

They can enter skills manually, for example:

Python, SQL, Pandas, Machine Learning

RoleSync then generates role recommendations using the same hybrid recommendation engine.

---

## Technology Stack

### Programming Language

- Python

### Application Framework

- Streamlit

### Data Processing

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

### Resume Processing

- PyPDF

### Development

- Visual Studio Code
- Python Virtual Environment
- Git

---

## Project Architecture

```text
RoleSync
│
├── app.py
│
├── data
│   └── raw
│       └── jobs.csv
│
├── src
│   ├── data_loader.py
│   ├── recommender.py
│   ├── skill_engine.py
│   ├── roadmap.py
│   ├── resume_parser.py
│   ├── ml_recommender.py
│   └── hybrid_recommender.py
│
├── notebooks
│
├── tests
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
System Components
app.py
Main Streamlit application.
Responsible for:
User interface
Resume upload
Manual skill input
Displaying recommendations
Displaying skill gaps
Displaying career roadmap
skill_engine.py
RoleSync's skill intelligence layer.
Responsible for:
Skill normalization
Skill aliases
Resume skill extraction
Related skill discovery
Skill profile generation
recommender.py
Rule-based recommendation engine.
Responsible for:
Loading job data
Comparing user skills with job requirements
Calculating skill coverage
Identifying matched skills
Identifying missing skills
ml_recommender.py
Machine-learning similarity engine.
Uses:
TF-IDF Vectorizer
Cosine Similarity
It converts job skill descriptions and the user's skill profile into numerical vectors and measures their similarity.
hybrid_recommender.py
Combines the rule-based and ML recommendation engines.
Current weighting:
Rule-Based Match       65%
TF-IDF Similarity      35%
This produces the final hybrid ranking.
roadmap.py
Career learning roadmap engine.
Responsible for:
Skill priority scoring
Priority labels
Learning roadmap generation
Identifying the next recommended skill
resume_parser.py
PDF processing layer.
Responsible for:
Reading PDF files
Extracting resume text
Cleaning extracted text
Returning basic document information
Dataset
RoleSync currently uses a curated technical job-role dataset stored at:
data/raw/jobs.csv
The dataset contains technical roles with associated skills and experience requirements.
The application uses this dataset as the role knowledge base for recommendation.
Recommendation Logic
Suppose a user has:
Python
SQL
Pandas
Machine Learning
and a role requires:
Python
SQL
Pandas
Machine Learning
Statistics
The rule-based system identifies:
Matched:
Python
SQL
Pandas
Machine Learning

Missing:
Statistics
The rule-based score is then calculated from skill coverage.
The ML engine separately calculates TF-IDF similarity between the user's skill profile and the role's skill description.
Both scores are combined:
Hybrid Score =
(0.65 × Rule Match)
+
(0.35 × ML Similarity)
Roles are then ranked according to the hybrid score.
Example Output
A typical recommendation can look like:
Best Fit
--------
Data Scientist

Hybrid Match: 82.4%

Matched Skills:
Python
SQL
Pandas
Machine Learning

Skills To Develop:
Statistics
Deep Learning
The roadmap then prioritizes the missing capabilities.
Installation
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd RoleSync
2. Create a virtual environment
Windows:
python -m venv .venv
3. Activate the environment
Windows PowerShell:
.venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Run the application
streamlit run app.py
The application will open in the browser.

Usage
Resume Mode
Open RoleSync.
Upload a PDF resume.
Wait for resume analysis.
Review detected skills.
Review related capabilities.
View the best-fit role.
Compare recommended roles.
Review missing skills.
Follow the generated career roadmap.
Manual Mode
Scroll to Manual Skill Analysis.
Enter skills separated by commas.
Click Analyze My Skills.
Review the recommended roles and hybrid scores.
Machine Learning Approach
RoleSync does not use a supervised classification model.
Instead, its ML component is a content-based similarity system.
TF-IDF
TF-IDF converts textual skill descriptions into numerical representations based on the importance of terms.
Cosine Similarity
Cosine similarity measures how similar the user's skill vector is to each job-role vector.
This makes it possible to rank roles according to the similarity between the user's capabilities and the technical requirements of the roles.
The ML component is combined with explicit skill coverage to improve interpretability.
Why Hybrid Recommendation?
A purely rule-based system is easy to understand but can be rigid.
A purely similarity-based system can identify related text patterns but may not clearly explain which required skills are missing.
RoleSync combines both approaches.
Rule-Based Engine
        +
TF-IDF Similarity
        ↓
Hybrid Recommendation
This gives the user both:
A measurable skill match
A similarity-based recommendation signal
Design Principles
RoleSync is designed around four principles:
Explainability
Recommendations should show why a role matches.
Actionability
The system should identify what the user can learn next.
Modularity
Each major intelligence component is separated into its own Python module.
Extensibility
The architecture can later support more advanced recommendation and career intelligence capabilities.
Future Scope
Potential future improvements include:
Semantic embeddings for deeper skill similarity
Large language model assisted resume analysis
Job description ingestion from external sources
Personalized learning-resource recommendations
Experience-aware role matching
Salary and market-demand intelligence
Location-aware career recommendations
User profiles and recommendation history
Advanced skill graphs
Evaluation metrics for recommendation quality
Deployment as a production web application
Project Goals
RoleSync was built to demonstrate practical skills in:
Python
Data processing
Natural language processing concepts
Machine learning
Recommendation systems
Streamlit application development
Modular software architecture
Resume parsing
Career analytics
Status
Core Application       COMPLETE
Resume Intelligence    COMPLETE
Skill Engine           COMPLETE
Rule-Based Matching    COMPLETE
ML Similarity          COMPLETE
Hybrid Recommendation  COMPLETE
Skill Gap Analysis     COMPLETE
Career Roadmap         COMPLETE
Manual Analysis        COMPLETE

Author
Harris Mir
RoleSync
Career Intelligence Platform for skill discovery, role matching and structured career growth.
Your career is not defined by what you know today, but by what you choose to learn next.