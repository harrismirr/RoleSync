# =========================================================
# RoleSync | Career Intelligence Platform
# Final Streamlit Application
# =========================================================

import streamlit as st

from src.hybrid_recommender import hybrid_recommend_jobs
from src.resume_parser import parse_resume
from src.skill_engine import (
    extract_skills_from_resume,
    build_skill_profile,
)
from src.roadmap import (
    create_learning_roadmap,
    get_next_skill,
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="RoleSync | Career Intelligence",
    page_icon="◇",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
"""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 85% 8%,
            rgba(45, 212, 191, 0.08),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #07111f 0%,
            #091827 50%,
            #07111f 100%
        );
    color: #e6edf5;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: #f8fafc !important;
}

p {
    color: #91a5b8;
}

hr {
    border-color: rgba(148, 163, 184, 0.12);
}

.stButton > button {
    background: #123244;
    color: #eafaf7;
    border: 1px solid rgba(45, 212, 191, 0.28);
    border-radius: 10px;
    min-height: 44px;
    font-weight: 700;
}

.stButton > button:hover {
    border-color: rgba(45, 212, 191, 0.75);
    color: #ffffff;
}

.stTextInput input {
    background: rgba(10, 27, 43, 0.95);
    color: #f8fafc;
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 10px;
}

.stFileUploader {
    background: rgba(10, 27, 43, 0.70);
    border: 1px solid rgba(45, 212, 191, 0.16);
    border-radius: 14px;
    padding: 10px;
}

[data-testid="stMetric"] {
    background: rgba(10, 27, 43, 0.82);
    border: 1px solid rgba(45, 212, 191, 0.12);
    border-radius: 14px;
    padding: 15px;
}

[data-testid="stMetricLabel"] {
    color: #71879a !important;
}

[data-testid="stMetricValue"] {
    color: #f8fafc !important;
}

</style>
""",
unsafe_allow_html=True,
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ROLE INTELLIGENCE")

    st.write(
        "Analyze your skills, discover suitable "
        "technology roles and identify the "
        "capabilities you should learn next."
    )

    st.divider()

    st.markdown("### Recommendation Engine")

    st.caption(
        "RoleSync combines interpretable skill "
        "coverage with TF-IDF similarity."
    )

    st.divider()

    st.caption("Rule Match: 65%")
    st.caption("ML Similarity: 35%")

    st.divider()

    st.caption(
        "Career Intelligence Platform"
    )


# =========================================================
# HEADER
# =========================================================

header_left, header_right = st.columns(
    [0.7, 9.3],
    vertical_alignment="center",
)

with header_left:

    st.markdown(
        "# ◇"
    )

with header_right:

    st.markdown(
        "## RoleSync"
    )

    st.caption(
        "Career Intelligence Platform"
    )


st.divider()


# =========================================================
# HERO
# =========================================================

st.markdown(
    "### CAREER INTELLIGENCE"
)

st.title(
    "Discover where your skills can take you next."
)

st.write(
    "RoleSync analyzes your current capabilities, "
    "compares them with technology roles, identifies "
    "skill gaps and creates a structured roadmap "
    "for your next career move."
)


# =========================================================
# RESUME INTELLIGENCE
# =========================================================

st.divider()

st.header(
    "Resume Intelligence"
)

st.caption(
    "Upload your PDF resume to automatically discover "
    "your technical skill profile."
)


uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
)


# =========================================================
# RESUME ANALYSIS
# =========================================================

if uploaded_resume is not None:

    try:

        resume_data = parse_resume(
            uploaded_resume
        )

        resume_text = resume_data["text"]

        detected_skills = (
            extract_skills_from_resume(
                resume_text
            )
        )

        profile = build_skill_profile(
            detected_skills
        )

        st.success(
            "Resume analyzed successfully."
        )

        # -----------------------------------------------------
        # RESUME METRICS
        # -----------------------------------------------------

        metric1, metric2, metric3 = st.columns(3)

        with metric1:

            st.metric(
                "Detected Skills",
                profile["skill_count"],
            )

        with metric2:

            st.metric(
                "Related Skills",
                profile["related_skill_count"],
            )

        with metric3:

            st.metric(
                "Resume Pages",
                resume_data["pages"],
            )

        # -----------------------------------------------------
        # DETECTED SKILLS
        # -----------------------------------------------------

        st.subheader(
            "Detected Skill Profile"
        )

        if detected_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in detected_skills
                )
            )

        else:

            st.warning(
                "No recognized technical skills "
                "were detected in this resume."
            )

        # -----------------------------------------------------
        # RELATED SKILLS
        # -----------------------------------------------------

        if profile["related_skills"]:

            st.subheader(
                "Adjacent Capabilities"
            )

            st.write(
                ", ".join(
                    skill.title()
                    for skill in profile[
                        "related_skills"
                    ]
                )
            )

        # =====================================================
        # CAREER INTELLIGENCE
        # =====================================================

        if detected_skills:

            st.divider()

            st.header(
                "Career Intelligence"
            )

            st.caption(
                "Hybrid ranking combines skill coverage "
                "with machine-learning similarity."
            )

            recommendations = hybrid_recommend_jobs(
                detected_skills,
                top_n=5,
            )

            if recommendations:

                best = recommendations[0]

                # -------------------------------------------------
                # BEST FIT
                # -------------------------------------------------

                st.subheader(
                    "Best Fit"
                )

                best_col1, best_col2 = st.columns(
                    [7, 2]
                )

                with best_col1:

                    st.markdown(
                        f"### {best['role']}"
                    )

                    st.caption(
                        "Strongest hybrid career match"
                    )

                with best_col2:

                    st.metric(
                        "Hybrid Match",
                        f"{best['hybrid_score']}%",
                    )

                # -------------------------------------------------
                # TOP ROLE MATCHES
                # -------------------------------------------------

                st.subheader(
                    "Top Role Matches"
                )

                for number, result in enumerate(
                    recommendations,
                    start=1,
                ):

                    with st.container(
                        border=True
                    ):

                        role_col1, role_col2 = st.columns(
                            [7, 2]
                        )

                        with role_col1:

                            st.markdown(
                                f"**{number:02d}  "
                                f"{result['role']}**"
                            )

                        with role_col2:

                            st.metric(
                                "Match",
                                f"{result['hybrid_score']}%",
                            )

                        matched = [
                            skill.strip()
                            for skill in result[
                                "matched_skills"
                            ].split(",")
                            if skill.strip()
                        ]

                        missing = [
                            skill.strip()
                            for skill in result[
                                "missing_skills"
                            ].split(",")
                            if skill.strip()
                        ]

                        if matched:

                            st.write(
                                "**Matched:** "
                                + ", ".join(
                                    skill.title()
                                    for skill in matched
                                )
                            )

                        if missing:

                            st.write(
                                "**To Develop:** "
                                + ", ".join(
                                    skill.title()
                                    for skill in missing
                                )
                            )

                        if result.get(
                            "experience",
                            ""
                        ):

                            st.caption(
                                "Experience: "
                                + str(
                                    result["experience"]
                                )
                            )

                # =================================================
                # RECOMMENDATION BREAKDOWN
                # =================================================

                st.subheader(
                    "Recommendation Breakdown"
                )

                breakdown_data = []

                for result in recommendations:

                    breakdown_data.append(
                        {
                            "Role": result["role"],
                            "Skill Match": (
                                result[
                                    "rule_match_score"
                                ]
                            ),
                            "ML Similarity": (
                                result[
                                    "ml_match_score"
                                ]
                            ),
                            "Hybrid Score": (
                                result[
                                    "hybrid_score"
                                ]
                            ),
                        }
                    )

                st.dataframe(
                    breakdown_data,
                    use_container_width=True,
                    hide_index=True,
                )

                st.caption(
                    "Hybrid Score = "
                    "65% Skill Match + "
                    "35% ML Similarity"
                )

                # =================================================
                # CAREER ROADMAP
                # =================================================

                st.divider()

                st.header(
                    "Career Roadmap"
                )

                st.caption(
                    "Prioritized capabilities to strengthen "
                    "your strongest career direction."
                )

                missing_skills = [
                    skill.strip()
                    for skill in best[
                        "missing_skills"
                    ].split(",")
                    if skill.strip()
                ]

                roadmap = create_learning_roadmap(
                    missing_skills
                )

                if roadmap:

                    for number, item in enumerate(
                        roadmap,
                        start=1,
                    ):

                        with st.container(
                            border=True
                        ):

                            roadmap_col1, roadmap_col2 = st.columns(
                                [6, 2]
                            )

                            with roadmap_col1:

                                st.markdown(
                                    f"**STEP {number:02d}**"
                                )

                                st.markdown(
                                    f"### {item['skill']}"
                                )

                            with roadmap_col2:

                                st.metric(
                                    "Priority",
                                    item[
                                        "priority_label"
                                    ],
                                )

                    next_skill = get_next_skill(
                        missing_skills
                    )

                    if next_skill:

                        st.info(
                            "Recommended next skill: "
                            + next_skill["skill"]
                        )

                else:

                    st.success(
                        "Your current skills strongly "
                        "cover the selected role."
                    )

                # =================================================
                # ROLE REQUIREMENTS
                # =================================================

                st.subheader(
                    "Best-Fit Role Requirements"
                )

                required_skills = [
                    skill.strip()
                    for skill in best[
                        "required_skills"
                    ].split(",")
                    if skill.strip()
                ]

                if required_skills:

                    st.write(
                        ", ".join(
                            skill.title()
                            for skill in required_skills
                        )
                    )

    except Exception as error:

        st.error(
            "RoleSync could not process this resume."
        )

        st.caption(
            "Technical details:"
        )

        st.code(
            str(error)
        )


# =========================================================
# MANUAL SKILL ANALYSIS
# =========================================================

st.divider()

st.header(
    "Manual Skill Analysis"
)

st.caption(
    "Explore RoleSync without uploading a resume."
)


manual_skills_input = st.text_input(
    "Enter your skills",
    placeholder=(
        "Python, SQL, Pandas, Machine Learning"
    ),
)


analyze_button = st.button(
    "Analyze My Skills",
    use_container_width=True,
)


if analyze_button:

    manual_skills = [
        skill.strip()
        for skill in manual_skills_input.split(",")
        if skill.strip()
    ]

    if not manual_skills:

        st.warning(
            "Please enter at least one skill."
        )

    else:

        try:

            manual_results = hybrid_recommend_jobs(
                manual_skills,
                top_n=5,
            )

            if manual_results:

                st.success(
                    "Skill profile analyzed successfully."
                )

                st.subheader(
                    "Manual Profile Analysis"
                )

                st.caption(
                    "These recommendations are based "
                    "on the skills you entered manually."
                )

                for number, result in enumerate(
                    manual_results,
                    start=1,
                ):

                    with st.container(
                        border=True
                    ):

                        result_col1, result_col2 = st.columns(
                            [7, 2]
                        )

                        with result_col1:

                            st.markdown(
                                f"**{number}. "
                                f"{result['role']}**"
                            )

                            matched = [
                                skill.strip()
                                for skill in result[
                                    "matched_skills"
                                ].split(",")
                                if skill.strip()
                            ]

                            missing = [
                                skill.strip()
                                for skill in result[
                                    "missing_skills"
                                ].split(",")
                                if skill.strip()
                            ]

                            if matched:

                                st.caption(
                                    "Matched: "
                                    + ", ".join(
                                        skill.title()
                                        for skill in matched
                                    )
                                )

                            if missing:

                                st.caption(
                                    "To develop: "
                                    + ", ".join(
                                        skill.title()
                                        for skill in missing
                                    )
                                )

                        with result_col2:

                            st.metric(
                                "Hybrid Match",
                                f"{result['hybrid_score']}%",
                            )

            else:

                st.info(
                    "No recommendations were generated."
                )

        except Exception as error:

            st.error(
                "Manual analysis could not be completed."
            )

            st.code(
                str(error)
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    "##### Your career is not defined by what you know today, "
    "but by what you choose to learn next."
)

st.caption(
    "— HARRIS MIR"
)

st.caption(
    "RoleSync · Career Intelligence Platform for "
    "skill discovery, role matching and structured career growth."
)