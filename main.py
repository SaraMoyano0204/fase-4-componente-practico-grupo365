# Se importa el servicio de reserva de sala
from servicios import ReservaSala

# Se importa la excepcion personalizada
from excepciones import ServicioError

# Y se importa la funcion para guardar los logs
from logger import registrar_log


# Se hacen simulaciones para probar el correcto funcionamiento del servicio

# Primera simulacion
# Se hace una prueba inicial para un servicio de reserva valido
try:

    # Se crea el servicio de reserva
    servicio1 = ReservaSala("Sala VIP", 100)

    # Se obtiene el nombre del servicio
    nombre = servicio1.get_nombre()

    # Se calcula el costo total
    costo = servicio1.calcular_costo(2)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio1.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")


# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

# Se hace un salto de línea para separar la otra simulacion
print()

# Seguna simulacion
# Se hace una prueba para un servicio de reserva con nombre vacio
try:

    # Se crea un servicio con nombre vacio
    servicio2 = ReservaSala("", 100)

    # Se obtiene el nombre del servicio
    nombre = servicio2.get_nombre()

    # Se calcula el costo total
    costo = servicio2.calcular_costo(2)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio2.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")


# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

# Se hace un salto de línea para separar la otra simulacion
print()

# Tercera simulacion
# Se hace una prueba para un servicio de reserva con precio no valido
try:

    # Se crea un servicio con nombre vacio
    servicio3 = ReservaSala("Sala Premium", -50)

    # Se obtiene el nombre del servicio
    nombre = servicio3.get_nombre()

    # Se calcula el costo total
    costo = servicio3.calcular_costo(2)

    # Se muestra la descripcion junto al costo total
    print(f"{servicio3.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")


# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")