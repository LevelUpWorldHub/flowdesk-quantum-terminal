from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["paper_only"] is True

def test_regime():
    r = client.get("/v1/regime/SPY")
    assert r.status_code == 200
    assert r.json()["regime"] in {"low", "normal", "elevated", "crisis"}

def test_paper_order():
    r = client.post("/v1/paper/orders", json={"symbol": "SPY", "side": "buy", "qty": 1})
    assert r.status_code == 200
    assert r.json()["paper"] is True
