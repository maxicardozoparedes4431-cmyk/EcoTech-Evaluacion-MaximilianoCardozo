from getpass import getpass
from entradas import pedir_dato
from servicios.autenticacion import registrar_usuario, autenticar
from dominio.usuario import Usuario

def solicitar_registro():
        try:
                empleado_id = pedir_dato("ID del empleado: ", int)
                nombre = pedir_dato("Nuevo usuario: ", Usuario.normalizar_usuario)
                clave = pedir_dato("Contraseña: ", Usuario.validar_clave, getpass)
                
                if clave != getpass("Repita la contraseña: "):
                        print("Las contraseñas no coinciden. Vuelva al registro.")
                        return None
                
                rol = pedir_dato("Rol: ", Usuario.validar_rol)
                usuario_id = registrar_usuario(empleado_id, nombre, clave, rol)
        except (TypeError, ValueError) as error:
                print(error)
                return None
        input(f"Cuenta creada correctamente. ID: {usuario_id}")
        return usuario_id

def solicitar_login():
        nombre = input("Usuario: ")
        clave = getpass("Contraseña: ")

        try:
                usuario = autenticar(nombre, clave)
                
        except (TypeError, ValueError) as error:
                input(f"No se pudo validar el acceso. {error}")
                return None
        
        if usuario is None:
                input("Usuario o contraseña incorrectos.")
        else:
                input("Sesión iniciada correctamente, Presione Enter para continuar.")
                return usuario
