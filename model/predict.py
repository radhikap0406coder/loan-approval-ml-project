import os
import joblib
import pandas as pd

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "loan_approval_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_loan(input_data: dict):

    df = pd.DataFrame([input_data])

    # Feature Engineering

    df["total_assets"] = (
        df["residential_assets_value"]
        + df["commercial_assets_value"]
        + df["luxury_assets_value"]
        + df["bank_asset_value"]
    )

    df["loan_income_ratio"] = df["loan_amount"] / (df["income_annum"] + 1e-6)
    df["asset_loan_ratio"] = df["total_assets"] / (df["loan_amount"] + 1e-6)

    prediction = model.predict(df)[0]
    confidence = model.predict_proba(df)[0][prediction]

    return prediction, confidence