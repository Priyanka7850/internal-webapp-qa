from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    driver.find_element(By.ID,
"search-box").send_keys("Laptop")
    driver.find_element(By.ID,
"search-button").click()

    time.sleep(2)

    results = driver.find_elements(By.CLASS_NAME,
"product-item")
    assert len(results) > 0  # Validate search returns results

    driver.quit()
