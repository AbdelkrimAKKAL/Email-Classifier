from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint for basic API health."""
    response = client.get("/")
    assert response.status_code == 200
    assert "Simple Email Classifier" in response.json()["message"]
    assert response.json()["status"] == "online"

@patch('app.classifier.ZeroShotClassifier.predict')
def test_classify_endpoint_mocked(mock_predict):
    """
    Test the classify endpoint without hitting the real Hugging Face API.
    This ensures the FastAPI routes and response formatting work correctly.
    """
    # Define what the mock AI should return
    mock_predict.return_value = {
        "category": "customer support",
        "score": 0.95
    }

    # Make the request to the local API
    response = client.post(
        "/classify",
        json={"content": "I need help with my broken order."}
    )

    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "customer support"
    assert data["confidence"] == 0.9500
    
    # Ensure our mock was actually called
    mock_predict.assert_called_once_with("I need help with my broken order.")
    
