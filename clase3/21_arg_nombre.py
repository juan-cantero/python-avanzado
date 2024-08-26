# Argumentos por nombre y por posición


def datos(a, b, c=0):
    print(a + b + c)


datos(1, 2, 3)  # Argumentos por posición

datos(a=1, b=2, c=3)  # Argumentos por nombres
datos(c=10, b=22, a=3)  # Argumentos por nombres
