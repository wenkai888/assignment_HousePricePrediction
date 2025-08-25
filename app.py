import streamlit as st
import numpy as np
from joblib import load

# Load trained model
model = load("linear_regression_model.joblib")

st.title("💼 Salary Prediction App")
st.write("Enter the details below to predict salary:")

# Example inputs (you need to match them with your dataset features!)
experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=1)
test_score = st.number_input("Test Score", min_value=0, max_value=100, value=50)
interview_score = st.number_input("Interview Score", min_value=0, max_value=10, value=5)

if st.button("Predict Salary"):
    features = np.array([[experience, test_score, interview_score]])
    prediction = model.predict(features)
    st.success(f"💰 Predicted Salary: {prediction[0]:,.2f}")
