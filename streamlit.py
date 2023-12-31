import streamlit as st
import joblib
import numpy as np

model = joblib.load("trained_model.pkl")

st.title("Income Prediction App")
st.write("Predict income based on age and experience")

age = st.number_input("Enter Age")
experience = st.number_input("Enter Experience")

btn = st.button("Predict")
if btn:
    new_data = np.array([[age, experience]])  # Create a 2D array for prediction
    predicted_income = model.predict(new_data)
    st.write("Predicted Income:", predicted_income[0])
