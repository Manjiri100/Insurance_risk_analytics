# Data Quality Strategy

### Completeness
Mandatory customer, policy, claim, payment and risk fields.

### Validity
Financial values, dates, status values and risk bands.

### Referential Integrity
Customer → policy → claim → payment and assessment → policy relationships.

### Uniqueness
Business keys and event identifiers.

### Reconciliation
Claim amount, approved amount, payments and sum insured.

### Transparency
Issue counts and affected records are retained in the Data Trust layer rather than silently deleted.
