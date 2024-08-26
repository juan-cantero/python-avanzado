def mostrar(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


diccionario = {"a": 1, "b": 2, "c": 3}

mostrar(juan=25, maria=32, ana=28)
print()
mostrar(**diccionario)
