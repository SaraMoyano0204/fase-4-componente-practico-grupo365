# Se importa el servicio de reserva de sala
from servicios import ReservaSala

# Se importa el servicio de alquiler de equipos
from servicios import AlquilerEquipo

# Se importa el servicio de asesorias
from servicios import Asesoria

# Se importan las excepciones personalizadas
from excepciones import ServicioError

# Se importa la funcion para guardar logs
from logger import registrar_log

# Se hacen simulaciones para probar el correcto funcionamiento del sistema

# Se hace una prueba para un servicio de alquiler valido
try:

    # Se crea el servicio de alquiler
    servicio3 = AlquilerEquipo("Computador Gamer", 80)

    # Se obtiene el nombre del servicio
    nombre = servicio3.get_nombre()

    # Se calcula el costo total
    costo = servicio3.calcular_costo(3)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio3.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")

# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

print() # Se hace un salto de linea

# Se hace una prueba para un servicio de alquiler invalido
try:

    # Se crea un servicio con precio invalido
    servicio4 = AlquilerEquipo("Proyector", "cincuenta")

    # Se obtiene el nombre del servicio
    nombre = servicio4.get_nombre()

    # Se calcula el costo total
    costo = servicio4.calcular_costo(2)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio4.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")

# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

print() # Se hace un salto de linea

# Se hace una prueba para una asesoria valida
try:

    # Se crea el servicio de asesoria
    servicio5 = Asesoria("Asesoria de Diseño", 150)

    # Se obtiene el nombre del servicio
    nombre = servicio5.get_nombre()

    # Se calcula el costo total
    costo = servicio5.calcular_costo(2, 50)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio5.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")

# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

print() # Se hace un salto de linea

# Se hace una prueba para una asesoria con nombre vacio
try:

    # Se crea una asesoria con nombre invalido
    servicio6 = Asesoria("", 120)

    # Se obtiene el nombre del servicio
    nombre = servicio6.get_nombre()

    # Se calcula el costo total
    costo = servicio6.calcular_costo(2, 20)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio6.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")

# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")