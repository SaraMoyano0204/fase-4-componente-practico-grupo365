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

# Se hace una prueba para confirmar una reserva valida
try:

    # Se crea un cliente valido
    cliente1 = Cliente("Carlos Ruiz", "carlos@gmail.com")

    # Se crea un servicio valido
    servicio1 = ReservaSala("Sala Ejecutiva", 200)

    # Se crea la reserva
    reserva1 = Reserva(cliente1, servicio1, 3)

    # Se confirma la reserva
    reserva1.confirmar_reserva()

    # Se obtiene el nombre del cliente
    nombre_cliente = reserva1.get_cliente().get_nombre()

    # Se muestra el estado de la reserva
    print(f"Reserva confirmada para: {nombre_cliente}")
    print(f"Estado actual: {reserva1.get_estado()}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Reserva confirmada correctamente para: {nombre_cliente}")

# Si ocurre un error se captura
except ReservaError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Reserva: {error}")

print() # Se hace un salto de linea

# Se hace una prueba para confirmar una reserva ya cancelada
try:

    # Se crea un cliente valido
    cliente2 = Cliente("Laura Gomez", "laura@gmail.com")

    # Se crea un servicio valido
    servicio2 = ReservaSala("Sala Premium", 250)

    # Se crea la reserva
    reserva2 = Reserva(cliente2, servicio2, 2)

    # Se cancela la reserva
    reserva2.cancelar_reserva()

    # Se intenta confirmar nuevamente la reserva
    reserva2.confirmar_reserva()

    # Se obtiene el nombre del cliente
    nombre_cliente = reserva2.get_cliente().get_nombre()

    # Se muestra el estado de la reserva
    print(f"Reserva confirmada para: {nombre_cliente}")
    print(f"Estado actual: {reserva2.get_estado()}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Reserva confirmada correctamente para: {nombre_cliente}")

# Si ocurre un error se captura
except ReservaError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Reserva: {error}")