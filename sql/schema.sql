-- ClickHouse schema for credit card fraud detection transactions

CREATE TABLE IF NOT EXISTS credit_card_transactions
(
    transaction_id UUID,

    transaction_time DateTime,

    amount Float64,

    class UInt8,

    v1 Float64,
    v2 Float64,
    v3 Float64,
    v4 Float64,
    v5 Float64,
    v6 Float64,
    v7 Float64,
    v8 Float64,
    v9 Float64,
    v10 Float64,
    v11 Float64,
    v12 Float64,
    v13 Float64,
    v14 Float64,
    v15 Float64,
    v16 Float64,
    v17 Float64,
    v18 Float64,
    v19 Float64,
    v20 Float64,
    v21 Float64,
    v22 Float64,
    v23 Float64,
    v24 Float64,
    v25 Float64,
    v26 Float64,
    v27 Float64,
    v28 Float64,

    ingestion_time DateTime DEFAULT now()
)
ENGINE = MergeTree
PARTITION BY toDate(transaction_time)
ORDER BY (transaction_time, transaction_id);
