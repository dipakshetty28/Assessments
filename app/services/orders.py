from __future__ import annotations

import json
from pathlib import Path
from typing import Any

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "orders.json"


def load_orders() -> list[dict[str, Any]]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def calculate_order_total(order: dict[str, Any]) -> float:
    # BUG: quantity is ignored, so multi-unit items are undercounted.
    return round(sum(item["unit_price"] for item in order["items"]), 2)


def summarize_order(order: dict[str, Any]) -> dict[str, object]:
    return {
        "id": order["id"],
        "customer": order["customer"],
        "status": order["status"],
        "total": calculate_order_total(order),
    }
