# CREACION DE LA BASE DE DATOS

def creacion_base():
    # importamos la libreria
    import mariadb

    # conexion del motor de base de datos
    db = mariadb.connect(
        host = "127.0.0.1",
        # port es 3306 por defecto, solo se agrega si se configuro otro puerto
        port = 3307,
        user = "root",
        password = "123456",
        autocommit = True
    )

    #chequeamos conexion
    print(db)

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE BIBLIOTECA")

    db.commit()
    cursor.close()

    print('--------------------------------------------------------')
    print('------------ Base de datos creada con exito ------------')
    print('--------------------------------------------------------')
