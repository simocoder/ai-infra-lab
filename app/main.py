# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
from pathlib import Path

app = FastAPI()
model_path = Path("model/model.pkl")
if not model_path.exists():
    raise RuntimeError("Model file not found. Did you run train.py or build the Docker image?")
model = pickle.load(open(model_path, "rb"))

class Features(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Features):
    try:
        preds = model.predict([data.features])
        return {"prediction": int(preds[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))