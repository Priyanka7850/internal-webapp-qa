import requests
import pytest

BASE_URL = "https://api.example.com"

def test_delete_order():
    order_id = 123  # ID of the order to delete
    
    # Send DELETE request to delete the order
    response = requests.delete(f"{BASE_URL}/orders/{order_id}")
    
    # Validate response status
    assert response.status_code == 200, f"Expected status 200 but got {response.status_code}"
    
    # Validate the response body
    try:
        response_json = response.json()
        # Ensure the response contains the 'message' key and it has the expected value
        assert "message" in response_json, "'message' key is missing in the response"
        assert response_json["message"] == "Order deleted successfully", f"Unexpected message: {response_json['message']}"
    except ValueError:
        # If the response is not a valid JSON, print the raw response for debugging
        print("Error: Response is not in valid JSON format.")
        print("Response content:", response.text)
        assert False, "Response is not in valid JSON format"

    # Print the response for debugging
    print("Delete Order API response:", response_json)
