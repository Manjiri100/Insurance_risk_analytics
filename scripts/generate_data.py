import argparse, csv, random
from datetime import date, timedelta, datetime
from pathlib import Path

SEED = 42
random.seed(SEED)
OUT = Path('data/generated')
TARGETS = {
    'customers': 1_000_000,
    'policies': 2_000_000,
    'policy_transactions': 5_000_000,
    'claims': 3_000_000,
    'claim_events': 5_000_000,
    'payments': 4_000_000,
    'vehicles_assets': 1_500_000,
    'brokers': 20_000,
    'risk_assessments': 2_000_000,
}

def rand_date():
    return date(2025,1,1) + timedelta(days=random.randint(0,729))

def write_table(path, header, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(header)
        for row in rows: w.writerow(row)

def generate(scale):
    n = {k: max(1, int(v*scale)) for k,v in TARGETS.items()}
    OUT.mkdir(parents=True, exist_ok=True)
    specs = [
      ('customers',['customer_id','customer_type','date_of_birth','geography','customer_since','customer_status','income_band'],lambda i:[f'C{i:07d}',random.choice(['Individual','SME','Corporate']),str(date(1960,1,1)+timedelta(days=random.randint(0,18000))),random.choice(['North','South','East','West','Central']),str(rand_date()),random.choice(['Active','Active','Active','Lapsed']),random.choice(['Low','Middle','High'])]),
      ('brokers',['broker_id','broker_name','broker_region','broker_type','broker_status'],lambda i:[f'B{i:05d}',f'Broker {i:05d}',random.choice(['North','South','East','West','Central']),random.choice(['Independent','Corporate']),random.choice(['Active','Active','Active','Inactive'])]),
      ('vehicles_assets',['asset_id','customer_id','asset_type','asset_value','asset_age_years','usage_type','risk_category'],lambda i:[f'A{i:07d}',f'C{random.randint(1,n["customers"]):07d}',random.choice(['Vehicle','Property','Equipment']),round(random.uniform(5000,500000),2),random.randint(0,20),random.choice(['Personal','Commercial','Business']),random.choice(['Low','Medium','High'])]),
      ('policies',['policy_id','customer_id','broker_id','asset_id','policy_type','policy_start_date','policy_end_date','premium_amount','sum_insured','deductible','risk_band','geography','policy_status'],lambda i:[f'P{i:07d}',f'C{random.randint(1,n["customers"]):07d}',f'B{random.randint(1,n["brokers"]):05d}',f'A{random.randint(1,n["vehicles_assets"]):07d}',random.choice(['Motor','Property','Commercial','Travel','Liability']),str(rand_date()),str(rand_date()),round(random.uniform(300,15000),2),round(random.uniform(10000,1000000),2),random.choice([250,500,1000,2500]),random.choice(['Low','Medium','High','Critical']),random.choice(['North','South','East','West','Central']),random.choice(['Active','Active','Renewed','Lapsed','Cancelled'])]),
      ('policy_transactions',['transaction_id','policy_id','transaction_date','transaction_type','transaction_amount','payment_status'],lambda i:[f'T{i:08d}',f'P{random.randint(1,n["policies"]):07d}',str(rand_date()),random.choice(['New Business','Renewal Payment','Adjustment','Refund','Cancellation']),round(random.uniform(-500,15000),2),random.choice(['Paid','Paid','Pending','Failed'])]),
      ('claims',['claim_id','policy_id','customer_id','claim_date','incident_date','claim_type','claim_status','claim_amount','approved_amount','sum_insured','fraud_flag','severity','geography'],lambda i:[f'CL{i:08d}',f'P{random.randint(1,n["policies"]):07d}',f'C{random.randint(1,n["customers"]):07d}',str(rand_date()),str(rand_date()),random.choice(['Accident','Theft','Property Damage','Liability','Travel']),random.choice(['Open','Under Investigation','Approved','Settled','Closed']),round(random.uniform(200,200000),2),round(random.uniform(0,180000),2),round(random.uniform(10000,1000000),2),random.choice([0,0,0,0,1]),random.choice(['Low','Medium','High','Critical']),random.choice(['North','South','East','West','Central'])]),
      ('claim_events',['claim_event_id','claim_id','event_timestamp','event_type','event_status','handler_id','notes_code'],lambda i:[f'CE{i:08d}',f'CL{random.randint(1,n["claims"]):08d}',datetime(2025,1,1,8,0,0).isoformat(),random.choice(['FNOL','Assessment','Investigation','Fraud Review','Settlement','Closure']),random.choice(['Open','Completed','Pending']),f'H{random.randint(1,10000):05d}',random.choice(['FNOL_STD','ASSESS_STD','FRAUD_HIGH','SETTLE_STD'])]),
      ('payments',['payment_id','claim_id','payment_date','payment_type','payment_amount','payment_status','payment_reference'],lambda i:[f'PAY{i:08d}',f'CL{random.randint(1,n["claims"]):08d}',str(rand_date()),random.choice(['Settlement','Interim','Investigation Expense','Refund']),round(random.uniform(50,100000),2),random.choice(['Completed','Completed','Pending','Rejected']),f'REF{i:08d}']),
      ('risk_assessments',['risk_assessment_id','policy_id','assessment_date','risk_score','risk_band','assessment_source','model_version'],lambda i:[f'RA{i:08d}',f'P{random.randint(1,n["policies"]):07d}',str(rand_date()),random.randint(1,100),random.choice(['Low','Medium','High','Critical']),random.choice(['Underwriting','Renewal','Model','Manual Review']),random.choice(['v3.0','v3.1','v4.0'])]),
    ]
    for name, header, make in specs:
        write_table(OUT/f'{name}.csv', header, (make(i) for i in range(1,n[name]+1)))
    print('Generated rows:', sum(n.values()))

if __name__ == '__main__':
    p=argparse.ArgumentParser(); p.add_argument('--scale-factor',type=float,default=0.01)
    generate(p.parse_args().scale_factor)
