import streamlit as st

st.title("User Input Example")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=100)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])

if st.button("Submit"):
    st.write("Name:", name)
    st.write("Age:", age)
    st.write("Gender:", gender)
