def analyze_weekly_sleep(sleep_scores):
    avg_score = sum(sleep_scores) / len(sleep_scores)
    poor_days = sum(1 for s in sleep_scores if s < 60)
    good_days = sum(1 for s in sleep_scores if s >= 80)

    if poor_days >= 4:
        pattern = "Chronic Sleep Deficit"
        advice = "You have had multiple poor sleep nights this week. Focus on sleep hygiene and recovery."
    elif avg_score >= 75:
        pattern = "Healthy Sleep Pattern"
        advice = "Your sleep pattern is consistent and healthy. Keep it up!"
    else:
        pattern = "Irregular Sleep Pattern"
        advice = "Your sleep schedule has been inconsistent. Try maintaining fixed sleep and wake times."

    return {
        "weekly_pattern": pattern,
        "average_score": round(avg_score, 1),
        "poor_days": poor_days,
        "good_days": good_days,
        "advice": advice
    }