# Se importa la excepcion personalizada para clientes
from excepciones import ClienteError


# Se crea la clase para representar los clientes del sistema
class Cliente:

    # Se crea el constructor de la clase
    def __init__(self, nombre, correo):

        # Se valida que el nombre sea tipo texto
        if not isinstance(nombre, str):
            # Se lanza una excepcion si no es texto
            raise ClienteError("El nombre debe ser de tipo texto")

        # Se valida que el nombre no este vacio
        if nombre.strip() == "":
            # Se lanza una excepcion si esta vacio
            raise ClienteError("El nombre no puede estar vacio")

        # Se valida que el nombre tenga minimo 3 caracteres
        if len(nombre.strip()) < 3:
            # Se lanza una excepcion si es muy corto
            raise ClienteError("El nombre debe tener minimo 3 caracteres")
        
        # Se valida que el nombre solo tenga letras y espacios
        if not nombre.replace(" ", "").isalpha():
            # Se lanza una excepcion si tiene caracteres invalidos
            raise ClienteError("El nombre solo debe contener letras")

        # Se valida que el correo sea tipo texto
        if not isinstance(correo, str):
            # Se lanza una excepcion si no es texto
            raise ClienteError("El correo debe ser de tipo texto")
        
        # Se valida que el correo no este vacio
        if correo.strip() == "":
            # Se lanza una excepcion si esta vacio
            raise ClienteError("El correo no puede estar vacio")
        
        # Se valida que el correo tenga el simbolo @
        if "@" not in correo:
            # Se lanza una excepcion si no es valido
            raise ClienteError("El correo ingresado no es valido")
        
        # Se separa el correo usando el simbolo @
        partes_correo = correo.split("@")

        # Se valida que el correo tenga usuario y dominio
        if len(partes_correo) != 2:
            # Se lanza una excepcion si no tiene formato valido
            raise ClienteError("El correo no tiene un formato valido")

        # Se guarda la parte del dominio
        dominio = partes_correo[1]

        # Se valida que el dominio tenga un punto
        if "." not in dominio:
            # Se lanza una excepcion si no tiene punto
            raise ClienteError("El correo debe tener un dominio valido")

        # Se valida que el correo no tenga espacios
        if " " in correo:
            # Se lanza una excepcion si tiene espacios
            raise ClienteError("El correo no debe contener espacios")

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