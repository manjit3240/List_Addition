import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_numbers_success1():
    response = client.post("/api/add", json={"batchid":"12ndn", "payload": [[1, 2], [3,4], [4,5]]})
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['batchid'] == "12ndn"
    assert json_response['response'] == [3,7,9]

def test_add_numbers_success2():
    response = client.post("/api/add", json={"batchid":"12ndn", "payload": [[1, 2], [3], [4,5]]})
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['batchid'] == "12ndn"
    assert json_response['response'] == [3,3,9]

def test_add_numbers_with_non_integer():
    response = client.post("/api/add", json={"batchid":"12ndn", "payload": [[1, 2], [3, "three"]]})
    assert response.status_code == 422
    json_response = response.json()
    assert json_response["detail"][0]["msg"] == "Input should be a valid integer, unable to parse string as an integer"

def test_add_numbers_with_empty_list():
    response = client.post("/api/add", json={"batchid":"12ndn", "payload": []})
    json_response = response.json()
    assert response.status_code == 200
    assert json_response['batchid'] == "12ndn"
    assert json_response['response'] == []
