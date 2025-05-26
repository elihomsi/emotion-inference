from .model import get_model

def predict_emotion(text: str) -> str:
    model = get_model()
    prediction = model.predict([text])
    return prediction[0]