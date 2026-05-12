# Se importa la excepcion personalizada de clientes
from excepciones import ClienteError

# Se importa la funcion para guardar el log del error
from logger import registrar_log

# Bloque try para probar la excepcion
try:

    # Se lanza el error manualmente
    raise ClienteError("Error de prueba en clientes")


# Se captura el error
except ClienteError as error:

    # Se guarda el error en el archivo logs.txt
    registrar_log(f"ERROR: {error}")