import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_csv("data/animal-lives-lost-direct.csv")

df = load_data()

st.title("📊 Executive Summary")

total_foods = len(df)

highest = df.loc[
    df["lives_per_kg_direct"].idxmax(),
    "Entity"
]

lowest = df.loc[
    df["lives_per_kg_direct"].idxmin(),
    "Entity"
]

avg = round(
    df["lives_per_kg_direct"].mean(),
    3
)

c1,c2,c3,c4 = st.columns(4)

c1.metric("Food Categories", total_foods)
c2.metric("Average Impact", avg)
c3.metric("Highest Impact", highest)
c4.metric("Lowest Impact", lowest)

fig = px.bar(
    df.sort_values(
        "lives_per_kg_direct",
        ascending=False
    ),
    x="Entity",
    y="lives_per_kg_direct",
    color="lives_per_kg_direct",
    title="Animal Lives Lost per kg"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
