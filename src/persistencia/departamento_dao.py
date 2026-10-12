from persistencia.conexion import abrir_conexion, marcador_sql
from dominio.departamento import Departamento

class DepartamentoDAO:
    @staticmethod
    
    def agregarDepartamento(departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        INSERT INTO departamento (nombre, gerente)
        VALUES ({marcador}, ({marcador}))
        """
        cursor.execute(sql, (departamento.nombre, departamento.gerente))
        departamento.id = cursor.lastrowid

        conexion.commit()
        conexion.close()
        return departamento

    @staticmethod
    def buscarPorId(id_departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        SELECT id, nombre, gerente
        FROM departamento WHERE id = {marcador}
        """
        cursor.execute(sql, (id_departamento,))
        fila = cursor.fetchone()
        conexion.commit()
        conexion.close()

        if fila is None:
            return None

        return DepartamentoDAO._fila_a_departamento(fila)


    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
        "SELECT id, nombre, gerente FROM departamento"
        )
        filas = cursor.fetchall()
        conexion.close()
        departamentos = []
        for fila in filas:
            departamentos.append(
            DepartamentoDAO._fila_a_departamento(fila)
            )
        
        if fila is None:
            return None
        
        return departamentos

    @staticmethod
    def _fila_a_departamento(fila):
        return Departamento(
        id=fila[0],
        nombre=fila[1],
        gerente=fila[2]
        )

    @staticmethod
    def eliminarDepartmento(departmento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
    
        sql = f"""
        DELETE FROM departamento WHERE id = {marca}
        """
        cursor.execute(sql, (departmento.id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def actualizarDepartamento(departamento):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
    
        sql = f"""
        UPDATE departamento
        SET nombre = {marca}, gerente = {marca}
        WHERE id = {marca}
        """
    
        cursor.execute(sql, (departamento.nombre, departamento.gerente, departamento.id))
        conexion.commit()
        conexion.close()