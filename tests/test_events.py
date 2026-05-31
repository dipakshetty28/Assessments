from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_account_events_apply_limit_and_offset() -> None:
    response = client.get('/accounts/acct_1/events?limit=1&offset=1')
    assert response.status_code == 200
    payload = response.json()
    assert payload['total'] == 3
    assert [event['id'] for event in payload['items']] == ['evt_2']
