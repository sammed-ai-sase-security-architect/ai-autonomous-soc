from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(logs):
    df = pd.DataFrame(logs)

    if 'count' not in df:
        return df

    model = IsolationForest(contamination=0.2, random_state=42)
    df['anomaly'] = model.fit_predict(df[['count']])

    return df