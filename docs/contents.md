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

## Chi-squared: Test of Independence Example
- Dataset: [Heart Failure](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) from `kaggle`
- Objective: Test if the *biological sex (M/F)* of an individual affects heart disease.
- Techniques:
  - Perform chi-squared test of independence

## Chi-squared: Goodness-of-fit Test Example
- Dataset: [Heart Failure](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) from `kaggle`
- Objective: Test if the dataset is balanced in terms of *biological sex (M/F)*.
- Techniques:
  - Visualise feature split using a pie chart
  - Perform chi-squared goodness-of-fit test

## Chi-squared: Test of Homogeneity Test Example
- Dataset: [Heart Failure](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction) from `kaggle`
- Objective: Test if males and females with heart disease experience different types of chest pain at similar rates.
- Techniques:
  - Visualise categorical distributions across groups using stackedbar (column) plots
  - Perform chi-squared test of homogeneity