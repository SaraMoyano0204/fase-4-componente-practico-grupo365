# Se importa la clase Cliente
from clientes import Cliente

# Se importa el servicio de reservas de salas
from servicios import ReservaSala

# Se importa el servicio de alquiler de equipos
from servicios import AlquilerEquipo

# Se importa el servicio de asesorias
from servicios import Asesoria

# Se importa la clase Reserva
from reservas import Reserva

# Se importa las excepcion personalizada de clientes
from excepciones import ClienteError

# Se importa las excepcion personalizada de servicios
from excepciones import ServicioError

# Se importa las excepcion personalizada de reservas
from excepciones import ReservaError

# Se importa la funcion para guardar logs
from logger import registrar_log

# Se hacen distinas simulaciones para probar el correcto funcionamiento del sistema

# Primera simulacion: Se hace una prueba para un cliente valido
try:

    # Se guarda en los logs un mensaje de inicio de ejecucion de la simulacion
    registrar_log("Simulacion 1 Iniciada")
    
    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 1 Iniciada")

    # Se crea el cliente
    cliente1 = Cliente("Juan Perez", "juan@gmail.com")

    # Se obtiene el nombre del cliente
    nombre = cliente1.get_nombre()

except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Cliente: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Cliente: {error}")

else:

    # Se guarda el evento exitoso en los logs
    registrar_log("INFO: Cliente registrado correctamente")
    
    # Se guarda tambien la informacion del cliente en los logs
    registrar_log(f"INFO: {cliente1.mostrar_informacion()}")

    # Se muestra tambien en pantalla el mensaje
    print(f"Cliente registrado correctamente\n{cliente1.mostrar_informacion()}")

finally:

    # Se guarda el mensaje de cierre de la simulacion en los logs para llevar un registro claro
    registrar_log("Simulación 1 Finalizada\n")
    
    # Se muestra tambien en pantalla el mensaje
    print("Simulación 1 Finalizada\n")

# Segunda simulacion: Se hace una prueba para un cliente con correo invalido
try:

    # Se guarda en los logs un mensaje de inicio de ejecucion de la simulacion
    registrar_log("Simulacion 2 Iniciada")
    
    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 2 Iniciada")

    # Se crea el cliente con correo incorrecto
    cliente2 = Cliente("Maria Lopez", "mariagmail.com")

    # Se obtiene el nombre del cliente
    nombre = cliente2.get_nombre()

except ClienteError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Cliente: {error}")

else:

    # Se guarda el evento exitoso en los logs
    registrar_log("INFO: Cliente registrado correctamente")
    
    # Se guarda tambien la informacion del cliente en los logs
    registrar_log(f"INFO: {cliente2.mostrar_informacion()}")

    # Se muestra tambien en pantalla el mensaje
    print(f"Cliente registrado correctamente\n{cliente2.mostrar_informacion()}")

finally:

    # Se guarda el mensaje de cierre de la simulacion en los logs para llevar un registro claro
    registrar_log("Simulación 2 Finalizada\n")
    
    # Se muestra tambien en pantalla el mensaje
    print("Simulación 2 Finalizada\n")

# Tercera simulacion: Se hace una prueba para un servicio con precio invalido
try:

    # Se guarda en los logs un mensaje de inicio de ejecucion de la simulacion
    registrar_log("Simulacion 3 Iniciada")

    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 3 Iniciada")

    # Se crea el servicio
    servicio1 = ReservaSala("Sala Ejecutiva", "doscientos")

    # Se obtiene el nombre
    nombre = servicio1.get_nombre()

    # Se calcula el costo
    costo = servicio1.calcular_costo(2)

except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Servicio: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log(f"INFO: Servicio creado correctamente")

    # Se guarda tambien la informacion del cliente en los logs
    registrar_log(f"INFO: {servicio1.descripcion()} | Costo Total: {costo}")

    # Se muestra tambien en pantalla el mensaje
    print(f"Servicio creado correctamente\n{servicio1.descripcion()} | Costo Total: {costo}")

finally:

    # Se guarda el mensaje de cierre de la simulacion
    registrar_log("Simulación 3 Finalizada\n")

    # Se muestra tambien en pantalla el mensaje
    print("Simulación 3 Finalizada\n")

# Cuarta simulacion: Se hace una prueba para un servicio de alquiler valido
try:

    # Se guarda en los logs un mensaje de inicio de ejecucion de la simulacion
    registrar_log("Simulacion 4 Iniciada")

    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 4 Iniciada")

    # Se crea el servicio
    servicio2 = AlquilerEquipo("Computador Gamer", 80)

    # Se obtiene el nombre
    nombre = servicio2.get_nombre()

    # Se calcula el costo
    costo = servicio2.calcular_costo(3)

except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Servicio: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Servicio creado correctamente")

    # Se guarda tambien la informacion del servicio en los logs
    registrar_log(f"INFO: {servicio2.descripcion()} | Costo Total: {costo}")

    # Se muestra tambien en pantalla el mensaje
    print(f"Servicio creado correctamente\n{servicio2.descripcion()} | Costo Total: {costo}")

finally:

    # Se guarda el mensaje de cierre de la simulacion
    registrar_log("Simulación 4 Finalizada\n")

    # Se muestra tambien en pantalla el mensaje
    print("Simulación 4 Finalizada\n")

# Quinta simulacion: Se hace una prueba para un servicio con nombre vacio
try:

    # Se guarda en los logs un mensaje de inicio de ejecucion de la simulacion
    registrar_log("Simulacion 5 Iniciada")

    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 5 Iniciada")

    # Se crea el servicio
    servicio3 = Asesoria("", 150)

    # Se obtiene el nombre
    nombre = servicio3.get_nombre()

    # Se calcula el costo
    costo = servicio3.calcular_costo(2, 20)

except ServicioError as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Servicio: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Servicio: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Servicio creado correctamente")

    # Se guarda tambien la informacion del servicio en los logs
    registrar_log(f"INFO: {servicio3.descripcion()} | Costo Total: {costo}")

    # Se muestra tambien en pantalla el mensaje
    print(f"Servicio creado correctamente\n{servicio3.descripcion()} | Costo Total: {costo}")

finally:

    # Se guarda el mensaje de cierre de la simulacion
    registrar_log("Simulación 5 Finalizada\n")

    # Se muestra tambien en pantalla el mensaje
    print("Simulación 5 Finalizada\n")