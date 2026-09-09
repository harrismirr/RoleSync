# =========================================================
# RoleSync Skill Intelligence Engine
# =========================================================

import re


# =========================================================
# SKILL ALIASES
# =========================================================

SKILL_ALIASES = {
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "machine learning": "machine learning",

    "ai": "artificial intelligence",
    "artificial-intelligence": "artificial intelligence",

    "js": "javascript",
    "java script": "javascript",

    "ts": "typescript",

    "postgres": "postgresql",
    "postgres sql": "postgresql",
    "postgresql": "postgresql",

    "k8s": "kubernetes",

    "node": "node.js",
    "nodejs": "node.js",

    "reactjs": "react",

    "py": "python",

    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",

    "tf": "tensorflow",

    "nlp": "natural language processing",

    "powerbi": "power bi",

    "ms excel": "excel",

    "gcp": "google cloud",
}


# =========================================================
# KNOWN TECHNICAL SKILLS
# =========================================================

KNOWN_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "node.js",
    "express",
    "django",
    "flask",
    "fastapi",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "redis",
    "oracle",
    "sqlite",

    "pandas",
    "numpy",
    "scipy",
    "matplotlib",
    "seaborn",
    "excel",
    "power bi",
    "tableau",

    "statistics",
    "data analysis",
    "data visualization",
    "data science",

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "natural language processing",
    "computer vision",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "transformers",
    "llms",
    "rag",

    "git",
    "github",
    "docker",
    "kubernetes",
    "linux",
    "terraform",
    "jenkins",
    "ci/cd",

    "aws",
    "azure",
    "google cloud",
    "gcp",

    "spark",
    "hadoop",
    "kafka",

    "rest api",
    "graphql",

    "cybersecurity",
    "networking",
    "penetration testing",
    "ethical hacking",

    "selenium",
    "pytest",
    "junit",

    "android",
    "flutter",
    "react native",

    "figma",
    "agile",
    "scrum",
]


# =========================================================
# NORMALIZATION
# =========================================================

def normalize_skill(skill):
    """
    Converts a skill into a consistent format.
    """

    skill = str(skill).strip().lower()

    if not skill:
        return ""

    return SKILL_ALIASES.get(
        skill,
        skill
    )


def normalize_skills(skills):
    """
    Normalizes a complete skill collection.
    """

    normalized = set()

    for skill in skills:

        normalized_skill = normalize_skill(
            skill
        )

        if normalized_skill:
            normalized.add(
                normalized_skill
            )

    return sorted(normalized)


# =========================================================
# RESUME SKILL EXTRACTION
# =========================================================

def extract_skills_from_resume(resume_text):
    """
    Detects known technical skills inside resume text.
    """

    if not resume_text:
        return []

    text = str(
        resume_text
    ).lower()

    detected_skills = []

    # Longer skills first.
    # This helps phrases such as
    # "machine learning" get detected correctly.
    skills_to_check = sorted(
        KNOWN_SKILLS,
        key=len,
        reverse=True
    )

    for skill in skills_to_check:

        pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )

        if re.search(
            pattern,
            text
        ):

            normalized = normalize_skill(
                skill
            )

            if normalized:
                detected_skills.append(
                    normalized
                )

    return sorted(
        set(detected_skills)
    )


# =========================================================
# SKILL RELATIONSHIPS
# =========================================================

SKILL_RELATIONSHIPS = {

    "python": [
        "pandas",
        "numpy",
        "sql",
        "statistics"
    ],

    "pandas": [
        "python",
        "numpy",
        "data analysis"
    ],

    "numpy": [
        "python",
        "pandas",
        "statistics"
    ],

    "sql": [
        "mysql",
        "postgresql",
        "data analysis"
    ],

    "machine learning": [
        "python",
        "statistics",
        "pandas",
        "numpy",
        "deep learning"
    ],

    "deep learning": [
        "python",
        "machine learning",
        "pytorch",
        "tensorflow"
    ],

    "artificial intelligence": [
        "python",
        "machine learning",
        "deep learning"
    ],

    "data science": [
        "python",
        "statistics",
        "machine learning",
        "sql",
        "pandas"
    ],

    "data analysis": [
        "python",
        "sql",
        "pandas",
        "statistics",
        "data visualization"
    ],

    "data visualization": [
        "matplotlib",
        "seaborn",
        "power bi",
        "tableau"
    ],

    "javascript": [
        "html",
        "css",
        "node.js",
        "react"
    ],

    "typescript": [
        "javascript",
        "react",
        "node.js"
    ],

    "react": [
        "javascript",
        "html",
        "css",
        "typescript"
    ],

    "node.js": [
        "javascript",
        "express",
        "rest api"
    ],

    "docker": [
        "linux",
        "kubernetes",
        "terraform"
    ],

    "kubernetes": [
        "docker",
        "linux",
        "terraform"
    ],

    "aws": [
        "docker",
        "linux",
        "terraform"
    ],

    "azure": [
        "docker",
        "linux",
        "terraform"
    ],

    "google cloud": [
        "docker",
        "linux",
        "terraform"
    ],

    "tensorflow": [
        "python",
        "machine learning",
        "deep learning"
    ],

    "pytorch": [
        "python",
        "machine learning",
        "deep learning"
    ],

    "natural language processing": [
        "python",
        "machine learning",
        "transformers"
    ],

    "transformers": [
        "python",
        "natural language processing",
        "llms"
    ],

    "llms": [
        "python",
        "transformers",
        "rag"
    ],

    "rag": [
        "python",
        "llms",
        "embeddings"
    ],
}


# =========================================================
# RELATIONSHIP HELPERS
# =========================================================

def get_skill_relationships(skill):
    """
    Returns skills related to a given skill.
    """

    normalized_skill = normalize_skill(
        skill
    )

    return SKILL_RELATIONSHIPS.get(
        normalized_skill,
        []
    )


def discover_related_skills(user_skills):
    """
    Finds adjacent skills that could logically
    extend the user's current capabilities.
    """

    normalized_user_skills = set(
        normalize_skills(
            user_skills
        )
    )

    related = set()

    for skill in normalized_user_skills:

        relationships = get_skill_relationships(
            skill
        )

        for related_skill in relationships:

            normalized_related = normalize_skill(
                related_skill
            )

            if (
                normalized_related
                and normalized_related
                not in normalized_user_skills
            ):
                related.add(
                    normalized_related
                )

    return sorted(related)


# =========================================================
# COMPLETE SKILL PROFILE
# =========================================================

def build_skill_profile(user_skills):
    """
    Creates a structured profile containing:
    current skills, related skills and counts.
    """

    normalized_skills = normalize_skills(
        user_skills
    )

    related_skills = discover_related_skills(
        normalized_skills
    )

    return {
        "current_skills": normalized_skills,
        "related_skills": related_skills,
        "skill_count": len(
            normalized_skills
        ),
        "related_skill_count": len(
            related_skills
        )
    }
