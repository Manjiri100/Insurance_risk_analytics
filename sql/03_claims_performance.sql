SELECT claim_type,claim_status,COUNT(*) claims,SUM(claim_amount) claimed,SUM(approved_amount) approved,AVG(CASE WHEN claim_amount>0 THEN approved_amount/claim_amount END) approval_ratio FROM claims GROUP BY claim_type,claim_status;
SELECT geography,COUNT(*) claims,SUM(claim_amount) claimed,SUM(approved_amount) approved FROM claims GROUP BY geography ORDER BY claimed DESC;
SELECT severity,COUNT(*) claims,AVG(claim_amount) avg_claim,SUM(claim_amount) total_claim FROM claims GROUP BY severity;
