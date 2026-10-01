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