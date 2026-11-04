class Proyecto:

    def __init__(self, nombre:str, descripcion:str,id=None):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id = id

    def mostrarProyecto(self) -> str:
        return f"Nombre: {self.nombre}\n Descripción: {self.descripcion}\n ID: {self.id}"