import pandas as pd


# Load the jobs dataset
file_path = "data/raw/jobs.csv"

jobs = pd.read_csv(file_path)


# Inspect the dataset
print("\n--- FIRST 5 ROWS ---")
print(jobs.head())

print("\n--- DATASET INFO ---")
jobs.info()

print("\n--- STATISTICS ---")
print(jobs.describe())


# Clean the data
print("\n--- CLEANING DATA ---")

jobs["role"] = jobs["role"].str.strip()
jobs["skills"] = jobs["skills"].str.strip()

jobs = jobs.drop_duplicates()


print("\n--- CLEAN DATA ---")
print(jobs)


# Convert skills into Python lists
print("\n--- PROCESSED SKILLS ---")

jobs["skills_list"] = jobs["skills"].apply(
    lambda x: [skill.strip().lower() for skill in x.split(",")]
)

print(jobs[["role", "skills_list"]])


# Match user's skills with job requirements
def match_skills(user_skills, job_skills):
    user_skills = set(skill.lower().strip() for skill in user_skills)
    job_skills = set(skill.lower().strip() for skill in job_skills)

    matched = user_skills.intersection(job_skills)

    return list(matched)


# Example user skills
user_skills = ["Python", "SQL"]


print("\n--- SKILL MATCHING ---")

for _, job in jobs.iterrows():
    matched = match_skills(user_skills, job["skills_list"])
    print(job["role"], "→", matched)


# Calculate job match score
def calculate_match_score(user_skills, job_skills):
    user_skills = set(skill.lower().strip() for skill in user_skills)
    job_skills = set(skill.lower().strip() for skill in job_skills)

    if not job_skills:
        return 0

    matched = user_skills.intersection(job_skills)

    score = (len(matched) / len(job_skills)) * 100

    return round(score, 2)


print("\n--- JOB MATCH SCORES ---")

for _, job in jobs.iterrows():
    score = calculate_match_score(
        user_skills,
        job["skills_list"]
    )

    print(f"{job['role']} → {score}%")