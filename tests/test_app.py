import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app import app  # Import the FastAPI app from your main module

client = TestClient(app)


def test_welcome_root():
    # Test the root endpoint
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check():
    # Test the health check endpoint
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
