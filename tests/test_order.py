from fastapi.testclient import TestClient
from tests.fixtures import *


def test_create_order(client: TestClient, order_data: dict) -> None:
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == order_data["status"]
    assert "id" in data
    assert "created_at" in data
    assert len(data["items"]) == len(order_data["items"])


def test_get_orders(client: TestClient, created_order: dict) -> None:
    response = client.get("/orders/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["id"] == created_order["id"]


def test_get_order_by_id(client: TestClient, created_order: dict) -> None:
    order_id = created_order["id"]
    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["status"] == created_order["status"]


def test_update_order_status(client: TestClient, created_order: dict) -> None:
    order_id = created_order["id"]
    updated_status = {"status": "completed"}
    update_response = client.patch(f"/orders/{order_id}/status", json=updated_status)
    assert update_response.status_code == 200
    assert (
        update_response.json()["message"]
        == f"Статус заказа id={order_id} изменен на '{updated_status['status']}'"
    )

    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == updated_status["status"]
