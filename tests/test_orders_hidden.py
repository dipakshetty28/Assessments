from app.services.orders import calculate_order_total


def test_zero_quantity_items_do_not_inflate_totals() -> None:
    order = {"items": [{"sku": "trial", "quantity": 0, "unit_price": 99.0}]}
    assert calculate_order_total(order) == 0.0
