class Registro:

    def __init__(self, fecha:str, horas:str,id=None):
        self.fecha = fecha
        self.horas = horas
        self.id = id

    def mostrarRegistros(self) -> str:
        return f"Fecha: {self.fecha}, Horas: {self.horas}, ID: {self.id}"