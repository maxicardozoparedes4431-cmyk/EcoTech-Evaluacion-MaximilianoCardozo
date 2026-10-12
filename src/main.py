from persistencia.crear_bd import crear_tablas
from time import sleep

from menus.menu_inicio import menu as menu_inicio
from menus.menu_empleado import menu as menu_empleado
from menus.menu_departamento import menu as menu_departamento
from menus.menu_proyecto import menu as menu_proyecto
from menus.menu_registros import menu as menu_registros


from dominio.empleado import Empleado
from dominio.departamento import Departamento
from dominio.proyecto import Proyecto
from dominio.registrotiempo import Registro

from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.proyecto_dao import ProyectoDAO
from persistencia.registro_dao import RegistroDAO

import subprocess
def cls():
    subprocess.run("cls", shell=True)

crear_tablas()


while True:
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
                    if nombre == "" or nombre.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un nombre válido.")
                    else:
                        break

                while True:
                    correo = input("Ingrese el correo del empleado: ")
                    if correo == "" or correo.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un correo válido.")
                    else:
                        break

                while True:
                    departamento = input("Ingrese el departamento del empleado: ")
                    if departamento == "" or departamento.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un departamento válido.")
                    else:
                        break

                while True:
                    direccion = input("Ingrese la dirección del empleado: ")
                    if direccion == "" or direccion.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese una dirección válida.")
                    else:
                        break
    
                while True:
                    telefono = input("Ingrese el teléfono del empleado: ")
                    if telefono == "" or telefono.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un teléfono válido.")
                    else:
                        break

                empleado = Empleado(nombre, correo, departamento, direccion, telefono)

                try:
                    empleado_registrado = EmpleadoDAO.registrarEmpleado(empleado)
                    print(f"Empleado registrado con éxito: {empleado_registrado.mostrarDatos()}")
                    break
                except Exception:
                    print("Error al registrar el empleado. Por favor, intente nuevamente.")
                    continue

            elif opcion1 == "2": # busqueda de empleado, ya sea por ID o listados
                cls()

                while True:
                    cls()
                    print("--- EMPLEADOS ---")
                    print("1. Buscar por ID")
                    print("2. Listar todos los empleados")
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
                        id_empleado = input("Ingrese el ID del empleado: ")
                        empleado_encontrado = EmpleadoDAO.buscarPorId(id_empleado)
                        try:
                            print(f"Empleado encontrado: {empleado_encontrado.mostrarDatos()}")
                            input("Presione Enter para continuar...")
                            break
                        except Exception as e:
                            print(f"Error al mostrar datos del empleado: {e}")
                            continue
                    elif opcion_busqueda == "2":
                        empleados = EmpleadoDAO.listar()
                        if empleados:
                            print("Lista de empleados:")
                            for emp in empleados:
                                print(emp.mostrarDatos())
                        else:
                            print("No hay empleados registrados.")
                        input("Presione Enter para continuar...")
                        break
                    elif opcion_busqueda == "3":
                        break
                    else:
                        print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")
    
            elif opcion1 == "3": # actualizar empleado
                cls()
                idEmpleado = input("Ingrese el ID del empleado a actualizar: ")
                empleado = EmpleadoDAO.buscarPorId(idEmpleado)
                if empleado:
                    print(f"Empleado encontrado: {empleado.mostrarDatos()}")
                    nombre = input("Ingrese el nuevo nombre completo del empleado (deje en blanco para no cambiar): ")
                    correo = input("Ingrese el nuevo correo del empleado (deje en blanco para no cambiar): ")
                    departamento = input("Ingrese el nuevo departamento del empleado (deje en blanco para no cambiar): ")
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
                    print(f"Empleado con ID {idEmpleado} actualizado con éxito.")

            elif opcion1 == "4":
                cls()
                idEmpleado = input("Ingrese el ID del empleado a eliminar: ")
                empleado = EmpleadoDAO.buscarPorId(idEmpleado)
                if empleado:
                    EmpleadoDAO.eliminarEmpleado(empleado)
                    print(f"Empleado con ID {idEmpleado} eliminado con éxito.")
                else:
                    print(f"No se encontró un empleado con ID {idEmpleado}.")

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
                    if nombre == "" or nombre.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un nombre válido.")
                    else:
                        break

                while True:
                    gerente = input("Ingrese el nombre del gerente del departamento: ")
                    if gerente == "" or gerente.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un nombre válido para el gerente.")
                    else:
                        break

                departamento = Departamento(nombre, gerente)

                try:
                    departamentoAgregado = DepartamentoDAO.agregarDepartamento(departamento)
                    print(f"Departamento registrado con éxito: {departamentoAgregado.mostrarDepartamento()}")
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
                print("3: Salir")
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
                        idDepa = input("Ingrese el ID del departamento: ")

                        try:
                            departamento = DepartamentoDAO.buscarPorId(idDepa)
                        except Exception as e:
                            print(f"Error al buscar el departamento: {e}")
                            continue

                        try:
                            print(f"Departamento encontrado: {departamento.mostrarDepartamento()}")
                            input("Presione Enter para continuar...")
                            break
                        except Exception as e:
                            print(f"Error al mostrar datos del departamento: {e}")
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
                idDepa = input("Ingrese el ID del departamento a actualizar: ")

                try:
                    if idDepa.isdigit():
                        int(idDepa)
                        print(idDepa)
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue

                try:
                    departamento = DepartamentoDAO.buscarPorId(idDepa)
                except Exception as e:
                    print(f"Error al buscar el departamento: {e}")
                    continue

                if departamento:
                    print(f"Departamento encontrado: {departamento.mostrarDepartamento()}")
                    nombre = input("Ingrese el nuevo nombre del departamento (deje en blanco para no cambiar): ")
                    gerente = input("Ingrese el nuevo gerente del departamento (deje en blanco para no cambiar): ")

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
                    idDepa = input("Ingrese el ID del departamento a eliminar: ")

                    try:
                        if idDepa.isdigit():
                            int(idDepa)
                            print(idDepa)
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
                    if nombre == "" or nombre.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese un nombre válido.")
                    else:
                        break

                while True:
                    descripcion = input("Ingrese la descripción para el proyecto: ")
                    if descripcion == "" or descripcion.upper() in ["SELECT", "INSERT", "UPDATE", "DELETE"]:
                        print("Por favor, ingrese una descripción válida.")
                    else:
                        break

                proyecto = Proyecto(nombre, descripcion)

                try:
                    proyectoAgregado = ProyectoDAO.agregarProyecto(proyecto)
                    print(f"Proyecto registrado con éxito: {proyectoAgregado.mostrarProyecto()}")
                    break
                except Exception as e:
                    print(f"Error al registrar el proyecto. Por favor, intente nuevamente. Error: {e}")
                    
                input("Presione Enter para continuar...")

            elif opcion3 == "2":
                cls()
                print("---- BUSCAR PROYECTO ----")
                print("1: Buscar por ID")
                print("2: Listar todos los proyectos")
                print("3: Salir")
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
                        idProyecto = input("Ingrese el ID del proyecto: ")

                        try:
                            proyecto = ProyectoDAO.buscarPorId(idProyecto)
                        except Exception as e:
                            print(f"Error al buscar el proyecto: {e}")
                            continue

                        try:
                            print(f"Proyecto encontrado: {proyecto.mostrarProyecto()}")
                            input("Presione Enter para continuar...")
                            break
                        except Exception as e:
                            print(f"Error al mostrar datos del proyecto: {e}")
                            
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
                    print(f"Proyecto encontrado: {proyecto.mostrarProyecto()}")
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
                idProyecto = input("Ingrese el ID del proyecto a eliminar: ")

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
                horas = input("Ingrese la cantidad de horas trabajadas: ")
                fecha = input("Ingrese la fecha (Año/Mes/Día): ")
                proyecto = input("Ingrese el nombre del proyecto asociado a este registro: ")

                registro = Registro(fecha, horas, proyecto)

                try:
                    registroAgregado = RegistroDAO.RegistrarTiempo(registro)
                    print(f"Registro de tiempo agregado con éxito: {registroAgregado.mostrarRegistros()}")
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
                            print(f"Registro encontrado: {registro.mostrarRegistros()}")
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
                except Exception as e:
                    print(f"Error al buscar el registro: {e}")
                    continue

                if registro:
                    print(f"Registro encontrado: {registro.mostrarRegistros()}")
                    horas = input("Ingrese las nuevas horas (deje en blanco para no cambiar): ")
                    fecha = input("Ingrese la nueva fecha (deje en blanco para no cambiar) [Año-Mes-Día]: ")
                    proyecto = input("Ingrese el nuevo proyecto (deje en blanco para no cambiar): ")
                    
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


    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")


