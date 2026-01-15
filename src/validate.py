# src/validate.py
import pandas as pd

ALLOWED_SUBJECTS = ["Discrete Mathematics", "English", "Advanced Programming"]

def validate_data(df: pd.DataFrame) -> None:
    assert df["hours"].ge(0).all(), "Study hours must be non-negative"
    assert df["subject"].isin(ALLOWED_SUBJECTS).all(), "Unknown subject found"
    assert pd.api.types.is_datetime64_any_dtype(df["date"]), "date must be datetime"