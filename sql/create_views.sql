-- Create analytical views for the DutchBank data warehouse

CREATE OR REPLACE VIEW customer_transaction_summary AS
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(t.transaction_id) AS transaction_count,
    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Deposit'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_deposits,
    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Purchase'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_purchases,
    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Withdrawal'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_withdrawals
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id = a.customer_id
LEFT JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY c.customer_id;

CREATE OR REPLACE VIEW merchant_transaction_summary AS
SELECT
    m.merchant_id,
    m.merchant_name,
    m.merchant_category,
    m.city,
    COUNT(t.transaction_id) AS purchase_count,
    COALESCE(SUM(t.amount), 0) AS total_purchase_amount,
    COALESCE(AVG(t.amount), 0) AS average_purchase_amount
FROM merchants m
LEFT JOIN transactions t
    ON m.merchant_id = t.merchant_id
    AND t.transaction_type = 'Purchase'
    AND t.status = 'Completed'
GROUP BY
    m.merchant_id,
    m.merchant_name,
    m.merchant_category,
    m.city
ORDER BY total_purchase_amount DESC;

CREATE OR REPLACE VIEW account_transaction_summary AS
SELECT
    a.account_id,
    a.customer_id,
    a.account_type,
    a.account_status,
    COUNT(t.transaction_id) AS transaction_count,

    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Deposit'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_deposits,

    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Purchase'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_purchases,

    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Withdrawal'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_withdrawals,

    COALESCE(SUM(
        CASE
            WHEN t.transaction_type = 'Transfer'
                 AND t.status = 'Completed'
            THEN t.amount
            ELSE 0
        END
    ), 0) AS total_transfers

FROM accounts a
LEFT JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY
    a.account_id,
    a.customer_id,
    a.account_type,
    a.account_status
ORDER BY a.account_id;

CREATE OR REPLACE VIEW transaction_detail AS
SELECT
    t.transaction_id,
    t.transaction_date,
    t.transaction_type,
    t.amount,
    t.currency_code,
    t.status,
    a.account_id,
    a.account_type,
    a.account_status,
    c.customer_id,
    c.first_name,
    c.last_name,
    m.merchant_id,
    m.merchant_name,
    m.merchant_category
FROM transactions t
JOIN accounts a
    ON t.account_id = a.account_id
JOIN customers c
    ON a.customer_id = c.customer_id
LEFT JOIN merchants m
    ON t.merchant_id = m.merchant_id
ORDER BY t.transaction_date;