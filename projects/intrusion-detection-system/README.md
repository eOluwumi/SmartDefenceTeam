# Intrusion Detection System

An atomic Smart Cyber Defence Team project focused on detecting malicious or abnormal network and system activity using rule-based, machine learning, and later deep learning approaches.

## Legacy Alignment

This project aligns strongly with the research legacy of Prof. A. S. Sodiya, whose work spans cybersecurity, attack/intrusion detection, authentication systems, cryptography, privacy protection, system security, distributed systems security, and critical information infrastructure protection.

## Purpose

The project aims to build a practical intrusion detection system that can analyse traffic or event records and identify suspicious activity patterns.

## MVP Scope

The first version focuses on:

- Reading structured intrusion detection datasets
- Extracting relevant traffic/event features
- Training a baseline machine learning classifier
- Producing intrusion labels and confidence scores
- Reporting basic evaluation metrics

## Possible Dataset Options

- NSL-KDD
- CICIDS2017
- UNSW-NB15
- CSE-CIC-IDS2018
- Custom enterprise/network logs

## Core Detection Categories

- Normal activity
- Denial of Service
- Probe / scanning
- Brute force
- Web attack
- Botnet activity
- Data exfiltration
- Other suspicious traffic

## Project Structure

```text
projects/intrusion-detection-system/
├── README.md
├── requirements.txt
├── sample_data/
├── notebooks/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
└── docs/
```

## MVP Pipeline

```text
Dataset → Preprocessing → Feature Selection → Model Training → Evaluation → Prediction Report
```

## Baseline Models

- Logistic Regression
- Random Forest
- XGBoost / LightGBM, later
- Autoencoder, later
- LSTM / Transformer sequence model, later

## Strategic Direction

This project may evolve into:

- Network intrusion detection engine
- Critical infrastructure monitoring module
- Enterprise cyber defence analytics tool
- Research prototype for adaptive intrusion detection

## Guiding Principle

Machine learning and deep learning are tools. The true mission is cyber defence: detecting attacks early, reducing damage, and protecting critical systems.
