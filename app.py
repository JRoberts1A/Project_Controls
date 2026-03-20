import streamlit as st

# Page config - makes it look like a real app
st.set_page_config(
    page_title="Residential Project Tracker",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---- Custom CSS ----
st.markdown("""
    <style>
    .hero-text {
        text-align: center;
        padding: 3rem 0 2rem 0;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.4rem;
        color: #555555;
        margin-bottom: 1.5rem;
    }

    .hero-body {
        font-size: 1.05rem;
        color: #444444;
        max-width: 720px;
        margin: 0 auto;
    }

    footer {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown("<div class='hero-text'>", unsafe_allow_html=True)

st.markdown("<div class='hero-title'>🏠 Residential Project Tracker</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Plan smarter. Track costs & schedules. Build with confidence.</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class='hero-body'>
    Whether it's a <b>new home build</b>, a <b>full remodel</b>, or just a <b>quick cost check</b>,  
    get a simple, powerful dashboard without the complexity of P6 or endless Excel sheets.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# ---- Three main options ----
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧱 New Construction")
    st.markdown("Start from scratch: full timeline, budget, phases, alerts.")
    if st.button("Start New Build →", key="new", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "new"
        st.switch_page("pages/new_construction.py")   # We'll create this

with col2:
    st.markdown("### 🛠️ Remodel")
    st.markdown("Existing home? Demo, changes, cost overruns, progress tracking.")
    if st.button("Start Remodel →", key="remodel", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "remodel"
        st.switch_page("pages/remodel.py")

with col3:
    st.markdown("### 📏 Quick Estimate")
    st.markdown("Fast ballpark: sq ft, finishes, rough total in seconds.")
    if st.button("Get Quick Price →", key="quick", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "quick"
        st.switch_page("pages/quick_estimate.py")

st.markdown("---")

# ---- Trust / Benefits Section ----
st.markdown("### Why this tool?")

left, right = st.columns(2)

with left:
    st.markdown("""
    - Built for **residential projects** (not mega-construction bloat)  
    - Real-time **cost vs. budget** tracking  
    - Simple, visual **phase timelines**  
    """)

with right:
    st.markdown("""
    - Export to **PDF/Excel** for owners & banks  
    - Built with **builders in mind**, not just PMs  
    - **Free to start** – no subscriptions
    """)

st.caption("Made for builders in Dothan, AL and beyond. Questions? Reach out anytime.")
