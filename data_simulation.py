import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Simulated smartwatch sleep data
data = {
    "total_sleep_minutes": np.random.randint(300, 520, 200),
    "awake_minutes": np.random.randint(10, 120, 200),
    "hrv": np.random.randint(20, 100, 200),
    "avg_heart_rate": np.random.randint(55, 90, 200)
}

df = pd.DataFrame(data)

print("Sample smartwatch sleep data:\n")
print(df.head())


df.to_csv("sleep_metrics.csv", index=False)
print("\nData saved as sleep_metrics.csv")
