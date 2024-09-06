"""
Refactorizar el siguiente código con funciones y buenas prácticas:

try:
    numero_1 = float(input("Primer número: "))
    numero_2 = float(input("Segundo número: "))
    division = numero_1 / numero_2
except ValueError:
    print("Error: Debes ingresar un número.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except KeyboardInterrupt:
    print("\nInterrumpido por el usuario")
except Exception as e:
    print("Error:", repr(e))
else:
    print("La división es:", division)
"""


def dividir(numero_1: float, numero_2: float) -> float | None:
    try:
        division = numero_1 / numero_2
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    except Exception as e:
        print("Error inesperado:", repr(e))
    else:
        return division


def introducir_numeros() -> tuple[float, float] | None:
    try:
        numero_1 = float(input("Primer número: "))
        numero_2 = float(input("Segundo número: "))
    except ValueError:
        print("Error: Debes ingresar un número.")
    except Exception as e:
        print("Error inesperado:", repr(e))
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
