import os
import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)

# Only run integration tests if we have an API key configured and it is not empty
HAS_API_KEY = bool(os.getenv("HUGGINGFACE_API_KEY"))

@pytest.mark.skipif(not HAS_API_KEY, reason="HUGGINGFACE_API_KEY is required for integration tests.")
def test_classify_endpoint_live():
    """
    Test the classify endpoint by actually hitting the Hugging Face API.
    This verifies the end-to-end flow is completely functional.
    """
    response = client.post(
        "/classify",
        json={"content": "Hello, I need help resetting my password."}
    )

    # Verification
    assert response.status_code == 200
    data = response.json()
    
    # We expect this to be support-related.
    # The actual category prediction depends on the live HF model.
    assert "category" in data
    assert "confidence" in data
    assert data["category"] == "customer support"
    assert data["confidence"] > 0.4  # Ensure it has reasonable confidence
