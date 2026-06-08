import pandas as pd
import requests


def extract_api_data():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    response = requests.get(url)
    data = response.json()

    price = data["bpi"]["USD"]["rate_float"]

    api_data = {
        "price": [price]
    }

    return pd.DataFrame(api_data)


def extract_csv_data(path):
    return pd.read_csv(path)