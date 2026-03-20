import streamlit as st

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Roberts Residential | Project Tracker",
    page_icon="🏠",
    layout="wide",
)

# -------------------------------------------------
# GLOBAL BRAND COLORS (Roberts Residential, LLC)
# -------------------------------------------------
PRIMARY_RED = "#c00000"
DARK_TEXT = "#222222"
LIGHT_BG = "#ffffff"
SOFT_GRAY = "#f5f5f5"

# -------------------------------------------------
# Custom CSS — polished layout
# -------------------------------------------------
st.markdown(f"""
    <style>

    /* Force LIGHT MODE for consistent branding */
    body {{
        background-color: {LIGHT_BG} !important;
        color: {DARK_TEXT} !important;
    }}

    /* Remove padding from top of page */
    .block-container {{
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }}

    /* HERO CARD */
    .hero-card {{
        background-color: {LIGHT_BG};
        padding: 2rem 1rem;
        border-radius: 16px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        max-width: 900px;
        margin: 0 auto 2rem auto;
        text-align: center;
    }}

    .hero-title {{
        font-size: 2.4rem;
        font-weight: 800;
        color: {PRIMARY_RED};
        margin-top: 1rem;
        margin-bottom: 0.25rem;
    }}

    .hero-subtitle {{
        font-size: 1.2rem;
        color: #444;
        margin-bottom: 1rem;
    }}

    .hero-body {{
        max-width: 700px;
        margin: 0 auto;
        font-size: 1.05rem;
        color: #333;
    }}

    /* Section titles */
    .section-heading {{
        font-size: 1.4rem;
        font-weight: 700;
        color: {PRIMARY_RED};
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }}

    /* Hide Streamlit chrome */
    #MainMenu, footer {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# HERO SECTION (logo + text)
# -------------------------------------------------
st.markdown("<div class='hero-card'>", unsafe_allow_html=True)

# LOGO — scaled to a clean width
st.image("Logo_White.jpg", width=260)

st.markdown("<div class='hero-title'>Residential Project Tracker</div>", unsafe_allow_html=True)

st.markdown(
    "<div class='hero-subtitle'>Plan smarter. Track costs & schedules. Build with confidence.</div>",
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='hero-body'>
    Built by <b>Roberts Residential, LLC</b> for real‑world homebuilding and remodeling.
    Keep your owners, lenders, and subcontractors aligned with clean, easy‑to‑read dashboards.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

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

# -------------------------------------------------
# AUDIENCE SECTIONS
# -------------------------------------------------
st.markdown("<div class='section-heading'>Built for residential work.</div>", unsafe_allow_html=True)

a, b, c = st.columns(3)

with a:
    st.markdown("#### 🧱 Builders & GCs")
    st.markdown("- Track multiple jobs easily\n- Phase‑based views\n- Budget vs. actual clarity")

with b:
    st.markdown("#### 🏡 Homeowners")
    st.markdown("- Know where money goes\n- Phase progress\n- Fewer surprises")

with c:
    st.markdown("#### 🧮 Lenders / Banks")
    st.markdown("- Clean draw schedules\n- Proof of progress\n- Exportable summaries")

st.markdown("---")
st.caption("Roberts Residential, LLC – Serving Dothan, AL and surrounding communities.")
