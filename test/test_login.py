from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")

    driver.find_element(By.ID,
"username").send_keys("testuser")
    driver.find_element(By.ID,
"password").send_keys("password123")
    driver.find_element(By.ID,
"login-button").click()

    time.sleep(2)
    assert "Dashboard" in driver.title  # Validate login success

    driver.quit()
