#Calculate ATS score based on the extracted text and job description

def calculate_ats_score(
    similarity_score,
    matched_skills,
    total_skills
):
    try:
        similarity_score = float(similarity_score)
        total_skills = int(total_skills)

        if not 0 <= similarity_score <= 100:
            return 0.0

        if total_skills < 0:
            return 0.0

        if total_skills == 0:
            return round(similarity_score, 2)

        matched_count = len(matched_skills)

        if matched_count < 0 or matched_count > total_skills:
            return 0.0

        skill_score = (matched_count / total_skills) * 100

        ats_score = (
            similarity_score * 0.6
            + skill_score * 0.4
        )

        return round(ats_score, 2)

    except (TypeError, ValueError):
        return 0.0
