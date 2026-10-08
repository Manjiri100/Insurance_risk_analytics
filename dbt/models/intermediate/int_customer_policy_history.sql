SELECT customer_id,COUNT(*) policy_count,SUM(premium_amount) premium,AVG(CASE WHEN policy_status='Lapsed' THEN 1.0 ELSE 0 END) lapse_rate FROM stg_policies GROUP BY customer_id;
