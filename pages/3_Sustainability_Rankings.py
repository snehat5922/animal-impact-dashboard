import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv(
    "data/animal-lives-lost-direct.csv"
)

st.title("🏆 Sustainability Rankings")

ranking = df.sort_values(
    "lives_per_kg_direct"
)

ranking["Rank"] = range(
    1,
    len(ranking)+1
)

st.dataframe(
    ranking,
    use_container_width=True
)

fig = px.bar(
    ranking,
    x="Entity",
    y="lives_per_kg_direct",
    color="Rank",
    title="Most Sustainable to Least Sustainable"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
