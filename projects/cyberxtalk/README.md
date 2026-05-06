# CyberXTalk — Multilingual Cyber Incident Reporting System

**Status:** Internal research and implementation workspace  
**Parent initiative:** Smart Cyber Defence Team

CyberXTalk is a cyber incident reporting and response system under the Smart Cyber Defence Team initiative. It is being developed as a protected project workspace for multilingual / voice-assisted incident intake, structured cyber incident intelligence, severity scoring, analyst review, and response guidance.

## IP / Exposure Position

CyberXTalk is intentionally subsumed inside the Smart Cyber Defence Team repository while implementation, research framing, experiments, and architecture are still being refined.

Public-facing details should remain deliberately limited until the system is ready for responsible publication, demonstration, or controlled disclosure.

## Purpose

CyberXTalk transforms unstructured cyber incident narratives into structured, actionable cyber intelligence.

## Problem

Cyber incidents are underreported due to language barriers, lack of structure, low technical awareness, fragmented reporting channels, and fear of exposure.

## MVP Scope

- Accept cyber incident reports through an API
- Support text and voice-assisted reporting
- Detect or infer language where possible
- Normalize multilingual / code-mixed reports
- Classify incident type
- Assign severity / priority
- Store incident records
- Provide recommended response actions
- Prepare analyst-facing dashboard and analytics layer

## Initial Voice Pipeline

```text
User Voice Input
   ↓
STT Layer: Whisper / Azure Speech / YarnGPT ASR experiment
   ↓
CyberXTalk Incident Intelligence Engine
   ↓
Generated Response Text
   ↓
YarnGPT TTS
   ↓
Nigerian-accented Spoken Response
```

## Current Proof-of-Concept

A YarnGPT TTS test successfully generated a CyberXTalk-style voice response as a `.wav` file inside GitHub Codespaces.

Milestone:

> CyberXTalk can speak.

Next objective:

> Make CyberXTalk listen, understand, classify, and respond with structure.

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
  "priority": "Medium",
  "recommended_actions": [
    "Change password immediately",
    "Enable multi-factor authentication",
    "Preserve evidence for analyst review"
  ]
}
```

## Run

```bash
pip install -r requirements.txt
uvicorn src.app:app --reload
```

## Next Steps

- Keep the repository private while implementation is refined
- Move YarnGPT integration experiments into this project folder
- Add STT baseline with Whisper or Azure Speech
- Add database layer: SQLite first, then PostgreSQL
- Improve classification from rules to ML / transformer models
- Add dashboard and analyst workflow

## Safety Rule

Do not commit runtime artifacts, model checkpoints, generated audio, secrets, or datasets that may expose sensitive implementation details.
