from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"


def test_detect_pest() -> None:
    payload = {"image_id": "img-01", "crop": "rice", "region": "zone-a"}
    resp = client.post("/api/detect-pest", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    assert body["pest_type"] == "brown_planthopper"
    assert body["confidence"] > 0.5
