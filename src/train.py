import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from src.preprocess import preprocess

def train_and_save(data_path="data/raw_data.csv", model_path="models/model.pkl"):
    df = pd.read_csv(data_path)
    df = preprocess(df)

    X = df.drop('delivery_time', axis=1)
    y = df['delivery_time']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    preds = model.predict(X_val)
    mae = mean_absolute_error(y_val, preds)
    print(f"Validation MAE: {mae:.3f}")

    with open(model_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Model saved to {model_path}")
    return mae

if __name__ == "__main__":
    train_and_save()
