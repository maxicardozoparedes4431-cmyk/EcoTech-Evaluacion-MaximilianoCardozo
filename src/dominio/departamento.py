# src/dominio/departamento.py

class Departamento:
    """Clase que representa a un departamento"""

    def __init__(self, nombre:str, gerente:str, id:int = None):
        self.nombre = nombre
        self.gerente = gerente
        self.id = id

    def mostrarDepartamento(self) -> str:
        return f"Departamento: {self.nombre}, Gerente: {self.gerente}, ID: {self.id}"