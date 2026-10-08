SELECT * FROM int_claim_payments WHERE fraud_flag=1 OR claim_amount>approved_amount OR claim_amount>0;
