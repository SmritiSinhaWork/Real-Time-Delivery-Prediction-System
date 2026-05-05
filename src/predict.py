import pickle
import pandas as pd
from src.preprocess import preprocess

MODEL_PATH = "models/model.pkl"


with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_one(payload: dict) -> float:
    df = pd.DataFrame([payload])
    df = preprocess(df)
    pred = model.predict(df)[0]
    return float(pred)
