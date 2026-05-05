# Real-Time Delivery Time Prediction System

A production-inspired machine learning system that predicts delivery time using real-time inputs and simulates key MLOps components such as monitoring, drift detection, and retraining.

---

## Overview

This project builds an end-to-end ML pipeline for predicting delivery time based on factors like distance, traffic, weather, and time of day.

It simulates a real-world production system by integrating:
- Model training and evaluation
- Real-time inference using API
- Model monitoring
- Data drift detection
- Automated retraining

---

## Tech Stack

- Python
- Scikit-learn (Random Forest)
- FastAPI (real-time API)
- Pandas, NumPy
- Uvicorn

---

## Features

### 1. Real-Time Inference
- REST API using FastAPI
- Accepts real-time input and returns predictions

### 2. Feature Engineering
- Encodes categorical variables (traffic, weather)
- Uses domain-inspired features (peak hours, traffic levels)

### 3. Model Training
- Random Forest Regressor
- Evaluated using Mean Absolute Error (MAE)

### 4. Monitoring
- Tracks model performance on new incoming data
- Evaluates prediction error

### 5. Drift Detection
- Detects distribution shifts between old and new data
- Flags performance degradation

### 6. Retraining Pipeline
- Automatically retrains model when:
  - Drift is detected OR
  - Error exceeds threshold

---

## Architecture
flowchart TD

A[Raw Data / Input] --> B[Preprocessing]
B --> C[Feature Engineering]
C --> D[ML Model Training<br/>Random Forest]
D --> E[Model Saved<br/>model.pkl]

E --> F[FastAPI Server<br/>Real-Time Inference]
F --> G[Prediction API<br/>/predict]

E --> H[Monitoring]
H --> I[MAE Evaluation]

I --> J[Drift Detection]
J --> K{Drift or High Error?}

K -- Yes --> L[Retrain Model]
L --> E

K -- No --> M[Continue Serving Predictions]

---

## How to Run
1. Clone the Repository
git clone <your-repo-link>
cd delivery-time-ml
2. Install Dependencies
pip install -r requirements.txt
3. Generate Dataset
python src/generate_data.py

This creates:

data/raw_data.csv
data/new_data.csv
4. Train the Model
python src/train.py

This saves:

models/model.pkl
5. Run Monitoring & Drift Detection (Optional)
python src/monitor.py
python src/drift.py
python src/retrain.py
6. Start the API Server
python -m uvicorn app:app --reload
7. Open Swagger UI

Go to:

http://127.0.0.1:8000/docs

8. Test Prediction

Use the /predict endpoint with:

{
  "distance_km": 5.2,
  "traffic_level": "medium",
  "weather": "clear",
  "order_hour": 13
}
Output Example
{
  "predicted_delivery_time_min": 39.5
}

---

##Use Case

Inspired by real-world logistics systems (e.g., Zepto, Swiggy), where delivery time prediction directly impacts customer experience and operational efficiency.
