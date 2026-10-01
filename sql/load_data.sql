-- Load raw CSV data into PostgreSQL tables

\copy customers
FROM 'D:/Data Engineering Projects/DutchBank-Data-Warehouse/data/raw/customers.csv'
WITH (FORMAT csv, HEADER true);

\copy branches
FROM 'D:/Data Engineering Projects/DutchBank-Data-Warehouse/data/raw/branches.csv'
WITH (FORMAT csv, HEADER true);

\copy merchants
FROM 'D:/Data Engineering Projects/DutchBank-Data-Warehouse/data/raw/merchants.csv'
WITH (FORMAT csv, HEADER true);

\copy currencies
FROM 'D:/Data Engineering Projects/DutchBank-Data-Warehouse/data/raw/currencies.csv'
WITH (FORMAT csv, HEADER true);

\copy accounts
FROM 'D:/Data Engineering Projects/DutchBank-Data-Warehouse/data/raw/accounts.csv'
WITH (FORMAT csv, HEADER true);

\copy transactions
FROM 'D:/Data Engineering Projects/DutchBank-Data-Warehouse/data/raw/transactions.csv'
WITH (FORMAT csv, HEADER true);