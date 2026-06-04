import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/animal-lives-lost-direct.csv"
)

st.title("🐔 Food Impact Analysis")

fig = px.treemap(
    df,
    path=["Entity"],
    values="lives_per_kg_direct",
    title="Animal Impact Treemap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

fig = px.pie(
    df,
    names="Entity",
    values="lives_per_kg_direct",
    hole=.5,
    title="Impact Share"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
