import pandas as pd


def compute_class_distribution(df):
    """
    Compute the distribution of legitimate and fraudulent transactions.
    """

    summary = (
        df.groupby("Class")
        .agg(
            total_transactions=("Class", "count"),
            average_amount=("Amount", "mean"),
            maximum_amount=("Amount", "max"),
            minimum_amount=("Amount", "min"),
        )
        .reset_index()
    )

    summary["Class"] = summary["Class"].map(
        {0: "Legitimate", 1: "Fraud"}
    )

    return summary


def compute_daily_transaction_trend(df):
    """
    Compute daily transaction statistics.
    """

    df = df.copy()

    df["Date"] = pd.to_datetime(df["Time"], unit="s").dt.date

    daily = (
        df.groupby("Date")
        .agg(
            total_transactions=("Class", "count"),
            fraud_transactions=("Class", "sum"),
            average_amount=("Amount", "mean"),
        )
        .reset_index()
    )

    daily["fraud_rate"] = (
        daily["fraud_transactions"]
        / daily["total_transactions"]
    )

    return daily
