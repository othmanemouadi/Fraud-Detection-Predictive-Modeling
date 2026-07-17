"""
Data preprocessing pipeline for fraud detection.

This module loads raw transaction data, performs basic cleaning,
creates derived features, and prepares the dataset for machine
learning model training and evaluation.
"""

from pathlib import Path
import pandas as pd


def load_raw_data(path: str) -> pd.DataFrame:
    """
    Load raw transaction data from a CSV file.
    """
    return pd.read_csv(path)


def preprocess_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess transaction data.
    """

    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(0)

    # Ensure numeric columns are properly formatted
    if "Amount" in df.columns:
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)

        # Log-transform transaction amounts
        df["LogAmount"] = df["Amount"].apply(lambda x: 0 if x <= 0 else pd.np.log1p(x))

    # Convert fraud labels to integers
    if "Class" in df.columns:
        df["Class"] = df["Class"].astype(int)

    return df


def save_processed_data(df: pd.DataFrame, output_path: str):
    """
    Save the processed dataset.
    """

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def main():

    raw_path = "data/raw/creditcard.csv"
    processed_path = "data/processed/creditcard_processed.csv"

    df_raw = load_raw_data(raw_path)

    df_processed = preprocess_transactions(df_raw)

    save_processed_data(df_processed, processed_path)

    print(f"Processed dataset saved to: {processed_path}")


if __name__ == "__main__":
    main()
