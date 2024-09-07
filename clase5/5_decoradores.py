def mi_decorador(funcion):
    def nueva_funcion():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")

    return nueva_funcion


def subrayar(funcion):
    def nueva_funcion(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        if isinstance(resultado, str):
            print(resultado)
            print(len(resultado) * "-")
        else:
            print("La función no devolvió una cadena para subrayar")

    return nueva_funcion


@mi_decorador
def saludar():
    print("¡Hola, mundo!")


# saludar()


@subrayar
def saludar2(nombre):
    return f"¡Hola, {nombre}!"


print(saludar2("Lu"))
print(saludar2("HOLAAAAAAAAAAAAAAAA"))
