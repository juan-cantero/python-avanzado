"""
numeros = [1, 10, 0, 4, 2, 3, 5, 6]
Recorre la lista "numeros" y realiza las siguientes
acciones para cada elemento:
Si el número es igual a 2, imprime "Soy el 2" y continúa con el bucle,
sin ejecutar la línea posterior.
Si el número es igual a 5, imprime "Soy el 5" y sale del bucle,
sin ejecutar la línea posterior.
En cualquier otro caso, imprime el número.
Después de cada iteración, imprime "✨ di una vuelta ✨".
"""

numeros = [1, 10, 0, 4, 2, 3, 5, 6]

for numero in numeros:
    if numero == 2:
        print("Soy el 2")
        continue
    elif numero == 5:
        print("Soy el 5")
        break
    else:
        print(numero)
    print("✨ di una vuelta ✨")
else:
    pass
