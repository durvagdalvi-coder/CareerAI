import streamlit as st

from text_extractor import extract_text

from matcher import analyze_match

from recommendations import (
    generate_suggestions,
    generate_summary,
    generate_questions
)

from report_generator import generate_report

from role_detector import detect_role



st.set_page_config(
    page_title="CareerAI",
    page_icon="🚀",
    layout="wide"
)



# ----------------------------
# PREMIUM STYLE
# ----------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #f7f9fc;
    }


    h1 {
        font-size: 48px !important;
        font-weight: 800 !important;
    }


    .card {

        background:white;

        padding:25px;

        border-radius:18px;

        box-shadow:
        0 8px 25px rgba(0,0,0,0.08);

        text-align:center;

        margin-bottom:20px;

    }


    .big {

        font-size:45px;

        font-weight:800;

    }


    .badge {

        display:inline-block;

        padding:8px 15px;

        margin:5px;

        border-radius:20px;

        background:#eef2ff;

        font-weight:600;

    }

    </style>

    """,
    unsafe_allow_html=True
)



# ----------------------------
# HEADER
# ----------------------------

st.title(
    "🚀 CareerAI"
)


st.subheader(
    "AI-Assisted Resume Optimization Platform"
)


st.write(
    """
    Analyze your resume against any job description.
    Discover your match score, skills, gaps,
    and resume improvement areas.
    """
)


st.divider()



# ----------------------------
# INPUT SECTION
# ----------------------------

left, right = st.columns(2)



with left:

    st.subheader(
        "📄 Resume"
    )


    resume_method = st.radio(
        "Resume Input",
        [
            "Upload File",
            "Paste Text"
        ],
        key="resume_input"
    )


    resume_text = ""


    if resume_method == "Upload File":

        resume_file = st.file_uploader(
            "Upload Resume",
            type=[
                "pdf",
                "docx",
                "txt"
            ]
        )


        if resume_file:

            resume_text = extract_text(
                resume_file
            )


    else:

        resume_text = st.text_area(
            "Paste Resume",
            height=200
        )





with right:

    st.subheader(
        "💼 Job Description"
    )


    job_method = st.radio(
        "Job Input",
        [
            "Upload File",
            "Paste Text"
        ],
        key="job_input"
    )


    job_text = ""


    if job_method == "Upload File":

        job_file = st.file_uploader(
            "Upload Job Description",
            type=[
                "pdf",
                "docx",
                "txt"
            ]
        )


        if job_file:

            job_text = extract_text(
                job_file
            )


    else:

        job_text = st.text_area(
            "Paste Job Description",
            height=200
        )



st.divider()



# ----------------------------
# ANALYSIS
# ----------------------------

if st.button(
    "🚀 Analyze Career Match",
    use_container_width=True
):


    if resume_text and job_text:


        result = analyze_match(
            resume_text,
            job_text
        )


        role = detect_role(
            job_text
        )


        # Smart role-based suggestions

        suggestions = generate_suggestions(
            result["missing"],
            role["role"]
        )


        summary = generate_summary(
            result["matched"]
        )


        questions = generate_questions(
            role["role"]
        )



        report = generate_report(
            result["score"],
            result["matched"],
            result["missing"],
            suggestions,
            summary,
            questions
        )



        st.success(
            "CareerAI Analysis Complete"
        )



        # ----------------------------
        # ROLE DETECTION
        # ----------------------------

        st.header(
            "🎯 Detected Job Profile"
        )


        c1, c2 = st.columns(2)



        with c1:

            st.markdown(
                f"""
                <div class="card">

                <div class="big">
                🎯
                </div>

                <h3>
                {role["role"]}
                </h3>

                Detected Role

                </div>
                """,
                unsafe_allow_html=True
            )



        with c2:

            st.markdown(
                f"""
                <div class="card">

                <div class="big">
                🏢
                </div>

                <h3>
                {role["industry"]}
                </h3>

                Industry

                </div>
                """,
                unsafe_allow_html=True
            )



        # ----------------------------
        # SCORE
        # ----------------------------

        st.header(
            "📊 Career Match Score"
        )


        a,b,c = st.columns(3)



        with a:

            st.metric(
                "ATS Score",
                f'{result["score"]}%'
            )


        with b:

            st.metric(
                "Matched Skills",
                len(result["matched"])
            )


        with c:

            st.metric(
                "Skill Gaps",
                len(result["missing"])
            )



        st.divider()



        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🎯 Skills",
                "💡 Suggestions",
                "📝 Summary",
                "📄 Report"
            ]
        )



        with tab1:

            st.subheader(
                "Matched Skills"
            )


            for skill in result["matched"]:

                st.markdown(
                    f"""
                    <span class="badge">
                    ✅ {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )



            st.subheader(
                "Skill Gaps"
            )


            for skill in result["missing"]:

                st.markdown(
                    f"""
                    <span class="badge">
                    ⚠️ {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )



        with tab2:

            st.subheader(
                "Resume Improvement Suggestions"
            )


            if suggestions:

                for item in suggestions:

                    st.write(
                        "⭐ " + item
                    )

            else:

                st.write(
                    "No major improvement areas detected."
                )



        with tab3:

            st.subheader(
                "Professional Summary"
            )


            st.info(
                summary
            )



        with tab4:

            st.subheader(
                "CareerAI Analysis Report"
            )


            st.text_area(
                "Report Preview",
                report,
                height=500
            )


            st.download_button(
                "⬇️ Download Report",
                report,
                file_name="CareerAI_Report.txt",
                use_container_width=True
            )



    else:


        st.warning(
            "Please provide both resume and job description."
        )