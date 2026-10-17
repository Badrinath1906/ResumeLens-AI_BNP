
import re
from collections import OrderedDict

SKILL_ALIASES = OrderedDict({
    "Python": ["python", "python3"],
    "Java": ["java"],
    "C": ["c"],
    "C++": ["c++"],
    "C#": ["c#", "c sharp"],
    "JavaScript": ["javascript", "js"],
    "TypeScript": ["typescript", "ts"],
    "HTML": ["html"],
    "CSS": ["css"],
    "React": ["react", "reactjs", "react.js"],
    "Node.js": ["node.js", "nodejs"],
    "Express.js": ["express.js", "expressjs"],
    "Flask": ["flask"],
    "Django": ["django"],
    "Spring Boot": ["spring boot", "springboot"],
    "SQL": ["sql"],
    "MySQL": ["mysql"],
    "PostgreSQL": ["postgresql", "postgres"],
    "MongoDB": ["mongodb", "mongo db"],
    "Oracle": ["oracle database"],
    "Machine Learning": ["machine learning", "ml"],
    "Deep Learning": ["deep learning"],
    "Artificial Intelligence": ["artificial intelligence", "ai"],
    "Natural Language Processing": [
        "natural language processing",
        "nlp"
    ],
    "Data Science": ["data science"],
    "Data Analysis": ["data analysis", "data analytics"],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "Scikit-learn": ["scikit-learn", "sklearn"],
    "TensorFlow": ["tensorflow"],
    "PyTorch": ["pytorch"],
    "Matplotlib": ["matplotlib"],
    "Seaborn": ["seaborn"],
    "Excel": ["excel", "microsoft excel"],
    "Power BI": ["power bi", "powerbi"],
    "Tableau": ["tableau"],
    "Git": ["git"],
    "GitHub": ["github"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes"],
    "Linux": ["linux"],
    "REST API": ["rest api", "restful api"],
    "GraphQL": ["graphql"],
    "AWS": ["aws", "amazon web services"],
    "Microsoft Azure": ["microsoft azure", "azure"],
    "Google Cloud": ["google cloud", "gcp"],
    "HTML/CSS": ["html/css"],
    "OOP": ["oop", "object-oriented programming"],
    "Data Structures and Algorithms": [
        "data structures and algorithms",
        "dsa"
    ],
    "Problem Solving": ["problem solving"],
    ".NET": [".net", "dotnet"],
    "PHP": ["php"],
    "Ruby": ["ruby"],
    "Go": ["golang"],
    "Rust": ["rust"],
    "R": ["r language"],
    "SAP ABAP": ["sap abap", "abap"],
})


def _contains_skill(text, alias):
    pattern = (
        r"(?<![a-zA-Z0-9])"
        + re.escape(alias)
        + r"(?![a-zA-Z0-9])"
    )
    return re.search(pattern, text, flags=re.IGNORECASE) is not None


def extract_skills(text):
    if not isinstance(text, str) or not text.strip():
        return []

    found_skills = []

    for canonical_name, aliases in SKILL_ALIASES.items():
        for alias in aliases:
            if _contains_skill(text, alias):
                found_skills.append(canonical_name)
                break

    return found_skills


def compare_skills(resume_text, job_description):
    resume_skills = extract_skills(resume_text)
    required_skills = extract_skills(job_description)

    resume_set = set(resume_skills)
    required_set = set(required_skills)

    matched_skills = [
        skill for skill in required_skills
        if skill in resume_set
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_set
    ]

    return {
        "resume_skills": resume_skills,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }
