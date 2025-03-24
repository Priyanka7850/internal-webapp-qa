import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/products")
    yield driver
    driver.quit()

def test_product_reviews(driver):
    driver.find_element(By.CLASS_NAME, "product_link").click()
    driver.find_element(By.NAME, "review_text").send_keys("Great product!")
    driver.find_element(By.NAME, "submit_review").click()
    reviews = driver.find_elements(By.CLASS_NAME, "review")
    assert len(reviews) > 0
