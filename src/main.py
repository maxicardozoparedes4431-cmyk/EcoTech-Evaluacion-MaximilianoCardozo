from persistencia.crear_bd import crear_tablas

from menus.menu_inicio import menu as menu_inicio
from menus.menu_empleado import menu as menu_empleado

from dominio.empleado import Empleado
from dominio.departamento import Departamento

from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO

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

    if opcion == "1":
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

            if opcion1 == "1":
                cls()
                nombre = input("Ingrese el nombre completo del empleado: ")
                correo = input("Ingrese el correo del empleado: ")
                departamento = input("Ingrese el departamento del empleado: ")
                direccion = input("Ingrese la dirección del empleado: ")
                telefono = input("Ingrese el teléfono del empleado: ")

                empleado = Empleado(nombre, correo, departamento, direccion, telefono)

                try:
                    empleado_registrado = EmpleadoDAO.registrarEmpleado(empleado)
                    print(f"Empleado registrado con éxito: {empleado_registrado.mostrarDatos()}")
                    break
                except Exception:
                    print("Error al registrar el empleado. Por favor, intente nuevamente.")
                    continue
            elif opcion1 == "2":
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
                        empleado_encontrado = EmpleadoDAO.buscar_por_id(id_empleado)
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

            elif opcion1 == "4":
                cls()
                id_empleado = input("Ingrese el ID del empleado a eliminar: ")
                empleado_a_eliminar = EmpleadoDAO.buscar_por_id(id_empleado)
                if empleado_a_eliminar:
                    EmpleadoDAO.eliminar(empleado_a_eliminar)
                    print(f"Empleado con ID {id_empleado} eliminado con éxito.")
                else:
                    print(f"No se encontró un empleado con ID {id_empleado}.")

            elif opcion1 == "5":
                break

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")


