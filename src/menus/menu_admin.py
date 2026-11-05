import subprocess

from time import sleep
from consultarUSD import consultar_dolar
from servicios.gestion_empleados import listar_todos

from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.proyecto_dao import ProyectoDAO
from persistencia.registro_dao import RegistroDAO

from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.registrotiempo import Registro

def cls():
    subprocess.run("cls", shell=True)
    sleep(0.5)

def menu_inicio():
        print("---- ECHO-TECH ----")

        print("0: Perfil")
        print("1: Empleados")
        print("2: Departamentos")
        print("3: Proyectos")
        print("4: Registros de Tiempos")
        print("5: Consultar USD")
        print("6: Cerrar Sesión")

def menu_empleado():

    print("---- EMPLEADOS ----")

    print("1: Registrar Empleado")
    print("2: Buscar Empleado")
    print("3: Actualizar Empleado")
    print("4: Eliminar Empleado")
    print("5: Volver")

def menu_departamento():

    print("---- DEPARTAMENTOS ----")

    print("1: Agregar Departamento")
    print("2: Buscar Departamento")
    print("3: Actualizar Departamento")
    print("4: Eliminar Departamento")
    print("5: Volver")

def menu_proyecto():

    print("---- PROYECTO ----")

    print("1: Añadir Proyecto")
    print("2: Buscar Proyecto")
    print("3: Actualizar Proyecto")
    print("4: Eliminar Proyecto")
    print("5: Volver")

def menu_registros():

    print("---- REGISTROS ----")

    print("1: Agregar Registro")
    print("2: Buscar Registro")
    print("3: Actualizar Registro")
    print("4: Eliminar Registro")
    print("5: Volver")


def menu_administrador(usuario):

    def actualizar_empleado():
        cls()
        empleado = EmpleadoDAO.buscarPorId(usuario.empleado_id)
        
        if empleado:
            nombre = input("Ingrese el nuevo nombre completo del empleado (deje en blanco para no cambiar): ")
            correo = input("Ingrese el nuevo correo del empleado (deje en blanco para no cambiar): ")
            direccion = input("Ingrese la nueva dirección del empleado (deje en blanco para no cambiar): ")
            telefono = input("Ingrese el nuevo teléfono del empleado (deje en blanco para no cambiar): ")

            if nombre:
                empleado.nombre = nombre
            if correo:
                empleado.correo = correo
            if direccion:
                empleado.direccion = direccion
            if telefono:
                empleado.telefono = telefono

            EmpleadoDAO.actualizarEmpleado_comoEmpleado(empleado)
            print(f"Empleado actualizado con éxito.\n {empleado.mostrarDatos()}")
            input("Presione Enter para continuar...")

    while True: # desastre absoluto
            cls()
            menu_inicio()
            opcion = input("Seleccione una opción: ")
    
            try:
                if opcion.isdigit():
                    int(opcion)
                    print(opcion)
    
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
    
            if opcion == "1": # menu de empleados
                while True:
                    cls()
                    menu_empleado()
    
                    opcion1 = input("Seleccione una opción: ")
    
                    try:
                        if opcion1.isdigit():
                            int(opcion1)
                            print(opcion1)
    
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
    
                    if opcion1 == "1": # registro de empleado
                        cls()
                        while True:
                            nombre = input("Ingrese el nombre completo del empleado: ")
                            if not nombre:
                                print("Por favor, ingrese un nombre válido.")
                            else:
                                break
    
                        while True:
                            correo = input("Ingrese el correo del empleado: ")
                            if not correo:
                                print("Por favor, ingrese un correo válido.")
                            else:
                                break
    
                        while True:
                            departamento = input("Ingrese la id del departamento para el empleado: ")
    
                            try:
                                if departamento.isdigit():
                                    int(departamento)
                                    print(departamento)
                                    break
                            except ValueError:
                                print("Por favor, ingrese un número válido del departamento.")
                                continue
    
                        while True:
                            direccion = input("Ingrese la dirección del empleado: ")
                            if not direccion:
                                print("Por favor, ingrese una dirección válida.")
                            else:
                                break
            
                        while True:
                            telefono = input("Ingrese el teléfono del empleado: ")
                            if not telefono:
                                print("Por favor, ingrese un teléfono válido.")
                            else:
                                break
    
                        empleado = Empleado(nombre, correo, departamento, direccion, telefono)
    
                        try:
                            empleado_registrado = EmpleadoDAO.registrarEmpleado(empleado)
                            print(f"Empleado registrado con éxito: {empleado_registrado.mostrarDatos()}")
                        except Exception:
                            print("Error al registrar el empleado. Por favor, intente nuevamente.")
                        
                        input("Presione Enter para continuar...")
    
                    elif opcion1 == "2": # busqueda de empleado, ya sea por ID o listados
                        cls()
    
                        while True:
                            cls()
                            print("--- EMPLEADOS ---")
                            print("1. Buscar por ID")
                            print("2. Listar todos los empleados")
                            print("3. Volver")
                            opcion_busqueda = input("Seleccione una opción: ")
    
                            try:
                                if opcion_busqueda.isdigit():
                                    int(opcion_busqueda)
                                    print(opcion_busqueda)
    
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                            if opcion_busqueda == "1": 
                                id_empleado = input("Ingrese el ID del empleado: ")
                                empleado_encontrado = EmpleadoDAO.buscarPorId(id_empleado)
                                try:
                                    print(f"Empleado encontrado:\n{empleado_encontrado.mostrarDatos()}")
                                    input("Presione Enter para continuar...")
                                    break
                                except Exception as e:
                                    print(f"Error al mostrar datos del empleado: {e}")
                                    input("Presione Enter para continuar...")
                                    continue
    
                            elif opcion_busqueda == "2":
                                lista = listar_todos()
                                if lista:
                                    for emp in lista:
                                        print(emp.mostrarDatos())
                                else:
                                    print("No hay empleados registrados.")
                                input("Presione Enter para continuar...")
                                
                            elif opcion_busqueda == "3":
                                break
                            else:
                                print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")
            
                    elif opcion1 == "3": # actualizar empleado
                        cls()
                        while True:
                            try:
                                idEmpleado = input("Ingrese el ID del empleado a actualizar: ")
                                if not idEmpleado.isdigit():
                                    print("Por favor, ingrese un número válido.")
                                    continue
                                break
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                        empleado = EmpleadoDAO.buscarPorId(idEmpleado)
                        
                        if empleado:
                            print(f"Empleado encontrado:\n{empleado.mostrarDatos()}")
                            nombre = input("Ingrese el nuevo nombre completo del empleado (deje en blanco para no cambiar): ")
                            correo = input("Ingrese el nuevo correo del empleado (deje en blanco para no cambiar): ")
                            while True:
                                try:
                                    departamento = input("Ingrese la id del departamento para el empleado (deje en blanco para no cambiar): ")
                                    if not departamento:
                                        break
                                    break
                                except ValueError:
                                    print("Por favor, ingrese un valor válido.")
                                    continue
                            direccion = input("Ingrese la nueva dirección del empleado (deje en blanco para no cambiar): ")
                            telefono = input("Ingrese el nuevo teléfono del empleado (deje en blanco para no cambiar): ")
    
                            if nombre:
                                empleado.nombre = nombre
                            if correo:
                                empleado.correo = correo
                            if departamento:
                                empleado.departamento = departamento
                            if direccion:
                                empleado.direccion = direccion
                            if telefono:
                                empleado.telefono = telefono
    
                            EmpleadoDAO.actualizarEmpleado(empleado)
                            print(f"Empleado con ID {idEmpleado} actualizado con éxito.\n {empleado.mostrarDatos()}")
                            input("Presione Enter para continuar...")
    
                    elif opcion1 == "4":
                        cls()
                        while True:
                            try:
                                idEmpleado = input("Ingrese el ID del empleado a eliminar: ")
                                if not idEmpleado.isdigit():
                                    print("Por favor, ingrese un número válido.")
                                    continue
                                break
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                        empleado = EmpleadoDAO.buscarPorId(idEmpleado)
    
                        if empleado:
                            EmpleadoDAO.eliminarEmpleado(empleado)
                            print(f"Empleado con ID {idEmpleado} eliminado con éxito.")
                        else:
                            print(f"No se encontró un empleado con ID {idEmpleado}.")
                        
                        input("Presione Enter para continuar...")
    
                    elif opcion1 == "5":
                        break
    
                    else:
                        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
                        sleep(1)
    
            if opcion == "2":
                while True:
                    cls()
                    menu_departamento()
                    opcion2 = input("Seleccione una opción: ")
    
                    try:
                        if opcion2.isdigit():
                            int(opcion2)
                            print(opcion2)
                
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
    
                    if opcion2 == "1": # agregar departamento
                        cls()
                        while True:
                            nombre = input("Ingrese el nombre para el departamento: ")
                            if not nombre:
                                print("Por favor, ingrese un nombre válido.")
                            else:
                                break
    
                        while True:
                            gerente = input("Ingrese la id del gerente del departamento: ")
    
                            try:
                                if gerente.isdigit():
                                    int(gerente)
                                    print(gerente)
                                    break
                            except ValueError:
                                print("Por favor, ingrese una id válida de un empleado.")
    
                        departamento = Departamento(nombre, gerente)
    
                        try:
                            departamentoAgregado = DepartamentoDAO.agregarDepartamento(departamento)
                            print(f"Departamento registrado con éxito: {departamentoAgregado.mostrarDepartamento()}")
                            input("Presione Enter para continuar...")
                            break
                        except Exception as e:
                            print(f"Error al registrar el departamento. Por favor, intente nuevamente. Error: {e}")
                            input("Presione Enter para continuar...")
                            continue
    
                    elif opcion2 == "2": # buscar departamento, ya sea por ID o listados
                        cls()
                        print("---- BUSCAR DEPARTAMENTO ----")
                        print("1: Buscar por ID")
                        print("2: Listar todos los departamentos")
                        print("3: Volver")
                        while True:
                            opcionBusqueda = input("Seleccione una opción: ")
    
                            try:
                                if opcionBusqueda.isdigit():
                                    int(opcionBusqueda)
                                    print(opcionBusqueda)
                            
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
                            
                            if opcionBusqueda == "1": 
                                
                                while True:
                                    idDepa = input("Ingrese el ID del departamento: ")
                                    
                                    try:
                                        if idDepa.isdigit():
                                            int(idDepa)
                                            print(idDepa)
                                            break
                                    except ValueError:
                                        print("Por favor, ingrese una ID válida.")
                                        continue
    
                                try:
                                    departamento = DepartamentoDAO.buscarPorId(idDepa)
                                except Exception as e:
                                    print(f"Error al buscar el departamento: {e}")
                                    continue
    
                                try:
                                    print(f"Departamento encontrado:\n{departamento.mostrarDepartamento()}")
                                    input("Presione Enter para continuar...")
                                    break
                                except Exception as e:
                                    print(f"Error al mostrar datos del departamento: {e}")
                                    input("Presione Enter para continuar...")
                                    continue
    
                            elif opcionBusqueda == "2":
                                try:
                                    departamentos = DepartamentoDAO.listar()
                                except Exception as e:
                                    print(f"Error al listar departamentos: {e}")
                                    break
                                if departamentos:
                                    print("Lista de departamentos:")
                                    for dep in departamentos:
                                        print(dep.mostrarDepartamento())
                                else:
                                    print("No hay departamentos.")
    
                                input("Presione Enter para continuar...")
                                break
    
                            elif opcionBusqueda == "3":
                                break
                            else:
                                print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")
    
                    elif opcion2 == "3": # actualizar departamento, ya sea nombre o su gerente
                        cls()
                        while True:
                            idDepa = input("Ingrese el ID del departamento a actualizar: ")
    
                            try:
                                if idDepa.isdigit():
                                    int(idDepa)
                                    print(idDepa)
                                break
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                        try:
                            departamento = DepartamentoDAO.buscarPorId(idDepa)
                        except Exception as e:
                            print(f"Error al buscar el departamento: {e}")
                            continue
    
                        if departamento:
                            print(f"Departamento encontrado:\n{departamento.mostrarDepartamento()}")
                            nombre = input("Ingrese el nuevo nombre del departamento (deje en blanco para no cambiar): ")
                            while True:
    
                                try:
                                    gerente = input("Ingrese la id del nuevo gerente del departamento (deje en blanco para no cambiar): ")
                                    if not gerente:
                                        break
                                    if not gerente.isdigit():
                                        print("Por favor, ingrese un número válido.")
                                        continue
                                    break
                                except ValueError:
                                    print("Por favor, ingrese un número válido.")
                                    continue
    
                            if nombre:
                                departamento.nombre = nombre
                            if gerente:
                                departamento.gerente = gerente
    
                            try:
                                DepartamentoDAO.actualizarDepartamento(departamento)
                                print(f"Departamento con ID {idDepa} actualizado con éxito.")
                            except Exception as e:
                                print(f"Error al actualizar el departamento: {e}")
                            
                            input("Presione Enter para continuar...")
    
                    elif opcion2 == "4": # eliminar departamento
                        while True:
                            while True:
                                idDepa = input("Ingrese el ID del departamento a eliminar: ")
    
                                try:
                                    if idDepa.isdigit():
                                        int(idDepa)
                                        print(idDepa)
                                        break
                                except ValueError:
                                    print("Por favor, ingrese un número válido.")
                                    continue
    
                            try:
                                departamento = DepartamentoDAO.buscarPorId(idDepa)
                                break
                            except Exception as e:
                                print(f"Error al buscar el departamento: {e}")
    
                        if departamento:
                            try:
                                DepartamentoDAO.eliminarDepartmento(departamento)
                                print(f"Departamento con ID {idDepa} eliminado con éxito.")
                            except Exception as e:
                                print(f"Error al eliminar el departamento: {e}")
                        else:
                            print(f"No se encontró un departamento con ID {idDepa}.")
    
                        input("Presione Enter para continuar...")
    
                    elif opcion2 == "5": # salir del menu de departamentos
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
                        sleep(1)
            
            if opcion == "3":
                while True:
                    cls()
                    menu_proyecto()
    
                    opcion3 = input("Seleccione una opción: ")
    
                    try:
                        if opcion3.isdigit():
                            int(opcion3)
                            print(opcion3)
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
    
                    if opcion3 == "1":
                        cls()
                        while True:
                            nombre = input("Ingrese el nombre para el proyecto: ")
                            if not nombre:
                                print("Por favor, ingrese un nombre válido.")
                            else:
                                break
    
                        while True:
                            descripcion = input("Ingrese la descripción para el proyecto: ")
                            if not descripcion:
                                print("Por favor, ingrese una descripción válida.")
                            else:
                                break
    
                        proyecto = Proyecto(nombre, descripcion)
    
                        try:
                            proyectoAgregado = ProyectoDAO.agregarProyecto(proyecto)
                            print(f"Proyecto registrado con éxito: {proyectoAgregado.mostrarProyecto()}")
                            input("Presione Enter para continuar...")
                            break
                        except Exception as e:
                            print(f"Error al registrar el proyecto. Por favor, intente nuevamente. Error: {e}")
                            input("Presione Enter para continuar...")
                            
                    elif opcion3 == "2":
                        cls()
                        print("---- BUSCAR PROYECTO ----")
                        print("1: Buscar por ID")
                        print("2: Listar todos los proyectos")
                        print("3: Volver")
                        while True:
                            opcionBusqueda = input("Seleccione una opción: ")
    
                            try:
                                if opcionBusqueda.isdigit():
                                    int(opcionBusqueda)
                                    print(opcionBusqueda)
                            
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
                            
                            if opcionBusqueda == "1": 
                                while True:
                                    idProyecto = input("Ingrese el ID del proyecto: ")
    
                                    try:
                                        if idProyecto.isdigit():
                                            int(idProyecto)
                                            print(idProyecto)
                                            break
                                    except ValueError:
                                        print("Por favor, ingrese un número válido.")
                                        continue
    
                                try:
                                    proyecto = ProyectoDAO.buscarPorId(idProyecto)
                                except Exception as e:
                                    print(f"Error al encontrar el proyecto: {e}")
                                    continue
    
                                try:
                                    print(f"Proyecto encontrado:\n{proyecto.mostrarProyecto()}")
                                    input("Presione Enter para continuar...")
                                    break
                                except Exception as e:
                                    print(f"Error al mostrar datos del proyecto: {e}")
                                    input("Presione Enter para continuar...")
                                    break
                                    
                            elif opcionBusqueda == "2":
                                try:
                                    proyectos = ProyectoDAO.listar()
                                except Exception as e:
                                    print(f"Error al listar proyectos: {e}")
                                    break
                                if proyectos:
                                    print("Lista de proyectos:")
                                    for proy in proyectos:
                                        print(proy.mostrarProyecto())
                                else:
                                    print("No hay proyectos.")
    
                                input("Presione Enter para continuar...")
                                break
    
                            elif opcionBusqueda == "3":
                                break
                            else:
                                print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")               
                    
                    elif opcion3 == "3":
                        cls()
                        idProyecto = input("Ingrese el ID del proyecto a actualizar: ")
    
                        try:
                            if idProyecto.isdigit():
                                int(idProyecto)
                                print(idProyecto)
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                            continue
    
                        try:
                            proyecto = ProyectoDAO.buscarPorId(idProyecto)
                        except Exception as e:
                            print(f"Error al buscar el proyecto: {e}")
                            continue
    
                        if proyecto:
                            print(f"Proyecto encontrado:\n{proyecto.mostrarProyecto()}")
                            nombre = input("Ingrese el nuevo nombre del proyecto (deje en blanco para no cambiar): ")
                            descripcion = input("Ingrese la nueva descripcion del proyecto (deje en blanco para no cambiar): ")
    
                            if nombre:
                                proyecto.nombre = nombre
                            if descripcion:
                                proyecto.descripcion = descripcion
    
                            try:
                                ProyectoDAO.actualizarProyecto(proyecto)
                                print(f"Proyecto con ID {idProyecto} actualizado con éxito.")
                            except Exception as e:
                                print(f"Error al actualizar el proyecto: {e}")
                            
                            input("Presione Enter para continuar...")
    
                    elif opcion3 == "4":
                        while True:
                            idProyecto = input("Ingrese el ID del proyecto a eliminar: ")
    
                            try:
                                if idProyecto.isdigit():
                                    int(idProyecto)
                                    print(idProyecto)
                                    break
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                        try:
                            proyecto = ProyectoDAO.buscarPorId(idProyecto)
                        except Exception as e:
                            print(f"Error al buscar el proyecto: {e}")
                            continue
    
                        if proyecto:
                            try:
                                ProyectoDAO.eliminarProyecto(proyecto)
                                print(f"Proyecto con ID {idProyecto} eliminado con éxito.")
                            except Exception as e:
                                print(f"Error al eliminar el proyecto: {e}")
    
                        input("Presione Enter para continuar...")
    
                    elif opcion3 == "5":
                        break
                    else:
                        print("Opcion invalida, por favor seleccione una opcion del 1 al 5")
                        sleep(1)
                
            if opcion == "4":
                while True:
                    cls()
                    menu_registros()
                    
                    opcion4 = input("Seleccione una opción: ")
    
                    try:
                        if opcion4.isdigit():
                            int(opcion4)
                            print(opcion4)
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue
    
                    if opcion4 == "1":
                        cls()
                        while True:
                            horas = input("Ingrese la cantidad de horas trabajadas: ")
                            if not horas:
                                print("Por favor, ingrese una cantidad de horas válida.")
                            else:
                                break
    
                        while True:
                            fecha = input("Ingrese la fecha (Año/Mes/Día): ")
                            if not fecha:
                                print("Por favor, ingrese una fecha válida.")
                            else:
                                break
    
                        while True:
                            proyecto = input("Ingrese la id del proyecto asociado a este registro: ")
    
                            try:
                                if proyecto.isdigit():
                                    int(proyecto)
                                    print(proyecto)
                                    break
                            except ValueError:
                                print("Por favor, ingrese una id válida de un proyecto.")
    
                        registro = Registro(fecha, horas, proyecto)
    
                        try:
                            registroAgregado = RegistroDAO.RegistrarTiempo(registro)
                            print(f"Registro de tiempo agregado:\n{registroAgregado.mostrarRegistros()}")
                            input("Presione Enter para continuar...")
                        except Exception as e:
                            print(f"Error al agregar el registro de tiempo. Por favor, intente nuevamente. Error: {e}")
                            input("Presione Enter para continuar...")
                    
                    elif opcion4 == "2":
                        cls()
    
                        while True:
                            cls()
                            print("--- BUSCAR REGISTROS ---")
                            print("1. Buscar por ID")
                            print("2. Listar todos los registros")
                            print("3. Salir")
                            opcion_busqueda = input("Seleccione una opción: ")
    
                            try:
                                if opcion_busqueda.isdigit():
                                    int(opcion_busqueda)
                                    print(opcion_busqueda)
    
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                            if opcion_busqueda == "1": 
                                idRegistro = input("Ingrese el ID del registro: ")
                                registro = RegistroDAO.buscarPorId(idRegistro)
                                try:
                                    print(f"Registro encontrado:\n{registro.mostrarRegistros()}")
                                    input("Presione Enter para continuar...")
                                    break
                                except Exception as e:
                                    print(f"Error al mostrar datos del registro: {e}")
                                    continue
    
                            elif opcion_busqueda == "2":
                                registros = RegistroDAO.listar()
                                if registros:
                                    print("Lista de registros:")
                                    for reg in registros:
                                        print(reg.mostrarRegistros())
                                else:
                                    print("No hay registros registrados.")
                                input("Presione Enter para continuar...")
                                break
                            elif opcion_busqueda == "3":
                                break
                            else:
                                print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")
    
                    elif opcion4 == "3":
                        cls()
                        while True:
                            idRegistro = input("Ingrese el ID del registro a actualizar: ")
    
                            try:
                                if idRegistro.isdigit():
                                    int(idRegistro)
                                    print(idRegistro)
                            except ValueError:
                                print("Por favor, ingrese un número válido.")
                                continue
    
                            try:
                                registro = RegistroDAO.buscarPorId(idRegistro)
                                break
                            except Exception as e:
                                print(f"Error al buscar el registro: {e}")
                                continue
    
                        if registro:
                            print(f"Registro encontrado:\n{registro.mostrarRegistros()}")
                            horas = input("Ingrese las nuevas horas (deje en blanco para no cambiar): ")
                            fecha = input("Ingrese la nueva fecha (deje en blanco para no cambiar) [Año-Mes-Día]: ")
                            while True:
                                proyecto = input("Ingrese el nuevo proyecto (deje en blanco para no cambiar): ")
                                try:
                                    if proyecto.isdigit():
                                        int(proyecto)
                                        print(proyecto)
                                        break
                                except ValueError:
                                    print("Por favor, ingrese una id válida de un proyecto.")
                                    continue
                            if horas:
                                registro.horas = horas
                            if fecha:
                                registro.fecha = fecha
                            if proyecto:
                                registro.proyecto = proyecto
    
                            try:
                                RegistroDAO.actualizarProyecto(registro)
                                print(f"Registro con ID {idRegistro} actualizado con éxito.")
                            except Exception as e:
                                print(f"Error al actualizar el registro: {e}")
                            
                            input("Presione Enter para continuar...")
                        
                    elif opcion4 == "4":
                        cls()
                        idRegistro = input("Ingrese el ID del registro a eliminar: ")
    
                        try:
                            if idRegistro.isdigit():
                                int(idRegistro)
                                print(idRegistro)
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                            continue
    
                        try:
                            registro = RegistroDAO.buscarPorId(idRegistro)
                        except Exception as e:
                            print(f"Error al buscar el registro: {e}")
                            continue
    
                        if registro:
                            try:
                                RegistroDAO.eliminarProyecto(registro)
                                print(f"Registro con ID {idRegistro} eliminado con éxito.")
                            except Exception as e:
                                print(f"Error al eliminar el registro: {e}")
    
                        input("Presione Enter para continuar...")
    
                    elif opcion4 == "5":
                        break
                    else:
                        print("Opcion invalida, por favor seleccione una opcion del 1 al 5")
                        sleep(1)

            if opcion == "0":
                    while True:
                        cls()
                        print("---- PERFIL ----")
                        datosPerfil = EmpleadoDAO.buscarPorId(usuario.empleado_id)
                        print(datosPerfil.mostrarDatos())
                        print("\n1: Actualizar Perfil")
                        print("2: Volver")

                        opcionPerfil = input("Seleccione una opción: ")

                        try:  
                            if opcionPerfil.isdigit():
                                int(opcionPerfil)
                                print(opcionPerfil)

                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                            continue

                        if opcionPerfil == "1":
                            actualizar_empleado()
                        elif opcionPerfil == "2":
                            break
                        else:
                            print("Opción inválida. Por favor, seleccione una opción del 1 al 2.")

            elif opcion == "5":
                cls()
                consultar_dolar()
                input("Presione Enter para continuar...")
    
            elif opcion == "6":
                print("Cerrando Sesión...")
                break
                
            else:
                print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

