def compute_score(row):
    score = 0

    title = row["title"].lower()
    keywords = str(row["keywords"]).lower()
    year = row["year"]

    # Role Fit
    if any(x in title for x in ["director", "head", "vp"]):
        score += 30

    # Scientific Intent
    if "liver" in keywords and year >= 2023:
        score += 40

    # Company Intent
    if str(row["stage"]).lower() in ["series a", "series b"]:
        score += 20

    # Technographic
    if any(x in keywords for x in ["3d", "in-vitro", "organ-on-chip"]):
        score += 15

    # Location
    if row["in_hub"]:
        score += 10

    return min(score, 100)
