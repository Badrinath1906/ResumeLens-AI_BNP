# CHeck Resume Sections
# Purpose: Check if the resume contains the required sections (Education, Experience, Skills, etc.)


import re


SECTION_ALIASES = {
    "Education": [
        "education",
        "educational background",
        "academic background",
        "academic qualifications",
    ],
    "Experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
    ],
    "Projects": [
        "projects",
        "personal projects",
        "academic projects",
        "project experience",
    ],
    "Skills": [
        "skills",
        "technical skills",
        "key skills",
        "core competencies",
        "technical competencies",
    ],
    "Certifications": [
        "certifications",
        "certificates",
        "licenses and certifications",
        "professional certifications",
    ],
    "Summary": [
        "summary",
        "professional summary",
        "profile",
        "career summary",
        "career objective",
        "objective",
    ],
    "Achievements": [
        "achievements",
        "accomplishments",
        "awards and achievements",
        "honors and awards",
    ],
    "Internship": [
        "internship",
        "internships",
        "internship experience",
    ],
    "Contact": [
        "contact",
        "contact information",
        "personal details",
    ],
    "Links": [
        "links",
        "social links",
        "professional links",
    ],
}


def _normalize_heading(line):
    line = line.strip().lower()

    line = re.sub(r"^[\W_]+|[\W_]+$", "", line)
    line = re.sub(r"\s+", " ", line)

    return line


def check_missing_sections(resume_text):
    if not isinstance(resume_text, str) or not resume_text.strip():
        return list(SECTION_ALIASES.keys())

    lines = [
        _normalize_heading(line)
        for line in resume_text.splitlines()
        if line.strip()
    ]

    found_sections = set()

    for section, aliases in SECTION_ALIASES.items():
        for line in lines:
            if line in aliases:
                found_sections.add(section)
                break

    missing_sections = [
        section
        for section in SECTION_ALIASES
        if section not in found_sections
    ]

    return missing_sections
