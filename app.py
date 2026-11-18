
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from career_model import recommend, load_roles

st.set_page_config(
    page_title="CareerPath AI",
    page_icon="🎯",
    layout="wide"
)

# ---------------- CUSTOM DESIGN ----------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f3ff, #eef4ff);
    color: #202846;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    max-width: 1350px;
}

h1, h2, h3 {
    color: #30245f !important;
    font-weight: 750 !important;
}

.hero {
    background: linear-gradient(120deg, #5536a5, #3478d4);
    padding: 38px;
    border-radius: 24px;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(64, 55, 140, .18);
}

.hero h1 {
    color: white !important;
    font-size: 2.7rem;
    margin-bottom: 8px;
}

.hero p {
    color: #eeeeff;
    font-size: 1.08rem;
}

.panel {
    background: white;
    border: 1px solid #e5e7f4;
    border-radius: 18px;
    padding: 22px;
    margin: 10px 0;
    box-shadow: 0 5px 20px rgba(43, 54, 100, .07);
}

.metric {
    font-size: 2rem;
    font-weight: 800;
    color: #6544c8;
}

.small {
    color: #727b99;
    font-size: .9rem;
}

div.stButton > button {
    background: linear-gradient(90deg, #6845c5, #3478d4);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
    transition: .3s;
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #47318e, #245ca8);
    color: white;
    border: none;
    transform: translateY(-2px);
}

div.stDownloadButton > button {
    background: #e9e3ff;
    color: #50359e;
    border-radius: 10px;
    border: 1px solid #d4c9fa;
    font-weight: 700;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
    background-color: white;
    border-radius: 10px;
    border-color: #d9d7eb;
}

[data-testid="stFileUploader"] {
    background: white;
    padding: 12px;
    border-radius: 12px;
    border: 1px dashed #a89bd8;
}

[data-testid="stMetric"] {
    background: #f5f2ff;
    padding: 15px;
    border-radius: 12px;
}

hr {
    border-color: #dedcf0;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SESSION STATE ----------------

if "results" not in st.session_state:
    st.session_state.results = None

# ---------------- HERO SECTION ----------------

st.markdown("""
<div class="hero">
    <h1>🎯 CareerPath AI</h1>
    <p>AI-Powered Career Guidance & Job Prediction Platform</p>
    <p>Discover your strengths, explore career opportunities
    and build your professional future with Artificial Intelligence.</p>
</div>
""", unsafe_allow_html=True)


# ---------------- TOP INFORMATION CARDS ----------------

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="panel">
        <div class="metric">🤖 AI</div>
        <b>Smart Recommendations</b>
        <p class="small">Machine learning based career matching.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="panel">
        <div class="metric">📊 Skills</div>
        <b>Skill Gap Analysis</b>
        <p class="small">Discover skills you need to improve.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="panel">
        <div class="metric">🚀 Future</div>
        <b>Career Roadmap</b>
        <p class="small">Plan your next learning steps.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- STUDENT PROFILE ----------------

st.markdown("## 👤 Student Career Profile")
st.write("Enter your academic details, skills and interests below.")

left, right = st.columns([1.1, .9], gap="large")

with left:

    with st.container(border=True):

        st.subheader("🎓 Academic Information")

        education = st.selectbox(
            "Highest education",
            ["Diploma", "BCA / BSc", "B.Tech / BE",
             "MCA / MSc", "M.Tech / ME", "MBA", "Other"]
        )

        field = st.selectbox(
            "Study specialization",
            ["Computer Science", "Data Science",
             "Artificial Intelligence", "Information Technology",
             "Electronics", "Business", "Design", "Other"]
        )

        experience = st.selectbox(
            "Experience level",
            ["Fresher", "Internship", "Less than 1 year",
             "1–3 years", "3–5 years", "5+ years"]
        )

        st.subheader("💡 Skills & Interests")

        skills = st.text_area(
            "Your skills",
            placeholder="Python, SQL, Machine Learning, Pandas, Excel",
            height=100
        )

        interests = st.text_area(
            "Career interests",
            placeholder="Artificial Intelligence, Data Analytics, Software Development",
            height=80
        )

        projects = st.text_area(
            "Projects or certifications",
            placeholder="House Price Prediction, Python Certification",
            height=75
        )

        st.subheader("📄 Upload Resume")

        uploaded = st.file_uploader(
            "Upload PDF, DOCX or TXT",
            type=["pdf", "docx", "txt"]
        )

        analyze = st.button(
            "✨ Analyze My Career",
            use_container_width=True
        )

with right:

    st.markdown("### 🌟 What You Will Discover")

    st.markdown("""
    <div class="panel">
        <h3>🏆 Top 3 Career Matches</h3>
        <p class="small">Explore the three most relevant career roles based on your profile.</p>
    </div>

    <div class="panel">
        <h3>🧠 Skill Gap Analysis</h3>
        <p class="small">Identify your existing skills and areas that need improvement.</p>
    </div>

    <div class="panel">
        <h3>📚 Learning Roadmap</h3>
        <p class="small">Get suggested learning steps to prepare for your selected career.</p>
    </div>

    <div class="panel">
        <h3>💰 Salary Insights</h3>
        <p class="small">Explore indicative salary ranges for recommended job roles.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("💡 Tip: Add specific technical skills for better career matching.")


# ---------------- CAREER ANALYSIS ----------------

if analyze:

    resume_text = ""

    if uploaded:
        try:
            if uploaded.name.lower().endswith(".pdf"):
                from pypdf import PdfReader
                reader = PdfReader(uploaded)
                resume_text = " ".join(
                    page.extract_text() or "" for page in reader.pages
                )

            elif uploaded.name.lower().endswith(".docx"):
                from docx import Document
                doc = Document(uploaded)
                resume_text = " ".join(
                    p.text for p in doc.paragraphs
                )

            else:
                resume_text = uploaded.read().decode(
                    "utf-8", errors="ignore"
                )

        except Exception as e:
            st.warning(f"Could not read resume: {e}")

    profile = " ".join([
        education, field, experience,
        skills, interests, projects, resume_text
    ]).strip()

    if len(profile) < 12:
        st.error("Please enter education and some skills or interests.")

    else:
        with st.spinner("🤖 AI is analyzing your career profile..."):
            st.session_state.results, st.session_state.model_score = recommend(profile, 3)
            st.session_state.profile = profile

        st.success("Career analysis completed successfully!")


# ---------------- RESULTS ----------------

if st.session_state.results:

    st.divider()

    st.markdown("## 🚀 Your Career Recommendations")

    results = st.session_state.results

    cols = st.columns(3)

    for col, item in zip(cols, results):

        with col:

            with st.container(border=True):

                st.markdown("### 🏆 " + str(item["role"]))

                st.caption(item["category"])

                st.metric(
                    "Model Match Score",
                    f'{item["model_score"]*100:.1f}%'
                )

                st.markdown("**✅ Matched Skills**")

                st.write(
                    ", ".join(item["matched_skills"])
                    if item["matched_skills"]
                    else "Add role-specific skills."
                )

                st.markdown("**📌 Skills to Develop**")

                st.write(
                    ", ".join(item["missing_skills"][:6])
                    if item["missing_skills"]
                    else "Your listed skills cover this role's sample skill profile."
                )

                st.markdown("**💰 Indicative Salary Range**")

                st.write(
                    f'₹{item["salary_min_lpa"]:g} – ₹{item["salary_max_lpa"]:g} LPA'
                )

                st.markdown("**🗺️ Career Roadmap**")

                st.write(item["roadmap"])

                st.caption(
                    "Illustrative salary estimate; actual pay varies."
                )


    # ---------------- CHART ----------------

    st.markdown("## 📈 Career Match Analytics")

    chart_df = pd.DataFrame({
        "Career Role": [r["role"] for r in results],
        "Model Match Score (%)": [
            round(r["model_score"]*100, 1) for r in results
        ]
    })

    st.bar_chart(
        chart_df.set_index("Career Role"),
        color="#7656ce"
    )

    st.caption(
        f"Internal holdout accuracy on synthetic examples: "
        f"{st.session_state.model_score*100:.1f}%. "
        "This is not real-world hiring accuracy."
    )

    # ---------------- DOWNLOAD REPORT ----------------

    report = pd.DataFrame([{
        "Recommended role": r["role"],
        "Category": r["category"],
        "Model match score (%)": round(r["model_score"]*100, 1),
        "Matched skills": ", ".join(r["matched_skills"]),
        "Skills to develop": ", ".join(r["missing_skills"]),
        "Indicative salary min (LPA)": r["salary_min_lpa"],
        "Indicative salary max (LPA)": r["salary_max_lpa"],
        "Roadmap": r["roadmap"]
    } for r in results])

    st.download_button(
        "⬇️ Download Career Report (CSV)",
        report.to_csv(index=False).encode("utf-8"),
        file_name="careerpath_ai_report.csv",
        mime="text/csv"
    )


# ---------------- ABOUT ----------------

with st.expander("ℹ️ About CareerPath AI"):

    st.write("""
    CareerPath AI is an academic machine-learning project
    designed to recommend career roles based on student
    education, skills, interests and experience.

    Model: TF-IDF + Logistic Regression.

    The recommendations and salary bands are educational
    examples and are not guarantees of employment or salary.
    """)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:15px; color:#777;">
    <b>CareerPath AI</b><br>
    M.Tech AIML Academic Project<br>
    Built using Python, Streamlit, Pandas and Scikit-learn
</div>
""", unsafe_allow_html=True)
