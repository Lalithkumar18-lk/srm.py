import streamlit as st

st.set_page_config(page_title="AI Advocate", page_icon="⚖️")

st.title("⚖️ AI Advocate – Legal Assistant")
st.write("Get basic legal guidance for educational purposes")

problem = st.text_area("Describe your legal issue:")

def legal_advice(text):
    text = text.lower()

    if "theft" in text or "stolen" in text:
        return (
            "🔹 Applicable Law: IPC Section 378 (Theft)\n\n"
            "🔹 Action: File an FIR at nearest police station\n\n"
            "🔹 Documents Needed:\n"
            "- ID Proof\n- Complaint Letter\n- Evidence (if any)"
        )

    elif "divorce" in text:
        return (
            "🔹 Applicable Law: Hindu Marriage Act\n\n"
            "🔹 Action: Consult family court advocate\n\n"
            "🔹 Documents Needed:\n"
            "- Marriage Certificate\n- Address Proof\n- ID Proof"
        )

    elif "accident" in text:
        return (
            "🔹 Applicable Law: Motor Vehicles Act\n\n"
            "🔹 Action: File FIR and insurance claim\n\n"
            "🔹 Documents Needed:\n"
            "- FIR Copy\n- RC Book\n- Insurance Papers"
        )

    else:
        return (
            "⚠️ Legal advice not found.\n\n"
            "Please consult a licensed advocate for detailed guidance."
        )

if st.button("Get Legal Advice"):
    if problem.strip() == "":
        st.warning("Please enter your legal problem.")
    else:
        result = legal_advice(problem)
        st.success("AI Advocate Response")
        st.text(result)

st.markdown("---")
st.caption("⚠️ This app provides educational legal information only.")
