from pipeline.identify import identify_leads
from pipeline.enrich import enrich_leads
from pipeline.score import compute_score
import os

def generate_ranked_leads():
    os.makedirs("output", exist_ok=True)

    leads = identify_leads("data/pubmed.csv", "data/conferences.csv")
    leads = enrich_leads(leads, "data/funding.csv")

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

    output_path = "output/ranked_leads.csv"
    leads[final_cols].to_csv(output_path, index=False)

    return output_path


if __name__ == "__main__":
    generate_ranked_leads()
