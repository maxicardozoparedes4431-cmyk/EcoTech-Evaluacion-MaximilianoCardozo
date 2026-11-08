import subprocess

from time import sleep

from consultarUSD import consultarDolar
from consultarUSD import mostrarHistorial

from dominio.proyecto import Proyecto
from dominio.registrotiempo import Registro

from persistencia.proyecto_dao import ProyectoDAO
from persistencia.registro_dao import RegistroDAO
from persistencia.usuario_dao import UsuarioDAO
from persistencia.empleado_dao import EmpleadoDAO

def cls():
    subprocess.run("cls", shell=True)
    sleep(0.5)

def menu_inicio():
        print("---- ECHO-TECH ----")

        print("1: Perfil")
        print("2: Proyectos")
        print("3: Registros de Tiempos")
        print("4: Consultar USD")
        print("5: Cerrar Sesión")

def menu_proyecto():
    print("---- PROYECTO ----")

    print("1: Añadir Proyecto")
    print("2: Buscar Proyecto")
    print("3: Actualizar Proyecto")
    print("4: Volver")

def menu_registros():
    print("---- REGISTROS ----")

    print("1: Agregar Registro")
    print("2: Buscar Registro")
    print("3: Actualizar Registro")
    print("4: Volver")

def menu_empleado(usuario):

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
            
            if opcion == "1":
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

            if opcion == "2":
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
                
            if opcion == "3":
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

            elif opcion == "4":
                    while True:
                        cls()
                        print("--- API: CONSULTA DEL DÓLAR ----")
                        print("1: Consultar Dólar Observado")
                        print("2: Ver el historial de Dólar Observado")
                        print("3: Volver")

                        opcionAPI = input("Seleccione una opción: ")

                        try:
                            if opcionAPI.isdigit():
                                int(opcionAPI)
                                print(opcionAPI)
                        except ValueError:
                            print("Por favor, ingrese un número válido.")
                            continue

                        if opcionAPI == "1":
                            cls()
                            print("Consultando la tasa de cambio del Dólar Observado...")
                            sleep(1)
                            consultarDolar()
                            input("Presione Enter para continuar...")

                        if opcionAPI == "2":
                            cls()
                            print("Mostrando el historial de Dólar Observado...")
                            sleep(1)
                            mostrarHistorial()
                            input("Presione Enter para continuar...")

                        if opcionAPI == "3":
                            break

                        else:
                            print("Opción inválida. Por favor, seleccione una opción del 1 al 3.")

            elif opcion == "5":
                print("Cerrando Sesión...")
                sleep(1)
                break

                
            else:
                print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")
