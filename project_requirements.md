# DutchBank Data Warehouse

## Project Overview

A fictional Dutch retail bank receives data from multiple operational systems. The bank needs a centralized data warehouse to support reliable reporting on customers, accounts, transactions, merchants and branches.

## Business Questions

### Customers

1. How many customers does the bank have?
2. How many new customers joined each month?
3. How many customers are active?
4. Which cities have the most customers?

### Accounts

5. How many accounts does the bank have?
6. How many accounts are checking vs savings?
7. How many accounts were opened each month?
8. How many accounts are closed?
9. Which branches have the most accounts?

### Transactions

10. How many transactions occur each day/month?
11. What is the total value of transactions?
12. How much money is deposited vs withdrawn?
13. What percentage of transactions fail?
14. What are the most common transaction types?
15. Which merchants process the most payments?
16. Which months have the highest transaction volume?

### Customers and Transactions

17. Which customers have the highest transaction volume?
18. Which customers haven't made a transaction in 90 days?
19. What is the average transaction amount?
20. How does transaction activity differ by customer?

### Branches

21. Which branches have the most customers?
22. Which branches have the most accounts?
23. Which branches have the highest transaction volume?

## Initial Datasets

- customers.csv
- accounts.csv
- transactions.csv
- merchants.csv
- branches.csv
- currencies.csv

## Technologies

- SQL
- PostgreSQL
- Git
- GitHub

## Future Technologies

- Python
- Pandas
- Power BI
- Azure

## Database Schema

### Customers

| Column | Data Type | Key |
|---|---|---|
| customer_id | INTEGER | PK |
| first_name | VARCHAR(50) | |
| last_name | VARCHAR(50) | |
| date_of_birth | DATE | |
| city | VARCHAR(50) | |
| postcode | VARCHAR(10) | |
| customer_since | DATE | |
| customer_status | VARCHAR(20) | |

### Accounts

| Column | Data Type | Key |
|---|---|---|
| account_id | VARCHAR(20) | PK |
| customer_id | INTEGER | FK |
| branch_id | INTEGER | FK |
| account_type | VARCHAR(20) | |
| open_date | DATE | |
| close_date | DATE | |
| account_status | VARCHAR(20) | |

### Transactions

| Column | Data Type | Key |
|---|---|---|
| transaction_id | VARCHAR(20) | PK |
| account_id | VARCHAR(20) | FK |
| merchant_id | INTEGER | FK |
| transaction_date | TIMESTAMP | |
| transaction_type | VARCHAR(30) | |
| amount | DECIMAL(12,2) | |
| currency_code | CHAR(3) | FK |
| status | VARCHAR(20) | |

### Merchants

| Column | Data Type | Key |
|---|---|---|
| merchant_id | INTEGER | PK |
| merchant_name | VARCHAR(100) | |
| merchant_category | VARCHAR(50) | |
| city | VARCHAR(50) | |

### Branches

| Column | Data Type | Key |
|---|---|---|
| branch_id | INTEGER | PK |
| branch_name | VARCHAR(100) |  |
| city | VARCHAR(50) | |

### Currencies

| Column | Data Type | Key |
|---|---|---|
| currency_code | CHAR(3) | PK |
| currency_name | VARCHAR(50) | |