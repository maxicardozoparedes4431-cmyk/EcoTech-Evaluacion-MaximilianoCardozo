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
        departamento INTEGER NOT NULL,
        direccion TEXT,
        telefono TEXT
        );
        '''

        sql_departamento = '''
        CREATE TABLE IF NOT EXISTS departamento (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        id_gerente INTEGER NOT NULL
        );
        '''

        sql_registro = '''
        CREATE TABLE IF NOT EXISTS registroTiempo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        horas INTEGER NOT NULL,
        comentario TEXT,
        proyecto INTEGER NOT NULL
        );
        '''

        sql_proyecto = '''
        CREATE TABLE IF NOT EXISTS proyecto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
        );
        '''

        sql_usuario = '''
        CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        pass_hash TEXT NOT NULL,
        id_empleado INTEGER NOT NULL
        rol TEXT NOT NULL DEFAULT 'empleado'
            check (rol IN ('admin', 'empleado'))
        );
        '''

        sql_indicador = '''
        CREATE TABLE IF NOT EXISTS indicador_dolar(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL,
        valor REAL NOT NULL,
        fuente TEXT NOT NULL
            check (fuente in ('API', 'Historial'))
        );
        '''
    else:   
        sql_empleado = '''
        CREATE TABLE IF NOT EXISTS empleado (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100) NOT NULL,
        correo VARCHAR(150) NOT NULL,
        departamento INT NOT NULL,
        direccion VARCHAR(255),
        telefono VARCHAR(20),

        CONSTRAINT fk_departamento FOREIGN KEY (departamento) REFERENCES departamento(id),
        CONSTRAINT uq_correo UNIQUE (correo),
        CONSTRAINT uq_telefono UNIQUE (telefono)
        );
        '''
        
        sql_departamento = '''
        CREATE TABLE IF NOT EXISTS departamento (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(20),
        id_gerente INT NOT NULL,

        CONSTRAINT fk_gerente FOREIGN KEY (id_gerente) REFERENCES empleado(id)
        );
        '''

        sql_registro = '''
        CREATE TABLE IF NOT EXISTS registroTiempo(
        id INT PRIMARY KEY AUTO_INCREMENT,
        fecha DATE NOT NULL,
        horas INT NOT NULL,
        comentario VARCHAR(255),
        id_proyecto INT NOT NULL,

        CONSTRAINT fk_proyecto FOREIGN KEY (id_proyecto) REFERENCES proyecto(id)
        );
        '''

        sql_proyecto = '''
        CREATE TABLE IF NOT EXISTS proyecto(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100) NOT NULL,
        descripcion VARCHAR(255)
        );
        '''

        sql_usuario = '''
        CREATE TABLE IF NOT EXISTS usuario(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(50) NOT NULL,
        pass_hash VARCHAR(255) NOT NULL,
        id_empleado INT NOT NULL,
        rol VARCHAR(20) NOT NULL DEFAULT 'empleado'
        check (rol IN ('admin', 'empleado')),
        
        CONSTRAINT fk_empleado FOREIGN KEY (id_empleado) REFERENCES empleado(id),
        CONSTRAINT uq_nombre UNIQUE (nombre));
        '''

        sql_indicador = '''
                CREATE TABLE IF NOT EXISTS indicador(
                id INT PRIMARY KEY AUTO_INCREMENT,
                fecha VARCHAR(50) NOT NULL,
                valor FLOAT NOT NULL,
                fuente VARCHAR(20) NOT NULL
                    CHECK(fuente IN('API', 'Historial'))
                );
        '''

    cursor.execute(sql_empleado)
    cursor.execute(sql_departamento)
    cursor.execute(sql_registro)
    cursor.execute(sql_proyecto)
    cursor.execute(sql_usuario)
    cursor.execute(sql_indicador)


    if obtener_motor() == "mysql":
        cursor.execute(
            "ALTER TABLE usuario MODIFY COLUMN pass_hash VARCHAR(255) NOT NULL"
        )
    else:
        columnas_usuario = {
            fila[1] for fila in cursor.execute("PRAGMA table_info(usuario)")
        }
        if "id_empleado" not in columnas_usuario:
            cursor.execute(
                "ALTER TABLE usuario ADD COLUMN id_empleado INTEGER"
            )

    conexion.commit()
    conexion.close()
