def funcion_number(numero):
    return numero * 2


numero = 4
resultado = funcion_number(numero)
print(numero)  # 4
print(resultado)  # 8


def funcion_string(string):
    return string + "!"


string = "saludos"
resultado = funcion_string(string)
print(string)  # saludos
print(resultado)  # saludos!


def funcion_lista(lista):
    lista.append("Python")
    return lista


lista_original = ["Java", "C++", "C#"]
resultado = funcion_lista(lista_original)
print(lista_original)  # ['Java', 'C++', 'C#', 'Python']
print(resultado)  # ['Java', 'C++', 'C#', 'Python']


def funcion_lista_mejorada(lista):
    lista.append("Python")
    return lista


lista_original = ["Java", "C++", "C#"]
resultado = funcion_lista_mejorada(lista_original.copy())
print(lista_original)  # ['Java', 'C++', 'C#']
print(resultado)  # ['Java', 'C++', 'C#', 'Python']
