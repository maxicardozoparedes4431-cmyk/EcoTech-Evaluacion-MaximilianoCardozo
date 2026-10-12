class Registro:

    def __init__(self, fecha:str, horas:str, proyecto,id=None):
        self.fecha = fecha
        self.horas = horas
        self.id = id
        self.proyecto = proyecto

    def mostrarRegistros(self) -> str:
        return f"Fecha: {self.fecha}, Horas: {self.horas}, Proyecto: {self.proyecto}, ID: {self.id}"