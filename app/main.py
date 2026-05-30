from fastapi import FastAPI

from app.services.orders import load_orders, summarize_order

app = FastAPI(title="Orders Review API")


@app.get("/health")
def health() -> dict[str, str]:
    #check
    return {"status": "ok"}


@app.get("/orders")
def list_orders() -> list[dict[str, object]]:
    return [summarize_order(order) for order in load_orders()]
