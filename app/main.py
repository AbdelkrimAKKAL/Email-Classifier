from fastapi import FastAPI
from pydantic import BaseModel
from .classifier import ZeroShotClassifier
import logging
from dotenv import load_dotenv


load_dotenv()


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="Email Classifier - Learning Edition")
classifier = ZeroShotClassifier()

class EmailRequest(BaseModel):
    content: str

@app.post("/classify")
def classify_email(request: EmailRequest):
    """
    Endpoint simple pour classifier le contenu d'un email.
    Idéal pour apprendre Docker et le CI/CD.
    """
    logging.info(f"Classifying content: {request.content[:50]}...")
    
    # Classification via Hugging Face Cloud
    prediction = classifier.predict(request.content)
    
    # Retourner uniquement le résultat
    return {
        "category": prediction["category"],
        "confidence": round(prediction["score"], 4)
    }

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Welcome to the Simple Email Classifier API",
        "instructions": "Use POST /classify to categorize your emails."
    }
