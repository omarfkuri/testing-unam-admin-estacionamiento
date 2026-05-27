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

echo "Todas las pruebas fueron exitosas."
