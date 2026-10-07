
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
        return f" ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, Departamento: {self.departamento}, Direccion: {self.direccion}, Teléfono: {self.telefono}"