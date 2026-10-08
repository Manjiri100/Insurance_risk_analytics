SELECT policy_id,MAX(risk_score) risk_score,MAX(risk_band) risk_band FROM stg_risk_assessments GROUP BY policy_id;
