from persistencia.conexion import abrir_conexion, marcador_sql
from servicios.autenticacion import crear_hash

def cargar_datos():
    conexion = abrir_conexion()
    cursor = conexion.cursor()
    marcador = marcador_sql()

    departamentos = [
        ("Recursos Humanos", 1),
        ("Ventas", 2),
        ("Marketing", 3),
        ("Finanzas", 4),
        ("Tecnología de la Información", 5),]

    empleados = [
        ("Sofía Martínez", "sofia.martinez@ecotech.test", 1,
        "Av. Central 101", "11-4000-1001"),
        ("Diego Fernández", "diego.fernandez@ecotech.test", 2,
        "Calle Los Olivos 202", "11-4000-1002"),
        ("Valentina Rojas", "valentina.rojas@ecotech.test", 3,
        "Av. del Trabajo 303", "11-4000-1003"),
        ("Mateo González", "mateo.gonzalez@ecotech.test", 4,
        "Calle San Martín 404", "11-4000-1004"),
        ("Camila Herrera", "camila.herrera@ecotech.test", 5,
        "Av. Innovación 505", "11-4000-1005"),
        ("Nicolás Castro", "nicolas.castro@ecotech.test", 2,
        "Calle Belgrano 606", "11-4000-1006"),
        ("Martina Silva", "martina.silva@ecotech.test", 3,
        "Av. Independencia 707", "11-4000-1007"),
        ("Tomás Acosta", "tomas.acosta@ecotech.test", 4,
        "Calle Mitre 808", "11-4000-1008"),
        ("Lucía Benítez", "lucia.benitez@ecotech.test", 1,
        "Av. Libertad 909", "11-4000-1009"),
        ("Joaquín Molina", "joaquin.molina@ecotech.test", 5,
        "Calle Rivadavia 110", "11-4000-1010"),
        ("Agustina Navarro", "agustina.navarro@ecotech.test", 2,
        "Av. San Juan 211", "11-4000-1011"),
        ("Franco Vega", "franco.vega@ecotech.test", 3,
        "Calle Moreno 312", "11-4000-1012"),
        ("Emilia Paredes", "emilia.paredes@ecotech.test", 4,
        "Av. Corrientes 413", "11-4000-1013"),
        ("Benjamín Sosa", "benjamin.sosa@ecotech.test", 5,
        "Calle Tucumán 514", "11-4000-1014"),
        ("Renata Méndez", "renata.mendez@ecotech.test", 1,
        "Av. Santa Fe 615", "11-4000-1015"),
        ("Santiago Duarte", "santiago.duarte@ecotech.test", 2,
        "Calle Viamonte 716", "11-4000-1016"),
        ("Pilar Campos", "pilar.campos@ecotech.test", 3,
        "Av. Pueyrredón 817", "11-4000-1017"),
        ("Facundo Ibarra", "facundo.ibarra@ecotech.test", 4,
        "Calle Junín 918", "11-4000-1018"),
        ("Clara Peralta", "clara.peralta@ecotech.test", 5,
        "Av. Boedo 219", "11-4000-1019"),
        ("Ramiro Fuentes", "ramiro.fuentes@ecotech.test", 1,
        "Calle Lavalle 320", "11-4000-1020"),
    ]

    sql = f"""
    INSERT INTO departamento (nombre, id_gerente)
    SELECT {marcador}, {marcador}
    WHERE NOT EXISTS (
        SELECT 1
        FROM departamento
        WHERE nombre = {marcador} AND id_gerente = {marcador}
    )"""

    parametros = [
        (*departamento, *departamento)
        for departamento in departamentos
    ]
    cursor.executemany(sql, parametros)

    sql_empleado = f"""
    INSERT INTO empleado (nombre, correo, departamento, direccion, telefono)
    SELECT {marcador}, {marcador}, {marcador}, {marcador}, {marcador}
    WHERE NOT EXISTS (
        SELECT 1
        FROM empleado
        WHERE correo = {marcador}
    )"""

    parametros_empleados = [
        (*empleado, empleado[1])
        for empleado in empleados
    ]
    cursor.executemany(sql_empleado, parametros_empleados)

    usuarios = [
        ("admin_sys", "admin123", 1),
    ]

    sql_usuario = f"""
    INSERT INTO usuario (nombre, pass_hash, id_empleado)
    SELECT {marcador}, {marcador}, {marcador}
    WHERE NOT EXISTS (
        SELECT 1
        FROM usuario
        WHERE nombre = {marcador}
    )"""

    parametros_usuarios = [
        (nombre, crear_hash(clave), empleado_id, nombre)
        for nombre, clave, empleado_id in usuarios
    ]
    cursor.executemany(sql_usuario, parametros_usuarios)
    conexion.commit()
    conexion.close()
