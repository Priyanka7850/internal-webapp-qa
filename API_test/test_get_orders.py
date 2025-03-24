import requests
import pytest

BASE_URL = "https://api.example.com"

def test_get_orders():
    # Send GET request to retrieve orders
    response = requests.get(f"{BASE_URL}/orders")
    
    # Validate response status
    assert response.status_code == 200
    
    # Validate the response body
    response_json = response.json()
    assert isinstance(response_json, list)
    assert "orders" in response_json[
    0
]
    assert "id" in response_json[
    0
][
    "orders"
][
    0
]
    print("Get Orders API response:", response_json)
