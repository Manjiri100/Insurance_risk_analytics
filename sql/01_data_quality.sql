-- Data-quality investigation: duplicates, orphan records, invalid values and reconciliation.
SELECT policy_id, COUNT(*) duplicate_count FROM policies GROUP BY policy_id HAVING COUNT(*) > 1;
SELECT claim_id, COUNT(*) duplicate_count FROM claims GROUP BY claim_id HAVING COUNT(*) > 1;
SELECT payment_id, COUNT(*) duplicate_count FROM payments GROUP BY payment_id HAVING COUNT(*) > 1;
SELECT p.policy_id FROM policies p LEFT JOIN customers c ON p.customer_id=c.customer_id WHERE c.customer_id IS NULL;
SELECT c.claim_id FROM claims c LEFT JOIN policies p ON c.policy_id=p.policy_id WHERE p.policy_id IS NULL;
SELECT pay.payment_id FROM payments pay LEFT JOIN claims c ON pay.claim_id=c.claim_id WHERE c.claim_id IS NULL;
SELECT policy_id FROM policies WHERE premium_amount < 0 OR sum_insured <= 0 OR deductible < 0;
SELECT claim_id FROM claims WHERE claim_amount < 0 OR approved_amount < 0 OR claim_amount > sum_insured;
SELECT claim_id FROM claims WHERE approved_amount > claim_amount OR approved_amount > sum_insured;
SELECT policy_id FROM policies WHERE policy_end_date < policy_start_date;
SELECT claim_id FROM claims WHERE incident_date > claim_date;
SELECT claim_id, SUM(payment_amount) total_paid FROM payments GROUP BY claim_id HAVING SUM(payment_amount) < 0;
SELECT p.policy_id,p.sum_insured,COALESCE(c.total_claimed,0) total_claimed FROM policies p LEFT JOIN (SELECT policy_id,SUM(claim_amount) total_claimed FROM claims GROUP BY policy_id) c ON p.policy_id=c.policy_id WHERE COALESCE(c.total_claimed,0)>p.sum_insured;
