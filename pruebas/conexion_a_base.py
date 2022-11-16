#importamos la libreria
import mariadb

#conecto el motor de base de datos
mydb = mariadb.connect(
    host = "127.0.0.1",
    port = 3307,
    user = "root",
    password = "123456",
    autocommit = True
)

#chequeamos conexion
print(mydb)

#conecto a la base que quiero
base_tienda = mariadb.connect(
    host = "127.0.0.1",
    port = 3307,
    user = "root",
    password = "123456",
    database = "TIENDA"
)

#chequeamos conexion
print(base_tienda)

cursor = base_tienda.cursor()
cursor.execute(
    "CREATE TABLE Cliente(dni INT PRIMARY KEY, nombre VARCHAR(100), direccion VARCHAR(200), telefono VARCHAR(50))"
)

cursor.close()