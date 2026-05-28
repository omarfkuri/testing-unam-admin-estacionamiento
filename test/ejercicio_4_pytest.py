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

def test_carga_pagina(driver):
    driver.get(URL)
    assert driver.title == "Inicio"

def test_login_correcto(driver):
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
    time.sleep(5)

    try:
        assert "principal" in driver.current_url
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise

def test_login_incorrecto(driver):
    driver.get(URL)
    workerIDInput = driver.find_element(
    By.CSS_SELECTOR, "input[name='workerID']")

    workerIDInput.send_keys("412909034")
    time.sleep(1)

    passwordInput = driver.find_element(
        By.CSS_SELECTOR, "input[name='password']")

    passwordInput.send_keys("987654321")
    time.sleep(1)

    submitButton = driver.find_element(
        By.CSS_SELECTOR, "button")
    submitButton.click()
    time.sleep(5)

    mensaje = driver.find_element(
        By.CSS_SELECTOR, "#mensaje"
    )

    try:
        assert "El usuario o contraseña son incorrectos." == mensaje.text
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise