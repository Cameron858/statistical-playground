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


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Cameron858/t-tests-and-anova
    ```

2. Navigate to the project directory:
    ```bash
    cd knapsack-ga
    ```

3. Install [uv](https://github.com/astral-sh/uv) if not already installed:
    ```bash
    pipx install uv
    ```

4. Create `venv` with uv:
    ```bash
    uv venv
    ```

5. Activate the virtual environment:
    ```bash
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate # On macOS/Linux
    ```

6. Install the required dependencies using uv:
    ```bash
    uv pip install -e .
    ```

7. When you're done working, deactivate the virtual environment:
    ```bash
    deactivate
    ```
