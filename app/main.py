from os import path
import pandas as pd
import pickle

from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Features(BaseModel):
    energy_cost: float
    gov_policy_score: int
    demand_index: float


# load scaler and model
model_path = path.join(path.dirname(__file__), "../models")
with open(path.join(model_path, "model.pkl"), "rb") as f:
    model = pickle.load(f)
with open(path.join(model_path, "scaler.pkl"), "rb") as f:
    scaler = pickle.load(f)


@app.get("/health")
def health_check():
    return {"message": "ok"}


@app.post("/predict")
def predict(features: Features):
    """Predict the hydrogen price based on the input features."""
    input_df = pd.DataFrame(
        [
            {
                "energy_cost": features.energy_cost,
                "gov_policy_score": features.gov_policy_score,
                "demand_index": features.demand_index,
            }
        ]
    )
    data_scaled = scaler.transform(input_df)
    prediction = model.predict(data_scaled)
    return {"prediction": prediction[0]}


@app.post("/predict_batch")
def predict_batch(features: list[Features]):
    """Predict the hydrogen price based on a batch of input features."""
    input_df = pd.DataFrame(
        [
            {
                "energy_cost": feature.energy_cost,
                "gov_policy_score": feature.gov_policy_score,
                "demand_index": feature.demand_index,
            }
            for feature in features
        ]
    )
    data_scaled = scaler.transform(input_df)
    prediction = model.predict(data_scaled)
    return {"predictions": prediction.tolist()}
