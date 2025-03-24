from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_checkout():
    driver = webdriver.Chrome()
    driver.get("https://example.com/shop")

    driver.find_element(By.ID,
"add-to-cart-button").click()
    time.sleep(2)

    driver.find_element(By.ID,
"cart-icon").click()
    time.sleep(2)

    driver.find_element(By.ID,
"checkout-button").click()
    time.sleep(2)

    driver.find_element(By.ID,
"card-number").send_keys("4111111111111111")
    driver.find_element(By.ID,
"expiry-date").send_keys("12/25")
    driver.find_element(By.ID,
"cvv").send_keys("123")

    driver.find_element(By.ID,
"place-order-button").click()
    time.sleep(2)

    success_message = driver.find_element(By.ID,
"order-success").text
    assert "Order placed successfully" in success_message

    driver.quit()
