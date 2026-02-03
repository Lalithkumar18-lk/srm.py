import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime

st.set_page_config(page_title="Advocate AI", layout="wide")

# ---------------- LOGIN ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("⚖️ Advocate AI – Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pwd == "admin123":
            st.session_state.logged_in = True
            st.success("Login Successful")
        else:
            st.error("Invalid credentials")

if not st.session_state.logged_in:
    login()
    st.stop()

# ---------------- DATA ----------------
case_laws = [
    "Divorce under Hindu Marriage Act",
    "Bail provisions under CrPC",
    "Property dispute civil law",
    "Domestic violence act India",
    "Consumer protection act case"
]

documents = []
cases = []

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Navigation",
    ["Home", "AI Legal Chatbot", "Case Law Search", "Document Generator", "Case Management"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.title("⚖️ Advocate AI – Intelligent Legal Assistance")
    st.write("""
    Advocate AI is an AI-powered legal assistance platform that helps users
    understand laws, generate legal documents, and manage cases digitally.
    """)

# ---------------- CHATBOT ----------------
elif menu == "AI Legal Chatbot":
    st.header("🤖 AI Legal Chatbot")
    query = st.text_input("Ask your legal question")

    def chatbot(q):
        q = q.lower()
        if "divorce" in q:
            return "Divorce laws in India are governed by the Hindu Marriage Act, 1955."
        if "bail" in q:
            return "Bail is a legal right in bailable offences under CrPC."
        if "fir" in q:
            return "FIR can be filed at the nearest police station."
        if "property" in q:
            return "Property disputes fall under civil law."
        return "Please consult an advocate for detailed advice."

    if st.button("Get Answer"):
        st.success(chatbot(query))

# ---------------- CASE LAW SEARCH ----------------
elif menu == "Case Law Search":
    st.header("📚 Case Law Recommendation System")

    search = st.text_input("Enter legal topic")

    if st.button("Search"):
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(case_laws + [search])
        similarity = cosine_similarity(vectors[-1], vectors[:-1])
        best_match = case_laws[similarity.argmax()]
        st.info(f"Relevant Case Law: {best_match}")

# ---------------- DOCUMENT GENERATOR ----------------
elif menu == "Document Generator":
    st.header("📄 Legal Document Generator")

    doc_type = st.selectbox("Select Document", ["Legal Notice", "Affidavit", "Rental Agreement"])
    name = st.text_input("Name")
    address = st.text_area("Address")

    if st.button("Generate"):
        doc = f"""
        {doc_type}
        Date: {datetime.now().strftime('%d-%m-%Y')}

        I, {name}, residing at {address}, hereby declare that the information
        provided is true and correct.

        Signature:
        """
        st.text_area("Generated Document", doc, height=250)

# ---------------- CASE MANAGEMENT ----------------
elif menu == "Case Management":
    st.header("📁 Advocate Case Management")

    client = st.text_input("Client Name")
    case_type = st.selectbox("Case Type", ["Civil", "Criminal", "Family", "Property"])

    if st.button("Add Case"):
        cases.append({"Client": client, "Case Type": case_type})
        st.success("Case Added")

    if cases:
        st.table(pd.DataFrame(cases))
