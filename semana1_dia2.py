# Empezamos Día 2 el 23 de Mayo 2026 #

# Control de flujo: condicionales
# Utilizaremos el mismo programa de clasificación de tickets de soporte,
# pero mejorado para manejar entradas no válidas 
# y para ser más amigable con el usuario.

# Nuestras condicionales a explorar hoy serán: if, elif y else

print(" \n\n--- CLASIFICADOR DE TICKETS DE SOPORTE --- ")

prioridad = input( "\nIngresa la prioridad del ticket (alta, media, baja): ").lower()
if prioridad == "":
    print("\nNo se ingresó una prioridad válida. Por favor, vuelve a intentarlo.")

es_vip = input("¿El cliente es VIP? (si/no): ").lower()
if es_vip == "":
    print("\nNo se ingresó una respuesta válida. Por favor, vuelve a intentarlo.")

# --- #
# Ahora, vamos a agregar una pregunta adicional para los tickets de prioridad media,
# para saber si el cliente es VIP o no, y así ajustar la respuesta del programa.

# Observa que el método .lower() convierte la entrada del usuario a minúsculas, 
# Y del mismo modo, iniciamos esta condicional con "if" con una verificación 
# para asegurarnos de que el usuario no deje el campo vacío.

if prioridad == "alta" and es_vip == "si":
    print("\n🚨 Ticket crítico de cliente VIP - escalar al manager y al equipo senior.")

# Aquí, hemos agregado una condición adicional para los tickets de prioridad alta, 
# verificando si el cliente es VIP.
          
# Adicionalmente, existe una opción donde el cliente no es VIP, 
# pero el ticket es de prioridad alta, 
# lo cual también es crítico pero no tan urgente como el caso VIP.

elif prioridad == "alta" and es_vip == "no":
    print("\n🔴 Ticket crítico - escalar inmediatamente.")

# Continuamos con las otras condiciones para prioridad media y baja,

elif prioridad == "media":
    print("\n🟠 Ticket moderado - atender en las próximas 3 horas.")

elif prioridad == "baja":
    print("\n🟢 Ticket menor - atender antes de fin de día.")

else:
    print("\n⚪ Prioridad/Respuesta no reconocida - ingresa alta, media o baja.")

# En Python, los métodos como .lower() son funciones que se aplican a cadenas de texto (strings) para transformarlas. 
# El método .lower() convierte todas las letras de una cadena a minúsculas.
# La línea para convertir la entrada del usuario a minúsculas sería:

# prioridad = input("Ingresa la prioridad del ticket (alta/media/baja): ").lower() #

# Vamos a finalizar el programa con un resumen de la información ingresada 
# por el usuario, utilizando un f-string para mostrar la prioridad y 
# si el cliente es VIP o no.
print(f"\n\nResumen: \nPrioridad del Ticket: {prioridad}\nEs cliente VIP: {es_vip}")
