from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

URL = "https://omarfkuri.github.io/unam-admin-estacionamiento/"

# A – Preparar
driver = webdriver.Chrome()
driver.get(URL)
time.sleep(2)

# A – Ejecutar
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

# A – Verificar
assert "El usuario o contraseña son incorrectos." == mensaje.text
print("El login fue exitoso")

driver.save_screenshot("evidencias/test_fallido.png")

# Limpiar

logoutButton = driver.find_element(
	By.CSS_SELECTOR, "button")
logoutButton.click()
time.sleep(2)

driver.quit()