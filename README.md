# IT Project Delay & Performance Analytics

**A Data Analytics Project to Identify Factors Associated with IT Project Delays, Effort Variance, and Performance Differences**

## About the Project

IT projects frequently experience differences between their estimated and actual schedules and effort. These differences can be associated with several factors, including project size, team experience, requirements, project complexity, development methodology, and project management practices.

**IT Project Delay & Performance Analytics** is a data analytics project that explores historical software project data to understand these differences, identify performance patterns, and generate meaningful insights that can support better project planning and management.

The project uses a real-world research dataset and follows a structured data analytics workflow, from data understanding and cleaning to exploratory analysis, visualization, and dashboard development.

## Objectives

- Analyze differences between estimated and actual project duration.
- Examine estimated versus actual project effort.
- Identify project characteristics associated with schedule and effort variance.
- Explore relationships between project size, complexity, team characteristics, requirements, and performance.
- Analyze project gain/loss information where the available data supports it.
- Develop visualizations and a dashboard to communicate important findings.
- Provide evidence-based recommendations for improving project planning and management.

## Dataset

This project uses the **SEERA (Software enginEERing in SudAn) dataset**, a publicly available research dataset containing information from 120 software development projects across 42 organizations in Sudan.

The dataset contains 76 attributes covering different aspects of software projects, including effort, size, developers, users, product characteristics, project information, and environmental factors.

**Dataset source:** [SEERA Dataset on Zenodo](https://zenodo.org/records/4312777)

**Primary raw data file:** `SEERA dataset original raw data.xlsx`

The dataset will be examined before finalizing the analytical variables. Only variables relevant to the project objectives and sufficiently documented for interpretation will be selected.

## Key Areas of Analysis

### 1. Schedule Performance
- Estimated versus actual project duration
- Duration variance and percentage variance
- Identification of early, on-time, and delayed projects, subject to validation of the source data

### 2. Effort Performance
- Estimated versus actual project effort
- Effort variance and percentage variance
- Comparison of effort differences across project characteristics

### 3. Project Characteristics
- Project size and complexity
- Team size and experience
- Requirements stability and flexibility
- Development methodology
- Project management practices
- Technical and environmental factors

### 4. Overall Project Performance
- Analysis of available project gain/loss information
- Exploration of factors associated with differences in project outcomes
- Identification of patterns that may support better project planning

The final analysis will depend on the actual variables, data quality, and coding definitions available in the dataset.

## Tools and Technologies

- **Python** — Data analysis and processing
- **Pandas** — Data manipulation and cleaning
- **NumPy** — Numerical operations
- **Matplotlib** — Data visualization
- **Seaborn** — Statistical visualization
- **Power BI and/or Streamlit** — Dashboard development
- **Jupyter Notebook / Google Colab / VS Code** — Development environment
- **Git and GitHub** — Version control and project documentation

## Project Workflow

The project follows these stages:

1. Dataset acquisition and source verification
2. Dataset understanding and column audit
3. Data cleaning and quality assessment
4. Selection of relevant variables
5. Feature engineering and metric calculation
6. Exploratory Data Analysis (EDA)
7. Data visualization and relationship analysis
8. Dashboard development
9. Interpretation of findings
10. Recommendations, documentation, and presentation

## Preliminary Performance Metrics

The following metrics will be considered after validating the source variables and their definitions.

**Duration Variance**

`Actual Duration - Estimated Duration`

**Duration Variance (%)**

`(Actual Duration - Estimated Duration) / Estimated Duration * 100`

**Effort Variance**

`Actual Effort - Estimated Effort`

**Effort Variance (%)**

`(Actual Effort - Estimated Effort) / Estimated Effort * 100`

A positive variance indicates that the actual value exceeds the estimate, while a negative variance indicates that the actual value is below the estimate. These interpretations assume that the underlying source values use compatible units and valid numeric scales.

## Repository Structure

```text
IT-Project-Delay-Performance-Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│
├── visualizations/
│
├── dashboard/
│
├── docs/
│
├── README.md
└── requirements.txt
```

- `data/raw/` — Original dataset, preserved without modification.
- `data/processed/` — Cleaned dataset and analysis-ready files.
- `notebooks/` — Exploratory analysis and experiments.
- `src/` — Reusable Python scripts and functions.
- `visualizations/` — Exported charts and figures.
- `dashboard/` — Dashboard implementation and related files.
- `docs/` — Synopsis, methodology, reports, and project documentation.
- `requirements.txt` — Python dependencies.

## Data Authenticity and Integrity

This project uses an existing public research dataset.

- No synthetic project records will be generated.
- No web scraping will be used.
- The original raw dataset will be preserved separately from processed data.
- Data cleaning and transformations will be documented.
- Missing values will be handled transparently rather than replaced with fabricated observations.
- The dataset source and relevant usage terms will be acknowledged.

## Expected Outcomes

The project aims to deliver:

- A documented, cleaned dataset suitable for analysis
- A reproducible Python-based analytics workflow
- Schedule and effort performance metrics
- Exploratory analysis of relevant project characteristics
- Meaningful data visualizations
- An interactive dashboard
- Evidence-based findings and practical recommendations
- A project report and presentation suitable for academic evaluation and future portfolio use

## Scope and Limitations

The project focuses on descriptive and exploratory data analytics. It does not aim to build an advanced machine learning or real-time prediction system.

The analysis will identify **associations, not prove causation**. Findings will be interpreted in the context of the available SEERA data and its source population. Results will not automatically be generalized to every IT organization or software project.

The final research questions, metrics, and dashboard indicators will be confirmed after the dataset audit.

## Project Status

**Current stage:** Dataset selected; detailed data audit and variable selection are pending.

Upcoming work includes data cleaning, feature engineering, exploratory analysis, visualization, dashboard development, and documentation.

## Acknowledgement

The SEERA dataset is used as the underlying source of historical software project data. Credit belongs to the original dataset authors and contributors.

**Official dataset:** https://zenodo.org/records/4312777

---

*This project is developed for academic learning and portfolio development, with an emphasis on data authenticity, reproducibility, analytical reasoning, and clear communication of findings.*
