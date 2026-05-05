from sklearn.metrics import mean_absolute_error
import pandas as pd
from src.preprocess import preprocess
import pickle

MODEL_PATH = "models/model.pkl"

def evaluate_on_file(data_path="data/new_data.csv"):
    df = pd.read_csv(data_path)
    y_true = df['delivery_time'].values

    X = df.drop('delivery_time', axis=1)
    X = preprocess(X)

    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)

    preds = model.predict(X)
    mae = mean_absolute_error(y_true, preds)
    print(f"New Data MAE: {mae:.3f}")
    return mae

if __name__ == "__main__":
    evaluate_on_file()