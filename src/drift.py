import pandas as pd

NUM_COLS = ['distance_km', 'order_hour', 'delivery_time']

def detect_drift(old_path="data/raw_data.csv", new_path="data/new_data.csv", threshold=1.5):
    old = pd.read_csv(old_path)
    new = pd.read_csv(new_path)

    report = {}
    for col in NUM_COLS:
        old_mean = old[col].mean()
        new_mean = new[col].mean()
        diff = abs(old_mean - new_mean)
        report[col] = diff

    print("Mean differences:", report)

    drift_flag = any(v > threshold for v in report.values())
    print("Drift detected?" , drift_flag)
    return drift_flag

if __name__ == "__main__":
    detect_drift()