def validate_data(df):

    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset contains null values")

    return True