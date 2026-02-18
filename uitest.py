from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

def test_login():
    # Use CHROMEDRIVER_PATH env var if set, otherwise fall back to Selenium Manager
    driver_path = os.environ.get("CHROMEDRIVER_PATH")
    if driver_path and os.path.exists(driver_path):
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)
    else:
        driver = webdriver.Chrome()

    driver.get('http://127.0.0.1:5500/index.html')

    driver.find_element(By.NAME, 'username').send_keys('Aayush')
    driver.find_element(By.NAME, 'password').send_keys('pass123')
    driver.find_element(By.ID, 'login-button').click()

    message = driver.find_element(By.ID, 'welcome').text
    assert 'Welcome Test User' in message
    driver.quit()