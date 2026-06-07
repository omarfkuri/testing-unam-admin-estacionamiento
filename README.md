# Testing – EasyPark
Este modulo existe para ejecutar las pruebas automatizadas para la aplicación web **EasyPark**

## Tecnologías utilizadas
- Python
- Selenium
- PyTest

---
## Instalación

Clonar repo
```
git clone https://github.com/omarfkuri/testing-unam-admin-estacionamiento.git
```

---
## Ejecutar sistema
Correr pruebas
```
./scripts/run.sh
```

## Uso del sistema
Este sistema permite la observación de la ejecución de las pruebas automatizada. Simplemente
ejecute el comando en terminal y observe los resultados de las pruebas.

---
## Funcionalidades principales
- Probar carga
- Probar login
- Probar cerrar sesión

---
## Evidencias
Reportes encontrables en la carpeta `evidencias`.

---
## Estructura del proyecto
```
├── evidencias
│		 └── test_fallido.png
├── scripts
│		 └── run.sh
└── test
    ├── ejercicio_0_busqueda.py
    ├── ejercicio_1_carga.py
    ├── ejercicio_2_login.py
    ├── ejercicio_3_login_incorrecto.py
    ├── ejercicio_4_pytest.py
    └── ejercicio_5_cerrar_sesion.py
```
---
## Notas adicionales
Debe ser ejecutado en una computadora con acceso a navegadores modernos.
