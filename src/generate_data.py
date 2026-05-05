import numpy as np
import pandas as pd

np.random.seed(42)

def generate(n=2000, shift=False):
    distance = np.random.uniform(1, 15, n)
    traffic = np.random.choice(['low', 'medium', 'high'], n, p=[0.4, 0.4, 0.2])
    weather = np.random.choice(['clear', 'rainy'], n, p=[0.8, 0.2])
    hour = np.random.randint(0, 24, n)

    # Base time (minutes)
    base = 10 + distance * 3

    # Traffic impact
    traffic_map = {'low': 0, 'medium': 5, 'high': 12}
    t_effect = np.array([traffic_map[t] for t in traffic])

    # Weather impact
    w_effect = np.where(weather == 'rainy', 6, 0)

    # Peak hours
    peak = np.where((hour >= 12) & (hour <= 14) | (hour >= 18) & (hour <= 21), 5, 0)

    # Drift (simulate distribution change)
    drift = 5 if shift else 0

    noise = np.random.normal(0, 2, n)

    delivery_time = base + t_effect + w_effect + peak + drift + noise

    df = pd.DataFrame({
        'distance_km': distance,
        'traffic_level': traffic,
        'weather': weather,
        'order_hour': hour,
        'delivery_time': delivery_time
    })
    return df

if __name__ == "__main__":
    df = generate(2000, shift=False)
    df.to_csv("data/raw_data.csv", index=False)

    new_df = generate(800, shift=True)
    new_df.to_csv("data/new_data.csv", index=False)

    print("Generated raw_data.csv and new_data.csv")