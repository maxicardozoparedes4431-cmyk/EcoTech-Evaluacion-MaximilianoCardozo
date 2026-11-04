from dominio.usuario import Usuario
from persistencia.conexion import abrir_conexion, marcador_sql

class UsuarioDAO:

    @staticmethod
    def registrarUsuario(usuario):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        INSERT INTO usuario (nombre, pass_hash, id_empleado)
        VALUES ({marcador}, {marcador}, {marcador})
        """
        cursor.execute(sql, (usuario.nombre_usuario, usuario.password_hash, usuario.empleado_id))
        usuario.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return usuario

    @staticmethod
    def _fila_a_usuario(fila):
        return Usuario(
            id=fila[0],
            nombre_usuario=fila[1],
            password_hash=fila[2],
            empleado_id=fila[3]
        )

    @staticmethod
    def buscar_por_nombre(nombre_usuario):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        
        sql =f"""
        SELECT id, nombre, pass_hash, id_empleado
        FROM usuario WHERE nombre = {marca}
        """

        cursor.execute(sql, (nombre_usuario,))
        fila = cursor.fetchone()
        conexion.commit()
        conexion.close()

        if fila is None:
            return None

        return UsuarioDAO._fila_a_usuario(fila)


    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
        "SELECT id, nombre from usuario"
        )
        filas = cursor.fetchall()
        conexion.close()
        usuarios = []
        for fila in filas:
            usuarios.append(
            UsuarioDAO._fila_a_usuario(fila)
            )
        
        if fila is None:
            return None
        
        return usuarios

    @staticmethod
    def eliminarUsuario(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()

        sql = f"""
        DELETE FROM usuario WHERE id = {marca}
        """
        cursor.execute(sql, (empleado.id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def actualizarUsuario(usuario):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()

        sql = f"""
        UPDATE usuario
        SET nombre = {marca}, pass_hash = {marca}, id_empleado = {marca}
        WHERE id = {marca}
        """

        cursor.execute(sql, (usuario.nombre_usuario, usuario.password_hash, usuario.empleado_id, usuario.id))
        conexion.commit()
        conexion.close()

