import pandas as pd
import joblib

# Load trained model and encoder ONCE
model = joblib.load("sleep_rf_model.pkl")
le = joblib.load("label_encoder.pkl")

def predict_sleep(input_data: dict):
    """
    Input:
    {
        total_sleep_minutes: int,
        awake_minutes: int,
        hrv: int,
        avg_heart_rate: int
    }
    """

    df = pd.DataFrame([input_data])
    pred = model.predict(df)[0]
    label = le.inverse_transform([pred])[0]

    return {
        "sleep_pattern": label
    }

