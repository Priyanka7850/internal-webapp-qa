import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/orders")
    yield driver
    driver.quit()

def test_order_cancellation(driver):
    driver.find_element(By.CLASS_NAME, "order_link").click()
    driver.find_element(By.NAME, "cancel_order").click()
    cancellation_message = driver.find_element(By.ID, "cancellation_message").text
    assert "Order cancelled successfully" in cancellation_message
