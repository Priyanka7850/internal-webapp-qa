import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/register")
    yield driver
    driver.quit()

def test_user_registration(driver):
    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
    driver.find_element(By.NAME, "password").send_keys("securepassword")
    driver.find_element(By.NAME, "confirm_password").send_keys("securepassword")
    driver.find_element(By.NAME, "submit").click()
    success_message = driver.find_element(By.ID, "success_message").text
    assert "Registration successful" in success_message
