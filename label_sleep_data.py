import pandas as pd

# Load smartwatch-like data (from DB / CSV)
df = pd.read_csv("sleep_metrics.csv")

# Sleep score calculation
def calculate_sleep_score(row):
    score = 0

    # Sleep duration (max 40)
    score += min((row["total_sleep_minutes"] / 480) * 40, 40)

    # Awake time penalty (max -20)
    score -= min((row["awake_minutes"] / 120) * 20, 20)

    # HRV contribution (max 30)
    score += min((row["hrv"] / 100) * 30, 30)

    # Heart rate stability (max 10)
    score += 10 if row["avg_heart_rate"] < 70 else 5

    return max(0, min(100, score))

# Apply score
df["sleep_score"] = df.apply(calculate_sleep_score, axis=1)

# Sleep pattern labels
def label_sleep_pattern(score):
    if score >= 80:
        return "Good"
    elif score >= 60:
        return "Inconsistent"
    else:
        return "Poor"

df["sleep_pattern"] = df["sleep_score"].apply(label_sleep_pattern)

# Save training-ready data
df.to_csv("sleep_training_data.csv", index=False)

print("Sleep training data generated successfully!")
print(df.head())
