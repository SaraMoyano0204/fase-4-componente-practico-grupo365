# Se importa la excepcion personalizada para clientes
from excepciones import ClienteError


# Se crea la clase para representar los clientes del sistema
class Cliente:

    # Se crea el constructor de la clase
    def __init__(self, nombre, correo):

        # Se valida que el nombre no este vacio
        if nombre.strip() == "":

            # Se lanza una excepcion personalizada
            raise ClienteError("El nombre no puede estar vacio")

        # Se valida que el correo tenga el simbolo @
        if "@" not in correo:

            # Se lanza una excepcion si el correo no es valido
            raise ClienteError("El correo ingresado no es valido")

        # Se guarda el nombre como atributo privado
        self.__nombre = nombre

        # Se guarda el correo como atributo privado también
        self.__correo = correo

    # Se crea el metodo para obtener el nombre del cliente
    def get_nombre(self):

        # Se retorna el nombre del cliente
        return self.__nombre

    # Se crea el metodo para obtener el correo del cliente
    def get_correo(self):
        
        # Se retorna el correo del cliente
        return self.__correo

    # Y se crea otro metodo para mostrar la informacion del cliente
    def mostrar_informacion(self):
        
        # Se retorna la información
        return f"Cliente: {self.__nombre} \nCorreo: {self.__correo}"