# CyberXTalk — Multilingual Cyber Incident Reporting System

CyberXTalk is an atomic Smart Cyber Defence Team project for reporting, classifying, translating, and managing cyber attack incidents across multilingual user groups.

## Purpose

Many victims of cyber attacks cannot report incidents clearly because of language barriers, technical complexity, fear, or lack of structured reporting channels.

CyberXTalk provides a guided reporting interface that helps users describe cyber incidents in plain language, supports multilingual input, classifies the incident type, and generates structured reports for response teams.

## MVP Scope

The first version focuses on:

- Accepting incident reports through a simple API
- Supporting multilingual report text
- Classifying common cyber incident categories
- Generating a structured incident case record
- Assigning case priority
- Returning basic recommended next steps

## Core Incident Categories

- Phishing
- Malware infection
- Account compromise
- Financial fraud
- Data breach
- Identity theft
- Insider threat
- Ransomware
- Social engineering
- Other / unknown

## MVP Fields

| Field | Description |
|---|---|
| reporter_name | Name of person submitting the incident |
| contact | Email or phone contact |
| language | Language used in the report |
| organization | Affected organization, if any |
| incident_description | Free-text description of the cyber incident |
| affected_asset | Account, device, system, file, wallet, bank account, etc. |
| date_observed | Date the incident was noticed |
| evidence_link | Optional URL or reference to screenshots/logs |

## Project Structure

```text
projects/cyberxtalk/
├── README.md
├── requirements.txt
├── sample_data/
│   └── sample_incidents.json
└── src/
    └── app.py
```

## Run

From this project folder:

```bash
pip install -r requirements.txt
uvicorn src.app:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Strategic Direction

CyberXTalk can evolve into:

- National cyber incident reporting platform
- Multilingual citizen-facing reporting channel
- Case management workflow for cybersecurity teams
- Threat intelligence collection layer
- B9 Sentinel incident response module

## Design Principle

CyberXTalk should remain simple at the core:

> Receive incident. Understand incident. Classify incident. Structure incident. Route incident.
