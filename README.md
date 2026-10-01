# DutchBank Data Warehouse

## Project Overview

DutchBank Data Warehouse is a portfolio data engineering project built using PostgreSQL and SQL.

The project simulates a banking data environment containing customers, branches, merchants, accounts, currencies, and financial transactions.

The goal of the project is to demonstrate practical data engineering skills, including:

- Relational database design
- SQL data loading
- Table relationships and foreign keys
- Data validation
- SQL joins
- Aggregations and transformations
- Analytical views
- Data quality considerations
- Reproducible database workflows

## Technologies

- PostgreSQL
- pgAdmin 4
- SQL
- CSV
- Git / GitHub

## Database Structure

The database contains six related tables:

| Table | Description |
|---|---|
| `customers` | Customer information |
| `branches` | Bank branch information |
| `merchants` | Merchant information and categories |
| `currencies` | Supported currencies |
| `accounts` | Customer bank accounts and account status |
| `transactions` | Financial transactions linked to accounts and, where applicable, merchants |

### Relationships

The main relationships between the tables are:

- One customer can have multiple accounts.
- Each account belongs to one customer.
- Each account belongs to one branch.
- Each account can have multiple transactions.
- A transaction can optionally be linked to a merchant.
- Transactions reference a currency through `currency_code`.

## Data Pipeline

The project follows a simple data pipeline:

1. Raw banking data is provided as CSV files.
2. CSV data is loaded into PostgreSQL tables.
3. Relationships between the tables are defined using primary and foreign keys.
4. SQL is used to validate and transform the data.
5. Analytical views are created to make the data easier to analyse.

### Analytical Views

The project currently includes four SQL views:

| View | Purpose |
|---|---|
| `customer_transaction_summary` | Summarises transactions and spending by customer |
| `merchant_transaction_summary` | Summarises completed purchases by merchant |
| `account_transaction_summary` | Summarises transactions by bank account |
| `transaction_detail` | Combines transaction, account, customer and merchant information into a detailed analytical dataset |

## Data Validation

The loaded data was validated using SQL queries to check:

- Row counts for each table
- Relationships between customers, accounts and transactions
- Transaction types and statuses
- Transactions with and without associated merchants
- Aggregated transaction amounts
- Customers and accounts with no transactions

The final dataset contains:

| Table | Rows |
|---|---:|
| `customers` | 10 |
| `branches` | 5 |
| `merchants` | 15 |
| `currencies` | 4 |
| `accounts` | 15 |
| `transactions` | 50 |

The validation process also confirmed that transactions without a merchant are valid for transaction types such as deposits, transfers, withdrawals and direct debits, while purchases are associated with merchants.