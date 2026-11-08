
class Indicador:

    def __init__(self, fecha, valor, fuente, id=None):
        # Validar fecha ISO y valor numérico finito positivo.
        self.fecha = fecha
        self.valor = valor
        self.fuente = fuente
        self.id = id
        
    def mostrarDatos(self) -> str:
        return f"Fecha: {self.fecha}\nValor: {self.valor}\nFuente: {self.fuente}"