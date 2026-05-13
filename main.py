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

    # Sexta simulacion: Se hace una prueba para una reserva con duracion invalida
try:

    # Se guarda en los logs un mensaje de inicio de ejecucion de la simulacion
    registrar_log("Simulacion 6 Iniciada")

    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 6 Iniciada")

    # Se crea el cliente
    cliente3 = Cliente("Carlos Ruiz", "carlos@gmail.com")

    # Se crea el servicio
    servicio4 = ReservaSala("Sala VIP", 200)

    # Se crea la reserva con duracion incorrecta
    reserva1 = Reserva(cliente3, servicio4, "tres")

    # Se obtiene el estado
    estado = reserva1.get_estado()

except (ClienteError, ServicioError, ReservaError) as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Reserva: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Reserva: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Reserva creada correctamente")

    # Se guarda la informacion de la reserva
    registrar_log(f"INFO: Cliente: {cliente3.get_nombre()} | Servicio: {servicio4.get_nombre()} | Estado: {estado}")

    # Se muestra tambien en pantalla el mensaje
    print(f"Reserva creada correctamente\nCliente: {cliente3.get_nombre()} | Servicio: {servicio4.get_nombre()} | Estado: {estado}")

finally:

    # Se guarda el mensaje de cierre
    registrar_log("Simulación 6 Finalizada\n")

    # Se muestra tambien en pantalla el mensaje
    print("Simulación 6 Finalizada\n")

# Septima simulacion: Se hace una prueba para confirmar una reserva cancelada
try:

    # Se guarda en los logs un mensaje de inicio
    registrar_log("Simulacion 7 Iniciada")

    # Se muestra tambien en pantalla el mensaje
    print("Simulacion 7 Iniciada")

    # Se crea el cliente
    cliente4 = Cliente("Laura Gomez", "laura@gmail.com")

    # Se crea el servicio
    servicio5 = ReservaSala("Sala Premium", 250)

    # Se crea la reserva
    reserva2 = Reserva(cliente4, servicio5, 2)

    # Se cancela la reserva
    reserva2.cancelar_reserva()

    # Se intenta confirmar nuevamente
    reserva2.confirmar_reserva()

    # Se obtiene el estado
    estado = reserva2.get_estado()

except (ClienteError, ServicioError, ReservaError) as error:

    # Se guarda el error en los logs
    registrar_log(f"ERROR en Reserva: {error}")

    # Se muestra tambien en pantalla el mensaje
    print(f"ERROR en Reserva: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Reserva confirmada correctamente")

    # Se guarda informacion de la reserva
    registrar_log(f"INFO: Cliente: {cliente4.get_nombre()} | Servicio: {servicio5.get_nombre()} | Estado: {estado}")

    # Se muestra tambien en pantalla
    print(f"Reserva confirmada correctamente\nCliente: {cliente4.get_nombre()} | Servicio: {servicio5.get_nombre()} | Estado: {estado}")

finally:

    # Se guarda el mensaje de cierre
    registrar_log("Simulación 7 Finalizada\n")

    # Se muestra tambien en pantalla
    print("Simulación 7 Finalizada\n")

# Octava simulacion: Se hace una prueba para un cliente con nombre invalido
try:

    # Se guarda el inicio de la simulacion
    registrar_log("Simulacion 8 Iniciada")

    # Se muestra tambien en pantalla
    print("Simulacion 8 Iniciada")

    # Se crea el cliente
    cliente5 = Cliente("12345", "pedro@gmail.com")

    # Se obtiene el nombre
    nombre = cliente5.get_nombre()

except ClienteError as error:

    # Se guarda el error
    registrar_log(f"ERROR en Cliente: {error}")

    # Se muestra tambien en pantalla
    print(f"ERROR en Cliente: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Cliente registrado correctamente")

    # Se guarda la informacion del cliente
    registrar_log(f"INFO: {cliente5.mostrar_informacion()}")

    # Se muestra tambien en pantalla
    print(f"Cliente registrado correctamente\n{cliente5.mostrar_informacion()}")

finally:

    # Se guarda el cierre
    registrar_log("Simulación 8 Finalizada\n")

    # Se muestra tambien en pantalla
    print("Simulación 8 Finalizada\n")

# Novena simulacion: Se hace una prueba para una reserva valida
try:

    # Se guarda el inicio de la simulacion
    registrar_log("Simulacion 9 Iniciada")

    # Se muestra tambien en pantalla
    print("Simulacion 9 Iniciada")

    # Se crea el cliente
    cliente6 = Cliente("Sofia Martinez", "sofia@gmail.com")

    # Se crea el servicio
    servicio6 = Asesoria("Asesoria UX", 300)

    # Se crea la reserva
    reserva3 = Reserva(cliente6, servicio6, 2)

    # Se confirma la reserva
    reserva3.confirmar_reserva()

    # Se obtiene el estado
    estado = reserva3.get_estado()

except (ClienteError, ServicioError, ReservaError) as error:

    # Se guarda el error
    registrar_log(f"ERROR en Reserva: {error}")

    # Se muestra tambien en pantalla
    print(f"ERROR en Reserva: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Reserva realizada correctamente")

    # Se guarda la informacion de la reserva
    registrar_log(f"INFO: Cliente: {cliente6.get_nombre()} | Servicio: {servicio6.get_nombre()} | Estado: {estado}")

    # Se muestra tambien en pantalla
    print(f"Reserva realizada correctamente\nCliente: {cliente6.get_nombre()} | Servicio: {servicio6.get_nombre()} | Estado: {estado}")

finally:

    # Se guarda el cierre
    registrar_log("Simulación 9 Finalizada\n")

    # Se muestra tambien en pantalla
    print("Simulación 9 Finalizada\n")

# Decima simulacion: Se hace una prueba para un servicio con precio negativo
try:

    # Se guarda el inicio de la simulacion
    registrar_log("Simulacion 10 Iniciada")

    # Se muestra tambien en pantalla
    print("Simulacion 10 Iniciada")

    # Se crea el servicio
    servicio7 = AlquilerEquipo("Camara Profesional", -100)

    # Se obtiene el nombre
    nombre = servicio7.get_nombre()

    # Se calcula el costo
    costo = servicio7.calcular_costo(5)

except ServicioError as error:

    # Se guarda el error
    registrar_log(f"ERROR en Servicio: {error}")

    # Se muestra tambien en pantalla
    print(f"ERROR en Servicio: {error}")

else:

    # Se guarda el evento exitoso
    registrar_log("INFO: Servicio creado correctamente")

    # Se guarda tambien la informacion del servicio
    registrar_log(f"INFO: {servicio7.descripcion()} | Costo Total: {costo}")

    # Se muestra tambien en pantalla
    print(f"Servicio creado correctamente\n{servicio7.descripcion()} | Costo Total: {costo}")

finally:

    # Se guarda el cierre
    registrar_log("Simulación 10 Finalizada\n")

    # Se muestra tambien en pantalla
    print("Simulación 10 Finalizada\n")