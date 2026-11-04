
class Empleado:
    """Clase que representa a un empleado"""

    def __init__(self, nombre:str, correo:str, departamento:str, direccion:str, telefono:str, id=None):
        self.nombre = nombre
        self.correo = correo
        self.id = id
        self.departamento = departamento
        self.direccion = direccion
        self.telefono = telefono

    def mostrarDatos(self) -> str:
        return f" ID: {self.id}\n Nombre: {self.nombre}\n Correo: {self.correo}\n Departamento: {self.departamento}\n Direccion: {self.direccion}\n Teléfono: {self.telefono}"