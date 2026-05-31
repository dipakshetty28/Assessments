from fastapi import FastAPI, Query

from app.services.events import list_events

app = FastAPI(title="Account Events API")


@app.get("/accounts/{account_id}/events")
def account_events(account_id: str, limit: int = Query(25, ge=1, le=100), offset: int = Query(0)):
    return list_events(account_id=account_id, limit=limit, offset=offset)
