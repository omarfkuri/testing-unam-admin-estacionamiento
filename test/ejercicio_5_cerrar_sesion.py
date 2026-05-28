import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL = "https://omarfkuri.github.io/unam-admin-estacionamiento/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    yield d
    d.quit()

def test_cerrar_sesion(driver):
    driver.get(URL)
    workerIDInput = driver.find_element(
    By.CSS_SELECTOR, "input[name='workerID']")

    workerIDInput.send_keys("412909034")
    time.sleep(1)

    passwordInput = driver.find_element(
        By.CSS_SELECTOR, "input[name='password']")

    passwordInput.send_keys("12345678")
    time.sleep(1)

    submitButton = driver.find_element(
        By.CSS_SELECTOR, "button")
    submitButton.click()
    time.sleep(10)

    cerrarSessButton = driver.find_element(
        By.CSS_SELECTOR, "#cerrarSesionBtn")
    cerrarSessButton.click()

    try:
        assert "Inicio" in driver.title
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise