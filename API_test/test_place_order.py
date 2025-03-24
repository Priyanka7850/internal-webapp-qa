import requests
import pytest

BASE_URL = "https://api.example.com"

def test_place_order():
    order_data = {
    "product_id": 1,
    "quantity": 2,
    "address": "123 Street"
}
    
    # Send POST request to place an order
    response = requests.post(f"{BASE_URL}/orders", json=order_data)
    
    # Validate response status
    assert response.status_code == 201
    
    # Validate the response body
    response_json = response.json()
    assert response_json[
    "message"
] == "Order placed successfully"
    print("Place Order API response:", response_json)
