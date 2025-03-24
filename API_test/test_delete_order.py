import requests
import pytest

BASE_URL = "https://api.example.com"

def test_delete_order():
    order_id = 123  # ID of the order to delete
    
    # Send DELETE request to delete the order
    response = requests.delete(f"{BASE_URL}/orders/{order_id}")
    
    # Validate response status
    assert response.status_code == 200
    
    # Validate the response body
    response_json = response.json()
    assert response_json[
    "message"
] == "Order deleted successfully"
    print("Delete Order API response:", response_json)
