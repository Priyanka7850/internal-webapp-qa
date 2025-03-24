import requests
import pytest

BASE_URL = "https://api.example.com"

@pytest.mark.parametrize(
    "product_id, quantity, expected_status",
[(1,
    2,
    201), (2,
    5,
    201), (3,
    0,
    400)
]  # Example test cases with expected status codes
)
def test_place_order(product_id, quantity, expected_status):
    order_data = {
    "product_id": product_id,
    "quantity": quantity
}
    
    response = requests.post(f"{BASE_URL}/orders", json=order_data)
    
    # Validate response status
    assert response.status_code == expected_status
    
    if expected_status == 201:
        response_json = response.json()
        assert response_json[
    "message"
] == "Order placed successfully"
    print(f"Tested product_id={product_id}, quantity={quantity} with status {expected_status}")
