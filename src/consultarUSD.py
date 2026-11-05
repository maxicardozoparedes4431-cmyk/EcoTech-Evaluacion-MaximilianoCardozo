import requests
from time import sleep

def obtener_datos():
    respuesta = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=(3, 5),
    )
    print("Estado HTTP:", respuesta.status_code)
    respuesta.raise_for_status()
    return respuesta.json()


import math

def extraer_tasa(datos, moneda="CLP"):
    # Verificar que la respuesta sea un diccionario.
    if not isinstance(datos, dict):
        raise ValueError("Respuesta inesperada.")
    
    # Obtener la fecha de la última actualización.
    fecha = datos.get("time_last_update_utc")
    if not isinstance(fecha, str) or not fecha:
        raise ValueError("Fecha de actualización no disponible.")
    
    # Obtener el diccionario de tasas de cambio.
    rates = datos.get("rates")
    if not isinstance(rates, dict) or not rates:
        raise ValueError("No hay tasas de cambio disponibles.")
    
    # Comprobar que la moneda solicitada exista en el diccionario.
    if moneda not in rates:
        raise ValueError(f"La moneda '{moneda}' no se encuentra disponible.")
    
    # Obtener el valor para la moneda seleccionada.
    valor = rates[moneda]
    
    # Aceptar solo números finitos y mayores que cero.
    if (
        type(valor) not in (int, float)
        or not math.isfinite(valor)
        or valor <= 0
    ):
        raise ValueError("Valor del indicador inválido.")
        
    # Devolver la fecha y el valor como una tupla.
    return fecha, valor

def consultar_dolar():
    try:
        # Consultar la API y obtener los datos.
        datos = obtener_datos()
        # Extraer y validar la fecha y el valor del primer registro.
        fecha, valor = extraer_tasa(datos)
        print("Consultando la tasa de cambio...")
        # Mostrar el valor con dos decimales y su unidad.
        sleep(1)
        print(f"Dólar observado: {valor:.2f} CLP por USD")
        # Mostrar la fecha a la que corresponde el dato.
        print(f"Fecha del registro: {fecha}")
    except requests.exceptions.RequestException:
        # Controlar fallos de conexión, espera, HTTP o decodificación JSON.
        print("No pudimos consultar el servicio. Reintente.")
    except (ValueError, KeyError, TypeError):
        # Controlar valores inválidos, claves ausentes o tipos incorrectos.
        print("La respuesta no contiene un indicador válido.")


