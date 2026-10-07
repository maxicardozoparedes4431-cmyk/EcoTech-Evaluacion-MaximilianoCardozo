from persistencia.conexion import (abrir_conexion, obtener_motor)


def crear_tablas():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    if obtener_motor() == "sqlite":
        sql_empleado = '''
        CREATE TABLE IF NOT EXISTS empleado (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT NOT NULL,
        departamento TEXT,
        direccion TEXT,
        telefono TEXT
        )
        '''

        sql_departamento = '''
        CREATE TABLE IF NOT EXISTS departamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
        )
        '''

        sql_registro = '''
        CREATE TABLE IF NOT EXISTS registroTiempo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        horas INTEGER NOT NULL
        )
        '''

        sql_proyecto = '''
        CREATE TABLE IF NOT EXISTS proyecto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
        )
        '''
    else:
        sql_empleado = '''
        CREATE TABLE IF NOT EXISTS empleado (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100) NOT NULL,
        correo VARCHAR(150) NOT NULL,
        departamento VARCHAR(100),
        direccion VARCHAR(255),
        telefono VARCHAR(20)
        )
        '''
        
        sql_departamento = '''
        CREATE TABLE IF NOT EXISTS departamento (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100)
        )
        '''

        sql_registro = '''
        CREATE TABLE IF NOT EXISTS registroTiempo(
        id INT PRIMARY KEY AUTO_INCREMENT,
        fecha DATE NOT NULL,
        horas INT NOT NULL
        )
        '''

        sql_proyecto = '''
        CREATE TABLE IF NOT EXISTS proyecto(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100) NOT NULL,
        descripcion VARCHAR(255)
        )
        '''
    cursor.execute(sql_empleado)
    cursor.execute(sql_departamento)
    cursor.execute(sql_registro)
    cursor.execute(sql_proyecto)
    conexion.commit()
    conexion.close()
