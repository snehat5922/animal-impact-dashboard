import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/animal-lives-lost-direct.csv"
)

st.title("📈 Comparative Insights")

food1 = st.selectbox(
    "Food A",
    df["Entity"]
)

food2 = st.selectbox(
    "Food B",
    df["Entity"],
    index=1
)

compare = df[
    df["Entity"].isin(
        [food1, food2]
    )
]

fig = px.bar(
    compare,
    x="Entity",
    y="lives_per_kg_direct",
    color="Entity",
    title="Food Comparison"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

difference = abs(
    compare.iloc[0]["lives_per_kg_direct"]
    -
    compare.iloc[1]["lives_per_kg_direct"]
)

st.success(
    f"Difference in impact: {difference:.3f} lives/kg"
)
