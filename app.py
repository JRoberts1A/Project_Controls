import streamlit as st

st.set_page_config(page_title="Residential Project Tracker", layout="wide")

st.title("Welcome to Project Tracker")
st.markdown("Choose your project type:")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("New Construction", use_container_width=True):
        st.write("You picked New Construction! Dashboard coming soon...")

with col2:
    if st.button("Remodel", use_container_width=True):
        st.write("Remodel mode—let's fix something!")

with col3:
    if st.button("Quick Estimate", use_container_width=True):
        st.write("Fast price check—coming up!")
