# Argumentos indeterminados


# def sumar(n1, n2, n3):
#     print(n1 + n2 + n3)


# sumar(10, 20, 5)


def sumar(*args):
    print(sum(args))


sumar(10, 20, 5)
sumar(1)
sumar(10, 20, 5, 10, 20, 5)
