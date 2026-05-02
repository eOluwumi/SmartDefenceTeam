from fastapi import FastAPI
from pydantic import BaseModel
from langdetect import detect

app = FastAPI(title="CyberXTalk API")

class Incident(BaseModel):
    reporter_name: str
    contact: str
    organization: str | None = None
    incident_description: str
    affected_asset: str
    date_observed: str


def classify_incident(text: str):
    text = text.lower()
    if "phish" in text:
        return "Phishing"
    if "ransom" in text:
        return "Ransomware"
    if "login" in text or "account" in text:
        return "Account Compromise"
    if "malware" in text or "virus" in text:
        return "Malware"
    return "Other"


def assign_priority(category: str):
    high = ["Ransomware", "Data Breach", "Financial Fraud"]
    return "High" if category in high else "Medium"


@app.post("/report")
def report_incident(incident: Incident):
    language = detect(incident.incident_description)
    category = classify_incident(incident.incident_description)
    priority = assign_priority(category)

    return {
        "language_detected": language,
        "category": category,
        "priority": priority,
        "message": "Incident received and classified",
    }
