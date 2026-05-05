from src.train import train_and_save
from src.monitor import evaluate_on_file
from src.drift import detect_drift

ERROR_THRESHOLD = 6.0

def maybe_retrain():
    drift = detect_drift()
    mae = evaluate_on_file()

    if drift or mae > ERROR_THRESHOLD:
        print("Triggering retraining...")
        train_and_save("data/new_data.csv", "models/model.pkl")
    else:
        print("No retraining needed.")

if __name__ == "__main__":
    maybe_retrain()