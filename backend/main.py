from fastapi import FastAPI
from pydantic import BaseModel
from backend.model_loader import load_model

app = FastAPI(title="Cirrhosis Stage Prediction API")

# Load trained model
model = load_model()

# Patient input schema: 15 features only
class PatientData(BaseModel):
    Age: float
    Sex: float
    Ascites: float
    Hepatomegaly: float
    Spiders: float
    Edema: float
    Bilirubin: float
    Cholesterol: float
    Albumin: float
    Copper: float
    Alk_Phos: float
    SGOT: float
    Tryglicerides: float
    Platelets: float
    Prothrombin: float

@app.get("/health")
def health_check():
    return {"status": "✅ API is running and model is loaded"}

@app.post("/predict")
def predict(data: PatientData):
    try:
        features = [
            data.Age, data.Sex, data.Ascites, data.Hepatomegaly, data.Spiders, data.Edema,
            data.Bilirubin, data.Cholesterol, data.Albumin, data.Copper,
            data.Alk_Phos, data.SGOT, data.Tryglicerides,
            data.Platelets, data.Prothrombin
        ]
        prediction = model.predict([features])[0]
        return {"predicted_stage": int(prediction) + 1}  # 0-based → 1-based
    except Exception as e:
        return {"error": str(e)}