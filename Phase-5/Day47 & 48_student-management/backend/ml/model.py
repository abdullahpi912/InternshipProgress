"""
Crop recommendation model wrapper.

Loads the Phase 2 model (Day 20 - tuned Random Forest, trained on the
Kaggle Crop Recommendation Dataset) once and exposes a single predict()
function. Kept separate from app.py so the API layer doesn't know or
care how the prediction is actually produced.
"""
import os
import pickle

import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "crop_recommendation_model.pkl")

# Exact feature order the model was trained on (see feature_names_in_).
FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

_model = None


def load_model():
    """Load the pickled model into memory. Called once at app startup."""
    global _model
    with open(MODEL_PATH, "rb") as f:
        _model = pickle.load(f)
    return _model


def predict(values: dict) -> str:
    """
    values: dict with keys N, P, K, temperature, humidity, ph, rainfall
    (all numeric). Raises ValueError if the model hasn't been loaded yet.
    Returns the predicted crop name as a string.
    """
    if _model is None:
        raise RuntimeError("Model not loaded — call load_model() at startup first")

    # No scaling/encoding needed: it's a tree-based model trained on raw values.
    row = pd.DataFrame([[values[f] for f in FEATURES]], columns=FEATURES)
    prediction = _model.predict(row)[0]
    return str(prediction)
