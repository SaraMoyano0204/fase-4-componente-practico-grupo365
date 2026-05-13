# Se importa la clase Cliente
from clientes import Cliente

# Se importa el servicio de reserva de sala
from servicios import ReservaSala

# Se importan las excepciones personalizadas
from excepciones import ClienteError, ServicioError

# Se importa la funcion para guardar logs
from logger import registrar_log

# Se hacen simulaciones para probar el correcto funcionamiento de las nuevas validaciones

# Primera simulacion
# Se hace una prueba para un cliente valido
try:

    # Se crea el cliente
    cliente1 = Cliente("Juan Perez", "juan@gmail.com")

    # Se obtiene el nombre del cliente
    nombre = cliente1.get_nombre()

    # Se muestra la informacion del cliente
    print(f"Cliente registrado: {nombre}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Cliente registrado correctamente: {nombre}")


# Si ocurre un error se captura
except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Cliente: {error}")

print() # Se hace un salto de linea

# Segunda simulacion
# Se hace una prueba para un correo invalido
try:

    # Se crea un cliente con correo invalido
    cliente2 = Cliente("Maria Lopez", "mariagmail.com")

    # Se obtiene el nombre del cliente
    nombre = cliente2.get_nombre()

    # Se muestra la informacion del cliente
    print(f"Cliente registrado: {nombre}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Cliente registrado correctamente: {nombre}")


# Si ocurre un error se captura
except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Cliente: {error}")

print() # Se hace un salto de linea

# Tercera simulacion
# Se hace una prueba para un servicio con precio tipo texto
try:

    # Se crea un servicio con precio invalido
    servicio1 = ReservaSala("Sala Empresarial", "cien")

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

print() # Se hace un salto de linea

# Cuarta simulacion
# Se hace una prueba para horas invalidas
try:

    # Se crea el servicio
    servicio2 = ReservaSala("Sala Empresarial", 120)

    # Se obtiene el nombre del servicio
    nombre = servicio2.get_nombre()

    # Se calcula el costo con horas invalidas
    costo = servicio2.calcular_costo("dos")

    # Se muestra la descripcion junto al costo total
    print(f"{servicio2.descripcion()}\nCosto Total: {costo}")

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Servicio creado correctamente: {nombre}")


# Si ocurre un error se captura
except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")