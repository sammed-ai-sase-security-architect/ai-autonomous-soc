# 🚀 AI-Autonomous SOC Platform (AISecOps)

Enterprise-grade SOC automation project combining **Detection Engineering + Lightweight AI + MITRE + SOAR simulation**

---

## 🔥 What This Project Shows

* Real SOC workflow
* Anomaly detection (Isolation Forest)
* Rule-based detection
* MITRE ATT&CK mapping
* Automated response (SOAR simulation)

---

## 🧱 Architecture

Logs → Detection → MITRE Mapping → Response → Alerts

---

## ▶️ Run

pip install -r requirements.txt
python src/main.py

---

## 📊 Sample Output

{
"alert": "Suspicious Login Spike",
"severity": "high",
"mitre": "T1110",
"response": "quarantine_host"
}

---

## 💼 Use Case

Designed for:

* SOC Analyst (L2/L3)
* Security Architect
* Detection Engineer

---

## 👤 Author

Cybersecurity | SASE | AI Security Architect
