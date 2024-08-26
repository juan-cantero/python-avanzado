"""
Crear un bucle while que pida al usuario
un número. Si el número es menor a 1, salir del bucle
-> crear un bloque else que imprima "fin del programa"
"""

# while True:
#     numero = int(input("Por favor, ingresa un número: "))
#     if numero < 1:
#         break
# else:
#     print("Fin del programa")

continuar = True

while continuar:
    numero = int(input("Por favor, ingresa un número: "))
    if numero < 1:
        continuar = False
    # Hasta aquí llega el bucle
else:
    print("Fin del programa")
