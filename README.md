# Statistical Hypothesis Testing Examples

This project provides practical examples of common statistical hypothesis tests applied to real-world datasets using Python. The goal is to demonstrate how to:

- Visualise data and group differences
- Check key assumptions of tests
- Perform hypothesis tests
- Interpret results clearly and correctly

## Current Contents

### One-tailed t-test Example
- Dataset: [Diabetes dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) from `scikit-learn`
- Objective: Test whether the average disease progression differs by sex, specifically testing if one sex group has a lower average target value than the other.
- Techniques:
  - Boxplots to visualise group distributions
  - Q-Q plots to check normality
  - Levene's test to check homoscedasticity (equal variances)
  - One-tailed independent samples t-test using `scipy.stats`

## Planned Additions

- Two-tailed t-test example  
- One-way ANOVA example  
Each will include the same structured workflow for data visualization, assumptions testing, hypothesis formulation, and interpretation.
