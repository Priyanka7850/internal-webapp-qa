from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_remove_from_cart():
    driver = webdriver.Chrome()
    driver.get("https://example.com/cart")

    driver.find_element(By.ID,
"remove-product-1").click()
    
    time.sleep(2)

    cart_empty_msg = driver.find_element(By.ID,
"cart-empty-message").text
    assert "Your cart is empty" in cart_empty_msg  # Validate cart is empty

    driver.quit()

    