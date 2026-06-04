import streamlit as st
import pandas as pd

df = pd.read_csv(
    "data/animal-lives-lost-direct.csv"
)

st.title("💡 Sustainability Recommendations")

best = (
    df.sort_values(
        "lives_per_kg_direct"
    )
    .head(5)
)

worst = (
    df.sort_values(
        "lives_per_kg_direct",
        ascending=False
    )
    .head(5)
)

st.subheader(
    "✅ Lower Impact Food Choices"
)

st.dataframe(best)

st.subheader(
    "⚠ Higher Impact Food Choices"
)

st.dataframe(worst)

st.success("""
Choosing foods with lower animal impact can significantly
reduce total animal lives affected by food consumption.
""")
