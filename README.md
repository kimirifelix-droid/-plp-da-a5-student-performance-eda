# Student Performance EDA for a County Education Office

## Project Overview

This project performs exploratory data analysis (EDA) on a dataset containing 1,200 student records generated using seed 55. The analysis examines learner performance across Mathematics, English and Science and investigates how average scores relate to attendance, study hours, gender, school type and county.

The purpose is to provide evidence that can help a County Education Office identify learners and locations that may require additional support.

## Dataset

The dataset contains one row per student and includes:

- student_id
- gender
- school_type
- county
- attendance
- study_hours
- math_score
- english_score
- science_score

Two derived variables are created during the analysis:

- average_score - mean score across Mathematics, English and Science
- performance_band - At Risk (<60), Meeting (60-74), Exceeding (75+)

## EDA Sections

The notebook contains five required EDA sections:

1. Structure
2. Univariate
3. Bivariate
4. Multivariate
5. Hypotheses

The analysis includes descriptive statistics, categorical shares, outlier detection, correlation analysis, group comparisons, pivot tables, trend analysis and charts.

## Key Insights

1. Mathematics has the strongest relationship with overall performance, with a correlation of approximately r = 0.752 with average_score.

2. Study hours are positively associated with average score. The fitted trend line has a slope of approximately 1.1907.

3. Private schools have a higher mean average score of approximately 66.34 compared with 62.36 for public schools.

4. Kisumu has the highest average county performance, with a mean average score of approximately 64.08.

5. Nairobi has the highest concentration of At Risk learners, with approximately 33.11% classified as At Risk.

## Recommendations

1. Prioritise learner-support resources toward counties with the highest observed At Risk shares, while validating the findings with local education officers before final resource allocation.

2. Combine academic support with attendance and study-support interventions by identifying learners with multiple risk indicators rather than relying on a single variable.

## Limitations

This analysis is exploratory and observational. Correlations and trend lines show associations rather than causation. The dataset contains no dates, so it cannot establish changes in performance over time. Study hours and attendance may not capture the quality of studying or the reasons behind attendance patterns. County and school-type comparisons may also reflect other factors that are not included in the dataset. Therefore, the findings should support targeting and further investigation rather than be treated as definitive evidence that one factor causes better or worse academic performance.

## Project Files

- generate_data.py - dataset generation script using seed 55
- student_performance.csv - student performance dataset
- student_eda.ipynb - complete EDA notebook
- figures/ - exported analysis charts
- requirements.txt - required Python libraries

## Figures

- figures/average_score_histogram.png
- figures/study_hours_boxplot.png
- figures/school_type_bar.png
- figures/study_hours_trend.png

## Requirements

Install the required Python libraries:

pip install -r requirements.txt

Required libraries:

- pandas
- numpy
- matplotlib

## How to Run

Create a virtual environment:

python -m venv .venv

Activate it in Windows PowerShell:

.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Generate the dataset:

python generate_data.py

Open Jupyter Notebook:

jupyter notebook

Open student_eda.ipynb and run all cells from top to bottom.

## Conclusion

The EDA provides evidence on learner performance, risk concentration and factors associated with average scores. The results can support evidence-based learner-support planning, followed by local validation and further investigation.
