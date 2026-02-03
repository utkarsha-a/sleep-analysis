from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from save_and_predict import predict_sleep
from weekly_sleep_analysis import analyze_weekly_sleep

app = FastAPI(title="Sleep ML API")

# ---------- Request Models ----------

class NightSleepInput(BaseModel):
    total_sleep_minutes: int
    awake_minutes: int
    hrv: int
    avg_heart_rate: int

class WeeklySleepInput(BaseModel):
    sleep_scores: List[float]

# ---------- Routes ----------

@app.post("/sleep/night")
def analyze_night_sleep(data: NightSleepInput):
    result = predict_sleep(data.dict())
    return result

@app.post("/sleep/weekly")
def analyze_weekly(data: WeeklySleepInput):
    result = analyze_weekly_sleep(data.sleep_scores)
    return result
