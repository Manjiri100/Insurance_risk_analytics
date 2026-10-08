SELECT 'policies' entity,COUNT(*) row_count,SUM(CASE WHEN premium_amount<0 OR sum_insured<=0 THEN 1 ELSE 0 END) critical_issues FROM stg_policies;
