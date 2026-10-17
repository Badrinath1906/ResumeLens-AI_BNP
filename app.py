
import streamlit as st
import plotly.express as px
import nltk

# ==========================
# IMPORT MODULES
# ==========================

from modules.pdf_parser import extract_text_from_pdf
from modules.similarity import calculate_similarity
from modules.skill_extractor import extract_skills
from modules.ats_score import calculate_ats_score
from modules.section_checker import check_missing_sections
from modules.suggestions import generate_suggestions
from modules.report_generator import generate_report


# ==========================
# NLTK DOWNLOADS
# ==========================

nltk.download("punkt")
nltk.download("stopwords")


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="ResumeLens AI",
    page_icon="🚀",
    layout="wide"
)


# ==========================
# PROFESSIONAL UI STYLING
# ==========================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');

.stApp {
    background: #f4f7fb;
    color: #172033;
    font-family: 'DM Sans', sans-serif;
}

.block-container {
    max-width: 1450px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

section[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263248;
}

section[data-testid="stSidebar"] * {
    color: #e8edf7;
}

.hero {
    padding: 35px;
    border-radius: 24px;
    background: linear-gradient(120deg, #171e36, #292c63, #5146c8);
    margin-bottom: 28px;
    box-shadow: 0 12px 35px rgba(36, 39, 90, 0.14);
}

.hero-label {
    color: #c7d2fe;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.hero h1 {
    color: white;
    font-family: 'Manrope', sans-serif;
    font-size: 38px;
    font-weight: 800;
    margin: 12px 0;
}

.hero p {
    color: #e0e7ff;
    font-size: 15px;
    margin-bottom: 0;
}

.section-heading {
    font-family: 'Manrope', sans-serif;
    color: #172033;
    font-size: 23px;
    font-weight: 800;
    margin-top: 20px;
}

.section-description {
    color: #68748a;
    font-size: 13px;
    margin-bottom: 20px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 17px;
    padding: 20px;
    box-shadow: 0 5px 18px rgba(24, 39, 75, 0.04);
}

div[data-testid="stMetricLabel"] {
    color: #68748a;
    font-size: 13px;
    font-weight: 600;
}

div[data-testid="stMetricValue"] {
    color: #172033;
    font-family: 'Manrope', sans-serif;
    font-weight: 800;
}

div[data-testid="stFileUploader"],
div[data-testid="stTextArea"] {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 15px;
    padding: 12px;
}

.stButton > button,
.stDownloadButton > button {
    min-height: 46px;
    border-radius: 12px;
    font-weight: 700;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #4f46e5, #7c3aed);
    color: white;
    border: none;
}

.stButton > button:hover,
.stDownloadButton > button:hover {
    border-color: #4338ca;
}

.result-card {
    background: white;
    border: 1px solid #e5eaf2;
    border-radius: 17px;
    padding: 22px;
    margin-bottom: 16px;
}

.skill-chip {
    display: inline-block;
    padding: 7px 11px;
    margin: 4px;
    border-radius: 9px;
    font-size: 12px;
    font-weight: 700;
}

.matched-chip {
    color: #087f5b;
    background: #e6f8f1;
    border: 1px solid #c5efdf;
}

.missing-chip {
    color: #b4233d;
    background: #fff0f2;
    border: 1px solid #ffd8df;
}

.footer {
    text-align: center;
    color: #8791a4;
    font-size: 11px;
    padding-top: 30px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}

@media (max-width: 700px) {
    .hero {
        padding: 23px;
    }

    .hero h1 {
        font-size: 28px;
    }

    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================
# CUSTOM HEADER
# ==========================

st.markdown("""
<div class="hero">
    <div class="hero-label">Career Toolkit · Resume Intelligence</div>
    <h1>🚀 ResumeLens AI</h1>
    <p>
        Analyze your resume, compare it with a job description,
        identify skill gaps, and discover opportunities to improve.
    </p>
</div>
""", unsafe_allow_html=True)


# ==========================
# SIDEBAR
# ==========================

with st.sidebar:

    st.markdown("## 🚀 ResumeLens AI")
    st.caption("Your resume analysis workspace")

    st.markdown("---")

    st.header("📌 About Project")

    st.info("""
    ResumeLens AI helps you:

    ✅ ATS Score Calculation

    ✅ Resume Matching

    ✅ Skill Gap Analysis

    ✅ Resume Section Analysis

    ✅ Improvement Suggestions
    """)

    st.markdown("---")

    st.header("📖 How To Use")

    st.write("""
    1. Upload Resume PDF

    2. Paste Job Description

    3. Click Analyze Resume

    4. Review Results

    5. Download Analysis Report
    """)

    st.markdown("---")
    st.caption("Scores are estimates based on the project's current methods.")


# ==========================
# FILE UPLOAD
# ==========================

st.markdown(
    '<div class="section-heading">Start an analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Upload your resume and paste the job description you want to target.'
    '</div>',
    unsafe_allow_html=True
)

col_input1, col_input2 = st.columns([0.9, 1.1], gap="large")

with col_input1:

    st.markdown("#### 📄 Your Resume")

    uploaded_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    if uploaded_file:
        st.success(f"File selected: {uploaded_file.name}")

with col_input2:

    st.markdown("#### 📝 Target Job")

    job_description = st.text_area(
        "Paste Job Description",
        height=220,
        placeholder="Paste the complete job description here..."
    )

    st.caption(f"{len(job_description.split())} words entered")


# ==========================
# ANALYZE BUTTON
# ==========================

if st.button("🚀 Analyze Resume", type="primary", use_container_width=True):

    if not uploaded_file:
        st.warning("Please upload a resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please paste a Job Description.")
        st.stop()

    with st.spinner("Analyzing Resume..."):

        # ==========================
        # EXTRACT TEXT
        # ==========================

        try:
            resume_text = extract_text_from_pdf(uploaded_file)
        except ValueError as exc:
            st.error(f"Unable to read PDF: {exc}")
            st.stop()
        except Exception:
            st.error("Unable to read this PDF. Please upload a valid PDF.")
            st.stop()

        if not resume_text:
            st.error("Unable to extract text from PDF.")
            st.stop()

        # ==========================
        # SIMILARITY SCORE
        # ==========================

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # ==========================
        # SKILL EXTRACTION
        # ==========================

        resume_skills = set(
            extract_skills(resume_text)
        )

        job_skills = set(
            extract_skills(job_description)
        )

        matched_skills = sorted(
            resume_skills & job_skills
        )

        missing_skills = sorted(
            job_skills - resume_skills
        )

        # ==========================
        # ATS SCORE
        # ==========================

        ats_score = calculate_ats_score(
            similarity_score,
            matched_skills,
            len(job_skills)
        )

        # ==========================
        # SECTION ANALYSIS
        # ==========================

        missing_sections = check_missing_sections(
            resume_text
        )

        # ==========================
        # SUGGESTIONS
        # ==========================

        suggestions = generate_suggestions(
            missing_skills,
            missing_sections
        )

        report = generate_report(
            ats_score,
            similarity_score,
            matched_skills,
            missing_skills,
            missing_sections,
            suggestions
        )


        # ==========================
        # DASHBOARD
        # ==========================

        st.markdown("---")

        st.markdown(
            '<div class="section-heading">📊 Resume Dashboard</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-description">'
            'Here is your resume analysis at a glance.'
            '</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "ATS Score",
                f"{ats_score}%"
            )

        with col2:
            st.metric(
                "Match Score",
                f"{similarity_score}%"
            )

        with col3:
            st.metric(
                "Matched Skills",
                len(matched_skills)
            )

        with col4:
            st.metric(
                "Missing Skills",
                len(missing_skills)
            )


        # ==========================
        # RESUME RATING
        # ==========================

        if ats_score >= 85:
            rating = "🏆 Excellent"

        elif ats_score >= 70:
            rating = "🥇 Good"

        elif ats_score >= 50:
            rating = "⚠ Average"

        else:
            rating = "❌ Needs Improvement"

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader("Resume Rating")
        st.success(rating)
        st.markdown('</div>', unsafe_allow_html=True)


        # ==========================
        # PROGRESS BARS
        # ==========================

        progress_col1, progress_col2 = st.columns(2, gap="large")

        with progress_col1:
            st.subheader("📈 ATS Strength")
            st.progress(
                max(0.0, min(float(ats_score), 100.0)) / 100.0
            )
            st.caption(f"{ats_score}%")

        with progress_col2:
            st.subheader("🎯 Resume Match")
            st.progress(
                max(0.0, min(float(similarity_score), 100.0)) / 100.0
            )
            st.caption(f"{similarity_score}%")


        # ==========================
        # RESULTS TABS
        # ==========================

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📊 Overview",
            "✅ Matched Skills",
            "❌ Missing Skills",
            "📌 Resume Sections",
            "💡 Suggestions & Report"
        ])


        # ==========================
        # PIE CHART
        # ==========================

        with tab1:

            st.subheader("📊 Skill Analysis")

            if matched_skills or missing_skills:

                fig = px.pie(
                    values=[
                        len(matched_skills),
                        len(missing_skills)
                    ],
                    names=[
                        "Matched Skills",
                        "Missing Skills"
                    ],
                    title="Skill Distribution",
                    hole=0.55,
                    color_discrete_sequence=[
                        "#10b981",
                        "#f87171"
                    ]
                )

                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    margin=dict(l=10, r=10, t=50, b=10),
                    legend=dict(orientation="h", y=-0.1)
                )

                fig.update_traces(
                    textposition="inside",
                    textinfo="percent+value"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No recognized skills found in the job description.")

            st.markdown("### Analysis Summary")
            st.write(f"Skills detected in resume: **{len(resume_skills)}**")
            st.write(f"Skills detected in job description: **{len(job_skills)}**")
            st.write(f"Missing resume sections: **{len(missing_sections)}**")


        # ==========================
        # MATCHED SKILLS
        # ==========================

        with tab2:

            st.subheader("✅ Matched Skills")

            if matched_skills:

                for skill in matched_skills:
                    st.markdown(
                        f'<span class="skill-chip matched-chip">{skill}</span>',
                        unsafe_allow_html=True
                    )

            else:
                st.warning("No matching skills found.")


        # ==========================
        # MISSING SKILLS
        # ==========================

        with tab3:

            st.subheader("❌ Missing Skills")

            if missing_skills:

                for skill in missing_skills:
                    st.markdown(
                        f'<span class="skill-chip missing-chip">{skill}</span>',
                        unsafe_allow_html=True
                    )

            else:
                st.success("No missing skills detected by the current rules.")

            st.caption(
                "Only add a skill to your resume if you genuinely have that skill."
            )


        # ==========================
        # MISSING SECTIONS
        # ==========================

        with tab4:

            st.subheader("📌 Missing Resume Sections")

            if missing_sections:

                for section in missing_sections:
                    st.warning(f"⚠ {section.title()}")

            else:
                st.success("All important sections found.")

            st.caption(
                "Section detection depends on the headings recognized by the current module."
            )


        # ==========================
        # SUGGESTIONS
        # ==========================

        with tab5:

            st.subheader("💡 Improvement Suggestions")

            if suggestions:

                for suggestion in suggestions:
                    st.info(suggestion)

            else:
                st.success("No suggestions available.")

            st.markdown("---")

            st.subheader("📥 Download Analysis Report")

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="resume_analysis_report.txt",
                mime="text/plain",
                use_container_width=True
            )

            with st.expander("Preview Report"):
                st.text(report)


        # ==========================
        # FINAL RESULT
        # ==========================

        st.markdown("---")

        st.success("🎉 Resume analyzed successfully.")


# ==========================
# FOOTER
# ==========================

st.markdown(
    '<div class="footer">'
    'AI Resume Analyzer · NLP-based resume analysis · '
    'Scores are estimates, not hiring decisions.'
    '</div>',
    unsafe_allow_html=True
)
