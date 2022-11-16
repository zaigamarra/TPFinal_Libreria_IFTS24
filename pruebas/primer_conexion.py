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

mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE TIENDA")
mycursor.execute("SHOW DATABASES")

#para ver la bases
for base in mycursor:
    print(base)


print('--------FIN--------')