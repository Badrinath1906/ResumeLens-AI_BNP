
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):
    if not isinstance(resume_text, str):
        return 0.0

    if not isinstance(job_description, str):
        return 0.0

    resume_text = resume_text.strip()
    job_description = job_description.strip()

    if not resume_text or not job_description:
        return 0.0

    try:
        vectorizer = TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2)
        )

        tfidf_matrix = vectorizer.fit_transform(
            [resume_text, job_description]
        )

        score = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        return round(float(score * 100), 2)

    except ValueError:
        return 0.0
