from pipeline.identify import identify_leads
from pipeline.enrich import enrich_leads
from pipeline.score import compute_score

def run():
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

    leads[final_cols].to_csv("ranked_leads.csv", index=False)
    print("MVP pipeline complete. Output saved as ranked_leads.csv")

if __name__ == "__main__":
    run()
