def analyze_event(row):
    if row['anomaly'] == -1 and row['count'] > 10:
        return {
            "alert": "Suspicious Login Spike",
            "severity": "high"
        }

    return None