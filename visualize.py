import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Cleaned data load
df = pd.read_csv('Cleaned_Telco_Churn.csv')

# Plot styling
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# 1. Churn by Contract
plt.subplot(2, 2, 1)
sns.barplot(
    data=df,
    x='Contract',
    y='Churn_Flag',
    estimator=lambda x: sum(x) / len(x) * 100,
    errorbar=None,
    palette='Blues_r',
)
plt.title('Churn Rate by Contract Type (%)')
plt.ylabel('Churn Rate (%)')
plt.xlabel('')

# 2. Churn by Tenure Cohort
plt.subplot(2, 2, 2)
order = ['0-12 M', '13-24 M', '25-36 M', '37-48 M', '49-60 M', '61-72 M']
sns.barplot(
    data=df,
    x='Tenure_Cohort',
    y='Churn_Flag',
    order=order,
    estimator=lambda x: sum(x) / len(x) * 100,
    errorbar=None,
    palette='Reds_r',
)
plt.title('Retention Drop by Tenure Cohort (%)')
plt.ylabel('Churn Rate (%)')
plt.xlabel('')

# 3. Monthly Charges vs Churn
plt.subplot(2, 2, 3)
sns.kdeplot(
    data=df[df['Churn'] == 'Yes']['MonthlyCharges'],
    label='Churned',
    fill=True,
    color='red',
)
sns.kdeplot(
    data=df[df['Churn'] == 'No']['MonthlyCharges'],
    label='Retained',
    fill=True,
    color='green',
)
plt.title('Monthly Charges Distribution (Retained vs Churned)')
plt.xlabel('Monthly Charges ($)')
plt.legend()

# 4. Churn by Tech Support
plt.subplot(2, 2, 4)
sns.barplot(
    data=df,
    x='TechSupport',
    y='Churn_Flag',
    estimator=lambda x: sum(x) / len(x) * 100,
    errorbar=None,
    palette='Purples_r',
)
plt.title('Churn Rate by Tech Support Status (%)')
plt.ylabel('Churn Rate (%)')
plt.xlabel('')

plt.tight_layout()
plt.savefig('churn_analysis_dashboard.png', dpi=300)
print(
    "Dashboard charts saved successfully as 'churn_analysis_dashboard.png'!"
)