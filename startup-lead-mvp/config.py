import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

PUBMED_PATH = os.path.join(DATA_DIR, "pubmed.csv")
FUNDING_PATH = os.path.join(DATA_DIR, "funding.csv")
CONFERENCES_PATH = os.path.join(DATA_DIR, "conferences.csv")

RANKED_LEADS_PATH = os.path.join(OUTPUT_DIR, "ranked_leads.csv")
