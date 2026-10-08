# Core Measures

- Gross Premium = SUM(mart_policy_portfolio[premium_amount])
- Approved Claims = SUM(mart_policy_portfolio[approved_amount])
- Loss Ratio = DIVIDE([Approved Claims],[Gross Premium])
- Claim Count = COUNTROWS(mart_claims_performance)
- Fraud Signals = SUM(mart_claims_performance[fraud_flag])
- Average Risk Score = AVERAGE(mart_portfolio_risk[risk_score])
- Lapsed Policy Rate = AVERAGE(mart_customer_retention[lapse_rate])
- Total Paid = SUM(mart_claims_performance[total_paid])
- Payment Leakage = [Total Paid] - [Approved Claims]
