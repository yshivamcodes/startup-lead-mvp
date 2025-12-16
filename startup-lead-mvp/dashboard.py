import streamlit as st
import pandas as pd
import os

st.set_page_config(layout="wide")
st.title("Lead Generation Dashboard – MVP")

FILE_PATH = "ranked_leads.csv"

if not os.path.exists(FILE_PATH):
    st.error("ranked_leads.csv not found. Please run run_pipeline.py first.")
    st.stop()

df = pd.read_csv(FILE_PATH)

search = st.text_input("Search")
if search:
    df = df[df.apply(
        lambda r: search.lower() in r.astype(str).str.lower().to_string(),
        axis=1
    )]

st.dataframe(df, use_container_width=True)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "ranked_leads.csv",
    "text/csv"
)
