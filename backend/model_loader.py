import joblib
import os

def load_model():
    model_path = os.path.join("models", "best_model.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model not found.")
    return joblib.load(model_path)
