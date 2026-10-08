SELECT policy_type,geography,risk_band,COUNT(*) policies,SUM(premium_amount) premium,AVG(premium_amount) avg_premium FROM policies GROUP BY policy_type,geography,risk_band;
SELECT broker_id,COUNT(*) policies,SUM(premium_amount) premium,AVG(CASE WHEN policy_status='Lapsed' THEN 1.0 ELSE 0 END) lapse_rate FROM policies GROUP BY broker_id ORDER BY premium DESC;
SELECT policy_status,COUNT(*) policies,SUM(premium_amount) premium FROM policies GROUP BY policy_status;
