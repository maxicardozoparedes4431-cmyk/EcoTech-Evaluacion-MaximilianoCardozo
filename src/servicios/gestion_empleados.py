from persistencia.empleado_dao import EmpleadoDAO

def listar_todos():
    return EmpleadoDAO.listar()
