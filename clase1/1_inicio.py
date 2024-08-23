# Los comentarios sirven para explicar el código y hacerlo más legible.

print("Hola mundo!")  # Comentario en línea.


def funcion():
    """documentacion"""


print(funcion.__doc__)  # Imprime la documentación de la función.

# Estilos para crear variables (snake_case, camelCase, UpperCamelCase).
# variables y funciones: snake_case (todo en minúsculas y separado por guiones bajos).
# clases: UpperCamelCase (todo en mayúsculas y sin separadores).

# Palabras reservadas en Python
import keyword

print(keyword.kwlist)  # Imprime todas las palabras reservadas en Python.

# Tipos de datos en Python

# Números: int, float, complex
# Texto: str (cadenas de caracteres)
# Booleans: bool (True o False)
# Colecciones: list, tuple, set, dict


# Ejemplos

# int: 1
# float: 1.0
# complex: 1j
# str: "Hola mundo!"
# bool: True, False
# list: [1, 2, 3, 4, 5] or ["Hola", "mundo!"] or [1, "Hola", True] or [1, [2, 3], 4] or [] (lista vacía)
# tuple: (1, 2, 3, 4, 5) or ("Hola", "mundo!") or (1, "Hola", True) or (1, (2, 3), 4) or () (tupla vacía)
# set: {1, 2, 3, 4, 5} or {"Hola", "mundo!"} or {1, "Hola", True} or {1, (2, 3), 4} or set() (conjunto vacío)
# dict: {"nombre": "Juan", "edad": 25} or {1: "Hola", 2: "mundo!"} or {} (diccionario vacío)

personas = [
    {"nombre": "Juan", "edad": 25},
    {"nombre": "Pedro", "edad": 30},
    {"nombre": "María", "edad": 28},
]
