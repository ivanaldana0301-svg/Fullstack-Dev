import pandas as pd


def transform_data(df_api, df_csv):

    price = df_api["price"].iloc[0]

    df_csv["price"] = price

    df_csv["transaction_value_usd"] = (
        df_csv["amount"] * df_csv["price"]
    )

    df_csv["category"] = df_csv["amount"].apply(
        lambda x: "High" if x >= 300 else "Low"
    )

    return df_csv