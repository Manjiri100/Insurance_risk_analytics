SELECT customer_status,COUNT(*) customers FROM customers GROUP BY customer_status;
SELECT customer_id,COUNT(*) policy_count,SUM(premium_amount) premium,SUM(CASE WHEN policy_status='Lapsed' THEN 1 ELSE 0 END) lapsed_policies FROM policies GROUP BY customer_id;
SELECT geography,COUNT(*) customers,AVG(CASE WHEN customer_status='Lapsed' THEN 1.0 ELSE 0 END) lapse_rate FROM customers GROUP BY geography;
