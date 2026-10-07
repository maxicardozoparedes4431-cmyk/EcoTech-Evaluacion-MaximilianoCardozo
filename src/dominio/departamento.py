# src/dominio/departamento.py
from dominio.empleado import Empleado

class Departamento:
    """Clase que representa a un departamento"""

    def __init__(self, nombre:str):
        self.nombre = nombre,
        self._empleados: list[Empleado] = []

    def mostrarDepartamento(self) -> str:
        return f"Departamento: {self.nombre}"