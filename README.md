# Customer Retention & Churn Analysis

## Overview
This project analyzes customer churn patterns, key retention drivers, and customer lifetime trends for a subscription-based business to reduce customer attrition and optimize revenue retention.

## Project Deliverables
- **Data Preprocessing & Metrics Script**: `analysis.py`
- **Visualization Script**: `visualize.py`
- **Cleaned Dataset**: `Cleaned_Telco_Churn.csv`
- **Dashboard / Charts**: `churn_analysis_dashboard.png`
- **Final Business Report**: `Customer_Retention_Report.pdf`

## Key Metrics
- **Total Customers Analyzed**: 7,032
- **Overall Churn Rate**: 26.58%
- **Monthly Recurring Revenue (MRR) Lost**: ~$139,130

## Key Findings & Churn Drivers
1. **Contract Vulnerability**: Month-to-month contracts experience the highest churn rate (~42%), whereas 1-year (~11%) and 2-year (~3%) contracts maintain significantly higher retention.
2. **Early Tenure Drop-off**: Highest customer attrition occurs during the initial 0–12 months of onboarding.
3. **Service Support Dependency**: Customers without dedicated Tech Support exhibit churn rates exceeding 40%.
4. **Pricing Sensitivity**: Churn concentration is elevated among users paying $70–$100/month without bundled value-added services.

## Strategic Recommendations
- **Incentivize Annual Contracts**: Transition month-to-month subscribers to annual plans using 15% discounts or loyalty perks.
- **90-Day Onboarding Program**: Provide structured proactive check-ins and customer success support during the initial 3 months.
- **Value-Added Bundles**: Offer complimentary 3-month trials of Tech Support and Online Security for high-risk basic tiers.

## Tech Stack
- **Language**: Python (pandas, numpy, matplotlib, seaborn)
- **Environment**: Visual Studio Code