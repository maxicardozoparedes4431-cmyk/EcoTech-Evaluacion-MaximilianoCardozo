from dominio.indicador_dolar import Indicador
from persistencia.conexion import abrir_conexion, marcador_sql

class IndicadorDAO:

    @staticmethod
    def registrarIndicador(indicador):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        sql = f"""
        INSERT INTO indicador (fecha, valor, fuente)
        VALUES ({marcador}, {marcador}, {marcador})
        """
        cursor.execute(sql, (indicador.fecha, indicador.valor, indicador.fuente))
        indicador.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return indicador

    @staticmethod
    def _fila_a_indicador(fila):
        return Indicador(
            id=fila[0],
            fecha=fila[1],
            valor=fila[2],
            fuente=fila[3]
        )

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
        "SELECT id, fecha, valor, fuente from indicador"
        )
        filas = cursor.fetchall()
        conexion.close()
        historial = []
        for fila in filas:
            historial.append(
            IndicadorDAO._fila_a_indicador(fila)
            )
        
        if fila is None:
            return None
        
        return historial

    @staticmethod
    def obtener_ultimo():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, fecha, valor, fuente "
            "FROM indicador ORDER BY id DESC LIMIT 1"
        )
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
            return None

        return IndicadorDAO._fila_a_indicador(fila)
