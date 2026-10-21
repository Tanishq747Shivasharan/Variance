# Project Milestones & Execution Plan

## IT Project Delay & Performance Analytics

### Project Objective

Analyze real-world software project data to identify patterns associated with project delays, effort variance, and overall performance. Use data analytics and visualization to communicate findings and develop evidence-based recommendations.

---

## Phase 1 — Dataset Understanding & Audit

**Goal:** Understand the SEERA dataset before writing analysis code.

### Milestone 1.1 — Dataset Familiarization

- [x] Identify all 10 sheets in the original Excel workbook.
- [x] Confirm that the main dataset reports 120 project records.
- [x] Inspect the main sheet's column headings and sample records.
- [x] Locate the official SEERA README and attribute formulas documentation.
- [x] Understand the documented distinction between `?` and `N/A`.
- [x] Establish how the consolidated sheet relates to the category-specific sheets.

### Milestone 1.2 — Data Quality Audit

- [x] Investigate the reported record counts in General Information and Environment.
- [x] Verify 120 project IDs in General Information.
- [x] Verify 120 records in Environment.
- [x] Identify `?` and `N/A` values in Environment.
- [ ] Use Python/Pandas to count missing values systematically.
- [ ] Check for duplicate project IDs, inconsistent records, and genuinely blank cells.
- [ ] Document the findings and decide how each special value should be handled.

**Deliverable:** Dataset audit notes and a reproducible data-quality report.

**Current position:** We have completed the initial manual inspection. The programmatic audit remains pending.

---

## Phase 2 — Development Environment Setup

**Goal:** Prepare a reproducible workspace for the team.

### Milestone 2.1 — Project Repository

- [ ] Establish the shared GitHub repository.
- [ ] Create the project folder structure.
- [ ] Add the README and project synopsis.
- [ ] Establish `.gitignore` and dependency-management practices.
- [ ] Check the dataset's redistribution terms before publishing raw data.

### Milestone 2.2 — Python Environment

- [ ] Verify Python installation.
- [ ] Create and activate a virtual environment.
- [ ] Install Pandas, NumPy, Matplotlib, Seaborn, Openpyxl, and JupyterLab.
- [ ] Create the first notebook: `01_seera_dataset_audit.ipynb`.
- [ ] Verify that Python can read the Excel workbook.

**Deliverable:** A working, documented development environment.

---

## Phase 3 — Data Understanding & Preparation

**Goal:** Convert the raw source into a reliable analysis-ready dataset.

### Milestone 3.1 — Attribute Selection

- [ ] Identify relevant attributes for schedule and performance analysis.
- [ ] Distinguish original attributes, sub-attributes, and derived attributes.
- [ ] Review the official formulas and coding definitions.
- [ ] Identify appropriate variables for project duration, effort, team, requirements, and management.

### Milestone 3.2 — Data Cleaning

- [ ] Handle missing values according to their documented meaning.
- [ ] Preserve `N/A` where it represents a non-applicable conditional question.
- [ ] Check data types and inconsistent entries.
- [ ] Investigate outliers without automatically deleting them.
- [ ] Keep the original raw workbook unchanged.

### Milestone 3.3 — Feature Engineering

- [ ] Derive duration variance where valid.
- [ ] Derive duration variance percentage where mathematically appropriate.
- [ ] Derive or verify effort variance using documented source definitions.
- [ ] Create additional performance indicators only when supported by the data.
- [ ] Validate calculations against example records.

**Deliverable:** A documented, analysis-ready dataset with validated metrics.

---

## Phase 4 — Exploratory Data Analysis (EDA)

**Goal:** Understand the data and discover meaningful patterns.

### Milestone 4.1 — Descriptive Statistics

- [ ] Calculate counts, distributions, averages, medians, and ranges.
- [ ] Understand the distribution of duration and effort.
- [ ] Examine missingness and unusual values.
- [ ] Summarize relevant project characteristics.

### Milestone 4.2 — Performance Analysis

- [ ] Compare estimated and actual project duration.
- [ ] Analyze estimated versus actual effort.
- [ ] Examine performance across project size and complexity.
- [ ] Explore team, requirements, management, and technical factors.
- [ ] Investigate relationships between project characteristics and performance.

**Deliverable:** EDA notebook with verified tables, observations, and findings.

---

## Phase 5 — Data Visualization

**Goal:** Communicate analytical findings clearly.

- [ ] Create duration and effort comparison charts.
- [ ] Visualize the distributions of key performance metrics.
- [ ] Compare performance across relevant project categories.
- [ ] Explore associations using suitable charts.
- [ ] Label charts correctly and explain their interpretation.
- [ ] Avoid visualizations that imply unsupported conclusions.

**Tools:** Matplotlib and Seaborn.

**Deliverable:** A set of meaningful, well-documented visualizations.

---

## Phase 6 — Dashboard Development

**Goal:** Present the findings in an interactive and understandable format.

- [ ] Select appropriate KPIs based on the final analysis.
- [ ] Design the dashboard layout.
- [ ] Add relevant charts and summary indicators.
- [ ] Add filters where the data supports useful comparisons.
- [ ] Verify calculations and displayed values.
- [ ] Test usability and prepare a demonstration.

**Tools:** Power BI and/or Streamlit, depending on the team's final choice.

**Deliverable:** A functional project-performance dashboard.

---

## Phase 7 — Insights & Recommendations

**Goal:** Turn analytical results into useful conclusions.

- [ ] Identify the strongest supported findings.
- [ ] Explain which characteristics are associated with schedule or effort differences.
- [ ] Distinguish observations from hypotheses.
- [ ] Avoid claiming causation from correlation.
- [ ] Develop practical recommendations based on the evidence.
- [ ] Document limitations and the dataset's context.

**Deliverable:** A findings and recommendations report.

---

## Phase 8 — Documentation & Presentation

**Goal:** Prepare the project for academic evaluation.

- [ ] Update the GitHub README with the completed methodology.
- [ ] Document the dataset source, cleaning decisions, and metrics.
- [ ] Prepare the final project report.
- [ ] Prepare the presentation slides.
- [ ] Explain the workflow, visualizations, and key findings.
- [ ] Prepare for viva questions and technical demonstrations.

**Deliverable:** Complete documentation and presentation materials.

---

## Phase 9 — Portfolio & Resume Readiness

**Goal:** Make the completed work understandable and defensible.

- [ ] Ensure the repository is organized and reproducible.
- [ ] Include verified findings rather than invented results.
- [ ] Document tools and techniques actually used.
- [ ] Prepare a concise project description for the resume.
- [ ] Practise explaining the project independently.
- [ ] Prepare answers to questions about data quality, metrics, limitations, and conclusions.

**Deliverable:** A portfolio-ready project that every team member can explain.

---

## Team Working Rules

1. Work on the current milestone before moving to the next.
2. Preserve the original dataset.
3. Do not fabricate data or use web scraping.
4. Verify calculations and assumptions before using results.
5. Record decisions so every team member understands the methodology.
6. Use Git for version control and communicate changes clearly.
7. Do not claim findings until the analysis supports them.
8. Learn the reasoning behind the code rather than copying solutions blindly.

## Current Status

**Active milestone:** Phase 1 — Dataset Understanding & Audit.

**Next task:** Use Python and Pandas to inspect the workbook systematically, verify the sheet structures, and count missing values.

**Immediate objective:** Complete the dataset audit before moving into cleaning, feature engineering, or exploratory analysis.

The project will progress milestone by milestone, with practical work and verification at each stage.
