from selenium import webdriver

URL = "https://omarfkuri.github.io/unam-admin-estacionamiento/"

# A – Preparar
driver = webdriver.Chrome()

# A – Ejecutar
driver.get(URL)

# A – Verificar
assert "Inicio" in driver.title
print("El sistema cargó correctamente")
print("Título:", driver.title)

# Limpiar
driver.quit()