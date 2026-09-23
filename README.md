# RoleSync

## Career Intelligence Platform for Skill Discovery and Role Matching

RoleSync is a career intelligence platform designed to help users understand how their existing technical skills align with technology roles.

The platform analyzes either a user's technical skills or PDF resume, recommends relevant technology roles, identifies skill gaps, and generates a structured career learning roadmap.

RoleSync combines an interpretable rule-based skill matching system with a machine-learning-based TF-IDF similarity engine to create a hybrid recommendation system.

---

## Live Demo

**Try RoleSync online:**

https://rolesync-career.streamlit.app

## Source Code

**GitHub Repository:**

https://github.com/harrismirr/RoleSync

---

# Overview

Choosing a technology career path can be difficult when a student has multiple technical skills but is unsure which roles align with their current capabilities.

RoleSync addresses this problem by transforming a user's skills or resume into an actionable career profile.

The system follows this pipeline:

```text
Resume / Manual Skills
        ↓
Resume Text Extraction
        ↓
Skill Detection
        ↓
Skill Normalization
        ↓
Skill Profile
        ↓
Role Matching
        ↓
Hybrid Recommendation
        ↓
Skill Gap Detection
        ↓
Career Roadmap

The goal is not simply to recommend a job title, but to explain:
Which skills already match a role
Which skills are missing
How strongly the profile matches
Which capabilities should be developed next
Key Features
1. Resume Intelligence
Users can upload a PDF resume and RoleSync extracts technical information from the document.
The resume intelligence pipeline:
PDF Resume
    ↓
Text Extraction
    ↓
Text Cleaning
    ↓
Skill Detection
    ↓
Skill Normalization
    ↓
Structured Skill Profile
RoleSync can:
Extract text from PDF resumes
Detect recognized technical skills
Normalize skill aliases
Build a structured skill profile
Discover related capabilities
For example:
Python
   ↓
Pandas
   ↓
NumPy
   ↓
Data Analysis
2. Hybrid Role Recommendation
RoleSync combines two recommendation signals.
Rule-Based Skill Matching
The rule-based engine compares the user's current skills with the skills required by each role.
It calculates skill coverage and identifies:
Matched skills
Missing skills
Required skills
Skill match percentage
TF-IDF Similarity
The machine-learning component represents skill descriptions using TF-IDF vectors.
Cosine similarity is then used to measure the similarity between the user's skill profile and each role's technical skill description.
Hybrid Score
The current recommendation system combines both signals:
Hybrid Score =
(0.65 × Rule-Based Skill Match)
+
(0.35 × TF-IDF Similarity)
This allows RoleSync to combine explicit skill coverage with text-based similarity.
3. Skill Gap Analysis
For recommended roles, RoleSync identifies the difference between the user's current capabilities and the role requirements.
Example:
Current Skills

Python
SQL
Pandas
Machine Learning
Role requirements:
Python
SQL
Pandas
Machine Learning
Statistics
Result:
Matched Skills

Python
SQL
Pandas
Machine Learning
Skills To Develop

Statistics
This makes the recommendation more actionable than simply displaying a role name.
4. Career Roadmap
RoleSync converts missing skills into a structured learning roadmap.
Each missing capability receives a priority level:
High Priority
Recommended
Useful
The roadmap engine can also identify the next recommended skill based on the priority system.
This creates a progression from:
Current Skills
      ↓
Skill Gaps
      ↓
Prioritized Learning
      ↓
Career Development
5. Manual Skill Analysis
Users do not need to upload a resume.
They can enter their skills manually.
Example:
Python, SQL, Pandas, Machine Learning, Statistics
RoleSync processes these skills through the same recommendation pipeline and generates:
Recommended roles
Hybrid match scores
Matched skills
Missing skills
Career development direction
Application Screenshots
RoleSync Dashboard

Resume Intelligence

Role Recommendations

Career Roadmap

Technology Stack
Programming Language
Python
Application Framework
Streamlit
Data Processing
Pandas
NumPy
Machine Learning
Scikit-learn
TF-IDF Vectorization
Cosine Similarity
Resume Processing
PyPDF
Development Tools
Visual Studio Code
Python Virtual Environment
Git
GitHub
Project Architecture
RoleSync
│
├── app.py
│
├── data
│   └── raw
│       └── jobs.csv
│
├── screenshots
│   ├── home.png
│   ├── resume-intelligence.png
│   ├── recommendations.png
│   └── roadmap.png
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
├── tests
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
System Architecture
RoleSync is divided into several independent intelligence layers.
                    ┌──────────────────────┐
                    │       User           │
                    │ Resume / Skills      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Resume Intelligence │
                    │   / Skill Input      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Skill Engine       │
                    │ Normalization /      │
                    │ Skill Detection      │
                    └──────────┬───────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
      ┌────────────────────┐      ┌────────────────────┐
      │ Rule-Based Engine  │      │ ML Similarity      │
      │                    │      │ Engine             │
      │ Skill Coverage     │      │ TF-IDF             │
      │ Matched Skills     │      │ Cosine Similarity  │
      │ Missing Skills     │      │                    │
      └─────────┬──────────┘      └─────────┬──────────┘
                │                           │
                └─────────────┬─────────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │ Hybrid Recommendation│
                   │       Engine         │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │ Skill Gap Analysis   │
                   └──────────┬───────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │ Career Roadmap       │
                   └──────────────────────┘

                   System Components
app.py
Main Streamlit application.
Responsible for:
User interface
Resume upload
Manual skill input
Displaying skill profiles
Displaying role recommendations
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
Skill relationships
Example aliases:
ML → Machine Learning
JS → JavaScript
Postgres → PostgreSQL
K8s → Kubernetes
Sklearn → Scikit-learn
This reduces inconsistencies between different ways of writing the same technology.
recommender.py
Rule-based recommendation engine.
Responsible for:
Loading job-role data
Comparing user skills with role requirements
Calculating skill coverage
Identifying matched skills
Identifying missing skills
Producing interpretable role matches
The rule-based engine focuses on explicit skill coverage.
ml_recommender.py
Machine-learning similarity engine.
The ML component uses:
TF-IDF Vectorizer
Cosine Similarity
The process is:
Role Skill Description
        ↓
TF-IDF Vectorization
        ↓
Numerical Vector
The user's skill profile is represented using the same vector space.
Cosine similarity is then calculated between the user's profile and the role descriptions.
hybrid_recommender.py
Combines the rule-based and ML recommendation engines.
Current weighting:
Rule-Based Match       65%
TF-IDF Similarity      35%
The resulting hybrid score is used to rank roles.
The hybrid architecture allows RoleSync to combine:
Explicit Skill Coverage
          +
Text Similarity
          ↓
Hybrid Role Ranking
roadmap.py
Career learning roadmap engine.
Responsible for:
Skill priority scoring
Priority labels
Learning roadmap generation
Identifying the next recommended skill
Priority levels currently include:
High Priority
Recommended
Useful
resume_parser.py
PDF processing layer.
Responsible for:
Reading PDF files
Extracting text
Cleaning extracted text
Returning document information
The extracted text is then passed to the skill intelligence layer.
data_loader.py
Data exploration and preprocessing utilities.
The module supports loading and preparing the role dataset for analysis and experimentation.


Dataset
RoleSync currently uses a curated technical job-role dataset:
data/raw/jobs.csv
The dataset contains technical roles with associated:
Role names
Required skills
Experience information
The dataset acts as the role knowledge base for the recommendation system.
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
The rule-based engine identifies:
Matched
Python
SQL
Pandas
Machine Learning
Missing
Statistics
The rule-based score represents the proportion of required role skills already present in the user's profile.
The ML engine separately calculates TF-IDF similarity.
The two signals are combined:
Hybrid Score =
(0.65 × Rule Match)
+
(0.35 × ML Similarity)
Roles are then ranked using the hybrid score.
Example Recommendation
A recommendation can contain:
Recommended Role
----------------
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
The roadmap engine can then prioritize the missing capabilities.
Machine Learning Approach
Content-Based Recommendation
RoleSync does not use a supervised classification model.
Instead, its machine-learning component uses a content-based similarity approach.
The system compares the user's skill profile against the technical skill descriptions associated with available roles.
TF-IDF
TF-IDF stands for:
Term Frequency-Inverse Document Frequency
It converts text into numerical representations based on the importance of terms within the available role descriptions.
In RoleSync, TF-IDF is applied to technical skill descriptions.
Conceptually:
Textual Skills
      ↓
Tokenization
      ↓
TF-IDF Vectorization
      ↓
Numerical Representation


Cosine Similarity
Cosine similarity measures the similarity between two numerical vectors.
RoleSync uses it to compare:
User Skill Vector
        ↕
Role Skill Vector
A higher similarity indicates that the skill descriptions have greater overlap in the vector space.
Why Use a Hybrid Recommendation System?
A purely rule-based system provides strong interpretability but can be rigid.
For example, it can clearly show:
Matched:
Python
SQL
Pandas

Missing:
Statistics
However, it does not capture all textual relationships between skill descriptions.
A purely similarity-based system can identify textual similarity, but it may not clearly explain which required skills are missing.
RoleSync therefore combines both.
Rule-Based Skill Matching
           +
     TF-IDF Similarity
           ↓
   Hybrid Recommendation
This provides:
Explicit skill coverage
Similarity-based ranking
Matched skills
Missing skills
Actionable learning direction
Skill Intelligence
RoleSync includes a skill normalization layer to handle variations in technology names.
For example:
ML
Machine Learning
machine-learning
can be normalized into:
machine learning
Similarly:
JS
JavaScript
can be normalized into:
javascript
This improves consistency when comparing user skills against role requirements.
Skill Relationships
RoleSync also contains relationships between related technical skills.
For example:
Python
 ├── Pandas
 ├── NumPy
 ├── SQL
 └── Statistics
Another example:
Machine Learning
 ├── Python
 ├── Statistics
 ├── Pandas
 ├── NumPy
 └── Deep Learning
These relationships allow the system to identify related capabilities that may be useful for further development.
Design Principles
RoleSync is designed around four principles.
Explainability
Recommendations should provide understandable reasons for a role match.
Users can inspect matched and missing skills rather than receiving only a role name.
Actionability
The system should help users understand what they can learn next.
Modularity
Major intelligence components are separated into individual Python modules.
This makes the system easier to maintain and extend.
Extensibility
The architecture is designed so that more advanced recommendation and career intelligence features can be added later.


Installation
1. Clone the Repository
git clone https://github.com/harrismirr/RoleSync.git
cd RoleSync
2. Create a Virtual Environment
Windows:
python -m venv .venv
3. Activate the Environment
Windows PowerShell:
.venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
5. Run the Application
streamlit run app.py
The application will open in the browser.
Usage
Resume Mode
Open RoleSync.
Upload a PDF resume.
Wait for resume analysis.
Review detected skills.
Review related capabilities.
Review recommended roles.
Compare hybrid match scores.
Review matched and missing skills.
Follow the generated career roadmap.
Manual Mode
Open the Manual Skill Analysis section.
Enter technical skills separated by commas.
Click Analyze My Skills.
Review recommended roles.
Review hybrid match scores.
Review missing capabilities.
Review the career roadmap.
Example Workflow
A typical RoleSync workflow looks like:
User
 │
 │ Uploads Resume
 │
 ▼
Resume Parser
 │
 │ Extracted Text
 ▼
Skill Engine
 │
 │ Normalized Skills
 ▼
Recommendation Engines
 │
 ├── Rule-Based Matching
 │
 └── TF-IDF Similarity
 │
 ▼
Hybrid Recommendation
 │
 ▼
Skill Gap Analysis
 │
 ▼
Career Roadmap
Future Scope
RoleSync can be extended into a more advanced career intelligence platform.
Potential future improvements include:
Semantic Skill Matching
Use embeddings to identify deeper semantic relationships between skills instead of relying primarily on keyword similarity.
LLM-Assisted Resume Analysis
Use large language models to extract richer information such as:
Projects
Responsibilities
Achievements
Experience level
Domains
Job Description Integration
Allow users to paste or upload real job descriptions and compare their profile directly against them.
Personalized Learning Resources
Recommend:
Courses
Documentation
Projects
Certifications
Practice resources
based on detected skill gaps.
Experience-Aware Matching
Consider years of experience and project complexity when recommending roles.
Market Intelligence
Potentially incorporate:
Salary information
Skill demand
Industry trends
Role demand
Location-Aware Recommendations
Compare career opportunities based on geographic preferences.
User Profiles
Allow users to maintain:
Skill history
Previous recommendations
Learning progress
Career goals
Advanced Skill Graphs
Build a graph of relationships between:
Skills
 ↓
Roles
 ↓
Learning Paths
 ↓
Career Opportunities
Recommendation Evaluation
Add formal evaluation metrics to measure recommendation quality and system performance.
Project Goals
RoleSync was built to demonstrate practical skills in:
Python
Data processing
Natural language processing concepts
Machine learning
Recommendation systems
TF-IDF
Cosine similarity
Streamlit application development
Modular software architecture
Resume parsing
Skill intelligence
Career analytics
Git and GitHub
Cloud deployment


Deployment
RoleSync is deployed using Streamlit Community Cloud.
The application is publicly accessible through:
https://rolesync-career.streamlit.app⁠
The source code is maintained on GitHub:
https://github.com/harrismirr/RoleSync⁠
Project Status
Component
Status
Core Application
Complete
Resume Intelligence
Complete
Skill Engine
Complete
Rule-Based Matching
Complete
ML Similarity
Complete
Hybrid Recommendation
Complete
Skill Gap Analysis
Complete
Career Roadmap
Complete
Manual Analysis
Complete
Streamlit Deployment
Complete
What This Project Demonstrates
RoleSync demonstrates an end-to-end machine-learning application workflow:
Data
 ↓
Preprocessing
 ↓
Feature Representation
 ↓
Similarity Modeling
 ↓
Recommendation
 ↓
Interpretation
 ↓
User Interface
 ↓
Deployment
The project combines software engineering, data processing, machine learning concepts, recommendation systems, and application deployment into a single working platform.


Author
Harris Mir
computer science Student | Data Science & AI Enthusiast
RoleSync
Career Intelligence Platform for skill discovery, role matching and structured career growth.
Your career is not defined by what you know today, but by what you choose to learn next.
Project Links
Live Demo:
https://rolesync-career.streamlit.app⁠
GitHub Repository:
https://github.com/harrismirr/RoleSync⁠

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.