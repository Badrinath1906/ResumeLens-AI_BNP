#Purpose: Analyze the resume and provide suggestions for improvement
#Check for missing sections (Education, Experience, Skills, etc.)
#Check for missing skills based on job description
#Generate improvement suggestions.

SKILL_SUGGESTIONS = {
    "Python": (
        "If you have Python experience, highlight a project "
        "that demonstrates your programming skills."
    ),
    "Java": (
        "If you know Java, include a relevant project or "
        "problem-solving example using Java."
    ),
    "SQL": (
        "If you have SQL experience, mention queries, joins, "
        "aggregations, or database projects you have completed."
    ),
    "Machine Learning": (
        "Highlight a machine learning project and explain "
        "the dataset, algorithm, and evaluation metric used."
    ),
    "Docker": (
        "If you have used Docker, describe how you containerized "
        "an application or managed its environment."
    ),
    "React": (
        "Include a React project and describe the components "
        "and interactive features you implemented."
    ),
    "Git": (
        "Mention how you used Git for version control and "
        "collaborated on project changes."
    ),
}

SECTION_SUGGESTIONS = {
    "Education": (
        "Add an Education section with your degree, institution, "
        "graduation year, and relevant academic details."
    ),
    "Experience": (
        "If applicable, add your internship or work experience "
        "with responsibilities and measurable achievements."
    ),
    "Projects": (
        "Add a Projects section describing the problem, your "
        "technical approach, tools used, and results."
    ),
    "Skills": (
        "Add a Skills section listing relevant technical skills "
        "that you can confidently demonstrate."
    ),
    "Certifications": (
        "If you have relevant certifications, list their names "
        "and issuing organizations."
    ),
    "Summary": (
        "Consider adding a concise professional summary that "
        "highlights your relevant skills and career goals."
    ),
    "Achievements": (
        "If applicable, include relevant awards, competition "
        "results, or measurable accomplishments."
    ),
    "Internship": (
        "If you have completed an internship, describe your "
        "role, tasks, and contributions."
    ),
    "Contact": (
        "Add appropriate contact information so recruiters can "
        "reach you."
    ),
    "Links": (
        "Consider adding relevant portfolio, GitHub, or "
        "LinkedIn links if available."
    ),
}


def generate_suggestions(missing_skills, missing_sections):
    suggestions = []

    for skill in missing_skills or []:
        if skill in SKILL_SUGGESTIONS:
            suggestion = SKILL_SUGGESTIONS[skill]
        else:
            suggestion = (
                f"If you have experience with {skill}, describe "
                "a relevant project or practical example."
            )

        suggestions.append(suggestion)

    for section in missing_sections or []:
        if section in SECTION_SUGGESTIONS:
            suggestions.append(SECTION_SUGGESTIONS[section])
        else:
            suggestions.append(
                f"Consider adding a {section} section if it "
                "is relevant to your background."
            )

    if not suggestions:
        suggestions.append(
            "No gaps were identified by the current rules. "
            "Review the resume for accuracy, relevance, and clarity."
        )

    return suggestions
