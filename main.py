# Se importa la clase Cliente
from clientes import Cliente

# Se importa la excepcion personalizada
from excepciones import ClienteError

# Y se importa la funcion para guardar los logs
from logger import registrar_log


# Se muestra por consola el titulo del sistema
print("SISTEMA SOFTWARE FJ\n")

# Se hacen las primeras simulaciones para probar el correcto funcionamiento del sistema

# Primera simulacion
# Se hace una prueba inicial para un cliente valido
try:

    # Se crea un cliente valido
    cliente1 = Cliente("Juan Perez", "juan@gmail.com")

    # Se muestra la informacion del cliente
    print(cliente1.mostrar_informacion())

    # Se trae el nombre del cliente para guardarlo en el log del resultado
    nombre = cliente1.get_nombre();

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Cliente registrado correctamente: {nombre}")


# Si ocurre un error con el cliente se captura
except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Cliente: {error}")

# Se hace un salto de línea para separar la otra simulacion
print()

# Segunda simulacion
# Se hace una prueba para un cliente con nombre no valido
try:

    # Se crea un cliente con nombre vacio
    cliente2 = Cliente("", "cliente2@gmail.com")

    # Se muestra la informacion del cliente
    print(cliente2.mostrar_informacion())

    # Se trae el nombre del cliente para guardarlo en el log del resultado
    nombre = cliente2.get_nombre();

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Cliente registrado correctamente: {nombre}")


# Si ocurre un error con el cliente se captura
except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Cliente: {error}")

# Se hace un salto de línea para separar la otra simulacion
print()


# Tercera simulacion
# Se hace una prueba para un cliente con correo no valido
try:

    # Se crea un cliente con correo incorrecto
    cliente3 = Cliente("Juana", "juanacorreo.com")

    # Se muestra la informacion del cliente
    print(cliente3.mostrar_informacion())

    # Se trae el nombre del cliente para guardarlo en el log del resultado
    nombre = cliente3.get_nombre();

    # Se guarda el evento exitoso en los logs
    registrar_log(f"Cliente registrado correctamente: {nombre}")


# Si ocurre un error con el cliente se captura
except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Cliente: {error}")