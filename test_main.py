from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_bmi_calc_1():
    # Test 1 -- Input 0 on Height
    payload = {
        "height": 0,
        "weight": 10
    }

    response = client.post("/bmi", json=payload)
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["body","height"],"msg":"Height must be greater than 0","type":"value_error"}]}

def test_bmi_calc_2():
    # Test 2 -- Input 0 on Weight
    payload = {
        "height": 10,
        "weight": 0
    }

    response = client.post("/bmi", json=payload)
    assert response.status_code == 422
    assert response.json() == {"detail":[{"loc":["body","weight"],"msg":"Weight must be greater than 0","type":"value_error"}]}