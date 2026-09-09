# =========================================================
# RoleSync Hybrid Recommendation Engine
# Rule-Based Matching + TF-IDF Similarity
# =========================================================

from src.recommender import get_all_recommendations
from src.ml_recommender import ml_recommend_jobs


# =========================================================
# HYBRID RECOMMENDATION
# =========================================================

def hybrid_recommend_jobs(
    user_skills,
    top_n=5
):
    """
    Combines two recommendation signals:

    65% - Rule-based skill coverage
    35% - TF-IDF ML similarity

    Returns the strongest career matches.
    """

    # -----------------------------------------------------
    # Rule-based results
    # -----------------------------------------------------

    rule_results = get_all_recommendations(
        user_skills
    )

    # -----------------------------------------------------
    # ML results
    # -----------------------------------------------------

    ml_results = ml_recommend_jobs(
        user_skills,
        top_n=len(rule_results)
    )

    # -----------------------------------------------------
    # ML lookup by role
    # -----------------------------------------------------

    ml_lookup = {
        item["role"]: item
        for item in ml_results
    }

    hybrid_results = []

    # -----------------------------------------------------
    # Combine scores
    # -----------------------------------------------------

    for item in rule_results:

        role = item["role"]

        ml_item = ml_lookup.get(
            role
        )

        if ml_item:

            ml_score = float(
                ml_item["ml_match_score"]
            )

        else:

            ml_score = 0.0

        rule_score = float(
            item["match_score"]
        )

        # -------------------------------------------------
        # Hybrid score
        # -------------------------------------------------

        hybrid_score = round(
            (
                rule_score * 0.65
            )
            +
            (
                ml_score * 0.35
            ),
            2
        )

        hybrid_results.append(
            {
                "role": role,

                "required_skills": item[
                    "required_skills"
                ],

                "matched_skills": item[
                    "matched_skills"
                ],

                "missing_skills": item[
                    "missing_skills"
                ],

                "experience": item.get(
                    "experience",
                    ""
                ),

                "rule_match_score": round(
                    rule_score,
                    2
                ),

                "ml_match_score": round(
                    ml_score,
                    2
                ),

                "hybrid_score": hybrid_score
            }
        )

    # -----------------------------------------------------
    # Sort by hybrid score
    # -----------------------------------------------------

    hybrid_results = sorted(
        hybrid_results,
        key=lambda item: (
            item["hybrid_score"],
            item["rule_match_score"],
            item["ml_match_score"]
        ),
        reverse=True
    )

    return hybrid_results[
        :top_n
    ]
