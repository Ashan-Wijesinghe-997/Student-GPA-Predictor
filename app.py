import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model = pk.load(open('LinearRegressionModel.pkl', 'rb'))

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 15px 20px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
        width: 100%;  /* Set the width to 100% to fill the container */
    }
    .stButton > button:hover {
        background-color: #45a049;
        color: white;  /* Keep the text color white on hover */
    }
    .header {
        font-size: 32px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="header">🎓 GPA Predictor</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox('👤 Select Gender', ['Select Gender', 'Male', 'Female'])
    study_time_weekly = st.number_input(
        '📚 Weekly Study Time (hours)', min_value=0, max_value=50, step=1, value=0
    )
    tutoring = st.selectbox('📖 Received Tutoring?', ['Select Tutoring Status', 'Yes', 'No'])

with col2:
    absences = st.number_input('🚸 Number of Absences', min_value=0, max_value=30, step=1, value=0)
    extracurricular = st.selectbox(
        '🎨 Participates in Extracurricular Activities?',
        ['Select Extracurricular Status', 'Yes', 'No']
    )
    sports = st.selectbox('⚽ Plays Sports?', ['Select Sports Status', 'Yes', 'No'])

if gender != 'Select Gender' and tutoring != 'Select Tutoring Status' and extracurricular != 'Select Extracurricular Status' and sports != 'Select Sports Status':
    gender_value = 0 if gender == 'Male' else 1
    tutoring_value = 1 if tutoring == 'Yes' else 0
    extracurricular_value = 1 if extracurricular == 'Yes' else 0
    sports_value = 1 if sports == 'Yes' else 0

def gpa_to_letter_grade(gpa):
    if gpa >= 4.0:
        return "A+"
    elif gpa >= 3.7:
        return "A-"
    elif gpa >= 3.3:
        return "B+"
    elif gpa >= 3.0:
        return "B"
    elif gpa >= 2.7:
        return "B-"
    elif gpa >= 2.3:
        return "C+"
    elif gpa >= 2.0:
        return "C"
    elif gpa >= 1.7:
        return "C-"
    elif gpa >= 1.3:
        return "D+"
    elif gpa >= 1.0:
        return "D"
    elif gpa >= 0.7:
        return "D-"
    else:
        return "F"

if st.button('🔮 Predict GPA'):
    if gender != 'Select Gender' and tutoring != 'Select Tutoring Status' and extracurricular != 'Select Extracurricular Status' and sports != 'Select Sports Status':
        input_data = np.array(
            [[gender_value, study_time_weekly, absences, tutoring_value, extracurricular_value, sports_value]]
        )

        prediction = model.predict(input_data)

        st.success(f'🎯 Predicted GPA: {prediction[0]:.2f}')

        result = gpa_to_letter_grade(prediction[0])
        st.success(f'🎓 Predicted Grade: {result}')
