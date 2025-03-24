import requests
import pytest

BASE_URL = "https://api.example.com"

def test_get_orders():
    # Send GET request to retrieve orders
    response = requests.get(f"{BASE_URL}/orders")
    
    # Validate response status
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    
    # Validate the response body
    response_json = response.json()
    
    # Check if the response is a list and contains 'orders' key
    assert isinstance(response_json, list), "Response should be a list"
    
    # Ensure the first order has the expected structure
    if len(response_json) > 0:
        assert "id" in response_json[0], "'id' key is missing in the order"
        assert "product_name" in response_json[0], "'product_name' key is missing in the order"
        print("Get Orders API response:", response_json)
    else:
        print("No orders returned.")
