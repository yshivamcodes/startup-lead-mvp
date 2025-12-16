import streamlit as st
import pandas as pd
import os
from run_pipeline import generate_ranked_leads
from config import RANKED_LEADS_PATH

st.set_page_config(layout="wide")
st.title("Lead Generation Dashboard – MVP")

if not os.path.exists(RANKED_LEADS_PATH):
    with st.spinner("Running lead generation pipeline..."):
        generate_ranked_leads()

df = pd.read_csv(RANKED_LEADS_PATH)

search = st.text_input("Search leads")
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
