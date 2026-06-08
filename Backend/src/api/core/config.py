from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

DATA_PATH = BASE_DIR / "src" / "output" / "final_data.parquet"
CSV_PATH = BASE_DIR / "src" / "data" / "transactions.csv"