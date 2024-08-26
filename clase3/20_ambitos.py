# Ámbitos globales y locales


clave_secreta = "Código Python"  # es una variable global


def adivinar_clave():
    print(clave_secreta)
    clave_introducida = input("Introduce la clave secreta: ")
    # clave_introducida es una variable local, solo existe dentro de la función
    return clave_introducida


# clave es una variable global
clave = adivinar_clave()
print(clave)
