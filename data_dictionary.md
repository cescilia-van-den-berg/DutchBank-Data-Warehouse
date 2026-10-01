# DutchBank Data Dictionary

## Customers

| Field | Description |
|---|---|
| customer_id | Unique identifier for the customer |
| first_name | Customer's first name |
| last_name | Customer's last name |
| date_of_birth | Customer's date of birth |
| city | Customer's city |
| postcode | Customer's Dutch postcode |
| customer_since | Date the customer joined the bank |
| customer_status | Current status of the customer |

## Branches

| Field | Description |
|---|---|
| branch_id | Unique identifier for the branch |
| branch_name | Name of the branch |
| city | City where the branch is located |
| postcode | Branch postcode |
| opening_date | Date the branch opened |
| branch_status | Current status of the branch |

## Merchants

| Field | Description |
|---|---|
| merchant_id | Unique identifier for the merchant |
| merchant_name | Name of the merchant |
| merchant_category | Category of the merchant |
| city | City where the merchant is located |

## Currencies

| Field | Description |
|---|---|
| currency_code | Three-letter currency code |
| currency_name | Name of the currency |

## Accounts

| Field | Description |
|---|---|
| account_id | Unique identifier for the account |
| customer_id | Customer who owns the account |
| branch_id | Branch associated with the account |
| account_type | Type of bank account |
| open_date | Date the account was opened |
| close_date | Date the account was closed |
| account_status | Current status of the account |

## Transactions

| Field | Description |
|---|---|
| transaction_id | Unique identifier for the transaction |
| account_id | Account associated with the transaction |
| merchant_id | Merchant associated with the transaction, when applicable |
| transaction_date | Date and time of the transaction |
| transaction_type | Type of transaction |
| amount | Transaction amount |
| currency_code | Currency used for the transaction |
| status | Status of the transaction |

---

# DutchBank Data Rules

## Customer Rules

### customer_status
Allowed values:
- Active
- Inactive
- Closed

### Customer relationships
- Each customer must have a unique customer_id.
- A customer can have one or more accounts.
- A customer can have multiple accounts at different branches.

---

## Branch Rules

### branch_status
Allowed values:
- Open
- Closed

### Branch relationships
- Each branch must have a unique branch_id.
- A branch can have many accounts.

---

## Merchant Rules

### merchant_category
Allowed values:
- Supermarket
- Restaurant
- Fuel
- Clothing
- Electronics
- Travel
- Healthcare
- Entertainment
- Online Shopping
- Public Transport

### Merchant relationships
- Each merchant must have a unique merchant_id.
- A merchant can appear in many transactions.

---

## Currency Rules

Supported currencies:
- EUR - Euro
- USD - US Dollar
- GBP - British Pound
- CHF - Swiss Franc

Rules:
- currency_code must contain exactly 3 characters.
- Each currency_code must be unique.

---

## Account Rules

### account_type
Allowed values:
- Checking
- Savings

### account_status
Allowed values:
- Active
- Closed

### Account relationships
- Each account must belong to exactly one customer.
- Each account must be associated with exactly one branch.
- A customer can have multiple accounts.

### Date rules
- open_date cannot be after close_date.
- close_date can be empty for active accounts.
- An account marked Closed should have a close_date.
- An account marked Active should normally have no close_date.

---

## Transaction Rules

### transaction_type
Allowed values:
- Purchase
- Withdrawal
- Deposit
- Transfer
- Direct Debit

### transaction_status
Allowed values:
- Completed
- Pending
- Failed

### Transaction relationships
- Each transaction must belong to exactly one account.
- A transaction can have a merchant.
- A merchant is not required for every transaction.
- Each transaction must have a valid currency_code.

### Transaction rules
- amount must contain a numeric value.
- amount must have a maximum of 2 decimal places.
- transaction_date cannot be before the account open_date.