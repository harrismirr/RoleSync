# =========================================================
# RoleSync Career Roadmap Engine
# =========================================================


# =========================================================
# SKILL PRIORITY
# =========================================================

SKILL_PRIORITY = {

    "python": 5,
    "sql": 5,
    "machine learning": 5,
    "statistics": 5,
    "data science": 5,
    "data analysis": 5,

    "deep learning": 5,
    "pytorch": 5,
    "tensorflow": 5,
    "natural language processing": 5,
    "transformers": 5,
    "llms": 5,
    "rag": 5,

    "kubernetes": 5,

    "pandas": 4,
    "numpy": 4,
    "data visualization": 4,
    "power bi": 4,
    "tableau": 4,
    "excel": 4,

    "docker": 4,
    "terraform": 4,
    "aws": 4,
    "azure": 4,
    "google cloud": 4,

    "javascript": 4,
    "typescript": 4,
    "react": 4,
    "node.js": 4,

    "git": 3,
    "github": 3,
    "linux": 3,

    "mysql": 3,
    "postgresql": 3,
    "mongodb": 3,

    "html": 3,
    "css": 3,

    "selenium": 3,
    "pytest": 3,
    "junit": 3,

    "networking": 3,
    "cybersecurity": 3,

    "figma": 2,
    "agile": 2,
    "scrum": 2,
}


# =========================================================
# PRIORITY SCORE
# =========================================================

def get_skill_priority(skill):
    """
    Returns the learning priority score for a skill.
    """

    skill = str(
        skill
    ).strip().lower()

    return SKILL_PRIORITY.get(
        skill,
        3
    )


# =========================================================
# PRIORITY LABEL
# =========================================================

def get_priority_label(skill):
    """
    Converts numerical priority into
    a human-readable category.
    """

    priority = get_skill_priority(
        skill
    )

    if priority >= 5:
        return "High Priority"

    if priority >= 4:
        return "Recommended"

    return "Useful"


# =========================================================
# ROADMAP CREATION
# =========================================================

def create_learning_roadmap(
    missing_skills
):
    """
    Creates a prioritized learning roadmap
    from missing technical skills.
    """

    roadmap = []

    seen_skills = set()

    for skill in missing_skills:

        skill = str(
            skill
        ).strip().lower()

        if not skill:
            continue

        # Avoid duplicate roadmap entries
        if skill in seen_skills:
            continue

        seen_skills.add(
            skill
        )

        priority = get_skill_priority(
            skill
        )

        roadmap.append(
            {
                "skill": skill.title(),

                "priority": priority,

                "priority_label": get_priority_label(
                    skill
                )
            }
        )

    # Highest priority first
    roadmap = sorted(
        roadmap,
        key=lambda item: (
            item["priority"],
            item["skill"]
        ),
        reverse=True
    )

    return roadmap


# =========================================================
# NEXT SKILL
# =========================================================

def get_next_skill(
    missing_skills
):
    """
    Returns the highest-priority
    next skill to learn.
    """

    roadmap = create_learning_roadmap(
        missing_skills
    )

    if not roadmap:
        return None

    return roadmap[0]
