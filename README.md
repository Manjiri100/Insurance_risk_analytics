Insurance Data & Risk Analytics

## Executive Summary
An enterprise-style insurance analytics platform covering customers, policies, premium transactions, claims, claim events, payments, risk assessments, brokers and insured assets.

The project follows a realistic analyst workflow:

**Business problem → data profiling → data-quality investigation → SQL → dbt transformation → analytical marts → Power BI semantic model → fraud/risk/root-cause analysis → executive recommendations.**

## Business Problem
Insurance leadership needs a trusted view of portfolio performance, claims exposure, customer retention, risk concentration and investigation priorities. The challenge is to reconcile multiple operational domains, identify unreliable records and turn claims/risk signals into defensible decision support.

## Production-Scale Dataset
The generator is designed for **20M+ records**:

| Table | Target rows |
|---|---:|
| customers | 1,000,000 |
| policies | 2,000,000 |
| policy_transactions | 5,000,000 |
| claims | 3,000,000 |
| claim_events | 5,000,000 |
| payments | 4,000,000 |
| vehicles_assets | 1,500,000 |
| brokers | 20,000 |
| risk_assessments | 2,000,000 |
| **Total** | **20M+** |

Full production-scale CSVs are generated locally and are intentionally not committed to the portfolio repository. Representative samples and the deterministic generator are included.

## Core Questions
- Which policy segments drive premium and loss ratio?
- Where are claims concentrated by product, geography, broker and risk band?
- Which customers show retention/lapse risk?
- Which claim and payment patterns warrant investigation?
- Which brokers or segments show unusual loss or cancellation patterns?
- Where are high/critical risks concentrated?
- Which data-quality defects could materially affect reporting?

## Deliberate Data-Quality Problems
The synthetic data includes realistic duplicate records, orphan relationships, invalid dates, negative financial values, claims exceeding sum insured, payment anomalies, missing risk assessments and inconsistent risk attributes.

These defects are measured in a dedicated **Data Trust** layer rather than silently removed.

## Technology
**Python | SQL | dbt | Power BI | GitHub Actions | optional LLM-assisted case summaries**

LLM assistance is limited to summarising already-calculated evidence. It does not make final underwriting, fraud, pricing or risk decisions.

## Power BI Pages
1. Insurance Executive
2. Portfolio Profitability
3. Claims Intelligence
4. Customer & Retention
5. Risk Concentration
6. Claims Investigation
7. Data Trust

## Reproducibility
```bash
python scripts/generate_data.py --scale-factor 0.01
python scripts/generate_data.py --scale-factor 1.0
```

## Data Disclaimer
All data is synthetic and created solely for portfolio demonstration. No real insurer, customer, policy or claim data is used.

<img width="1024" height="572" alt="image" src="https://github.com/user-attachments/assets/a9c90d82-e843-4107-9db1-bd3b9a2e5d8d" />
