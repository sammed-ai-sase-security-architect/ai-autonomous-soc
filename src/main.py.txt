from ingest import load_logs
from detection_engine import detect_anomalies
from ai_analyzer import analyze_event
from mitre_mapper import map_mitre
from response_engine import respond
import json

logs = load_logs("data/sample/logs.json")

df = detect_anomalies(logs)

alerts = []

for _, row in df.iterrows():
    result = analyze_event(row)

    if result:
        mitre = map_mitre(row['action'])
        action = respond(result)

        alert = {
            "alert": result["alert"],
            "severity": result["severity"],
            "mitre": mitre,
            "response": action
        }

        alerts.append(alert)

with open("outputs/alerts.json", "w") as f:
    json.dump(alerts, f, indent=4)

print("Alerts generated:", alerts)