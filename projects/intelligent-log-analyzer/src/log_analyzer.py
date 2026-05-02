import argparse
import pandas as pd
from sklearn.ensemble import IsolationForest


def load_logs(path):
    return pd.read_csv(path)


def feature_engineering(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['is_night'] = df['hour'].apply(lambda x: 1 if x < 6 else 0)
    df['failed'] = df['status'].apply(lambda x: 1 if x == 'failed' else 0)
    return df


def detect_anomalies(df):
    features = df[['hour', 'is_night', 'failed']]
    model = IsolationForest(contamination=0.05, random_state=42)
    df['anomaly'] = model.fit_predict(features)
    df['anomaly_score'] = model.decision_function(features)
    return df


def generate_alerts(df):
    alerts = df[df['anomaly'] == -1].copy()
    alerts['alert_reason'] = 'Anomalous behavior detected'
    return alerts


def main(input_path, output_path):
    df = load_logs(input_path)
    df = feature_engineering(df)
    df = detect_anomalies(df)
    alerts = generate_alerts(df)
    alerts.to_csv(output_path, index=False)
    print(f"Alerts saved to {output_path}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    main(args.input, args.output)
