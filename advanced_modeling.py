import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# 1. Load Data
print("Loading Maternal Nutrition & Fetal Growth Data...")
df = pd.read_csv("maternal_data.csv")

# Convert categorical variables to binary for regression
df['Folic_Acid_Num'] = df['Folic_Acid_Supplements'].map({'Yes': 1, 'No': 0})
df['Gestational_Diabetes_Num'] = df['Gestational_Diabetes'].map({'Yes': 1, 'No': 0})

print("\n--- Summary Statistics ---")
print(df.describe())

# 2. Multiple Linear Regression Model (Predicting Birth Weight)
print("\n--- Advanced Multiple Regression Analysis ---")
X = df[['Trimester_3_Protein_g', 'Trimester_3_Iron_mg', 'Folic_Acid_Num', 'Gestational_Diabetes_Num']]
X = sm.add_constant(X) # Add intercept
y = df['Birth_Weight_kg']

model = sm.OLS(y, X).fit()
print(model.summary())

# 3. Visualization 1: Protein Intake vs Birth Weight (with regression line)
plt.figure(figsize=(8, 6))
sns.regplot(x='Trimester_3_Protein_g', y='Birth_Weight_kg', data=df, 
            scatter_kws={'alpha':0.7}, line_kws={'color':'darkorange'})
plt.title('Impact of 3rd Trimester Protein Intake on Fetal Birth Weight')
plt.xlabel('Average Daily Protein Intake (g)')
plt.ylabel('Birth Weight (kg)')
plt.grid(True, alpha=0.3)
plt.savefig('protein_vs_birthweight.png')
print("\nSaved plot: protein_vs_birthweight.png")

# 4. Visualization 2: APGAR Scores by Folic Acid Supplementation
plt.figure(figsize=(7, 5))
sns.violinplot(x='Folic_Acid_Supplements', y='APGAR_Score', data=df, palette='muted')
plt.title('Neonatal APGAR Scores Based on Maternal Folic Acid Intake')
plt.xlabel('Folic Acid Supplements Taken')
plt.ylabel('APGAR Score (out of 10)')
plt.savefig('apgar_folic_acid.png')
print("Saved plot: apgar_folic_acid.png")

print("\nDetailed computational modeling complete. All graphs exported successfully.")
