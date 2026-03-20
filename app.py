import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Roberts Residential | Project Tracker",
    page_icon="🏠",
    layout="wide",
)

PRIMARY_RED = "#c00000"
DARK_TEXT = "#222222"

# -------------------------------------------------
# Custom CSS
# -------------------------------------------------
st.markdown(f"""
    <style>
    /* Reduce default padding */
    .block-container {{
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        max-width: 1100px !important;  /* prevents super-wide content */
    }}

    /* HERO CARD */
    .hero-card {{
        background-color: #ffffff;
        padding: 1.75rem 2rem;
        border-radius: 16px;
        box-shadow: 0px 4px 16px rgba(0,0,0,0.08);
        margin-bottom: 2.5rem;
    }}

    .hero-row {{
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 2rem;
    }}

    .hero-logo {{
        flex: 0 0 auto;
    }}

    .hero-text {{
        flex: 1 1 auto;
    }}

    .hero-title {{
        font-size: 2.4rem;
        font-weight: 800;
        color: {PRIMARY_RED};
        margin-bottom: 0.25rem;
    }}

    .hero-subtitle {{
        font-size: 1.1rem;
        color: #444444;
        margin-bottom: 0.75rem;
    }}

    .hero-body {{
        font-size: 1.0rem;
        color: #333333;
    }}

    .section-heading {{
        font-size: 1.3rem;
        font-weight: 700;
        color: {PRIMARY_RED};
        margin-top: 0.5rem;
        margin-bottom: 0.75rem;
    }}

    /* Hide Streamlit menu + footer for cleaner look */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------
st.markdown("<div class='hero-card'>", unsafe_allow_html=True)

st.markdown("<div class='hero-row'>", unsafe_allow_html=True)

# Left: logo
st.markdown("<div class='hero-logo'>", unsafe_allow_html=True)
st.image("Logo_White.jpg", width=220)
st.markdown("</div>", unsafe_allow_html=True)

# Right: text
st.markdown("<div class='hero-text'>", unsafe_allow_html=True)
st.markdown("<div class='hero-title'>Residential Project Tracker</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Plan smarter. Track costs & schedules. Build with confidence.</div>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div class='hero-body'>
    Built by <b>Roberts Residential, LLC</b> for real‑world homebuilding and remodeling.
    Keep your owners, lenders, and subcontractors aligned with clear, easy‑to‑read dashboards,
    without wrestling with P6 or monster spreadsheets.
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)  # close hero-text

st.markdown("</div>", unsafe_allow_html=True)  # close hero-row
st.markdown("</div>", unsafe_allow_html=True)  # close hero-card

# -------------------------------------------------
# MAIN ACTIONS
# -------------------------------------------------
st.markdown("<div class='section-heading'>What do you want to work on today?</div>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🧱 New Construction")
    st.write("Set up a ground‑up build with phases, budget, and schedule.")
    if st.button("Start New Build →", use_container_width=True, type="primary"):
        st.switch_page("pages/new_construction.py")

with c2:
    st.markdown("### 🛠️ Remodel / Renovation")
    st.write("Plan scope, demo, changes, and track cost overruns.")
    if st.button("Start Remodel →", use_container_width=True, type="primary"):
        st.switch_page("pages/remodel.py")

with c3:
    st.markdown("### 📏 Quick Estimate")
    st.write("Fast ballpark using sq ft + finish level.")
    if st.button("Get Quick Price →", use_container_width=True, type="primary"):
        st.switch_page("pages/quick_estimate.py")

st.markdown("---")

# -------------------------------------------------
# WHO IT'S FOR
# -------------------------------------------------
st.markdown("<div class='section-heading'>Built for residential work.</div>", unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.markdown("#### 🧱 Builders & GCs")
    st.markdown("""
    - Track multiple jobs easily  
    - Phase‑based views  
    - Budget vs. actual clarity  
    """)

with b:
    st.markdown("#### 🏡 Homeowners")
    st.markdown("""
    - Know where money goes  
    - See progress by phase  
    - Fewer budget surprises  
    """)

with c:
    st.markdown("#### 🧮 Lenders / Banks")
    st.markdown("""
    - Clean draw schedules  
    - Proof of progress  
    - Exportable summaries  
    """)

st.markdown("---")
st.caption("Roberts Residential, LLC – Serving Dothan, AL, and surrounding communities.")
``
