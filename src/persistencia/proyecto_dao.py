from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.proyecto import Proyecto

class ProyectoDAO:

    @staticmethod
    def agregarProyecto(proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        INSERT INTO proyecto (nombre, descripcion)
        VALUES ({marcador}, ({marcador}))
        """
        cursor.execute(sql, (proyecto.nombre, proyecto.descripcion))
        proyecto.id = cursor.lastrowid

        conexion.commit()
        conexion.close()
        return proyecto

    @staticmethod
    def buscarPorId(idProyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        SELECT id, nombre, descripcion
        FROM proyecto WHERE id = {marcador}
        """
        cursor.execute(sql, (idProyecto,))
        fila = cursor.fetchone()
        conexion.commit()
        conexion.close()

        if fila is None:
            return None

        return ProyectoDAO._fila_a_proyecto(fila)


    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
        "SELECT id, nombre, descripcion FROM proyecto"
        )
        filas = cursor.fetchall()
        conexion.close()
        proyectos = []
        for fila in filas:
            proyectos.append(
            ProyectoDAO._fila_a_proyecto(fila)
            )
        
        if fila is None:
            return None
        
        return proyectos

    @staticmethod
    def _fila_a_proyecto(fila):
        return Proyecto(
            id=fila[0],
            nombre=fila[1],
            descripcion=fila[2]
        )
    
    @staticmethod
    def eliminarProyecto(proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
    
        sql = f"""
        DELETE FROM proyecto WHERE id = {marca}
        """
        cursor.execute(sql, (proyecto.id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def actualizarProyecto(proyecto):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
    
        sql = f"""
        UPDATE proyecto
        SET nombre = {marca}, descripcion = {marca}
        WHERE id = {marca}
        """
    
        cursor.execute(sql, (proyecto.nombre, proyecto.descripcion, proyecto.id))
        conexion.commit()
        conexion.close()