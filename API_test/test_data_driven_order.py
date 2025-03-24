import requests
import pytest

BASE_URL = "https://api.example.com"

@pytest.mark.parametrize(
    "product_id, quantity, expected_status",
    [(1, 2, 201), (2, 5, 201), (3, 0, 400)]  # Example test cases with expected status codes
)
def test_place_order(product_id, quantity, expected_status):
    order_data = {"product_id": product_id, "quantity": quantity}
    
    # Send POST request to place the order
    response = requests.post(f"{BASE_URL}/orders", json=order_data)
    
    # Validate the response status
    assert response.status_code == expected_status, f"Expected status {expected_status} but got {response.status_code}"
    
    # If the order is successfully placed (status 201), check the response message
    if expected_status == 201:
        try:
            response_json = response.json()
            assert "message" in response_json, "'message' field is missing in the response"
            assert response_json["message"] == "Order placed successfully", f"Unexpected message: {response_json['message']}"
        except ValueError:
            # If the response is not JSON, print the raw response for debugging
            print("Error: Response is not in valid JSON format.")
            print("Response content:", response.text)
            assert False, "Response is not in valid JSON format"
    elif expected_status == 400:
        try:
            # For failed orders (status 400), ensure there's an error message
            response_json = response.json()
            assert "error" in response_json, "'error' field is missing in the response"
            assert response_json["error"] == "Invalid quantity", f"Unexpected error message: {response_json['error']}"
        except ValueError:
            print("Error: Response is not in valid JSON format.")
            print("Response content:", response.text)
            assert False, "Response is not in valid JSON format"
    
    # Print the response for debugging purposes
    print(f"Order Response: {
