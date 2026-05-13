# Se importa la clase Cliente
from clientes import Cliente

# Se importa el servicio de reserva de sala
from servicios import ReservaSala

# Se importa la clase Reserva
from reservas import Reserva

# Se importa la excepcion personalizada
from excepciones import ReservaError

# Se importa la funcion para guardar logs
from logger import registrar_log

# Se hacen simulaciones para probar el correcto funcionamiento del sistema

# Se hace una prueba para una reserva valida
try:

    # Se crea un cliente valido
    cliente1 = Cliente("Carlos Ruiz", "carlos@gmail.com")

    # Se crea un servicio valido
    servicio1 = ReservaSala("Sala Ejecutiva", 200)

    # Se crea la reserva
    reserva1 = Reserva(cliente1, servicio1, 3)

    # Se obtiene el nombre del cliente
    nombre_cliente = reserva1.get_cliente().get_nombre()

    # Se obtiene el nombre del servicio
    nombre_servicio = reserva1.get_servicio().get_nombre()

    # Se muestra la informacion de la reserva
    print(f"Reserva creada para: {nombre_cliente}")
    print(f"Servicio reservado: {nombre_servicio}")
    print(f"Estado de la reserva: {reserva1.get_estado()}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Reserva creada correctamente para: {nombre_cliente}")

# Si ocurre un error se captura
except ReservaError as error:
    # Se guarda el error en los logs
    registrar_log(f"ERROR en Reserva: {error}")

print() # Se hace un salto de linea

# Se hace una prueba para una reserva invalida
try:

    # Se crea un cliente valido
    cliente2 = Cliente("Laura Gomez", "laura@gmail.com")

    # Se crea un servicio valido
    servicio2 = ReservaSala("Sala Premium", 250)

    # Se crea una reserva con duracion invalida
    reserva2 = Reserva(cliente2, servicio2, "tres")

    # Se obtiene el nombre del cliente
    nombre_cliente = reserva2.get_cliente().get_nombre()

    # Se muestra la informacion de la reserva
    print(f"Reserva creada para: {nombre_cliente}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Reserva creada correctamente para: {nombre_cliente}")

# Si ocurre un error se captura
except ReservaError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Reserva: {error}")