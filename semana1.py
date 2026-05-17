# VARIABLES Y TIPOS DE DATOS
# El Símbolo # es un comentario, el cual es ignorado por el intérprete de Python.

nombre = "Fernando"
edad = 25
sueldo_actual = 20500.0
buscando_chamba = True

print (nombre)
print (edad)
print (sueldo_actual)
print (buscando_chamba)

# TIPOS DE DATOS
# str = string, texto = "Fernando"
# int = integer, número entero = 25
# float = número decimal = 20500.0
# bool = booleano, verdadero o falso = True

# Estos cuatro tipos de datos son los más comunes
# Pero existen otros tipos de datos que iremos viendo a lo largo del curso.


# ¿DE QUÉ TIPO ES CADA VARIABLE?
print(type(nombre))
print(type(edad))
print(type(sueldo_actual))
print(type(buscando_chamba))

# F-STRINGS: combinar texto con variables
print(f"Hola, me llamo {nombre} y tengo {edad} años")
print(f"Mi sueldo actual es ${sueldo_actual} y ¿buscando chamba? {buscando_chamba}")

# Los f-strings son una forma de formatear texto en Python. La letra "f" antes de las comillas indica que es un f-string.
# Permiten insertar variables usando llaves {} dentro de una cadena de texto, y el resultado es una cadena formateada con los valores de las variables.
# Un ejemplo de uso de f-strings es el siguiente:

# En QA Automation los usarás para generar mensajes de error descriptivos
# En DevOps para logs.

# Sigamos con operadores.

# Operadores aritméticos
sueldo_meta = 50000.0
diferencia = sueldo_meta - sueldo_actual
aumento_porcentaje = (diferencia / sueldo_actual) * 100

print(f"Sueldo actual:  ${sueldo_actual}")
print(f"Sueldo meta:    ${sueldo_meta}")
print(f"Diferencia:     ${diferencia}")
print(f"Necesitas aumentar tu sueldo un {aumento_porcentaje:.1f}%")

# El :.1f dentro del f-string indica que queremos formatear el número con un decimal y una "f" para indicar que es un número de punto flotante (float)
# Esto hace que el resultado se muestre con un decimal y redondeado a una cifra decimal, lo cual es útil para mostrar porcentajes de manera más legible.

# Hagamos el programa un poco más interactivo, pidiendo al usuario que ingrese algunos datos

# INPUT: el usuario escribe los datos
print("--- CALCULADORA DE AUMENTO ---")
nombre_usuario = input("¿Cuál es tu nombre? ")
sueldo_hoy = float(input("¿Cuánto ganas ahorita? (Solo ingresa números enteros sin comas) $"))
sueldo_objetivo = float(input("¿Cuánto quieres ganar? (Solo ingresa números enteros sin comas) $"))

diferencia = sueldo_objetivo - sueldo_hoy
porcentaje = (diferencia / sueldo_hoy) * 100

print(f"\nOk {nombre_usuario}, necesitas aumentar tu sueldo un {porcentaje:.1f}%")
print(f"Eso es ${diferencia:.0f} pesos más al mes.")
print(f"En un año serían ${diferencia * 12:.0f} pesos extra.")