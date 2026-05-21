# Multivariate Modeling of Maternal Nutrition & Fetal Growth Outcomes

## 📌 Project Overview
Maternal nutrition during the third trimester is a critical determinant of fetal development. This project utilizes advanced data science techniques—specifically **Multiple Linear Regression (OLS)**—to model how various maternal dietary factors (Protein, Iron, Folic Acid) and clinical conditions (Gestational Diabetes) collectively impact fetal birth weight and neonatal APGAR scores.

This repository serves as an example of applying **computational statistics and predictive analytics** to clinical dietetics and maternal-fetal medicine.

## 🔬 Key Research Objectives
1. Perform a multivariate regression analysis to isolate the statistical significance of protein and iron intake on birth weight.
2. Evaluate the categorical impact of Folic Acid supplementation on APGAR scores using violin plot distributions.
3. Quantify the negative coefficient of Gestational Diabetes on healthy fetal weight ranges.

## 📂 Repository Contents
- `maternal_data.csv`: An expanded, detailed clinical dataset containing continuous and categorical nutritional metrics.
- `advanced_modeling.py`: Python script utilizing `pandas` for data manipulation, `statsmodels` for rigorous OLS regression, and `seaborn` for complex visualizations.
- `protein_vs_birthweight.png`: Regression curve showing the correlation between protein and birth weight.
- `apgar_folic_acid.png`: Violin plot detailing the density distribution of APGAR scores.

## 🛠️ Tech Stack & Methodologies
- **Languages:** Python 3
- **Libraries:** Statsmodels (Advanced Econometrics/Statistics), Pandas, Matplotlib, Seaborn
- **Methodology:** Ordinary Least Squares (OLS) Regression, Continuous/Categorical Variable Mapping, Statistical Hypothesis Testing.

## 🚀 Execution Guide
```bash
# Install required advanced statistical libraries
pip install pandas statsmodels matplotlib seaborn

# Run the predictive model
python advanced_modeling.py
```

## 📊 Summary of Statistical Findings
- **High Statistical Significance (p < 0.01):** Third-trimester protein intake is a massive predictor of healthy birth weight, as proven by the OLS regression summary.
- **Categorical Impact:** Folic acid supplementation not only standardizes but elevates APGAR score density, reducing the variance in neonatal distress outcomes.
- **Clinical Insight:** The model successfully isolates the negative impact of gestational diabetes, allowing dietitians to quantitatively argue for strict nutritional interventions.
