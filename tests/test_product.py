from fastapi.testclient import TestClient
from tests.fixtures import *


def test_create_product(client: TestClient, product_data: dict) -> None:
    response = client.post("/products/", json=product_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == product_data["name"]
    assert data["description"] == product_data["description"]
    assert data["price"] == product_data["price"]
    assert "id" in data


def test_get_products(client: TestClient, created_product: dict) -> None:
    response = client.get("/products/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["name"] == created_product["name"]


def test_get_product_by_id(client: TestClient, created_product: dict) -> None:
    product_id = created_product["id"]
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == product_id
    assert data["name"] == created_product["name"]


def test_update_product(client: TestClient, created_product: dict) -> None:
    product_id = created_product["id"]
    updated_data = {
        "name": "Updated Product",
        "description": "Updated Description",
        "price": 59.99,
    }
    update_response = client.put(f"/products/{product_id}", json=updated_data)
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == updated_data["name"]
    assert data["description"] == updated_data["description"]
    assert data["price"] == updated_data["price"]


def test_delete_product(client: TestClient, created_product: dict) -> None:
    product_id = created_product["id"]
    delete_response = client.delete(f"/products/{product_id}")
    assert delete_response.status_code == 200
    data = delete_response.json()
    assert data["detail"] == "Product deleted"

    get_response = client.get(f"/products/{product_id}")
    assert get_response.status_code == 404
