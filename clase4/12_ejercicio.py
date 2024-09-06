"""
Crear un archivo que contenga los elementos de una lista.
La lista consiste en 2 elementos que son diccionarios (formularios)
list[dict]
    nombre: str
    apellido: str
    telefono: int

Usar json para guardar el archivo y luego abrirlo e imprimir en la terminal la información
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
ARCHIVO = "12_desafio.json"
RUTA = BASE_DIR / ARCHIVO

# Crear la lista de diccionarios para almacenar datos de personas
personas: list[dict] = []

# Ingresar datos
for _ in range(2):
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    telefono = int(input("Ingrese el teléfono: "))
    formulario = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
    }
    personas.append(formulario)

# Crear JSON y guardarlo en el archivo
with open(RUTA, "w") as f:
    json.dump(personas, f, indent=4)

# Leer JSON e imprimir en la consola
with open(RUTA, "r") as f:
    datos = json.load(f)
    print(datos)
