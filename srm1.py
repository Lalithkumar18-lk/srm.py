import streamlit as st
import pandas as pd

st.title("Student Marks Analysis and Visualization")

st.subheader("Enter Student Details")

name = st.text_input("Student Name")

marks = {
    "Subject 1": st.number_input("Subject 1 Marks", 0, 100),
    "Subject 2": st.number_input("Subject 2 Marks", 0, 100),
    "Subject 3": st.number_input("Subject 3 Marks", 0, 100)
}

if st.button("Analyze"):
    df = pd.DataFrame(list(marks.items()), columns=["Subject", "Marks"])

    total = df["Marks"].sum()
    average = df["Marks"].mean()

    if average >= 75:
        grade = "A"
        result = "Pass"
    elif average >= 50:
        grade = "B"
        result = "Pass"
    else:
        grade = "C"
        result = "Fail"

    st.success("Analysis Completed")

    st.write("Student Name:", name)
    st.write("Total Marks:", total)
    st.write("Average:", average)
    st.write("Grade:", grade)
    st.write("Result:", result)

    st.subheader("Marks Visualization")
    st.bar_chart(df.set_index("Subject"))
