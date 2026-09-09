# =========================================================
# RoleSync Rule-Based Recommendation Engine
# =========================================================

import pandas as pd

from src.skill_engine import (
    normalize_skill,
    normalize_skills
)


# =========================================================
# DATASET
# =========================================================

DATA_PATH = "data/raw/jobs.csv"


# =========================================================
# LOAD JOB DATA
# =========================================================

def load_jobs(file_path=DATA_PATH):
    """
    Loads and cleans the RoleSync job dataset.
    """

    jobs = pd.read_csv(
        file_path
    )

    # Clean role names
    jobs["role"] = (
        jobs["role"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Clean skills text
    jobs["skills"] = (
        jobs["skills"]
        .fillna("")
        .astype(str)
        .str.strip()
    )

    # Remove completely duplicate rows
    jobs = jobs.drop_duplicates().reset_index(
        drop=True
    )

    # Convert comma-separated skills
    # into normalized skill lists
    jobs["skills_list"] = jobs["skills"].apply(
        lambda value: [
            normalize_skill(skill)
            for skill in str(value).split(",")
            if str(skill).strip()
        ]
    )

    return jobs


# =========================================================
# MATCH SCORE
# =========================================================

def calculate_match_score(
    user_skills,
    job_skills
):
    """
    Calculates the percentage of required job skills
    that are already present in the user's profile.
    """

    user_skills = set(
        normalize_skills(
            user_skills
        )
    )

    job_skills = set(
        normalize_skills(
            job_skills
        )
    )

    if not job_skills:
        return 0.0

    matched_skills = (
        user_skills.intersection(
            job_skills
        )
    )

    score = (
        len(matched_skills)
        / len(job_skills)
    ) * 100

    return round(
        score,
        2
    )


# =========================================================
# SKILL ANALYSIS
# =========================================================

def get_skill_analysis(
    user_skills,
    job_skills
):
    """
    Returns matched skills, missing skills
    and the overall rule-based match score.
    """

    user_skills = set(
        normalize_skills(
            user_skills
        )
    )

    job_skills = set(
        normalize_skills(
            job_skills
        )
    )

    matched = sorted(
        user_skills.intersection(
            job_skills
        )
    )

    missing = sorted(
        job_skills.difference(
            user_skills
        )
    )

    score = calculate_match_score(
        user_skills,
        job_skills
    )

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_score": score
    }


# =========================================================
# ALL ROLE RECOMMENDATIONS
# =========================================================

def get_all_recommendations(
    user_skills,
    file_path=DATA_PATH
):
    """
    Calculates rule-based recommendations
    for every role in the dataset.
    """

    jobs = load_jobs(
        file_path
    )

    normalized_user_skills = normalize_skills(
        user_skills
    )

    recommendations = []

    for _, job in jobs.iterrows():

        analysis = get_skill_analysis(
            normalized_user_skills,
            job["skills_list"]
        )

        recommendations.append(
            {
                "role": job["role"],

                "required_skills": job[
                    "skills"
                ],

                "matched_skills": ", ".join(
                    analysis[
                        "matched_skills"
                    ]
                ),

                "missing_skills": ", ".join(
                    analysis[
                        "missing_skills"
                    ]
                ),

                "match_score": analysis[
                    "match_score"
                ],

                "experience": job.get(
                    "experience",
                    ""
                )
            }
        )

    recommendations = sorted(
        recommendations,
        key=lambda item: (
            item["match_score"],
            item["role"]
        ),
        reverse=True
    )

    return recommendations


# =========================================================
# TOP ROLE RECOMMENDATIONS
# =========================================================

def recommend_jobs(
    user_skills,
    top_n=5
):
    """
    Returns the top matching roles.
    """

    all_recommendations = (
        get_all_recommendations(
            user_skills
        )
    )

    return all_recommendations[
        :top_n
    ]
