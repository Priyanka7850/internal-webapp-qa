import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/profile")
    yield driver
    driver.quit()

def test_user_profile(driver):
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "username").send_keys("newusername")
    driver.find_element(By.NAME, "save_changes").click()
    success_message = driver.find_element(By.ID, "success_message").text
::contentReference[oaicite:28]{index=28}
 
