import os
from pipeline.identify import identify_leads
from pipeline.enrich import enrich_leads
from pipeline.score import compute_score
from config import (
    PUBMED_PATH,
    CONFERENCES_PATH,
    FUNDING_PATH,
    OUTPUT_DIR,
    RANKED_LEADS_PATH,
)

def generate_ranked_leads():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    leads = identify_leads(PUBMED_PATH, CONFERENCES_PATH)
    leads = enrich_leads(leads, FUNDING_PATH)

    leads["probability"] = leads.apply(compute_score, axis=1)
    leads = leads.sort_values("probability", ascending=False)
    leads["rank"] = range(1, len(leads) + 1)

    final_cols = [
        "rank",
        "probability",
        "name",
        "title",
        "affiliation",
        "email",
        "paper_title",
    ]

    leads[final_cols].to_csv(RANKED_LEADS_PATH, index=False)
    return RANKED_LEADS_PATH


if __name__ == "__main__":
    generate_ranked_leads()
