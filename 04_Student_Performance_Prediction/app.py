import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# Load Trained Model
# ------------------------------
model = joblib.load('student_performance_model.pkl')

# ------------------------------
# Streamlit App Configuration
# ------------------------------
st.set_page_config(page_title="🎓 Student Performance Prediction", layout="centered")
st.title("🎓 Student Performance Prediction App")
st.write("Predict a student's **grade** (A, B, C, D, or F) based on their test scores and background factors.")

# ------------------------------
# Input Section
# ------------------------------
st.header("🧾 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        "Gender",
        options=["male", "female"],
        help="Select the student's gender (e.g., male or female)."
    )

    race_ethnicity = st.selectbox(
        "Race/Ethnicity",
        options=["group A", "group B", "group C", "group D", "group E"],
        help="Choose the student's race/ethnicity group (A to E)."
    )

    parental_level_of_education = st.selectbox(
        "Parental Level of Education",
        options=[
            "some high school", "high school", "some college",
            "associate's degree", "bachelor's degree", "master's degree"
        ],
        help="Select the highest level of education completed by the student's parents."
    )

    lunch = st.selectbox(
        "Lunch Type",
        options=['Standard lunch', 'Free/Reduced lunch'],
        help="Select the type of lunch the student receives."
    )

    test_preparation_course = st.selectbox(
        "Test Preparation Course",
        options=['Completed', 'Not Completed'],
        help="Select whether the student completed the test preparation course."
    )

with col2:
    math_score = st.number_input(
        "Math Score",
        min_value=0, max_value=100, value=70,
        help="Enter the student's math test score (0–100)."
    )

    reading_score = st.number_input(
        "Reading Score",
        min_value=0, max_value=100, value=70,
        help="Enter the student's reading test score (0–100)."
    )

    writing_score = st.number_input(
        "Writing Score",
        min_value=0, max_value=100, value=70,
        help="Enter the student's writing test score (0–100)."
    )

    science_score = st.number_input(
        "Science Score",
        min_value=0, max_value=100, value=70,
        help="Enter the student's science test score (0–100)."
    )

# ------------------------------
# Predict Button
# ------------------------------
if st.button("🔍 Predict Grade"):
    # Create input DataFrame
    input_data = pd.DataFrame({
        'gender': [gender],
        'race_ethnicity': [race_ethnicity],
        'parental_level_of_education': [parental_level_of_education],
        'lunch': [lunch],
        'test_preparation_course': [test_preparation_course],
        'math_score': [math_score],
        'reading_score': [reading_score],
        'writing_score': [writing_score],
        'science_score': [science_score]
    })

    # Predict using the trained model
    prediction = model.predict(input_data)

    # --------------------------
    # Decode numeric prediction
    # --------------------------
    grade_mapping = {
        0: "A",
        1: "B",
        2: "C",
        3: "D",
        4: "F"
    }

    predicted_grade = grade_mapping.get(prediction[0], "Unknown")

    st.success(f"✅ Predicted Grade: **{predicted_grade}**")

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Developed by Farhan — Student Performance ML App (Streamlit + Scikit-learn)")
