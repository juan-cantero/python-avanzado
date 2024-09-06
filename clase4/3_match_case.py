def describir_numero(n: int) -> str:
    match n:
        case 0:
            return "cero"
        case 1:
            return "uno"
        case 2:
            return "dos"
        case _:
            return "otro número"


print(describir_numero(0))
print(describir_numero(1))
print(describir_numero(2))
print(describir_numero(3))
print(describir_numero(4))
