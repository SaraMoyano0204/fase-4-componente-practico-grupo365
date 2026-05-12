# Se importan las herramientas para crear clases abstractas
from abc import ABC, abstractmethod

# Se importa la excepcion personalizada de servicios
from excepciones import ServicioError

# Se crea la clase abstracta para representar los servicios del sistema
class Servicio(ABC):

    # Se crea el constructor de la clase
    def __init__(self, nombre, precio):

        # Se valida que el nombre no este vacio
        if nombre.strip() == "":

            # Se lanza la excepcion si el nombre esta vacio
            raise ServicioError("El nombre del servicio no puede estar vacio")

        # Se valida que el precio sea mayor a cero
        if precio <= 0:

            # Se lanza la excepcion si el precio no es valido
            raise ServicioError("El precio del servicio debe ser mayor a cero")

        # Se guarda el nombre como atributo privado
        self.__nombre = nombre

        # Se guarda el precio como atributo privado
        self.__precio = precio

    # Se crea el metodo para obtener el nombre del servicio
    def get_nombre(self):
        # Se retorna el nombre
        return self.__nombre

    # Se crea el metodo para obtener el costo del servicio
    def get_precio(self):
        # Se retorna el precio
        return self.__precio

    # Se indica que el metodo es abstracto
    @abstractmethod
    # Se crea el metodo para calcular el costo del servicio
    def calcular_costo(self):
        # Las clases hijas haran la implementacion
        pass

    # Se indica que el metodo es abstracto
    @abstractmethod
    # Se crea el metodo para mostrar la descripcion del servicio
    def descripcion(self):
        # Las clases hijas haran la implementacion
        pass

# Se crea una clase hija para manejar reservas de salas
class ReservaSala(Servicio):

    # Se crea el constructor de la clase hija
    def __init__(self, nombre, precio):
        
        # Se llama al constructor de la clase padre
        super().__init__(nombre, precio)

    # Se crea metodo para calcular el costo total
    def calcular_costo(self, horas=1):
        # Se retorna el precio multiplicado por las horas
        return self.get_precio() * horas

    # Se crea metodo para mostrar la descripcion del servicio
    def descripcion(self):
        # Se retorna la descripcion del servicio
        return f"Servicio de reserva de sala: {self.get_nombre()}\nPrecio por hora: {self.get_precio()}"