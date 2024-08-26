"""
Crear una función que reciba un diccionario y transformar sus valores en mayúsculas
Se debe crear un diccionario con 2 elementos cuyos valores sean cadenas
Pasarlo como argumento a la función
Debo guardar en una variable la devolución de la función
Imprimir el diccionario original y luego el diccionario transformado en mayúsculas
"""


def convertir_mayusculas(diccionario: dict[str, str]) -> dict[str, str]:
    for clave, valor in diccionario.items():
        diccionario[clave] = valor.upper()
    return diccionario


diccionario_original = {"nombre": "juan", "apellido": "perez"}
diccionario_transformado = convertir_mayusculas(diccionario_original.copy())

print(diccionario_original)
print(diccionario_transformado)
