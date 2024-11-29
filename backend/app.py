from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.middleware.cors import CORSMiddleware

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
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

# Define the predict endpoint
@app.post("/predict")
async def predict(email: EmailInput):
    # Vectorize the input email text
    email_text = email.email
    email_vector = vectorizer.transform([email_text])

    # Predict using the trained model
    prediction = model.predict(email_vector)[0]
    prediction_label = "Safe Email" if prediction == 0 else "Phishing Email"

    # Return the prediction result
    return {"prediction": prediction_label}
