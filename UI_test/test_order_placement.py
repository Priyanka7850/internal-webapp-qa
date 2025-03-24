import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/cart")
    yield driver
    driver.quit()

def test_order_placement(driver):
    driver.find_element(By.NAME, "checkout").click()
    driver.find_element(By.NAME, "payment_method").send_keys("Credit Card")
    driver.find_element(By.NAME, "place_order").click()
    confirmation_message = driver.find_element(By.ID, "confirmation_message").text
    assert "Order placed successfully" in confirmation_message
