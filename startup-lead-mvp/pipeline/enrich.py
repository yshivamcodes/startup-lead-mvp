import pandas as pd

HUBS = ["Boston", "Cambridge", "Basel", "San Francisco", "UK"]

def infer_email(name, company):
    parts = name.lower().replace("dr ", "").split()
    return f"{parts[0]}.{parts[-1]}@{company.lower().replace(' ', '')}.com"

def is_hub(location):
    return any(hub in location for hub in HUBS)

def enrich_leads(leads, funding_path):
    funding = pd.read_csv(funding_path)
    enriched = leads.merge(
        funding, left_on="affiliation", right_on="company", how="left"
    )

    enriched["email"] = enriched.apply(
        lambda x: infer_email(x["name"], x["affiliation"].split()[0]), axis=1
    )

    enriched["in_hub"] = enriched["affiliation"].apply(is_hub)

    return enriched
