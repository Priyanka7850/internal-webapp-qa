import requests
import pytest

BASE_URL = "https://api.example.com"

def test_update_order():
    # Test data
    order_id = 123
    update_data = {
    "quantity": 3
}
    
    # Send PUT request to update order
    response = requests.put(f"{BASE_URL}/orders/{order_id}", json=update_data)
    
    # Validate response status
    assert response.status_code == 200
    
    # Validate the response body
    response_json = response.json()
    assert response_json[
    "message"
] == "Order updated successfully"
    print("Update Order API response:", response_json)
