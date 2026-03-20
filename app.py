import streamlit as st

# Page config - makes it look like a real app
st.set_page_config(
    page_title="Residential Project Tracker",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"  # Keeps sidebar hidden at first
)

# Optional: Light custom styling (copy-paste this block)
st.markdown("""
    <style>
    .big-button {
        font-size: 24px !important;
        font-weight: bold;
        height: 120px;
        width: 100%;
        border-radius: 12px;
    }
    .hero-text {
        text-align: center;
        padding: 40px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Hero section - inspired by Plan7's big intro banner/text
st.markdown("<div class='hero-text'>", unsafe_allow_html=True)
st.title("🏠 Residential Project Tracker")
st.subheader("Plan smarter. Track costs & schedules. Build with confidence.")
st.markdown("""
Whether it's a **new home build**, a **full remodel**, or just a **quick cost check**,  
get a simple, powerful dashboard without the complexity of P6 or endless Excel sheets.
""")
st.markdown("</div>", unsafe_allow_html=True)

# Spacer
st.markdown("---")

# Three big choice buttons in columns (like Plan7's product tiers/cards)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### New Construction")
    st.markdown("Start from scratch: full timeline, budget, phases, alerts.")
    if st.button("Start New Build →", key="new", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "new"
        st.switch_page("pages/new_construction.py")   # We'll create this file next

with col2:
    st.markdown("### Remodel")
    st.markdown("Existing home? Demo, changes, cost overruns, progress tracking.")
    if st.button("Start Remodel →", key="remodel", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "remodel"
        st.switch_page("pages/remodel.py")

with col3:
    st.markdown("### Quick Estimate")
    st.markdown("Fast ballpark: sq ft, finishes, rough total in seconds.")
    if st.button("Get Quick Price →", key="quick", use_container_width=True, type="primary"):
        st.session_state["project_type"] = "quick"
        st.switch_page("pages/quick_estimate.py")

# Footer / trust elements (like Plan7's reviews/guarantees)
st.markdown("---")
st.markdown("""
**Why this tool?**  
- Built for residential projects (not mega construction bloat)  
- Real-time cost vs. budget tracking  
- Simple phase timelines  
- Export to PDF/Excel  
- Free to start – no subscriptions
""")

st.caption("Made for builders in Dothan, AL and beyond. Questions? Reach out anytime.")
