import os
from pathlib import Path
import requests
import joblib

MODEL_URL = "https://drive.google.com/uc?export=download&id=1-OTgGwqMrNeWwq3Vh9Aiw8Za56WN_fQv"
MODEL_PATH = Path(__file__).parent / "emotion_model.pkl"

def download_model():
    print("Downloading model... (only needed once)")
    response = requests.get(MODEL_URL)
    if response.status_code == 200:
        with open(MODEL_PATH, "wb") as f:
            f.write(response.content)
    else:
        raise RuntimeError(f"Failed to download model. Status code: {response.status_code}")

def get_model():
    if not MODEL_PATH.exists():
        download_model()
    return joblib.load(MODEL_PATH)