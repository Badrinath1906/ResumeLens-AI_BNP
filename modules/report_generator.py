# modules/report_generator.py


def generate_report(
    ats_score,
    similarity_score,
    matched_skills,
    missing_skills,
    missing_sections,
    suggestions
):
    matched_skills = matched_skills or []
    missing_skills = missing_skills or []
    missing_sections = missing_sections or []
    suggestions = suggestions or []

    report = []

    report.append("=" * 50)
    report.append("          RESUMELENS AI - ANALYSIS REPORT")
    report.append("=" * 50)

    report.append(f"\nATS Score: {ats_score}%")
    report.append(f"Similarity Score: {similarity_score}%")

    report.append("\n--- Matched Skills ---")
    if matched_skills:
        report.extend(f"- {skill}" for skill in matched_skills)
    else:
        report.append("No matching skills detected.")

    report.append("\n--- Missing Skills ---")
    if missing_skills:
        report.extend(f"- {skill}" for skill in missing_skills)
    else:
        report.append("No missing skills detected.")

    report.append("\n--- Missing Resume Sections ---")
    if missing_sections:
        report.extend(f"- {section}" for section in missing_sections)
    else:
        report.append("No missing sections detected.")

    report.append("\n--- Suggestions ---")
    if suggestions:
        report.extend(
            f"{index}. {suggestion}"
            for index, suggestion in enumerate(suggestions, start=1)
        )
    else:
        report.append("No suggestions available.")

    report.append("\n" + "=" * 50)
    report.append("End of Report")

    return "\n".join(report)
