import joblib

try:
    model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.joblib")
    print("Model and scaler loaded successfully.")
except Exception as e:
    print("Error loading model or scaler:", str(e))
