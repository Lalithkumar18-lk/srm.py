import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Advocate AI", layout="centered")

st.title("⚖️ Advocate AI – Legal Assistant")

menu = ["Legal Chatbot", "Document Generator", "Case Records"]
choice = st.sidebar.selectbox("Select Module", menu)

if "cases" not in st.session_state:
    st.session_state.cases = []

if choice == "Legal Chatbot":
    st.header("🤖 Legal Chatbot")

    user_query = st.text_input("Ask your legal question")

    def legal_response(query):
        query = query.lower()
        if "divorce" in query:
            return "Divorce laws in India fall under the Hindu Marriage Act, 1955."
        elif "fir" in query:
            return "FIR can be filed at the nearest police station or online in some states."
        elif "bail" in query:
            return "Bail is a legal right in bailable offenses under CrPC."
        elif "property" in query:
            return "Property disputes are handled under civil law."
        else:
            return "Please consult an advocate for detailed legal advice."

    if st.button("Get Answer"):
        if user_query:
            response = legal_response(user_query)
            st.success(response)
        else:
            st.warning("Please enter a question")

elif choice == "Document Generator":
    st.header("📄 Legal Document Generator")

    doc_type = st.selectbox(
        "Select Document Type",
        ["Legal Notice", "Affidavit", "Rental Agreement"]
    )

    name = st.text_input("Your Name")
    address = st.text_area("Address")
    date = datetime.now().strftime("%d-%m-%Y")

    if st.button("Generate Document"):
        if name and address:
            document = f"""
            {doc_type}
            
            Date: {date}

            I, {name}, residing at {address}, hereby declare that the above
            information is true to the best of my knowledge.

            Signature:
            """
            st.text_area("Generated Document", document, height=250)
        else:
            st.warning("Please fill all fields")

elif choice == "Case Records":
    st.header("📁 Case Management")

    client = st.text_input("Client Name")
    case_type = st.selectbox(
        "Case Type",
        ["Civil", "Criminal", "Family", "Property"]
    )

    if st.button("Add Case"):
        if client:
            st.session_state.cases.append({
                "Client": client,
                "Case Type": case_type
            })
            st.success("Case added successfully")
        else:
            st.warning("Enter client name")

    if st.session_state.cases:
        df = pd.DataFrame(st.session_state.cases)
        st.table(df)
