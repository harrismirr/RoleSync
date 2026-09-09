# =========================================================
# RoleSync ML Recommendation Engine
# TF-IDF + Cosine Similarity
# =========================================================

import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.skill_engine import normalize_skills


# =========================================================
# DATASET
# =========================================================

DATA_PATH = "data/raw/jobs.csv"


# =========================================================
# ML RECOMMENDATION MODEL
# =========================================================

class RoleRecommendationModel:

    def __init__(self, file_path=DATA_PATH):

        self.file_path = file_path
        self.jobs = None
        self.vectorizer = None
        self.job_matrix = None

    # =====================================================
    # LOAD DATA
    # =====================================================

    def load_data(self):

        self.jobs = pd.read_csv(
            self.file_path
        )

        self.jobs["role"] = (
            self.jobs["role"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        self.jobs["skills"] = (
            self.jobs["skills"]
            .fillna("")
            .astype(str)
            .str.strip()
        )

        if "experience" in self.jobs.columns:

            self.jobs["experience"] = (
                self.jobs["experience"]
                .fillna("")
                .astype(str)
                .str.strip()
            )

        else:

            self.jobs["experience"] = ""

        # Remove jobs without skills
        self.jobs = self.jobs[
            self.jobs["skills"] != ""
        ].copy()

        # Remove duplicates
        self.jobs = self.jobs.drop_duplicates(
            subset=["role", "skills"]
        ).reset_index(
            drop=True
        )

        return self.jobs

    # =====================================================
    # TRAIN / BUILD TF-IDF MATRIX
    # =====================================================

    def train(self):

        if self.jobs is None:
            self.load_data()

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            token_pattern=r"(?u)\b\w[\w+#./-]*\b"
        )

        self.job_matrix = (
            self.vectorizer.fit_transform(
                self.jobs["skills"].tolist()
            )
        )

        return self

    # =====================================================
    # RECOMMEND ROLES
    # =====================================================

    def recommend(
        self,
        user_skills,
        top_n=5
    ):

        if self.vectorizer is None:
            self.train()

        normalized_skills = normalize_skills(
            user_skills
        )

        if not normalized_skills:
            return []

        # Convert user's skills into text
        user_text = " ".join(
            normalized_skills
        )

        # Convert user profile into TF-IDF vector
        user_vector = (
            self.vectorizer.transform(
                [user_text]
            )
        )

        # Calculate similarity
        similarity_scores = cosine_similarity(
            user_vector,
            self.job_matrix
        )[0]

        # Highest similarity first
        ranked_indexes = (
            similarity_scores
            .argsort()[::-1]
        )

        recommendations = []

        limit = min(
            top_n,
            len(ranked_indexes)
        )

        for index in ranked_indexes[:limit]:

            score = round(
                float(
                    similarity_scores[index]
                ) * 100,
                2
            )

            recommendations.append(
                {
                    "role": self.jobs.iloc[index][
                        "role"
                    ],

                    "required_skills": self.jobs.iloc[
                        index
                    ]["skills"],

                    "experience": self.jobs.iloc[
                        index
                    ]["experience"],

                    "ml_match_score": score
                }
            )

        return recommendations


# =========================================================
# PUBLIC FUNCTION
# =========================================================

def ml_recommend_jobs(
    user_skills,
    top_n=5
):
    """
    Creates the ML model and returns
    the highest similarity roles.
    """

    model = RoleRecommendationModel()

    model.load_data()
    model.train()

    return model.recommend(
        user_skills,
        top_n=top_n
    )