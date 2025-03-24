import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/products")
    yield driver
    driver.quit()

def test_product_filtering(driver):
    driver.find_element(By.NAME, "category_filter").send_keys("Electronics")
    driver.find_element(By.NAME, "price_filter").send_keys("1000")
    driver.find_element(By.NAME, "apply_filters").click()
    products = driver.find_elements(By.CLASS_NAME, "product")
    assert len(products) > 0
