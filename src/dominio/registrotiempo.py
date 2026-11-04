class Registro:

    def __init__(self, fecha:str, horas:str, proyecto,id=None):
        self.fecha = fecha
        self.horas = horas
        self.id = id
        self.proyecto = proyecto

    def mostrarRegistros(self) -> str:
        return f"Fecha: {self.fecha}\n Horas: {self.horas}\n Proyecto: {self.proyecto}\n ID: {self.id}"