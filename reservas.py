# Se importa la excepcion personalizada de reservas
from excepciones import ReservaError

# Se importa la clase Cliente
from clientes import Cliente

# Se importa la clase Servicio
from servicios import Servicio

# Se crea la clase Reserva
class Reserva:

    # Se crea el constructor de la clase
    def __init__(self, cliente, servicio, duracion):

        # Se valida que el cliente sea un objeto de tipo Cliente
        if not isinstance(cliente, Cliente):
            # Se lanza una excepcion si el cliente no es valido
            raise ReservaError("El cliente ingresado no es valido")

        # Se valida que el servicio sea un objeto de tipo Servicio
        if not isinstance(servicio, Servicio):
            # Se lanza una excepcion si el servicio no es valido
            raise ReservaError("El servicio ingresado no es valido")

        # Se valida que la duracion sea numerica
        if not isinstance(duracion, (int, float)):
            # Se lanza una excepcion si no es numerica
            raise ReservaError("La duracion debe ser numerica")

        # Se valida que la duracion sea mayor a cero
        if duracion <= 0:
            # Se lanza una excepcion si la duracion no es valida
            raise ReservaError("La duracion debe ser mayor a cero")

        # Se guarda el cliente como atributo privado
        self.__cliente = cliente

        # Se guarda el servicio como atributo privado
        self.__servicio = servicio

        # Se guarda la duracion como atributo privado
        self.__duracion = duracion

        # Se guarda el estado inicial de la reserva
        self.__estado = "Pendiente"

    # Se crea metodo para obtener el cliente
    def get_cliente(self):
        # Se retorna el cliente
        return self.__cliente

    # Se crea metodo para obtener el servicio
    def get_servicio(self):
        # Se retorna el servicio
        return self.__servicio

    # Se crea metodo para obtener la duracion
    def get_duracion(self):
        # Se retorna la duracion
        return self.__duracion

    # Se crea metodo para obtener el estado
    def get_estado(self):
        # Se retorna el estado
        return self.__estado
    
    # Se crea metodo para confirmar la reserva
    def confirmar_reserva(self):

        # Se valida si la reserva ya fue confirmada
        if self.__estado == "Confirmada":
            # Se lanza una excepcion si ya esta confirmada
            raise ReservaError("La reserva ya fue confirmada")

        # Se valida si la reserva ya fue cancelada
        if self.__estado == "Cancelada":
            # Se lanza una excepcion si ya fue cancelada
            raise ReservaError("No se puede confirmar una reserva cancelada")

        # Se cambia el estado de la reserva
        self.__estado = "Confirmada"

    # Se crea metodo para cancelar la reserva
    def cancelar_reserva(self):

        # Se valida si la reserva ya fue cancelada
        if self.__estado == "Cancelada":
            # Se lanza una excepcion si ya fue cancelada
            raise ReservaError("La reserva ya fue cancelada")

        # Se cambia el estado de la reserva
        self.__estado = "Cancelada"