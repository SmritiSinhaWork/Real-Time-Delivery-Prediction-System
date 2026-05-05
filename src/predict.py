import os
import pickle
import pandas as pd
from src.preprocess import preprocess
from src.train import train_and_save

MODEL_PATH = "models/model.pkl"

# If model doesn't exist → train it
if not os.path.exists(MODEL_PATH):
    print("Model not found. Training model...")
    train_and_save()

# Load model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict_one(payload: dict):
    df = pd.DataFrame([payload])
    df = preprocess(df)
    prediction = model.predict(df)
    return float(prediction[0])
