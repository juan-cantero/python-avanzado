from el_paquete.constantes import PI  # importación absoluta

# from .constantes import PI  # importación relativa


def sumar(a, b):
    print(a + b)


def restar(a, b):
    print(a - b)


def multiplicar(a, b):
    print(a * b)


def dividir(a, b):
    if b != 0:
        print(a / b)
    else:
        print("No se puede dividir por cero")


print("Desde matematicas", PI)
