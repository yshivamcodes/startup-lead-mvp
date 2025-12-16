#  Startup Lead MVP

A lightweight end-to-end MVP that processes multiple startup-related datasets, identifies promising leads, enriches them with additional context, scores them, and presents ranked results through a simple dashboard.

---

##  Short Description

A Python-based MVP for generating, enriching, scoring, and visualizing startup leads using a modular data pipeline.

---

##  Problem Statement

Identifying high-potential startup leads from raw and scattered datasets is time-consuming and subjective.

This project demonstrates how a **structured data pipeline** can automate lead identification, enrichment, and scoring to support faster and more informed decision-making.

---

##  Features

-  Ingests multiple structured CSV datasets
-  Modular pipeline architecture
-  Lead identification logic
-  Data enrichment stage
-  Lead scoring and ranking mechanism
-  Lightweight dashboard for visualization
-  Simple and extensible MVP design

---

##  Project Structure

startup-lead-mvp/
│
├── data/
│   ├── pubmed.csv
│   ├── funding.csv
│   ├── conferences.csv
│
├── pipeline/
│   ├── identify.py
│   ├── enrich.py
│   ├── score.py
│
├── dashboard.py
├── requirements.txt
└── run_pipeline.py


---

## How the Pipeline Works

1. **Identify**  
   Extracts and filters relevant startup leads from raw datasets.

2. **Enrich**  
   Adds contextual or derived attributes to each identified lead.

3. **Score**  
   Assigns a numerical score using predefined heuristics to rank leads.

4. **Visualize**  
   Displays ranked startup leads through a simple dashboard interface.

---

## Installation & Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt

python run_pipeline.py

streamlit run dashboard.py

```
---

## License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this code with proper attribution.

---

## Author

Shivam Yadav
GitHub: https://github.com/yshivamcodes



