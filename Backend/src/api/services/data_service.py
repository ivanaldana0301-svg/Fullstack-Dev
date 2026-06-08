import pandas as pd
from src.api.core.config import DATA_PATH, CSV_PATH

from src.pipeline.extract import extract_api_data, extract_csv_data
from src.pipeline.transform import transform_data
from src.pipeline.load import save_to_parquet
from src.pipeline.quality import validate_data


def run_pipeline():
    df_api = extract_api_data()
    df_csv = extract_csv_data(CSV_PATH)

    df_final = transform_data(df_api, df_csv)

    validate_data(df_final)

    save_to_parquet(df_final, DATA_PATH)

    return df_final


def load_data():
    if not DATA_PATH.exists():
        run_pipeline()

    return pd.read_parquet(DATA_PATH)


def get_transactions():
    df = load_data()
    return df.to_dict(orient="records")


def get_metrics():
    df = load_data()

    return {
        "total_transactions": int(len(df)),
        "total_value": float(df["transaction_value_usd"].sum()),
        "avg_value": float(df["transaction_value_usd"].mean())
    }