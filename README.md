# Real-Time Delivery Time Prediction System

A production-style machine learning system that predicts delivery time using real-time inputs.
This project simulates a real-world ML pipeline with **API deployment, monitoring, drift detection, and automated retraining**.

---

## Live Demo

Access the deployed API:

https://real-time-delivery-prediction-system.onrender.com/docs

---

## Overview

This project builds an end-to-end ML pipeline for predicting delivery time based on:

* Distance
* Traffic conditions
* Weather
* Time of order

It demonstrates how ML systems are deployed and maintained in production environments.

---

## Tech Stack

* **Python**
* **Scikit-learn (Random Forest)**
* **FastAPI (real-time API)**
* **Pandas, NumPy**
* **Uvicorn**
* **Render (Deployment)**

---

## Key Features

### 🔹 Real-Time Inference

* REST API using FastAPI
* Accepts JSON input and returns predictions

### 🔹 Model Training

* Random Forest Regressor
* Evaluated using Mean Absolute Error (MAE)

### 🔹 Monitoring

* Tracks model performance on new data

### 🔹 Drift Detection

* Detects data distribution changes

### 🔹 Automated Retraining

* Retrains model when performance degrades

### 🔹 Deployment-Ready Design

* Auto-trains model during deployment
* No dependency on local model files

---

## System Architecture

flowchart

        +----------------------+
        |   Raw Training Data  |
        +----------+-----------+
                   |
                   v
          +------------------+
          |   Preprocessing  |
          | (Encoding, Clean)|
          +------------------+
                   |
                   v
          +------------------+
          |   ML Model       |
          | (Random Forest)  |
          +------------------+
                   |
                   v
          +------------------+
          |   Model Storage  |
          |   (model.pkl)    |
          +------------------+
                   |
                   v
         ------------------------
         |                      |
         v                      v
    +------------------+   +------------------+
    |   FastAPI        |   |   Monitoring     |
    |   (Inference)    |   |   (MAE Tracking) |
    +------------------+   +------------------+
             |                      |
             v                      v
    +-----------------------+   +------------------+        
    | Real-time Predictions |   |  Drift Detection |
    +-----------------------+   +------------------+       
                                       |
                                       v
                              +------------------+
                              | Retraining Logic |
                              +------------------+

---

## How to Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/SmritiSinhaWork/Real-Time-Delivery-Prediction-System.git
cd Real-Time-Delivery-Prediction-System
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Generate Dataset

```bash
python src/generate_data.py
```

---

### 4. Train Model

```bash
python -m src.train
```

---

### 5. Start API Server

```bash
python -m uvicorn app:app --reload
```

---

### 6. Open Swagger UI

http://127.0.0.1:8000/docs

---

### 7. Test Prediction

```json
{
  "distance_km": 5.2,
  "traffic_level": "medium",
  "weather": "clear",
  "order_hour": 13
}
```

---

## Deployment Strategy

* Model file is **not stored in the repository**
* On deployment:

  * System checks for model
  * If missing → trains automatically
* Ensures:

  * No GitHub size issues
  * No file corruption
  * Clean and scalable deployment

---

## Project Structure

```
Real-Time-Delivery-Prediction-System/
├── data/
├── models/              # auto-created during runtime
├── src/
│   ├── generate_data.py
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   ├── monitor.py
│   ├── drift.py
│   └── retrain.py
├── app.py
├── requirements.txt
└── README.md
```

---

## Screenshots

<img width="1880" height="843" alt="image" src="https://github.com/user-attachments/assets/704ad369-319c-4704-8e38-5b32ea367f94" />
* Swagger UI

<img width="1840" height="819" alt="image" src="https://github.com/user-attachments/assets/17a468db-18e1-4d18-94ad-015aebe63e11" />
* Input

<img width="1836" height="638" alt="image" src="https://github.com/user-attachments/assets/1103715b-7b86-402f-b8bb-5f0cc651bac3" />
* Prediction output

---

## Use Case

Inspired by real-world logistics platforms like **Swiggy / Zepto**, where accurate delivery time prediction directly impacts user experience and operational efficiency.

---

## Author

**Smriti Sinha**
GitHub: https://github.com/SmritiSinhaWork
