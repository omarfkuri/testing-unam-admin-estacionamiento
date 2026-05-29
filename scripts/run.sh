set -e

echo "Inicio de ejecución de pruebas."
echo ""

echo "Ejecutando prueba #1"
python3 test/ejercicio_0_busqueda.py
echo "Prueba exitosa"
echo ""

echo "Ejecutando prueba #2"
python3 test/ejercicio_1_carga.py
echo "Prueba exitosa"
echo ""

echo "Ejecutando prueba #3"
python3 test/ejercicio_2_login.py
echo "Prueba exitosa"
echo ""

echo "Ejecutando prueba #4"
python3 test/ejercicio_3_login_incorrecto.py
echo "Prueba exitosa"
echo ""

echo "Ejecutando pruebas PYTEST"
python3 -m pytest test/ejercicio_4_pytest.py
python3 -m pytest test/ejercicio_5_cerrar_sesion.py
echo "Prueba exitosa"
echo ""

echo "Todas las pruebas fueron exitosas."
