import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json

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
    .stButton>button {
        background-color: #3B82F6;
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        font-weight: bold;
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
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103655.png", width=100)
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
    
    st.markdown("---")
    
    # Quick Stats
    st.subheader("Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Learning Hours", "12")
    with col2:
        st.metric("Advocacy Score", "85%")

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
        st.markdown('<div class="metric-box"><h3>12</h3><p>Modules Completed</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-box"><h3>24</h3><p>Resources Accessed</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-box"><h3>8</h3><p>Advocacy Actions</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-box"><h3>85%</h3><p>Knowledge Score</p></div>', unsafe_allow_html=True)
    
    # Recent Activity
    st.markdown('<h2 class="section-header">📝 Recent Activity</h2>', unsafe_allow_html=True)
    
    activity_data = pd.DataFrame({
        'Date': ['2024-01-15', '2024-01-14', '2024-01-13', '2024-01-12'],
        'Activity': ['Completed Ethics Module', 'Shared AI Guidelines', 'Joined Community Discussion', 'Completed Quiz'],
        'Impact': [10, 15, 8, 12]
    })
    
    fig = px.bar(activity_data, x='Date', y='Impact', color='Activity',
                 title='Your Recent Advocacy Impact')
    st.plotly_chart(fig, use_container_width=True)

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
        
        **Principles to Advocate For:**
        1. Fairness and non-discrimination
        2. Transparency and explainability
        3. Privacy protection
        4. Human oversight
        5. Societal and environmental wellbeing
        """,
        "Applications": """
        ### AI in Real World Applications
        
        **Healthcare:**
        - Disease diagnosis assistance
        - Drug discovery acceleration
        - Personalized treatment plans
        
        **Environment:**
        - Climate change modeling
        - Wildlife conservation tracking
        - Pollution monitoring
        
        **Education:**
        - Personalized learning paths
        - Automated grading assistance
        - Accessibility tools
        """,
        "Future Trends": """
        ### Emerging AI Trends
        
        **Generative AI:**
        - Creative content generation
        - Code assistance tools
        - Synthetic data creation
        
        **AI Safety Research:**
        - Alignment with human values
        - Robustness against manipulation
        - Interpretability improvements
        
        **Edge AI:**
        - On-device processing
        - Reduced latency
        - Enhanced privacy
        """,
        "Policy": """
        ### AI Governance & Policy
        
        **Current Regulations:**
        - EU AI Act: Risk-based approach
        - US Executive Orders: Safety standards
        - Global frameworks developing
        
        **Advocacy Opportunities:**
        - Support transparency requirements
        - Advocate for public interest representation
        - Push for algorithmic auditing standards
        - Support open AI research
        """
    }
    
    st.markdown(content_map[selected_topic])
    
    # Interactive Quiz
    st.markdown("---")
    st.subheader("🧠 Quick Knowledge Check")
    
    quiz_questions = {
        "What is a common ethical concern in AI development?": 
            ["Algorithmic bias", "Battery life", "Screen resolution", "Keyboard design"],
        "Which principle emphasizes understanding AI decisions?":
            ["Transparency", "Speed", "Cost", "Color"],
        "What does ML stand for in AI?":
            ["Machine Learning", "Maximum Load", "Memory Limit", "Manual Labor"]
    }
    
    quiz_score = 0
    for question, options in quiz_questions.items():
        answer = st.radio(question, options)
        if answer == options[0]:  # First option is always correct in this example
            quiz_score += 1
    
    if st.button("Submit Quiz"):
        st.session_state.ai_quiz_score = quiz_score
        st.success(f"Your score: {quiz_score}/{len(quiz_questions)}")
        if quiz_score == len(quiz_questions):
            st.balloons()

elif page == "🧪 Interactive Tools":
    st.markdown('<h1 class="main-header">Interactive AI Tools</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["AI Ethics Simulator", "Bias Detector", "Explainable AI Demo"])
    
    with tab1:
        st.subheader("AI Ethics Decision Simulator")
        
        scenario = st.selectbox(
            "Choose an ethical scenario:",
            ["Autonomous Vehicles", "Healthcare Allocation", "Job Application Screening", 
             "Social Media Content Moderation"]
        )
        
        st.write(f"**Scenario:** {scenario}")
        st.write("**Dilemma:** How should the AI system prioritize different values?")
        
        # Interactive sliders for ethical trade-offs
        col1, col2 = st.columns(2)
        with col1:
            safety_weight = st.slider("Safety Priority", 0, 100, 50)
            fairness_weight = st.slider("Fairness Priority", 0, 100, 50)
        with col2:
            efficiency_weight = st.slider("Efficiency Priority", 0, 100, 50)
            privacy_weight = st.slider("Privacy Priority", 0, 100, 50)
        
        # Visualize ethical priorities
        fig = go.Figure(data=[
            go.Bar(name='Ethical Weights', 
                   x=['Safety', 'Fairness', 'Efficiency', 'Privacy'],
                   y=[safety_weight, fairness_weight, efficiency_weight, privacy_weight])
        ])
        fig.update_layout(title="Your Ethical Priorities", yaxis_title="Weight")
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("**Insight:** Different stakeholders might weight these values differently. Advocacy helps ensure diverse perspectives are considered.")
    
    with tab2:
        st.subheader("Algorithmic Bias Detector")
        
        st.write("Upload or simulate data to detect potential biases:")
        
        # Simulated bias analysis
        data_option = st.selectbox("Choose dataset:", ["Hiring Decisions", "Loan Approvals", "Healthcare Access"])
        
        if st.button("Analyze for Bias"):
            # Simulated bias detection
            bias_metrics = {
                "Gender Disparity": "Detected: 15% lower approval for women",
                "Racial Bias": "Detected: 20% disparity across ethnic groups",
                "Age Discrimination": "No significant bias detected",
                "Geographic Fairness": "Detected: Urban bias present"
            }
            
            for metric, result in bias_metrics.items():
                if "Detected" in result:
                    st.error(f"🚨 {metric}: {result}")
                else:
                    st.success(f"✅ {metric}: {result}")
            
            st.markdown("""
            **Advocacy Action Items:**
            1. Demand algorithmic audits
            2. Request diverse training data
            3. Push for transparency reports
            4. Advocate for human oversight
            """)
    
    with tab3:
        st.subheader("Explainable AI Demonstration")
        
        st.write("See how different AI models make decisions:")
        
        model_type = st.selectbox("Select AI model type:", 
                                 ["Decision Tree (Explainable)", 
                                  "Neural Network (Complex)", 
                                  "Rule-based System (Transparent)"])
        
        sample_input = st.text_area("Input data for explanation:", 
                                   "Customer profile: Age 35, Income $75k, Credit Score 720")
        
        if st.button("Explain Decision"):
            if "Decision Tree" in model_type:
                st.success("**Decision Path:**\n1. Credit Score > 700 ✓\n2. Income > $50k ✓\n3. Debt-to-Income < 40% ✓\n✅ **Approved**")
            elif "Neural Network" in model_type:
                st.warning("**Black Box Decision:**\nThe model's decision is based on 2.5 million parameters. While confidence is 92%, the exact reasoning path is not human-interpretable.")
            else:
                st.info("**Rule-based Decision:**\nIF Credit_Score >= 700 AND Income >= 50000 THEN Approve\n✅ **Approved**")
            
            st.markdown("""
            **Advocacy Insight:**
            - Transparent models build trust
            - Complex models need explanation layers
            - Regulatory requirements may demand explainability
            """)

elif page == "📊 Impact Metrics":
    st.markdown('<h1 class="main-header">AI Advocacy Impact Dashboard</h1>', unsafe_allow_html=True)
    
    # Global AI Impact Metrics
    st.subheader("🌍 Global AI Impact Trends")
    
    # Sample data
    impact_data = pd.DataFrame({
        'Year': [2020, 2021, 2022, 2023, 2024],
        'AI Regulations': [15, 28, 42, 65, 89],
        'Ethical Frameworks': [22, 35, 48, 62, 78],
        'Public Awareness': [30, 45, 58, 72, 85],
        'Corporate Policies': [18, 32, 47, 61, 76]
    })
    
    fig = px.line(impact_data, x='Year', y=['AI Regulations', 'Ethical Frameworks', 
                                           'Public Awareness', 'Corporate Policies'],
                  title='Global Responsible AI Progress',
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)
    
    # Advocacy Impact Calculator
    st.markdown("---")
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
        
        # Impact visualization
        impact_breakdown = pd.DataFrame({
            'Activity': ['Conversations', 'Resources Shared', 'Policy Engagements'],
            'Impact': [conversations * 2, resources_shared * 5, policy_engagements * 50]
        })
        
        fig2 = px.pie(impact_breakdown, values='Impact', names='Activity',
                     title='Your Impact Breakdown')
        st.plotly_chart(fig2, use_container_width=True)

elif page == "🗣️ Advocacy Toolkit":
    st.markdown('<h1 class="main-header">AI Advocacy Toolkit</h1>', unsafe_allow_html=True)
    
    # Template Generator
    st.subheader("📝 Advocacy Template Generator")
    
    advocacy_type = st.selectbox(
        "What do you need to create?",
        ["Social Media Post", "Email to Representatives", "Community Presentation", 
         "Policy Brief", "Educational Material"]
    )
    
    topic = st.text_input("Topic focus:", "AI transparency in healthcare")
    audience = st.selectbox("Target audience:", ["General Public", "Policymakers", 
                                                "Tech Community", "Students"])
    
    if st.button("Generate Advocacy Content"):
        templates = {
            "Social Media Post": f"""
            **Engaging Post about {topic}:**
            
            🤖 Did you know about {topic}? 
            
            AI systems are transforming healthcare, but we need transparency to ensure they work for everyone!
            
            ✅ What to advocate for:
            - Clear explanations of AI decisions
            - Regular bias audits
            - Public reporting standards
            
            #AIethics #ResponsibleAI #TechForGood #AIforHealth
            
            💬 Share your thoughts below!
            """,
            
            "Email to Representatives": f"""
            **Subject: Urgent Need for {topic} Regulations**
            
            Dear [Representative Name],
            
            I'm writing as a concerned constituent about {topic}. As AI becomes more integrated into healthcare, we must ensure these systems are transparent, fair, and accountable.
            
            Key recommendations:
            1. Require algorithmic impact assessments
            2. Mandate transparency for high-risk AI systems
            3. Fund independent AI auditing
            4. Establish clear accountability frameworks
            
            Thank you for considering these important issues.
            
            Sincerely,
            [Your Name]
            """,
            
            "Community Presentation": f"""
            **Presentation Outline: {topic}**
            
            Slide 1: Title - "Understanding {topic}"
            Slide 2: Why this matters to our community
            Slide 3: Current challenges and risks
            Slide 4: Real-world examples
            Slide 5: What responsible AI looks like
            Slide 6: How we can advocate together
            Slide 7: Action items for our community
            Slide 8: Resources and next steps
            """
        }
        
        st.markdown("### Generated Content")
        st.text_area("Your advocacy content:", templates.get(advocacy_type, "Select a template type"), height=300)
        
        st.download_button(
            label="Download Content",
            data=templates.get(advocacy_type, ""),
            file_name=f"ai_advocacy_{advocacy_type.lower().replace(' ', '_')}.txt",
            mime="text/plain"
        )
    
    # Resource Library
    st.markdown("---")
    st.subheader("📚 Advocacy Resource Library")
    
    resources = {
        "AI Ethics Frameworks": [
            "EU Ethics Guidelines for Trustworthy AI",
            "OECD AI Principles",
            "IEEE Ethically Aligned Design"
        ],
        "Policy Templates": [
            "Model Algorithmic Impact Assessment",
            "AI Transparency Report Template",
            "Stakeholder Engagement Guide"
        ],
        "Educational Materials": [
            "AI Literacy Handbook",
            "Bias Detection Toolkit",
            "Community Workshop Materials"
        ]
    }
    
    for category, items in resources.items():
        with st.expander(f"📁 {category}"):
            for item in items:
                st.write(f"• {item}")

elif page == "🌍 Community":
    st.markdown('<h1 class="main-header">AI Advocate Community</h1>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Discussion Forum
        st.subheader("💬 Community Discussions")
        
        discussion_topics = [
            {"topic": "How to advocate for AI ethics in schools?", "replies": 24, "author": "Alex M."},
            {"topic": "Recent AI policy developments in Europe", "replies": 18, "author": "Sophie K."},
            {"topic": "Tools for detecting algorithmic bias", "replies": 32, "author": "David R."},
            {"topic": "Building diverse AI teams", "replies": 15, "author": "Maria L."}
        ]
        
        for topic in discussion_topics:
            with st.container():
                st.markdown(f"**{topic['topic']}**")
                st.caption(f"By {topic['author']} • {topic['replies']} replies")
                if st.button("Join Discussion", key=f"btn_{topic['topic'][:10]}"):
                    st.session_state.selected_discussion = topic['topic']
                st.markdown("---")
        
        # New Discussion
        st.subheader("Start New Discussion")
        new_topic = st.text_input("Discussion topic:")
        new_content = st.text_area("Your message:", height=150)
        if st.button("Post Discussion"):
            if new_topic and new_content:
                st.success("Discussion posted successfully!")
    
    with col2:
        # Community Stats
        st.subheader("👥 Community Stats")
        
        stats = {
            "Total Advocates": "1,245",
            "Active This Week": "328",
            "Countries Represented": "78",
            "Collective Actions": "5,892"
        }
        
        for stat, value in stats.items():
            st.metric(stat, value)
        
        st.markdown("---")
        
        # Upcoming Events
        st.subheader("📅 Upcoming Events")
        
        events = [
            "Jan 25: AI Ethics Webinar",
            "Feb 3: Policy Advocacy Training",
            "Feb 15: Community Meetup",
            "Mar 1: Global AI Forum"
        ]
        
        for event in events:
            st.write(f"• {event}")
        
        if st.button("View All Events"):
            st.info("Redirecting to events calendar...")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
    <p>🤖 AI Advocate Hub | Empowering Responsible AI Development | 
    <a href='#' style='color: #3B82F6;'>Privacy Policy</a> | 
    <a href='#' style='color: #3B82F6;'>Contact</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
