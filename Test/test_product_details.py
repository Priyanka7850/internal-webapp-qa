import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/products")
    yield driver
    driver.quit()

def test_product_details_view(driver):
    driver.find_element(By.CLASS_NAME, "product_link").click()
    product_name = driver.find_element(By.ID, "product_name").text
    product_description = driver.find_element(By.ID, "product_description").text
    assert product_name != ""
    assert product_description != ""
