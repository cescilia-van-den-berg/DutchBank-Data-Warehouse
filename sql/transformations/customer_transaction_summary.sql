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