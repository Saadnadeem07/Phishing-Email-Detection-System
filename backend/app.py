import pickle
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Resolve model paths relative to this file so the app can be started
# from any working directory.
BASE_DIR = Path(__file__).resolve().parent

# Define email input schema
class EmailInput(BaseModel):
    email: str

# Initialize FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Load the model and vectorizer
with open(BASE_DIR / "model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open(BASE_DIR / "vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)


@app.get("/")
async def health():
    return {"status": "ok", "message": "Phishing Email Detection API is running"}

# Define the predict endpoint
@app.post("/predict")
async def predict(email: EmailInput):
    # Vectorize the input email text
    email_text = email.email
    email_vector = vectorizer.transform([email_text])

    # Predict using the trained model
    prediction = model.predict(email_vector)[0]
    prediction_proba = model.predict_proba(email_vector)[0]
    confidence = prediction_proba[1] if prediction == 1 else prediction_proba[0]
    prediction_label = "Safe Email" if prediction == 0 else "Phishing Email"

    # Return the prediction result and confidence
    return {
        "prediction": prediction_label,
        "confidence": float(confidence)
    }
