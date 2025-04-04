import pandas as pd
import numpy as np
from datetime import timedelta
from .models import Feeding, Sleep

class AIInsights:
    def __init__(self, baby):
        self.baby = baby

    def get_feeding_insights(self):
        """Predicts best feeding times based on past data."""
        feedings = Feeding.objects.filter(baby=self.baby).values("time")
        if not feedings.exists():
            return {"message": "Not enough feeding data yet."}

        df = pd.DataFrame(list(feedings))
        df["time"] = pd.to_datetime(df["time"])  # Convert to datetime
        df["hour"] = df["time"].dt.hour  # Extract feeding hour

        # Find the most common feeding hours
        peak_hours = df["hour"].mode().tolist()
        avg_interval = np.diff(sorted(df["time"].tolist())).mean()

        return {
            "recommended_feeding_hours": peak_hours,
            "average_feeding_interval": avg_interval / np.timedelta64(1, "h"),  # Convert to hours
        }

    def get_sleep_insights(self):
        """Predicts best nap times based on past sleep data."""
        sleeps = Sleep.objects.filter(baby=self.baby).values("start_time", "end_time")
        if not sleeps.exists():
            return {"message": "Not enough sleep data yet."}

        df = pd.DataFrame(list(sleeps))
        df["start_time"] = pd.to_datetime(df["start_time"])
        df["end_time"] = pd.to_datetime(df["end_time"])
        df["duration"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 3600  # Convert to hours
        avg_sleep_duration = df["duration"].mean()
        peak_sleep_times = df["start_time"].dt.hour.mode().tolist()

        return {
            "recommended_nap_times": peak_sleep_times,
            "average_sleep_duration": round(avg_sleep_duration, 2),
        }
