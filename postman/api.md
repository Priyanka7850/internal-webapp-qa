# API Testing with Postman

## Overview

This documentation covers the API testing for the E-Commerce system, using Postman for testing the endpoints related to orders. The collection includes **Get Orders**, **Place Order**, **Update Order**, and **Delete Order** APIs.

## Endpoints

### 1. **Get Orders (GET /orders)**
- **Description**: Retrieves all orders.
- **Expected Status**: `200 OK`
- **Response**: A list of orders.
- **Test Validation**:
  - The response should return a status code of `200`.
  - The response body should be a list of orders.

### 2. **Place Order (POST /orders)**
- **Description**: Places a new order.
- **Expected Status**: `201 Created`
- **Request Body**:
  ```json
  {
    "product_id": 1,
    "quantity": 2,
    "address": "123 Street"
  }
Test Validation:

The response status code should be 201.

The response should contain a message saying "Order placed successfully."

3. Update Order (PUT /orders/{id})
Description: Updates an existing order.

Expected Status: 200 OK

Request Body:

json
Copy
Edit
{
  "quantity": 3
}
Test Validation:

The response status code should be 200.

The response should contain a message saying "Order updated successfully."

4. Delete Order (DELETE /orders/{id})
Description: Deletes an order.

Expected Status: 200 OK

Test Validation:

The response status code should be 200.

The response should contain a message saying "Order deleted successfully."

Steps to Use the Postman Collection
1. Import the Collection:
Open Postman.

Click on the Import button in the top-left corner.

Choose File and select the ecommerce-api-collection.json file.

Click on Import to add the collection to Postman.

2. Create Environment Variables (Optional):
To parameterize order_id in URLs, create a Postman Environment.

Create a variable order_id and use it in the request URLs like {{order_id}}.

3. Run the Collection in Postman:
Select the collection from your Postman.

Click on the Run button to run all the requests in the collection.

Check the results and ensure all tests pass.

Running the Collection with Newman (Command Line)
If you want to automate this process and run the collection from the command line, use Newman.

1. Install Newman:
Newman is the command-line tool for Postman collections. Install it using npm:

bash
Copy
Edit
npm install -g newman
2. Run the Collection:
Run the Postman collection using the following command:

bash
Copy
Edit
newman run ecommerce-api-collection.json --reporters cli,html --reporter-html-export reports/api_report.html
This command will run all the API tests defined in the collection. The results will be displayed in the command line and saved as an HTML report in the reports/ folder.

Sample Test Results
Here is an example output of running the tests with Newman:

bash
Copy
Edit
=========================== test session starts ============================
collected 4 items

api_tests/test_get_orders.py .. [100%]
api_tests/test_place_order.py .. [100%]
api_tests/test_update_order.py .. [100%]
api_tests/test_delete_order.py .. [100%]

=========================== All tests passed! =============================
Conclusion
By following this documentation, you can easily test the APIs for the E-Commerce system using Postman and Newman. The integration of API tests into your CI/CD pipeline will ensure continuous testing of your API endpoints.
