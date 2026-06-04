import streamlit as st

st.set_page_config(
    page_title="Animal Impact Dashboard",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 Food Sustainability Analytics Dashboard")

st.markdown("""
Analyze the direct animal lives lost per kilogram of food production.

Explore:

- Food impact rankings
- Sustainability comparisons
- Animal welfare insights
- Food choice recommendations
""")

st.info("Select a page from the sidebar.")
