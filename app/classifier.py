from huggingface_hub import InferenceClient
import os

class ZeroShotClassifier:
    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY")
        self.model = "facebook/bart-large-mnli"
        self.client = InferenceClient(model=self.model, token=self.api_key)
        self.candidate_labels = ["customer support", "commercial inquiry", "spam junk", "other miscellaneous"]

    def predict(self, text):
        
        result = self.client.zero_shot_classification(text, self.candidate_labels)
        return {
            "category": result[0]["label"],
            "score": result[0]["score"]
        }
