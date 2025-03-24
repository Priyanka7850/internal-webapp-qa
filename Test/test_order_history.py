from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_order_history():
    driver = webdriver.Chrome()
    driver.get("https://example.com/account")

    driver.find_element(By.ID,
"order-history").click()
    
    time.sleep(2)

    orders = driver.find_elements(By.CLASS_NAME,
"order-item")
    assert len(orders) > 0  # Validate orders exist

    driver.quit()
