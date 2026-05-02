# CyberXTalk — Multilingual Cyber Incident Reporting System

## Purpose
A system for collecting, understanding, and structuring cyber incident reports across multiple languages.

## Problem
Cyber incidents are underreported due to language barriers, lack of structure, and low technical awareness.

## MVP Scope
- Accept incident reports (API)
- Detect language
- Classify incident type
- Assign priority
- Store incident (next step)

## Input Example
```json
{
  "reporter_name": "John",
  "incident_description": "My account was hacked",
  "affected_asset": "email",
  "date_observed": "2026-05-02"
}
```

## Output Example
```json
{
  "language_detected": "en",
  "category": "Account Compromise",
  "priority": "Medium"
}
```

## Run
```bash
pip install -r requirements.txt
uvicorn src.app:app --reload
```

## Next Steps
- Add translation layer
- Add database (SQLite → Postgres)
- Improve classification (ML)
- Add dashboard
