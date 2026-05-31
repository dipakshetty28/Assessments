from __future__ import annotations

import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "events.json"


def _events() -> list[dict[str, object]]:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def list_events(*, account_id: str, limit: int, offset: int) -> dict[str, object]:
    matching = [event for event in _events() if event["account_id"] == account_id]
    return {"items": matching, "total": len(matching)}
