from typing import Any


def decir_tipo_de_dato(objeto: Any):
    match objeto:
        case int():
            return "El objeto es un entero."
        case float():
            return "El objeto es un número de punto flotante."
        case str():
            return "El objeto es una cadena de texto."
        case list():
            return "El objeto es una lista."
        case dict():
            return "El objeto es un diccionario."
        case tuple():
            return "El objeto es una tupla."
        case set():
            return "El objeto es un conjunto."
        case bool():
            return "El objeto es un valor booleano."
        case None:
            return "El objeto es None."
        case _:
            return "El tipo de dato del objeto no se reconoce."


# Ejemplos de uso
print(decir_tipo_de_dato(10))  # "El objeto es un entero."
print(decir_tipo_de_dato(3.14))  # "El objeto es un número de punto flotante."
print(decir_tipo_de_dato("Hola, mundo!"))  # "El objeto es una cadena de texto."
print(decir_tipo_de_dato([1, 2, 3]))  # "El objeto es una lista."
print(decir_tipo_de_dato({"nombre": "Juan", "edad": 30}))  # "El objeto es un diccionario."
print(decir_tipo_de_dato(Exception))
