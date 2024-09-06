"""
Script que dados dos números, los divide y muestra el resultado.
Si se produce un error, lo maneja y muestra un mensaje de error.
Si no se produce un error, muestra el resultado de la división.
"""


def manejo_errores(e: Exception) -> None:
    """Maneja los errores que se producen durante la ejecución del programa."""
    match e:
        case ValueError():
            print("Error: Debes ingresar un número.")
        case ZeroDivisionError():
            print("Error: No se puede dividir entre cero.")
        case _:
            print("Error inesperado:", repr(e))


def dividir(numero_1: float, numero_2: float) -> float | None:
    """Divide dos números."""
    try:
        division = numero_1 / numero_2
    except Exception as e:
        manejo_errores(e)
    else:
        return division


def introducir_numeros() -> tuple[float, float] | None:
    """Introduce dos números y los valida."""
    try:
        numero_1 = float(input("Primer número: "))
        numero_2 = float(input("Segundo número: "))
    except Exception as e:
        manejo_errores(e)
    else:
        return numero_1, numero_2


def main() -> None:
    numeros_validos = introducir_numeros()
    if numeros_validos is None:
        print("No se pudo realizar la division")
        return
    division = dividir(*numeros_validos)
    if division is None:
        print("No se pudo realizar la division")
        return
    print("La división es:", division)


main()
