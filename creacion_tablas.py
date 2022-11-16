# CREACION DE LAS TABLAS usuarios, libros y prestamos

def creacion_tablas():
    # importamos la libreria
    import mariadb

    #conexion a la base de datos
    base = mariadb.connect(
        host = "127.0.0.1",
        # port es 3306 por defecto, solo se agrega si se configuro otro puerto
        port = 3307,
        user = "root",
        password = "123456",
        database = "BIBLIOTECA"
    )

    #chequeamos conexion
    print(base)

    usuarios = '''
        CREATE TABLE usuarios (
        dni VARCHAR(15) PRIMARY KEY NOT NULL,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        telefono VARCHAR(50) NOT NULL,
        direccion VARCHAR(200) NOT NULL,
        estado VARCHAR(10) NOT NULL,
        con_prestamo BOOLEAN NOT NULL DEFAULT 0
        );
        '''

    libros = '''
        CREATE TABLE libros (
        isbn VARCHAR(20) PRIMARY KEY NOT NULL,
        titulo VARCHAR(200),
        autor VARCHAR(150),
        editorial VARCHAR(50),
        anio_edicion INT,
        baja BOOLEAN NOT NULL DEFAULT 0,
        prestado BOOLEAN NOT NULL DEFAULT 0
        );
        '''

    prestamos = '''
        CREATE TABLE prestamos (
            id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
            dni VARCHAR(15) NOT NULL,
            isbn VARCHAR(20) NOT NULL,
            fh_prestamo DATE NOT NULL,
            fh_devolucion DATE,
            estado VARCHAR(10) NOT NULL,
            FOREIGN KEY(dni) REFERENCES usuarios(dni),
            FOREIGN KEY(isbn) REFERENCES libros(isbn)
        ) AUTO_INCREMENT = 1;
        '''

    tablas = [usuarios, libros, prestamos]

    cursor = base.cursor()

    for tabla in tablas:
        cursor.execute(tabla)

    base.commit()
    cursor.close()

    print('--------------------------------------------------------')
    print('--------------- Tablas creadas con exito ---------------')
    print('--------------------------------------------------------')