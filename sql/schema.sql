DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS merchants;
DROP TABLE IF EXISTS currencies;
DROP TABLE IF EXISTS branches;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers(
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    city VARCHAR(50) NOT NULL,
    postcode VARCHAR(10) NOT NULL,
    customer_since DATE NOT NULL,
    customer_status VARCHAR(20) NOT NULL
    );

CREATE TABLE branches(
    branch_id INTEGER PRIMARY KEY,
    branch_name VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    postcode VARCHAR(10) NOT NULL,
    opening_date DATE NOT NULL,
    branch_status VARCHAR(20) NOT NULL
);

CREATE TABLE merchants(
    merchant_id INTEGER PRIMARY KEY,
    merchant_name VARCHAR(100) NOT NULL,
    merchant_category VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL
);

CREATE TABLE currencies(
    currency_code CHAR(3) PRIMARY KEY,
    currency_name VARCHAR(50) NOT NULL
);

CREATE TABLE accounts(
    account_id VARCHAR(20) PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(customer_id),
    branch_id INTEGER NOT NULL REFERENCES branches(branch_id),
    account_type VARCHAR(20) NOT NULL,
    open_date DATE NOT NULL,
    close_date DATE,
    account_status VARCHAR(20) NOT NULL
);

CREATE TABLE transactions(
    transaction_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20) NOT NULL REFERENCES accounts(account_id),
    merchant_id INTEGER REFERENCES merchants(merchant_id),
    transaction_date TIMESTAMP NOT NULL,
    transaction_type VARCHAR(30) NOT NULL,
    amount DECIMAL(12,2) NOT NULL,
    currency_code CHAR(3) NOT NULL REFERENCES currencies(currency_code),
    status VARCHAR(20) NOT NULL
);