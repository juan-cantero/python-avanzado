# Cadenas método slicing

cadena = "Esto es una cadena de texto"

print(cadena[0])  # Indicamos el índice del carácter que queremos obtener
print(cadena[1])
print(cadena[2])
print(cadena[3])

# También podemos obtener un rango de caracteres utilizando el método slicing.
# cadena[inicio:fin]

esto = cadena[0:4]  # Obtenemos los caracteres desde el índice 0 hasta el 3
print(esto)  # Esto

# cadena[inicio:fin:paso]  # El paso indica cada cuántos caracteres queremos obtener
print(cadena[::2])

# inversa
print(cadena[::-1])  # Invertimos la cadena de texto


