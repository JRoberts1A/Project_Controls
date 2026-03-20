import streamlit as st

# -------------------------------------------------
# Basic page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Roberts Residential | Project Tracker",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------------------------
# Custom CSS for branding (Roberts Residential, LLC)
# -------------------------------------------------
st.markdown("""
    <style>
    /* Global background */
    .main {
        background-color: #ffffff;
    }

    /* Hero area */
    .hero-wrapper {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
        background: linear-gradient(180deg, #ffffff 0%, #f7f7f7 100%);
        border-radius: 0 0 16px 16px;
        border-bottom: 2px solid #c00000;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 800;
        color: #BA0C2F;
        margin-top: 0.5rem;
        margin-bottom: 0.25rem;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #444444;
        margin-bottom: 1.25rem;
    }

    .hero-body {
        font-size: 1.05rem;
        color: #333333;
        max-width: 720px;
        margin: 0 auto;
    }

    /* Section heading */
    .section-heading {
        font-size: 1.4rem;
        font-weight: 700;
        color: #c00000;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
    }

    /* Hide default Streamlit chrome if you want a cleaner “website” feel */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: visible;} /* keep the top bar or change to hidden */
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HERO SECTION WITH LOGO
# -------------------------------------------------
st.markdown("<div class='hero-wrapper'>", unsafe_allow_html=True)

# Logo row
logo_col = st.columns([1, 2, 1])[1]  # center column bigger
with logo_col:
    st.image("Logo_White.jpg", use_column_width=False, width=260)

# Hero text
st.markdown("<div class='hero-title'>Residential Project Tracker</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Plan smarter. Track costs & schedules. Build with confidence.</div>",
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class='hero-body'>
    Built by <b>Roberts Residential, LLC</b> for real-world homebuilding and remodeling.
    Keep your owners, lenders, and subs aligned without wrestling with P6 or monster spreadsheets.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)  # close hero-wrapper

st.markdown("---")

# -------------------------------------------------
# THREE MAIN OPTIONS (New, Remodel, Quick Estimate)
# -------------------------------------------------
st.markdown("<div class='section-heading'>What do you want to work on today?</div>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧱 New Construction")
    st.markdown("Set up a ground-up build with phases, budget, and schedule.")
    if st.button("Start New Build →", key="new", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "new"
        st.switch_page("pages/new_construction.py")   # we'll create this later

with col2:
    st.markdown("### 🛠️ Remodel / Renovation")
    st.markdown("Plan scope, demo, changes, and track cost overruns in one place.")
    if st.button("Start Remodel →", key="remodel", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "remodel"
        st.switch_page("pages/remodel.py")

with col3:
    st.markdown("### 📏 Quick Estimate")
    st.markdown("Need a fast ballpark? Use square footage and finish level to get a rough total.")
    if st.button("Get Quick Price →", key="quick", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "quick"
        st.switch_page("pages/quick_estimate.py")

st.markdown("---")

# -------------------------------------------------
# WHO IT'S FOR / BENEFITS
# -------------------------------------------------
st.markdown("<div class='section-heading'>Built for residential work.</div>", unsafe_allow_html=True)

a, b, c = st.columns(3)
with a:
    st.markdown("#### 🧱 Builders & GCs")
    st.markdown("""
    - Track multiple jobs at once  
    - Simple phase-based schedules  
    - Clear cost vs. budget at a glance  
    """)

with b:
    st.markdown("#### 🏡 Homeowners")
    st.markdown("""
    - See where the money is going  
    - Understand progress by phase  
    - Fewer surprises, better decisions  
    """)

with c:
    st.markdown("#### 🧮 Lenders / Banks")
    st.markdown("""
    - Clean draw schedules  
    - Proof of progress for site visits  
    - Exportable summaries to PDF/Excel  
    """)

st.markdown("---")

st.caption("Roberts Residential, LLC – serving Dothan, AL and surrounding areas.")
