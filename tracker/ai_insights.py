import pandas as pd
import numpy as np
from datetime import timedelta, datetime
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from .models import Feeding, Sleep, GrowthMilestone, DiaperChange
import warnings

# Suppress pandas FutureWarning
warnings.simplefilter(action='ignore', category=FutureWarning)

class AIInsights:
    def __init__(self, baby):
        self.baby = baby
        self.min_data_points = 5  # Minimum data points needed for analysis

    def get_feeding_insights(self):
        """Predicts best feeding times based on past data with enhanced analytics."""
        feedings = Feeding.objects.filter(baby=self.baby).values("time", "feeding_type", "quantity")
        if not feedings.exists() or len(feedings) < self.min_data_points:
            return {"message": "Not enough feeding data yet. Need at least 5 data points."}

        df = pd.DataFrame(list(feedings))
        df["time"] = pd.to_datetime(df["time"])  # Convert to datetime
        df["hour"] = df["time"].dt.hour  # Extract feeding hour
        df["day_of_week"] = df["time"].dt.dayofweek  # 0=Monday, 6=Sunday
        df["date"] = df["time"].dt.date

        # Basic insights
        peak_hours = df["hour"].mode().tolist()
        time_sorted = sorted(df["time"].tolist())
        intervals = np.diff(time_sorted)
        avg_interval = intervals.mean() / np.timedelta64(1, "h")  # Convert to hours
        
        # Pattern detection by day of week
        weekday_patterns = {}
        weekend_patterns = {}
        
        for day in range(7):
            day_data = df[df["day_of_week"] == day]
            if not day_data.empty:
                day_peak_hours = day_data["hour"].mode().tolist()
                if day < 5:  # Weekday
                    weekday_patterns[day] = day_peak_hours
                else:  # Weekend
                    weekend_patterns[day] = day_peak_hours
        
        # Feeding type analysis
        feeding_type_distribution = df["feeding_type"].value_counts().to_dict()
        
        # Quantity analysis if available
        quantity_insights = {}
        if "quantity" in df.columns and not df["quantity"].isna().all():
            avg_quantity = df["quantity"].mean()
            quantity_trend = self._calculate_trend(df, "quantity")
            quantity_insights = {
                "average_quantity": round(avg_quantity, 2),
                "quantity_trend": quantity_trend
            }
        
        # Anomaly detection
        anomalies = self._detect_feeding_anomalies(df)
        
        # Predictive analytics
        next_feeding_prediction = self._predict_next_feeding(df)
        
        # Combine all insights
        return {
            "basic_insights": {
                "recommended_feeding_hours": peak_hours,
                "average_feeding_interval": round(avg_interval, 2),
                "feedings_per_day": round(24 / avg_interval, 1) if avg_interval > 0 else 0,
            },
            "pattern_insights": {
                "weekday_patterns": weekday_patterns,
                "weekend_patterns": weekend_patterns,
                "different_weekend_pattern": bool(set(str(weekday_patterns)) ^ set(str(weekend_patterns))),
                "feeding_type_distribution": feeding_type_distribution,
            },
            "quantity_insights": quantity_insights,
            "anomalies": anomalies,
            "predictions": next_feeding_prediction
        }

    def get_sleep_insights(self):
        """Predicts best nap times based on past sleep data with enhanced analytics."""
        sleeps = Sleep.objects.filter(baby=self.baby).values("start_time", "end_time")
        if not sleeps.exists() or len(sleeps) < self.min_data_points:
            return {"message": "Not enough sleep data yet. Need at least 5 data points."}

        df = pd.DataFrame(list(sleeps))
        df["start_time"] = pd.to_datetime(df["start_time"])
        df["end_time"] = pd.to_datetime(df["end_time"])
        df["duration"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 3600  # Convert to hours
        df["start_hour"] = df["start_time"].dt.hour
        df["end_hour"] = df["end_time"].dt.hour
        df["day_of_week"] = df["start_time"].dt.dayofweek
        df["date"] = df["start_time"].dt.date
        
        # Basic insights
        avg_sleep_duration = df["duration"].mean()
        peak_sleep_times = df["start_hour"].mode().tolist()
        total_sleep_by_day = df.groupby("date")["duration"].sum().mean()
        
        # Pattern detection
        # Identify if there are consistent nap times using clustering
        if len(df) >= 10:  # Need more data for meaningful clusters
            # Convert hours to circular features for better clustering
            df["start_hour_sin"] = np.sin(df["start_hour"] * (2 * np.pi / 24))
            df["start_hour_cos"] = np.cos(df["start_hour"] * (2 * np.pi / 24))
            
            # Try to identify natural sleep clusters (naps vs night sleep)
            features = df[["start_hour_sin", "start_hour_cos", "duration"]].values
            kmeans = KMeans(n_clusters=2, random_state=42).fit(features)
            df["sleep_cluster"] = kmeans.labels_
            
            # Analyze clusters
            clusters = {}
            for cluster in df["sleep_cluster"].unique():
                cluster_data = df[df["sleep_cluster"] == cluster]
                clusters[int(cluster)] = {
                    "avg_start_hour": round(cluster_data["start_hour"].mean(), 1),
                    "avg_duration": round(cluster_data["duration"].mean(), 2),
                    "count": len(cluster_data)
                }
            
            # Label clusters as nap or night sleep based on duration
            if len(clusters) >= 2:
                cluster_ids = list(clusters.keys())
                if clusters[cluster_ids[0]]["avg_duration"] > clusters[cluster_ids[1]]["avg_duration"]:
                    night_cluster, nap_cluster = cluster_ids[0], cluster_ids[1]
                else:
                    night_cluster, nap_cluster = cluster_ids[1], cluster_ids[0]
                
                nap_data = df[df["sleep_cluster"] == nap_cluster]
                night_data = df[df["sleep_cluster"] == night_cluster]
                
                nap_insights = {
                    "recommended_nap_times": nap_data["start_hour"].mode().tolist(),
                    "avg_nap_duration": round(nap_data["duration"].mean(), 2),
                    "naps_per_day": round(nap_data.groupby("date").size().mean(), 1)
                }
                
                night_insights = {
                    "typical_bedtime": night_data["start_hour"].mode().tolist(),
                    "avg_night_sleep_duration": round(night_data["duration"].mean(), 2)
                }
            else:
                nap_insights = {"message": "Not enough data to differentiate naps from night sleep"}
                night_insights = {"message": "Not enough data to differentiate naps from night sleep"}
        else:
            clusters = {}
            nap_insights = {"message": "Need more sleep data for detailed nap analysis"}
            night_insights = {"message": "Need more sleep data for detailed night sleep analysis"}
        
        # Anomaly detection
        anomalies = self._detect_sleep_anomalies(df)
        
        # Predictive analytics
        next_sleep_prediction = self._predict_next_sleep(df)
        
        # Sleep quality estimation
        sleep_quality = self._estimate_sleep_quality(df)
        
        return {
            "basic_insights": {
                "recommended_sleep_times": peak_sleep_times,
                "average_sleep_duration": round(avg_sleep_duration, 2),
                "average_total_sleep_per_day": round(total_sleep_by_day, 2)
            },
            "pattern_insights": {
                "sleep_clusters": clusters,
                "nap_insights": nap_insights,
                "night_sleep_insights": night_insights
            },
            "sleep_quality": sleep_quality,
            "anomalies": anomalies,
            "predictions": next_sleep_prediction
        }
        
    def _calculate_trend(self, df, column):
        """Calculate trend for a given column over time."""
        if len(df) < 3 or column not in df.columns:
            return "insufficient data"
            
        # Ensure data is sorted by time
        if "time" in df.columns:
            df = df.sort_values("time")
        elif "start_time" in df.columns:
            df = df.sort_values("start_time")
        else:
            return "no time column"
        
        # Handle non-numeric data
        if not pd.api.types.is_numeric_dtype(df[column]):
            return "non-numeric data"
            
        # Get values and indices for regression
        y = df[column].values
        X = np.arange(len(y)).reshape(-1, 1)
        
        # Fit linear regression
        model = LinearRegression()
        model.fit(X, y)
        
        # Determine trend based on slope
        slope = model.coef_[0]
        
        if abs(slope) < 0.01:  # Threshold for flat trend
            return "stable"
        elif slope > 0:
            return "increasing"
        else:
            return "decreasing"
    
    def _detect_feeding_anomalies(self, df):
        """Detect anomalies in feeding patterns."""
        anomalies = []
        
        if len(df) < self.min_data_points:
            return anomalies
            
        # Check for unusual intervals
        if "time" in df.columns:
            times = sorted(df["time"].tolist())
            # Convert datetime objects to UTC timestamps first to avoid timezone warning
            times_utc = [t.timestamp() for t in times]
            times_np = np.array(times_utc)
            intervals = np.diff(times_np) / 3600  # Convert seconds to hours
            mean_interval = intervals.mean()
            std_interval = intervals.std()
            
            # Identify unusually long intervals (potential missed feedings)
            long_threshold = mean_interval + 2 * std_interval
            long_intervals = [(times[i], times[i+1]) for i, interval in enumerate(intervals) if interval > long_threshold]
            
            if long_intervals:
                anomalies.append({
                    "type": "unusual_feeding_interval",
                    "description": f"Unusually long intervals between feedings (possibly missed recordings)",
                    "details": {
                        "threshold_hours": round(long_threshold, 2),
                        "instances": len(long_intervals),
                        "example": str(long_intervals[0][0]) + " to " + str(long_intervals[0][1]) if long_intervals else None
                    }
                })
        
        # Check for unusual quantities
        if "quantity" in df.columns and not df["quantity"].isna().all():
            quantities = df["quantity"].values
            mean_qty = quantities.mean()
            std_qty = quantities.std()
            
            # Z-score analysis for outliers
            # Check if all values are nearly identical to avoid precision loss warning
            if np.std(quantities) < 1e-10:
                # If values are nearly identical, there are no outliers
                outliers = np.zeros(len(quantities), dtype=bool)
            else:
                z_scores = stats.zscore(quantities)
                outliers = np.abs(z_scores) > 2.5  # Threshold for outliers
            
            if outliers.any():
                anomalies.append({
                    "type": "unusual_feeding_quantity",
                    "description": "Unusually large or small feeding quantities detected",
                    "details": {
                        "instances": int(outliers.sum()),
                        "mean_quantity": round(mean_qty, 2),
                        "threshold": "±2.5 standard deviations"
                    }
                })
        
        # Check for sudden changes in feeding patterns
        if len(df) >= 10 and "hour" in df.columns:
            # Split data into two halves
            half = len(df) // 2
            first_half = df.iloc[:half]
            second_half = df.iloc[half:]
            
            # Compare distributions of feeding hours
            first_dist = first_half["hour"].value_counts(normalize=True)
            second_dist = second_half["hour"].value_counts(normalize=True)
            
            # Calculate distribution difference
            common_hours = set(first_dist.index) & set(second_dist.index)
            if common_hours:
                diffs = [abs(first_dist.get(h, 0) - second_dist.get(h, 0)) for h in common_hours]
                avg_diff = sum(diffs) / len(diffs)
                
                if avg_diff > 0.3:  # Threshold for significant change
                    anomalies.append({
                        "type": "feeding_pattern_shift",
                        "description": "Significant shift in feeding times detected",
                        "details": {
                            "pattern_difference": round(avg_diff * 100, 1),
                            "interpretation": "Baby's feeding schedule may be changing"
                        }
                    })
        
        return anomalies
    
    def _predict_next_feeding(self, df):
        """Predict when the next feeding is likely to occur."""
        if len(df) < self.min_data_points or "time" not in df.columns:
            return {"message": "Not enough data for prediction"}
            
        # Sort by time
        df = df.sort_values("time")
        
        # Get the last feeding time
        last_feeding = df["time"].max()
        
        # Calculate average interval
        times = sorted(df["time"].tolist())
        # Convert datetime objects to UTC timestamps first to avoid timezone warning
        times_utc = [t.timestamp() for t in times]
        times_np = np.array(times_utc)
        intervals = np.diff(times_np)  # Intervals in seconds
        avg_interval = intervals.mean()
        
        # Predict next feeding time
        # Convert seconds back to timedelta before adding to timestamp
        next_feeding = last_feeding + pd.Timedelta(seconds=avg_interval)
        
        # Get day of week patterns if available
        day_of_week = next_feeding.dayofweek
        hour_of_day = next_feeding.hour
        
        # Check if we have day-specific patterns
        day_specific_pattern = None
        if "day_of_week" in df.columns:
            day_data = df[df["day_of_week"] == day_of_week]
            if len(day_data) >= 3:  # Need enough data for this day
                day_specific_pattern = day_data["hour"].mode().tolist()
        
        return {
            "next_predicted_feeding": str(next_feeding),
            "confidence": "medium" if len(df) > 10 else "low",
            "day_specific_pattern": day_specific_pattern
        }
    
    def _predict_next_sleep(self, df):
        """Predict when the next sleep session is likely to occur."""
        if len(df) < self.min_data_points or "start_time" not in df.columns:
            return {"message": "Not enough data for prediction"}
            
        # Sort by time
        df = df.sort_values("start_time")
        
        # Get the last sleep end time
        if "end_time" in df.columns:
            last_wake = df["end_time"].max()
        else:
            last_wake = df["start_time"].max()
        
        # Calculate average awake interval
        awake_intervals = []
        for i in range(len(df) - 1):
            if i < len(df) - 1:
                end_time = df.iloc[i]["end_time"] if "end_time" in df.columns else df.iloc[i]["start_time"]
                next_start = df.iloc[i+1]["start_time"]
                awake_intervals.append((next_start - end_time).total_seconds() / 3600)  # hours
        
        if not awake_intervals:
            return {"message": "Cannot calculate awake intervals"}
            
        avg_awake = np.mean(awake_intervals)
        
        # Predict next sleep time
        next_sleep = last_wake + timedelta(hours=avg_awake)
        
        return {
            "next_predicted_sleep": str(next_sleep),
            "confidence": "medium" if len(df) > 10 else "low",
            "average_awake_time": round(avg_awake, 2)
        }
    
    def _detect_sleep_anomalies(self, df):
        """Detect anomalies in sleep patterns."""
        anomalies = []
        
        if len(df) < self.min_data_points:
            return anomalies
            
        # Check for unusual sleep durations
        if "duration" in df.columns:
            durations = df["duration"].values
            mean_duration = durations.mean()
            std_duration = durations.std()
            
            # Z-score analysis for outliers
            z_scores = stats.zscore(durations)
            outliers = np.abs(z_scores) > 2.5  # Threshold for outliers
            
            if outliers.any():
                anomalies.append({
                    "type": "unusual_sleep_duration",
                    "description": "Unusually long or short sleep sessions detected",
                    "details": {
                        "instances": int(outliers.sum()),
                        "mean_duration": round(mean_duration, 2),
                        "threshold": "±2.5 standard deviations"
                    }
                })
        
        # Check for fragmented sleep (many short sessions)
        if "duration" in df.columns and "date" in df.columns:
            # Count sleep sessions per day
            sessions_per_day = df.groupby("date").size()
            avg_sessions = sessions_per_day.mean()
            
            if avg_sessions > 5:  # Threshold for fragmented sleep
                anomalies.append({
                    "type": "fragmented_sleep",
                    "description": "Sleep appears to be fragmented with many short sessions",
                    "details": {
                        "average_sessions_per_day": round(avg_sessions, 1),
                        "interpretation": "Baby may be having trouble staying asleep"
                    }
                })
        
        # Check for inconsistent bedtimes
        if "start_hour" in df.columns and len(df) >= 7:
            # Focus on night sleep (8pm-12am typical bedtime range)
            night_starts = df[(df["start_hour"] >= 20) | (df["start_hour"] <= 0)]["start_hour"]
            
            if len(night_starts) >= 5:  # Need enough night sleep data
                # Handle hour wraparound (e.g., 23h and 0h are 1h apart, not 23h)
                night_starts = night_starts.apply(lambda x: x if x >= 20 else x + 24)
                std_bedtime = night_starts.std()
                
                if std_bedtime > 1.5:  # More than 1.5 hours standard deviation
                    anomalies.append({
                        "type": "inconsistent_bedtime",
                        "description": "Bedtime varies significantly from day to day",
                        "details": {
                            "bedtime_variation": round(std_bedtime, 1),
                            "interpretation": "Consistent bedtimes may help improve sleep quality"
                        }
                    })
        
        return anomalies
    
    def _estimate_sleep_quality(self, df):
        """Estimate sleep quality based on patterns."""
        if len(df) < self.min_data_points:
            return {"message": "Not enough data for sleep quality estimation"}
            
        quality_factors = []
        quality_score = 5  # Start with neutral score (1-10 scale)
        
        # Factor 1: Sleep duration
        if "duration" in df.columns:
            avg_duration = df["duration"].mean()
            
            # Age-based sleep recommendations
            baby_age_months = self._get_baby_age_months()
            
            if baby_age_months < 3:
                recommended_hours = 14
            elif baby_age_months < 6:
                recommended_hours = 13
            elif baby_age_months < 12:
                recommended_hours = 12
            else:
                recommended_hours = 11
                
            # Calculate daily total sleep
            if "date" in df.columns:
                daily_sleep = df.groupby("date")["duration"].sum().mean()
                
                # Adjust score based on how close to recommendation
                sleep_diff = abs(daily_sleep - recommended_hours)
                
                if sleep_diff < 1:
                    quality_score += 2
                    quality_factors.append("Sleep duration optimal for age")
                elif sleep_diff < 2:
                    quality_score += 1
                    quality_factors.append("Sleep duration near optimal for age")
                elif sleep_diff > 3:
                    quality_score -= 1
                    quality_factors.append("Sleep duration differs significantly from recommendations")
        
        # Factor 2: Sleep fragmentation
        if "date" in df.columns:
            sessions_per_day = df.groupby("date").size()
            avg_sessions = sessions_per_day.mean()
            
            if avg_sessions <= 3:
                quality_score += 1
                quality_factors.append("Sleep is consolidated with few interruptions")
            elif avg_sessions >= 5:
                quality_score -= 1
                quality_factors.append("Sleep appears fragmented with many sessions")
        
        # Factor 3: Consistent bedtime
        if "start_hour" in df.columns and len(df) >= 7:
            # Focus on night sleep (8pm-12am typical bedtime range)
            night_starts = df[(df["start_hour"] >= 20) | (df["start_hour"] <= 0)]["start_hour"]
            
            if len(night_starts) >= 5:
                # Handle hour wraparound
                night_starts = night_starts.apply(lambda x: x if x >= 20 else x + 24)
                std_bedtime = night_starts.std()
                
                if std_bedtime < 0.5:
                    quality_score += 2
                    quality_factors.append("Very consistent bedtime")
                elif std_bedtime < 1:
                    quality_score += 1
                    quality_factors.append("Fairly consistent bedtime")
                elif std_bedtime > 2:
                    quality_score -= 1
                    quality_factors.append("Inconsistent bedtime")
        
        # Ensure score is within range
        quality_score = max(1, min(10, quality_score))
        
        return {
            "score": quality_score,
            "factors": quality_factors,
            "interpretation": self._interpret_sleep_quality(quality_score)
        }
    
    def _interpret_sleep_quality(self, score):
        """Interpret sleep quality score."""
        if score >= 8:
            return "Excellent sleep patterns"
        elif score >= 6:
            return "Good sleep patterns"
        elif score >= 4:
            return "Average sleep patterns"
        else:
            return "Sleep patterns could be improved"
    
    def _get_baby_age_months(self):
        """Calculate baby's age in months."""
        if not hasattr(self.baby, 'birth_date'):
            return 6  # Default to 6 months if birth date not available
            
        birth_date = self.baby.birth_date
        today = datetime.now().date()
        
        # Calculate age in months
        months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)
        
        # Adjust if birth day hasn't occurred yet this month
        if today.day < birth_date.day:
            months -= 1
            
        return max(0, months)  # Ensure non-negative
    
    def get_growth_insights(self):
        """Analyze growth milestones (height and weight) to provide insights."""
        milestones = GrowthMilestone.objects.filter(baby=self.baby).values(
            "date", "height", "weight"
        ).order_by("date")
        
        if not milestones.exists() or len(milestones) < 2:  # Need at least 2 points for trend
            return {"message": "Not enough growth data yet. Need at least 2 measurements."}
            
        df = pd.DataFrame(list(milestones))
        df["date"] = pd.to_datetime(df["date"])
        
        # Calculate age at each measurement
        if hasattr(self.baby, 'birth_date'):
            birth_date = pd.Timestamp(self.baby.birth_date)
            df["age_days"] = (df["date"] - birth_date).dt.days
            df["age_months"] = df["age_days"] / 30.44  # Average days per month
        else:
            # If no birth date, use days since first measurement
            first_date = df["date"].min()
            df["age_days"] = (df["date"] - first_date).dt.days
            df["age_months"] = df["age_days"] / 30.44
        
        # Basic stats
        latest = df.iloc[-1]
        latest_height = latest["height"]
        latest_weight = latest["weight"]
        latest_age_months = latest["age_months"]
        
        # Calculate growth velocity
        if len(df) >= 3:
            # Height velocity (cm/month)
            df["height_diff"] = df["height"].diff()
            df["months_diff"] = df["age_months"].diff()
            df["height_velocity"] = df["height_diff"] / df["months_diff"]
            recent_height_velocity = df["height_velocity"].dropna().tail(3).mean()
            
            # Weight velocity (kg/month)
            df["weight_diff"] = df["weight"].diff()
            df["weight_velocity"] = df["weight_diff"] / df["months_diff"]
            recent_weight_velocity = df["weight_velocity"].dropna().tail(3).mean()
        else:
            # Simple calculation with just 2 points
            first = df.iloc[0]
            height_change = latest_height - first["height"]
            weight_change = latest_weight - first["weight"]
            months_diff = latest_age_months - first["age_months"]
            
            recent_height_velocity = height_change / months_diff if months_diff > 0 else 0
            recent_weight_velocity = weight_change / months_diff if months_diff > 0 else 0
        
        # Prepare visualization data
        viz_data = {
            "dates": df["date"].dt.strftime("%Y-%m-%d").tolist(),
            "heights": df["height"].tolist(),
            "weights": df["weight"].tolist(),
            "age_months": df["age_months"].round(1).tolist()
        }
        
        # Trend analysis
        height_trend = self._calculate_trend(df, "height")
        weight_trend = self._calculate_trend(df, "weight")
        
        # Growth percentile estimation (simplified)
        # In a real app, this would use WHO or CDC growth charts
        percentile_estimate = "unknown"  # Would require reference data
        
        return {
            "current_stats": {
                "height": round(latest_height, 1),
                "weight": round(latest_weight, 2),
                "age_months": round(latest_age_months, 1),
                "measurement_date": latest["date"].strftime("%Y-%m-%d")
            },
            "growth_velocity": {
                "height_cm_per_month": round(recent_height_velocity, 2),
                "weight_kg_per_month": round(recent_weight_velocity, 3),
                "height_trend": height_trend,
                "weight_trend": weight_trend
            },
            "visualization_data": viz_data,
            "data_points": len(df)
        }
    
    def get_diaper_insights(self):
        """Analyze diaper changes to provide insights on patterns and potential issues."""
        diaper_changes = DiaperChange.objects.filter(baby=self.baby).values(
            "time", "diaper_type"
        )
        
        if not diaper_changes.exists() or len(diaper_changes) < self.min_data_points:
            return {"message": "Not enough diaper data yet. Need at least 5 data points."}
            
        df = pd.DataFrame(list(diaper_changes))
        df["time"] = pd.to_datetime(df["time"])
        df["date"] = df["time"].dt.date
        df["hour"] = df["time"].dt.hour
        
        # Basic stats
        total_changes = len(df)
        days_span = (df["date"].max() - df["date"].min()).days + 1
        changes_per_day = total_changes / days_span if days_span > 0 else 0
        
        # Diaper type distribution
        type_counts = df["diaper_type"].value_counts()
        type_distribution = type_counts.to_dict()
        
        # Calculate wet vs. soiled ratio
        wet_count = type_counts.get("wet", 0)
        soiled_count = type_counts.get("soiled", 0)
        mixed_count = type_counts.get("mixed", 0)
        
        # Check for potential issues
        concerns = []
        
        # Check for hydration issues (too few wet diapers)
        if days_span >= 3:  # Need at least 3 days of data
            wet_per_day = (wet_count + mixed_count) / days_span
            if wet_per_day < 4 and self._get_baby_age_months() <= 12:  # For babies under 1 year
                concerns.append({
                    "type": "hydration",
                    "description": "Fewer wet diapers than expected",
                    "details": {
                        "wet_diapers_per_day": round(wet_per_day, 1),
                        "recommendation": "Monitor hydration and consult pediatrician if concerned"
                    }
                })
        
        # Check for constipation (too few soiled diapers)
        if days_span >= 3:
            soiled_per_day = (soiled_count + mixed_count) / days_span
            baby_age = self._get_baby_age_months()
            
            if baby_age <= 6 and soiled_per_day < 1:
                concerns.append({
                    "type": "constipation",
                    "description": "Fewer soiled diapers than expected for age",
                    "details": {
                        "soiled_diapers_per_day": round(soiled_per_day, 1),
                        "recommendation": "Monitor bowel movements and consult pediatrician if concerned"
                    }
                })
        
        # Time pattern analysis
        hour_distribution = df["hour"].value_counts().sort_index().to_dict()
        peak_hours = df["hour"].value_counts().nlargest(3).index.tolist()
        
        # Visualization data
        daily_counts = df.groupby("date").size()
        viz_data = {
            "dates": [str(date) for date in daily_counts.index],
            "counts": daily_counts.tolist(),
            "hour_distribution": hour_distribution
        }
        
        return {
            "basic_stats": {
                "total_changes": total_changes,
                "days_analyzed": days_span,
                "changes_per_day": round(changes_per_day, 1)
            },
            "type_distribution": type_distribution,
            "time_patterns": {
                "peak_hours": peak_hours,
                "hour_distribution": hour_distribution
            },
            "concerns": concerns,
            "visualization_data": viz_data
        }
    
    def get_comprehensive_insights(self):
        """Provide comprehensive insights across all tracked activities."""
        # Get individual insights
        feeding_insights = self.get_feeding_insights()
        sleep_insights = self.get_sleep_insights()
        growth_insights = self.get_growth_insights()
        diaper_insights = self.get_diaper_insights()
        
        # Check if we have enough data for meaningful insights
        has_feeding = "message" not in feeding_insights
        has_sleep = "message" not in sleep_insights
        has_growth = "message" not in growth_insights
        has_diaper = "message" not in diaper_insights
        
        # Find cross-activity correlations
        correlations = self._find_cross_activity_correlations(
            has_feeding, has_sleep, has_growth, has_diaper
        )
        
        # Generate personalized recommendations
        recommendations = self._generate_recommendations(
            feeding_insights if has_feeding else None,
            sleep_insights if has_sleep else None,
            growth_insights if has_growth else None,
            diaper_insights if has_diaper else None,
            correlations
        )
        
        # Combine all insights
        return {
            "summary": {
                "data_completeness": {
                    "feeding": has_feeding,
                    "sleep": has_sleep,
                    "growth": has_growth,
                    "diaper": has_diaper
                },
                "baby_age_months": self._get_baby_age_months()
            },
            "correlations": correlations,
            "recommendations": recommendations,
            "individual_insights": {
                "feeding": feeding_insights,
                "sleep": sleep_insights,
                "growth": growth_insights,
                "diaper": diaper_insights
            }
        }
    
    def _find_cross_activity_correlations(self, has_feeding=False, has_sleep=False, 
                                         has_growth=False, has_diaper=False):
        """Find correlations between different baby activities."""
        correlations = []
        
        # Need at least two types of data to find correlations
        data_types = sum([has_feeding, has_sleep, has_growth, has_diaper])
        if data_types < 2:
            return [{
                "message": "Need data from at least two different activities to find correlations"
            }]
        
        # Feeding and sleep correlation
        if has_feeding and has_sleep:
            feedings = Feeding.objects.filter(baby=self.baby).values("time")
            sleeps = Sleep.objects.filter(baby=self.baby).values("start_time", "end_time")
            
            if feedings.exists() and sleeps.exists():
                feeding_df = pd.DataFrame(list(feedings))
                feeding_df["time"] = pd.to_datetime(feeding_df["time"])
                feeding_df["date"] = feeding_df["time"].dt.date
                
                sleep_df = pd.DataFrame(list(sleeps))
                sleep_df["start_time"] = pd.to_datetime(sleep_df["start_time"])
                sleep_df["end_time"] = pd.to_datetime(sleep_df["end_time"])
                sleep_df["date"] = sleep_df["start_time"].dt.date
                sleep_df["duration"] = (sleep_df["end_time"] - sleep_df["start_time"]).dt.total_seconds() / 3600
                
                # Check if feeding before sleep leads to longer sleep
                feeding_before_sleep = []
                for _, sleep in sleep_df.iterrows():
                    # Find feedings in the 1 hour before this sleep
                    pre_feedings = feeding_df[
                        (feeding_df["time"] > sleep["start_time"] - pd.Timedelta(hours=1)) &
                        (feeding_df["time"] < sleep["start_time"])
                    ]
                    
                    if not pre_feedings.empty:
                        feeding_before_sleep.append({
                            "sleep_start": sleep["start_time"],
                            "sleep_duration": sleep["duration"],
                            "had_feeding_before": True
                        })
                    else:
                        feeding_before_sleep.append({
                            "sleep_start": sleep["start_time"],
                            "sleep_duration": sleep["duration"],
                            "had_feeding_before": False
                        })
                
                if feeding_before_sleep:
                    fb_df = pd.DataFrame(feeding_before_sleep)
                    with_feeding = fb_df[fb_df["had_feeding_before"] == True]["sleep_duration"].mean()
                    without_feeding = fb_df[fb_df["had_feeding_before"] == False]["sleep_duration"].mean()
                    
                    if not pd.isna(with_feeding) and not pd.isna(without_feeding) and with_feeding > without_feeding:
                        correlations.append({
                            "type": "feeding_sleep",
                            "description": "Feeding before sleep may lead to longer sleep duration",
                            "details": {
                                "with_feeding_hours": round(with_feeding, 2),
                                "without_feeding_hours": round(without_feeding, 2),
                                "difference_percent": round((with_feeding - without_feeding) / without_feeding * 100, 1)
                            }
                        })
        
        # Diaper changes and sleep disruption
        if has_diaper and has_sleep:
            diapers = DiaperChange.objects.filter(baby=self.baby).values("time")
            sleeps = Sleep.objects.filter(baby=self.baby).values("start_time", "end_time")
            
            if diapers.exists() and sleeps.exists():
                diaper_df = pd.DataFrame(list(diapers))
                diaper_df["time"] = pd.to_datetime(diaper_df["time"])
                
                sleep_df = pd.DataFrame(list(sleeps))
                sleep_df["start_time"] = pd.to_datetime(sleep_df["start_time"])
                sleep_df["end_time"] = pd.to_datetime(sleep_df["end_time"])
                
                # Check if diaper changes during sleep periods
                disruptions = 0
                for _, sleep in sleep_df.iterrows():
                    # Find diaper changes during this sleep period
                    changes_during_sleep = diaper_df[
                        (diaper_df["time"] >= sleep["start_time"]) &
                        (diaper_df["time"] <= sleep["end_time"])
                    ]
                    
                    if not changes_during_sleep.empty:
                        disruptions += 1
                
                disruption_rate = disruptions / len(sleep_df) if len(sleep_df) > 0 else 0
                if disruption_rate > 0.3:  # If more than 30% of sleep sessions have diaper changes
                    correlations.append({
                        "type": "diaper_sleep_disruption",
                        "description": "Diaper changes may be disrupting sleep",
                        "details": {
                            "disruption_rate": round(disruption_rate * 100, 1),
                            "recommendation": "Consider using overnight diapers or changing before bedtime"
                        }
                    })
        
        # Feeding and growth correlation
        if has_feeding and has_growth:
            # This would require more sophisticated analysis with feeding amounts
            # and growth measurements over time
            pass
        
        return correlations if correlations else [{
            "message": "No significant correlations found between activities"
        }]
    
    def _generate_recommendations(self, feeding_insights=None, sleep_insights=None, 
                                growth_insights=None, diaper_insights=None, correlations=None):
        """Generate personalized recommendations based on all insights."""
        recommendations = []
        baby_age_months = self._get_baby_age_months()
        
        # Feeding recommendations
        if feeding_insights:
            # Check feeding frequency
            if "basic_insights" in feeding_insights:
                feedings_per_day = feeding_insights["basic_insights"].get("feedings_per_day", 0)
                
                if baby_age_months < 3 and feedings_per_day < 8:
                    recommendations.append({
                        "category": "feeding",
                        "title": "Consider increasing feeding frequency",
                        "description": "Newborns typically need 8-12 feedings per day",
                        "priority": "high"
                    })
                elif baby_age_months < 6 and feedings_per_day < 6:
                    recommendations.append({
                        "category": "feeding",
                        "title": "Monitor feeding frequency",
                        "description": "Babies 3-6 months typically need 6-8 feedings per day",
                        "priority": "medium"
                    })
            
            # Check for feeding anomalies
            if "anomalies" in feeding_insights and feeding_insights["anomalies"]:
                for anomaly in feeding_insights["anomalies"]:
                    if anomaly["type"] == "unusual_feeding_interval":
                        recommendations.append({
                            "category": "feeding",
                            "title": "Feeding schedule may need adjustment",
                            "description": "Unusually long gaps between feedings detected",
                            "priority": "medium"
                        })
        
        # Sleep recommendations
        if sleep_insights:
            # Check sleep quality
            if "sleep_quality" in sleep_insights and "score" in sleep_insights["sleep_quality"]:
                sleep_score = sleep_insights["sleep_quality"]["score"]
                
                if sleep_score < 4:
                    recommendations.append({
                        "category": "sleep",
                        "title": "Sleep quality could be improved",
                        "description": "Consider establishing a consistent bedtime routine",
                        "priority": "high"
                    })
                elif sleep_score < 6:
                    recommendations.append({
                        "category": "sleep",
                        "title": "Sleep quality is average",
                        "description": "Small adjustments to sleep routine may help improve quality",
                        "priority": "medium"
                    })
            
            # Check for sleep anomalies
            if "anomalies" in sleep_insights and sleep_insights["anomalies"]:
                for anomaly in sleep_insights["anomalies"]:
                    if anomaly["type"] == "fragmented_sleep":
                        recommendations.append({
                            "category": "sleep",
                            "title": "Sleep appears fragmented",
                            "description": "Consider evaluating sleep environment and routine",
                            "priority": "high"
                        })
                    elif anomaly["type"] == "inconsistent_bedtime":
                        recommendations.append({
                            "category": "sleep",
                            "title": "Bedtime consistency could help",
                            "description": "A consistent bedtime may improve sleep quality",
                            "priority": "medium"
                        })
        
        # Growth recommendations
        if growth_insights and "growth_velocity" in growth_insights:
            velocity = growth_insights["growth_velocity"]
            
            if velocity["height_trend"] == "decreasing" or velocity["weight_trend"] == "decreasing":
                recommendations.append({
                    "category": "growth",
                    "title": "Growth trend shows slowing",
                    "description": "Consider discussing with your pediatrician at next visit",
                    "priority": "medium"
                })
            
            # Reminder for regular growth monitoring
            recommendations.append({
                "category": "growth",
                "title": "Regular growth monitoring",
                "description": f"Schedule next growth measurement in {1 if baby_age_months < 12 else 3} month(s)",
                "priority": "low"
            })
        
        # Diaper recommendations
        if diaper_insights and "concerns" in diaper_insights and diaper_insights["concerns"]:
            for concern in diaper_insights["concerns"]:
                if concern["type"] == "hydration":
                    recommendations.append({
                        "category": "diaper",
                        "title": "Monitor hydration",
                        "description": concern["details"]["recommendation"],
                        "priority": "high"
                    })
                elif concern["type"] == "constipation":
                    recommendations.append({
                        "category": "diaper",
                        "title": "Monitor bowel movements",
                        "description": concern["details"]["recommendation"],
                        "priority": "medium"
                    })
        
        # Recommendations based on correlations
        if correlations:
            for correlation in correlations:
                if isinstance(correlation, dict) and "type" in correlation:
                    if correlation["type"] == "feeding_sleep":
                        recommendations.append({
                            "category": "routine",
                            "title": "Feeding before sleep may be beneficial",
                            "description": "Data suggests feeding before sleep leads to longer sleep duration",
                            "priority": "medium"
                        })
                    elif correlation["type"] == "diaper_sleep_disruption":
                        recommendations.append({
                            "category": "routine",
                            "title": "Consider diaper change timing",
                            "description": correlation["details"]["recommendation"],
                            "priority": "medium"
                        })
        
        # Age-specific developmental recommendations
        if baby_age_months <= 3:
            recommendations.append({
                "category": "development",
                "title": "Tummy time",
                "description": "Include supervised tummy time daily to strengthen neck and shoulders",
                "priority": "medium"
            })
        elif baby_age_months <= 6:
            recommendations.append({
                "category": "development",
                "title": "Interactive play",
                "description": "Engage with toys, mirrors, and varied sounds to stimulate development",
                "priority": "medium"
            })
        elif baby_age_months <= 12:
            recommendations.append({
                "category": "development",
                "title": "Language development",
                "description": "Talk, read, and sing to your baby regularly to encourage language skills",
                "priority": "medium"
            })
        
        return recommendations
