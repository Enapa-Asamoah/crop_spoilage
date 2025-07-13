from fastapi import APIRouter, HTTPException
from schemas import CropData
import numpy as np
import joblib

router = APIRouter()

# Load your trained models
regression_model = joblib.load("C:\Users\user\Desktop\Programs\Ghana AI Hackathon\spoilage_time_regressor_enhanced.pkl")
classification_model = joblib.load("C:\Users\user\Desktop\Programs\Ghana AI Hackathon\spoilage_risk_classifier_enhanced.pkl")

# Crop encoding
crop_mapping = {
    "cassava": 0,
    "cocoyam": 1,
    "groundnut": 2,
    "maize": 3,
    "millet": 4,
    "plantain": 5,
    "rice": 6,
    "sorghum": 7,
    "yam": 8
}

@router.post("/predict")
def predict_spoilage(data: CropData):
    crop_encoded = crop_mapping.get(data.crop.lower())
    if crop_encoded is None:
        raise HTTPException(status_code=400, detail="Invalid crop name provided.")

    features = np.array([[crop_encoded, data.temperature, data.humidity, data.moisture]])

    predicted_days = regression_model.predict(features)[0]
    print(type(predicted_days), predicted_days)
    spoilage_risk = classification_model.predict(features)[0]

    return {
        "predicted_spoilage_days": round(predicted_days, 2),
        "spoilage_risk_level": spoilage_risk
    }
