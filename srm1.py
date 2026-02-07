import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="AI Advocate Hub",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #1E40AF;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #F0F9FF;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin-bottom: 1rem;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'ai_quiz_score' not in st.session_state:
    st.session_state.ai_quiz_score = 0
if 'selected_topic' not in st.session_state:
    st.session_state.selected_topic = "Introduction"

# Sidebar Navigation
with st.sidebar:
    st.title("🤖 AI Advocate Hub")
    
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigate to:",
        ["🏠 Dashboard", "📚 AI Education", "🧪 Interactive Tools", 
         "📊 Impact Metrics", "🗣️ Advocacy Toolkit", "🌍 Community"]
    )
    
    st.markdown("---")
    
    # User Profile
    st.subheader("Your AI Advocate Profile")
    ai_knowledge = st.slider("AI Knowledge Level", 1, 10, 5)
    advocacy_focus = st.multiselect(
        "Advocacy Focus Areas",
        ["Ethics", "Education", "Healthcare", "Environment", "Accessibility", "Transparency"],
        default=["Ethics", "Education"]
    )

# Main Content based on navigation
if page == "🏠 Dashboard":
    st.markdown('<h1 class="main-header">AI Advocate Dashboard</h1>', unsafe_allow_html=True)
    
    # Welcome section
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class="info-box">
            <h3>Welcome, AI Advocate! 👋</h3>
            <p>This platform helps you understand, explain, and advocate for responsible AI development.
            Track your learning, use advocacy tools, and join the community pushing for ethical AI.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Key Metrics
    st.markdown('<h2 class="section-header">📈 Your Advocacy Progress</h2>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Modules Completed", "12", "+2")
    with col2:
        st.metric("Resources Accessed", "24", "+5")
    with col3:
        st.metric("Advocacy Actions", "8", "+3")
    with col4:
        st.metric("Knowledge Score", "85%", "3%")
    
    # Recent Activity Table
    st.markdown('<h2 class="section-header">📝 Recent Activity</h2>', unsafe_allow_html=True)
    
    activity_data = pd.DataFrame({
        'Date': ['2024-01-15', '2024-01-14', '2024-01-13', '2024-01-12'],
        'Activity': ['Completed Ethics Module', 'Shared AI Guidelines', 
                    'Joined Community Discussion', 'Completed Quiz'],
        'Impact Score': [10, 15, 8, 12]
    })
    
    st.dataframe(activity_data, use_container_width=True)
    
    # Simple bar chart using Streamlit
    st.bar_chart(activity_data.set_index('Date')['Impact Score'])

elif page == "📚 AI Education":
    st.markdown('<h1 class="main-header">AI Education Center</h1>', unsafe_allow_html=True)
    
    # Topic Selection
    topics = {
        "Introduction": "Basic AI concepts and terminology",
        "Ethics": "AI ethics, bias, and fairness",
        "Applications": "Real-world AI applications",
        "Future Trends": "Emerging AI technologies",
        "Policy": "AI regulations and governance"
    }
    
    selected_topic = st.selectbox(
        "Choose a topic to learn about:",
        list(topics.keys()),
        index=list(topics.keys()).index(st.session_state.selected_topic)
    )
    
    st.session_state.selected_topic = selected_topic
    
    # Content based on topic
    st.markdown(f'<h2 class="section-header">{selected_topic}</h2>', unsafe_allow_html=True)
    
    content_map = {
        "Introduction": """
        ### What is Artificial Intelligence?
        AI refers to systems or machines that mimic human intelligence to perform tasks and can improve themselves based on information they collect.
        
        **Key Concepts:**
        - Machine Learning: Algorithms that learn patterns from data
        - Neural Networks: Inspired by human brain structure
        - Natural Language Processing: Computers understanding human language
        - Computer Vision: Machines interpreting visual information
        """,
        "Ethics": """
        ### AI Ethics & Responsible Development
        Ethical AI development focuses on creating systems that are fair, transparent, and accountable.
        
        **Critical Issues:**
        - Algorithmic Bias: Systems inheriting human prejudices
        - Privacy Concerns: Data collection and usage
        - Transparency: Understanding AI decisions
        - Accountability: Who is responsible for AI actions?
        """
    }
    
    st.markdown(content_map.get(selected_topic, "Content coming soon..."))
    
    # Interactive Quiz
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check")
    
    question = st.radio(
        "What is a common ethical concern in AI development?",
        ["Algorithmic bias", "Battery life", "Screen resolution", "Keyboard design"]
    )
    
    if st.button("Check Answer"):
        if question == "Algorithmic bias":
            st.success("✅ Correct! Algorithmic bias is a major ethical concern in AI.")
        else:
            st.error("❌ Not quite. The correct answer is 'Algorithmic bias'.")

elif page == "🧪 Interactive Tools":
    st.markdown('<h1 class="main-header">Interactive AI Tools</h1>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["AI Ethics Simulator", "Bias Detector"])
    
    with tab1:
        st.subheader("AI Ethics Decision Simulator")
        
        scenario = st.selectbox(
            "Choose an ethical scenario:",
            ["Autonomous Vehicles", "Healthcare Allocation", "Job Application Screening"]
        )
        
        st.write(f"**Scenario:** {scenario}")
        
        # Interactive sliders for ethical trade-offs
        safety_weight = st.slider("Safety Priority", 0, 100, 50)
        fairness_weight = st.slider("Fairness Priority", 0, 100, 50)
        
        # Simple visualization
        ethics_data = pd.DataFrame({
            'Principle': ['Safety', 'Fairness'],
            'Weight': [safety_weight, fairness_weight]
        })
        
        st.bar_chart(ethics_data.set_index('Principle'))
        
        st.info("**Insight:** Different stakeholders might weight these values differently.")

elif page == "📊 Impact Metrics":
    st.markdown('<h1 class="main-header">AI Advocacy Impact Dashboard</h1>', unsafe_allow_html=True)
    
    # Impact Calculator
    st.subheader("📊 Your Advocacy Impact Calculator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        conversations = st.number_input("Conversations about AI ethics", 0, 1000, 10)
    with col2:
        resources_shared = st.number_input("Educational resources shared", 0, 500, 5)
    with col3:
        policy_engagements = st.number_input("Policy engagements", 0, 100, 2)
    
    if st.button("Calculate Impact"):
        total_impact = (conversations * 2) + (resources_shared * 5) + (policy_engagements * 50)
        
        st.metric("Estimated Total Impact", f"{total_impact} points")
        
        # Simple pie chart using data
        impact_data = pd.DataFrame({
            'Activity': ['Conversations', 'Resources', 'Policy'],
            'Impact': [conversations * 2, resources_shared * 5, policy_engagements * 50]
        })
        
        st.write("Impact Breakdown:")
        st.dataframe(impact_data)

# ... (continue with other sections using similar Streamlit-only components)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    <p>🤖 AI Advocate Hub | Empowering Responsible AI Development</p>
    </div>
    """,
    unsafe_allow_html=True
)
