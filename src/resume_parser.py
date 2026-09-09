# =========================================================
# RoleSync Resume Intelligence
# PDF Resume Parsing Engine
# =========================================================

from pypdf import PdfReader


# =========================================================
# EXTRACT PDF TEXT
# =========================================================

def extract_text_from_pdf(file):
    """
    Extracts text from every page of a PDF resume.
    """

    reader = PdfReader(file)

    pages_text = []

    for page in reader.pages:

        text = page.extract_text()

        if text:
            pages_text.append(
                text
            )

    return "\n".join(
        pages_text
    )


# =========================================================
# CLEAN RESUME TEXT
# =========================================================

def clean_resume_text(text):
    """
    Cleans unnecessary blank lines and spaces.
    """

    if not text:
        return ""

    lines = []

    for line in str(text).splitlines():

        line = " ".join(
            line.strip().split()
        )

        if line:
            lines.append(
                line
            )

    return "\n".join(
        lines
    )


# =========================================================
# PARSE RESUME
# =========================================================

def parse_resume(file):
    """
    Parses a PDF resume and returns
    structured resume information.
    """

    reader = PdfReader(file)

    raw_text = extract_text_from_pdf(
        file
    )

    cleaned_text = clean_resume_text(
        raw_text
    )

    return {
        "text": cleaned_text,

        "characters": len(
            cleaned_text
        ),

        "pages": len(
            reader.pages
        )
    }