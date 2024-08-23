"""
Crear un bucle while que pida al usuario
un número. Si el número es menor a 1, salir del bucle
-> crear un bloque else que imprima "fin del programa"
"""


while True:
    num = int(input("Ingresa un número: "))
    if num < 1:
        break
else:
    print("Fin del programa")
