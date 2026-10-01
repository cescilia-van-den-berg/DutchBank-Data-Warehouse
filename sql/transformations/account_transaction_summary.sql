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