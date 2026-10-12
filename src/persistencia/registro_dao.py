from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.registrotiempo import Registro

class RegistroDAO:

    @staticmethod
    def RegistrarTiempo(registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        INSERT INTO registrotiempo (fecha, horas, proyecto)
        VALUES ({marcador}, ({marcador}), ({marcador}))
        """
        cursor.execute(sql, (registro.fecha, registro.horas, registro.proyecto))
        registro.id = cursor.lastrowid

        conexion.commit()
        conexion.close()
        return registro

    @staticmethod
    def buscarPorId(idProyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        SELECT id, fecha, horas, proyecto
        FROM registrotiempo WHERE id = {marcador}
        """
        cursor.execute(sql, (idProyecto,))
        fila = cursor.fetchone()
        conexion.commit()
        conexion.close()

        if fila is None:
            return None

        return RegistroDAO._fila_a_registro(fila)


    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
        "SELECT id, fecha, horas, proyecto FROM registrotiempo"
        )
        filas = cursor.fetchall()
        conexion.close()
        registros = []
        for fila in filas:
            registros.append(
            RegistroDAO._fila_a_registro(fila)
            )
        
        if fila is None:
            return None
        
        return registros

    @staticmethod
    def _fila_a_registro(fila):
        return Registro(
            id=fila[0],
            fecha=fila[1],
            horas=fila[2],
            proyecto=fila[3]
        )
    
    @staticmethod
    def eliminarProyecto(registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
    
        sql = f"""
        DELETE FROM registrotiempo WHERE id = {marca}
        """
        cursor.execute(sql, (registro.id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def actualizarProyecto(registro):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
    
        sql = f"""
        UPDATE registrotiempo
        SET fecha = {marca}, horas = {marca}, proyecto = {marca}
        WHERE id = {marca}
        """
    
        cursor.execute(sql, (registro.fecha, registro.horas, registro.proyecto, registro.id))
        conexion.commit()
        conexion.close()