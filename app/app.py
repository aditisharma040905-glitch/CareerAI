import streamlit as st
import pandas as pd 
import joblib
import os

st.set_page_config(
    page_title="CareerAI",
    page_icon="🎓",
    layout="centered"
)
MODEL_PATH = os.path.join("saved_models", "careerai_model.pkl")

model = joblib.load(MODEL_PATH)

st.title("🎓 CareerAI")
st.subheader("AI Powered Placement Prediction System")

st.markdown("---")

st.header("Student Details")

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
    "Workshops/Certifications",
    min_value=0,
    value=2
)

aptitude = st.number_input(
    "Aptitude Test Score",
    min_value=0,
    max_value=100,
    value=80
)

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

if st.button("Predict Placement"):

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

    st.markdown("---")

    if prediction[0] == 1:
        st.success("🎉 Prediction: Student is likely to be Placed")
    else:
        st.error("❌ Prediction: Student is likely to be Not Placed")