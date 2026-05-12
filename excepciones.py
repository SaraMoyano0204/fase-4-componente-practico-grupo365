# Clase para manejar errores relacionados con los clientes
class ClienteError(Exception):

    # pass se usa porque la clase no necesita codigo interno por ahora
    pass


# Clase para manejar errores relacionados con los servicios
class ServicioError(Exception):

    # La clase queda vacia porque solo se usa para identificar el tipo de error
    pass


# Clase para manejar errores relacionados con las reservas
class ReservaError(Exception):

    # Esta excepcion servira para controlar errores en las reservas
    pass