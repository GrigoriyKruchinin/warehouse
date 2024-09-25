import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def product_data():
    return {
        "name": "Test Product",
        "description": "Test Description",
        "price": 99.99,
    }


@pytest.fixture
def created_product(client: TestClient, product_data: dict) -> dict:
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    return response.json()
