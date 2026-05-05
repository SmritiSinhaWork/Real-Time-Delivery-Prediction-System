from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict_one

app = FastAPI(title="Delivery Time Prediction API")

class Payload(BaseModel):
    distance_km: float
    traffic_level: str  # low/medium/high
    weather: str        # clear/rainy
    order_hour: int     # 0-23

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: Payload):
    pred = predict_one(payload.dict())
    return {"predicted_delivery_time_min": round(pred, 2)}