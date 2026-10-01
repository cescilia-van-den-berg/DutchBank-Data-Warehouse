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