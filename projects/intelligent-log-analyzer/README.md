# Intelligent Log Analyzer — Insider Threat Detection

## Purpose
Detect suspicious user behavior from system logs using anomaly detection.

## Problem
Insider threats are hard to detect due to normal-looking activity patterns.

## MVP Scope
- Load CSV logs
- Extract behavioral features
- Detect anomalies
- Generate alert report

## Input
CSV logs with:
- timestamp
- user_id
- source_ip
- event_type
- resource
- action
- status

## Output
- anomaly label
- anomaly score
- alert reason

## Run
```bash
pip install -r requirements.txt
python src/log_analyzer.py --input sample_data/sample_logs.csv --output alerts.csv
```

## Next Steps
- Add user profiling
- Add sequence analysis
- Add real-time streaming
