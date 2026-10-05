-- Load raw CSV data into PostgreSQL tables

\copy customers
FROM 'data/raw/customers.csv'
WITH (FORMAT csv, HEADER true);

\copy branches
FROM 'data/raw/branches.csv'
WITH (FORMAT csv, HEADER true);

\copy merchants
FROM 'data/raw/merchants.csv'
WITH (FORMAT csv, HEADER true);

\copy currencies
FROM 'data/raw/currencies.csv'
WITH (FORMAT csv, HEADER true);

\copy accounts
FROM 'data/raw/accounts.csv'
WITH (FORMAT csv, HEADER true);

\copy transactions
FROM 'data/raw/transactions.csv'
WITH (FORMAT csv, HEADER true);