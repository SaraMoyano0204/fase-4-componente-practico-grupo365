# Importamos la libreria para traer la fecha en la que se guarda el mensaje :)
from datetime import datetime

# Funcion para guardar eventos y errores en el archivo logs.txt
def registrar_log(mensaje):

    # Obtener fecha y hora actual
    fecha = datetime.now()

    # Abrir el archivo logs.txt en modo agregar
    archivo = open("logs.txt", "a", encoding="utf-8")

    # Guardar el mensaje junto con la fecha
    archivo.write(f"{fecha} - {mensaje}\n")

    # Cerrar el archivo
    archivo.close()