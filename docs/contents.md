# Current Contents

## One-tailed t-test Example
- Dataset: [Diabetes dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html) from `scikit-learn`
- Objective: Test whether the average disease progression differs by sex, specifically testing if one sex group has a lower average target value than the other.
- Techniques:
  - Boxplots to visualise group distributions
  - Q-Q plots to check normality
  - Levene's test to check homoscedasticity (equal variances)
  - One-tailed independent samples t-test using `scipy.stats`

## Two-tailed t-test Example
- Dataset: [Breast cancer dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html) from `scikit-learn`
- Objective: Test whether the mean radius differs between malignant and benign tumors.
- Techniques:
  - Boxplots to visualise group distributions
  - Q-Q plots to check normality
  - Levene's test to check homoscedasticity (equal variances)
  - Two-tailed independent samples t-test using `scipy.stats`

## ANOVA Example
- Dataset: [Wine dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html) from `scikit-learn`
- Objective: Test whether alcohol measurements differ between wine cultivars.
- Techniques:
  - Boxplots to visualise group distributions
  - Q-Q plots to check normality
  - Levene's test to check homoscedasticity (equal variances)
  - ANOVA test (f_oneway()) using `scipy.stats`
