from fastapi.testclient import TestClient

from app.main import app
from app.services.orders import calculate_order_total

client = TestClient(app)


def test_order_total_uses_quantity() -> None:
    order = {
        "items": [
            {"sku": "seat-pro", "quantity": 3, "unit_price": 49.0},
            {"sku": "onboarding", "quantity": 1, "unit_price": 199.0},
        ]
    }
    assert calculate_order_total(order) == 346.0


def test_orders_can_be_filtered_by_status() -> None:
    response = client.get("/orders?status=paid")
    assert response.status_code == 200
    orders = response.json()
    assert orders
    assert {order["status"] for order in orders} == {"paid"}
