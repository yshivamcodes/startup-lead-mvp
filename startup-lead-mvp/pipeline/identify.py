import pandas as pd

def identify_leads(pubmed_path, conference_path):
    pubmed = pd.read_csv(pubmed_path)
    conf = pd.read_csv(conference_path)

    leads = pubmed.merge(conf, on="name", how="left")
    return leads
