from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://example.com/shop")

    driver.find_element(By.ID,
"product-1").click()  # Click on a product
    driver.find_element(By.ID,
"add-to-cart-button").click()
    
    time.sleep(2)

    cart_count = driver.find_element(By.ID,
"cart-count").text
    assert cart_count == "1"  # Validate cart updated

    driver.quit()

