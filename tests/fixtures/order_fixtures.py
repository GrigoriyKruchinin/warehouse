import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def product_data_1():
    return {
        "name": "Test Product 1",
        "description": "Description for product 1",
        "price": 99.99,
        "quantity_in_stock": 10,
    }


@pytest.fixture
def product_data_2():
    return {
        "name": "Test Product 2",
        "description": "Description for product 2",
        "price": 49.99,
        "quantity_in_stock": 20,
    }


@pytest.fixture
def created_product_1(client: TestClient, product_data_1: dict) -> dict:
    response = client.post("/products/", json=product_data_1)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def created_product_2(client: TestClient, product_data_2: dict) -> dict:
    response = client.post("/products/", json=product_data_2)
    assert response.status_code == 200
    return response.json()


@pytest.fixture
def order_data(created_product_1: dict, created_product_2: dict):
    return {
        "status": "in_process",
        "items": [
            {"product_id": created_product_1["id"], "quantity": 2},
            {"product_id": created_product_2["id"], "quantity": 1},
        ],
    }


@pytest.fixture
def created_order(client: TestClient, order_data: dict) -> dict:
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    return response.json()
