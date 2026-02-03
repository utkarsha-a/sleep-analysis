import joblib
import pandas as pd

# Load trained model
model = joblib.load("sleep_rf_model.pkl")

# Feature names (same order as training)
features = [
    "total_sleep_minutes",
    "awake_minutes",
    "hrv",
    "avg_heart_rate"
]

# Get feature importance
importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

print("\n🔍 Feature Importance (Global)")
print(importance)
