-- Transaction Summary
SELECT
    COUNT(*) AS total_transactions,
    SUM(class) AS fraudulent_transactions,
    COUNT(*) - SUM(class) AS legitimate_transactions,
    ROUND((SUM(class) * 100.0) / COUNT(*), 2) AS fraud_percentage
FROM credit_card_transactions;


-- Fraud vs Legitimate Transaction Amounts
SELECT
    class,
    COUNT(*) AS transaction_count,
    AVG(amount) AS average_amount,
    MIN(amount) AS minimum_amount,
    MAX(amount) AS maximum_amount
FROM credit_card_transactions
GROUP BY class
ORDER BY class;


-- Daily Transaction Activity
SELECT
    toDate(transaction_time) AS transaction_date,
    COUNT(*) AS total_transactions,
    SUM(class) AS fraud_transactions,
    AVG(amount) AS average_transaction_amount
FROM credit_card_transactions
GROUP BY transaction_date
ORDER BY transaction_date;


-- Top 20 Largest Fraudulent Transactions
SELECT
    transaction_id,
    transaction_time,
    amount
FROM credit_card_transactions
WHERE class = 1
ORDER BY amount DESC
LIMIT 20;


-- Fraud Rate by Hour of Day
SELECT
    toHour(transaction_time) AS transaction_hour,
    COUNT(*) AS total_transactions,
    SUM(class) AS fraud_transactions,
    ROUND((SUM(class) * 100.0) / COUNT(*), 2) AS fraud_rate_percent
FROM credit_card_transactions
GROUP BY transaction_hour
ORDER BY transaction_hour;
