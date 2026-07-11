# ==========================================================
# CareerAI - AI Powered Placement Prediction System
# Developed by: Aditi Sharma
# ==========================================================

# -----------------------------
# Import Libraries
# -----------------------------

import streamlit as st
import pandas as pd
import joblib
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from resume.resume_parser import extract_resume_text

# -----------------------------
# Streamlit Page Configuration
# -----------------------------

st.set_page_config(
    page_title="CareerAI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load Machine Learning Model
# -----------------------------

MODEL_PATH = os.path.join(
    "saved_models",
    "careerai_model.pkl"
)

if os.path.exists(MODEL_PATH):

    model = joblib.load(MODEL_PATH)

else:

    st.error("❌ Trained Model Not Found!")

    st.stop()

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🎓 CareerAI")

st.sidebar.markdown("---")

menu = st.sidebar.radio(

    "Navigation",

    [

        "🏠 Home",

        "🎓 Placement Prediction",

        "📄 Resume Analyzer",

        "📊 Prediction History",

        "👨‍💻 About"

    ]

)

st.sidebar.markdown("---")

st.sidebar.subheader("Technology Used")

st.sidebar.write("🐍 Python")

st.sidebar.write("🤖 Machine Learning")

st.sidebar.write("📊 Scikit-Learn")

st.sidebar.write("🗄️ MySQL")

st.sidebar.write("🌐 Streamlit")

st.sidebar.write("📑 Pandas")

st.sidebar.markdown("---")

st.sidebar.success("Developed by")

st.sidebar.info("Aditi Sharma")

# -----------------------------
# HOME PAGE
# -----------------------------

if menu == "🏠 Home":

    st.title("🎓 CareerAI")

    st.subheader("AI Powered Placement Prediction System")

    st.markdown("---")

    st.markdown(
        """
### Welcome to CareerAI

CareerAI is an Artificial Intelligence based Placement Prediction
System developed for students.

The application predicts whether a student is likely to be placed
based on academic performance and skill-related information.

### Main Features

- 🎓 Placement Prediction

- 📄 Resume Analyzer

- 📊 Prediction History

- 💡 Career Recommendation

- 🤖 Machine Learning Model

- 🗄️ MySQL Database

---

### Project Workflow

Student Details

⬇

Machine Learning Model

⬇

Placement Prediction

⬇

Career Suggestions

"""
    )

    st.info("Select **Placement Prediction** from the sidebar to start.")

# -----------------------------------------------------------
# Placement Prediction Page
# -----------------------------------------------------------

elif menu == "🎓 Placement Prediction":
    st.title("🎓 Placement Prediction")

    st.markdown(
        "Enter the student's academic and skill details below."
    )

    st.markdown("---")

    # ------------------------------------
    # Student Input Form
    # ------------------------------------

    col1, col2 = st.columns(2)

    with col1:
        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=8.0,
            step=0.1
        )

        internships = st.number_input(
            "Internships",
            min_value=0,
            value=1
        )

        projects = st.number_input(
            "Projects",
            min_value=0,
            value=2
        )

        workshops = st.number_input(
            "Workshops / Certifications",
            min_value=0,
            value=2
        )

        aptitude = st.number_input(
            "Aptitude Test Score",
            min_value=0,
            max_value=100,
            value=80
        )

    with col2:
        softskills = st.number_input(
            "Soft Skills Rating",
            min_value=0,
            max_value=10,
            value=8
        )

        extracurricular = st.selectbox(
            "Extracurricular Activities",
            ["No", "Yes"]
        )

        placement_training = st.selectbox(
            "Placement Training",
            ["No", "Yes"]
        )

        ssc = st.number_input(
            "SSC Marks",
            min_value=0.0,
            max_value=100.0,
            value=85.0
        )

        hsc = st.number_input(
            "HSC Marks",
            min_value=0.0,
            max_value=100.0,
            value=85.0
        )

    st.markdown("---")

    predict = st.button(
        "🚀 Predict Placement",
        use_container_width=True
    )

    # ------------------------------------
    # Prediction
    # ------------------------------------

    if predict:
        extracurricular_value = 1 if extracurricular == "Yes" else 0
        placement_training_value = 1 if placement_training == "Yes" else 0

        student = pd.DataFrame([[
            cgpa,
            internships,
            projects,
            workshops,
            aptitude,
            softskills,
            extracurricular_value,
            placement_training_value,
            ssc,
            hsc
        ]], columns=[
            "CGPA",
            "Internships",
            "Projects",
            "Workshops/Certifications",
            "AptitudeTestScore",
            "SoftSkillsRating",
            "ExtracurricularActivities",
            "PlacementTraining",
            "SSC_Marks",
            "HSC_Marks"
        ])

        prediction = model.predict(student)
        probability = model.predict_proba(student)
        confidence = probability.max() * 100

        st.markdown("---")
        st.subheader("📊 Prediction Result")

        if prediction[0] == 1:
            st.success("🎉 Student is Likely to be Placed")
        else:
            st.error("❌ Student is Likely to be Not Placed")

        st.metric(
            label="Prediction Confidence",
            value=f"{confidence:.2f}%"
        )

        st.markdown("---")

        # ------------------------------------
        # Student Summary
        # ------------------------------------

        st.subheader("📋 Student Summary")

        summary = pd.DataFrame({
            "Feature": [
                "CGPA",
                "Internships",
                "Projects",
                "Workshops",
                "Aptitude Score",
                "Soft Skills",
                "Extracurricular Activities",
                "Placement Training",
                "SSC Marks",
                "HSC Marks"
            ],
            "Value": [
                cgpa,
                internships,
                projects,
                workshops,
                aptitude,
                softskills,
                extracurricular,
                placement_training,
                ssc,
                hsc
            ]
        })

        st.table(summary)
        st.markdown("---")

        # ------------------------------------
        # Career Suggestions
        # ------------------------------------

        st.subheader("💡 Career Suggestions")

        suggestions = []

        if cgpa < 7.5:
            suggestions.append("📚 Improve your CGPA by focusing on academics.")

        if internships < 2:
            suggestions.append("🏢 Try to complete at least 2 internships.")

        if projects < 3:
            suggestions.append("💻 Build more real-world projects.")

        if aptitude < 70:
            suggestions.append("🧠 Practice aptitude and logical reasoning regularly.")

        if softskills < 7:
            suggestions.append("🎤 Improve communication and presentation skills.")

        if placement_training == "No":
            suggestions.append("🎯 Join placement preparation or coding training.")

        if len(suggestions) == 0:
            st.success("🎉 Excellent Profile! Keep maintaining your performance.")
        else:
            for item in suggestions:
                st.write(item)

        st.markdown("---")

# -----------------------------------------------------------
# Resume Analyzer
# -----------------------------------------------------------

elif menu == "📄 Resume Analyzer":
    st.title("📄 Resume Analyzer")

    st.info("This module will be implemented in the next phase.")

    uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume Uploaded Successfully!")

    temp_path = os.path.join("app", uploaded_file.name)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    resume_text = extract_resume_text(temp_path)

    st.subheader("📄 Extracted Resume Text")

    if resume_text:

        st.text_area(
            "Resume Content",
            resume_text,
            height=400
        )

    else:

        st.error("Unable to read the resume.")
# -----------------------------------------------------------
# Prediction History
# -----------------------------------------------------------

elif menu == "📊 Prediction History":
    st.title("📊 Prediction History")
    st.info("Prediction history will be connected to the MySQL database.")

# -----------------------------------------------------------
# About
# -----------------------------------------------------------

elif menu == "👨‍💻 About":

    st.title("👨‍💻 About CareerAI")

    st.markdown(
        """
### CareerAI

CareerAI is an AI Powered Placement Prediction System.

### Features

- Placement Prediction
- Resume Analyzer
- Machine Learning Model
- Streamlit Dashboard
- MySQL Database

### Technology

- Python
- Pandas
- Scikit-Learn
- Streamlit
- MySQL

### Developer

Aditi Sharma
"""
    )