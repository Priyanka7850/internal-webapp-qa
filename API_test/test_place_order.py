import requests
import pytest

BASE_URL = "https://api.example.com"

def test_place_order():
    # Order data to be sent in the POST request
    order_data = {
        "product_id": 1,
        "quantity": 2,
        "address": "123 Street"
    }

    # Send POST request to place an order
    response = requests.post(f"{BASE_URL}/orders", json=order_data)

    # Validate response status
    assert response.status_code == 201, f"Expected status 201 but got {response.status_code}"

    # Validate the response body
    response_json = response.json()
    
    # Ensure the response contains the 'message' key and it has the expected value
    assert "message" in response_json, "'message' key is missing in the response"
    assert response_json["message"] == "Order placed successfully", f"Unexpected message: {response_json['message']}"

    # Print the response for debugging
    print("Place Order API response:", response_json)
