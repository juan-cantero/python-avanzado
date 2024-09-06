def sumar_enteros(n1: int, n2: int) -> int:
    if isinstance(n1, int) and isinstance(n2, int):
        return n1 + n2
    raise ValueError("Ambos argumentos deben ser enteros")


suma = sumar_enteros(5, 3.2)
print(suma)
