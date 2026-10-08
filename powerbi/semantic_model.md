# Power BI Semantic Model

## Core analytical facts
- mart_policy_portfolio
- mart_claims_performance
- mart_loss_ratio
- mart_customer_retention
- mart_claim_investigation
- mart_portfolio_risk
- mart_data_trust

## Dimensions
Customer, Policy, Broker, Asset, Geography, Date, Risk Band and Claim Type.

## Modelling principle
Keep policy, claim and event grains distinct. Aggregate event/payment data before joining to executive facts to avoid fan-out and double counting.
