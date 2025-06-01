# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()
model = pickle.load(open("model/model.pkl", "rb"))

class Features(BaseModel):
    features: list

@app.post("/predict")
def predict(data: Features):
    try:
        preds = model.predict([data.features])
        return {"prediction": int(preds[0])}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))