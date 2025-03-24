import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://your-ecommerce-site.com/products")
    yield driver
    driver.quit()

def test_add_to_wishlist(driver):
    driver.find_element(By.CLASS_NAME, "product_link").click()
    driver.find_element(By.NAME, "add_to_wishlist").click()
    wishlist_count = driver.find_element(By.ID, "wishlist_count").text
    assert int(wishlist_count) > 0
