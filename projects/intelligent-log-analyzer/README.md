# Intelligent Log Analyzer for Insider Threat Detection

An atomic Smart Cyber Defence Team project for detecting suspicious insider activity from structured enterprise logs.

## Purpose

This project provides a lightweight baseline for analysing user activity logs and identifying anomalous behaviour patterns that may indicate insider threat activity.

## MVP Scope

The first version focuses on:

- Reading structured CSV logs
- Extracting simple behavioural features
- Detecting anomalies using Isolation Forest
- Producing an alert report with anomaly labels and scores

## Expected Log Columns

The MVP expects a CSV file with the following columns:

| Column | Description |
|---|---|
| timestamp | Date and time of event |
| user_id | User or account identifier |
| source_ip | Source IP address |
| event_type | Login, file_access, download, privilege_change, etc. |
| resource | System, file, database, or endpoint accessed |
| action | User action performed |
| status | success or failed |

## Project Structure

```text
projects/intelligent-log-analyzer/
├── README.md
├── requirements.txt
├── sample_data/
│   └── sample_logs.csv
└── src/
    └── log_analyzer.py
```

## Run

From this project folder:

```bash
pip install -r requirements.txt
python src/log_analyzer.py --input sample_data/sample_logs.csv --output alerts.csv
```

## Output

The script generates a CSV report containing:

- Original log fields
- Engineered features
- Anomaly label
- Anomaly score
- Alert reason

## Strategic Direction

This project can later evolve into:

- Insider threat detection module
- SIEM enrichment component
- B9 Sentinel detection engine
- Research prototype for behavioural cybersecurity analytics
