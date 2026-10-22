import pandas as pd
import numpy as np

# 1. Load Dataset
print("Loading data...")
df =df = pd.read_csv('archive/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(f"Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

# 2. Data Cleaning
# Convert TotalCharges to numeric; empty spaces coerce to NaN, then drop
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(subset=['TotalCharges'], inplace=True)

# Format SeniorCitizen to standard Yes/No
df['SeniorCitizen'] = df['SeniorCitizen'].map({1: 'Yes', 0: 'No'})

# 3. Churn Flag & Tenure Cohort Creation
df['Churn_Flag'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)

bins = [0, 12, 24, 36, 48, 60, 72]
labels = ['0-12 M', '13-24 M', '25-36 M', '37-48 M', '49-60 M', '61-72 M']
df['Tenure_Cohort'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=True)

# 4. Key Performance Indicators (KPIs)
total_cust = len(df)
churned_cust = df['Churn_Flag'].sum()
churn_rate = (churned_cust / total_cust) * 100
mrr_lost = df[df['Churn'] == 'Yes']['MonthlyCharges'].sum()

print("\n" + "=" * 40)
print("             KEY METRICS")
print("=" * 40)
print(f"Total Customers:          {total_cust:,}")
print(f"Churned Customers:        {churned_cust:,}")
print(f"Overall Churn Rate:       {churn_rate:.2f}%")
print(f"Monthly Revenue Lost:     ${mrr_lost:,.2f}")

# 5. Churn Drivers Analysis
print("\n" + "=" * 40)
print("       CHURN BY CONTRACT TYPE")
print("=" * 40)
contract_summary = df.groupby('Contract')['Churn_Flag'].agg(['count', 'mean']).reset_index()
contract_summary['Churn_Rate_%'] = (contract_summary['mean'] * 100).round(2)
contract_summary.rename(columns={'count': 'Customer_Count'}, inplace=True)
print(contract_summary[['Contract', 'Customer_Count', 'Churn_Rate_%']])

print("\n" + "=" * 40)
print("       CHURN BY TENURE COHORT")
print("=" * 40)
cohort_summary = df.groupby('Tenure_Cohort', observed=False)['Churn_Flag'].agg(['count', 'mean']).reset_index()
cohort_summary['Churn_Rate_%'] = (cohort_summary['mean'] * 100).round(2)
cohort_summary.rename(columns={'count': 'Customer_Count'}, inplace=True)
print(cohort_summary[['Tenure_Cohort', 'Customer_Count', 'Churn_Rate_%']])

print("\n" + "=" * 40)
print("    CHURN BY INTERNET SERVICE TYPE")
print("=" * 40)
internet_summary = df.groupby('InternetService')['Churn_Flag'].agg(['count', 'mean']).reset_index()
internet_summary['Churn_Rate_%'] = (internet_summary['mean'] * 100).round(2)
internet_summary.rename(columns={'count': 'Customer_Count'}, inplace=True)
print(internet_summary[['InternetService', 'Customer_Count', 'Churn_Rate_%']])

# 6. Export Cleaned Dataset for Dashboard / Reporting
output_filename = 'Cleaned_Telco_Churn.csv'
df.to_csv(output_filename, index=False)
print(f"\nSaved processed data to '{output_filename}' successfully.")