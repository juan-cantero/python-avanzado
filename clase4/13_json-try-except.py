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

personas: list[dict] = []

try:
    with open(RUTA, "r") as f:
        personas = json.load(f)
except FileNotFoundError:
    print("El archivo no existe. Se creará uno nuevo.")
except json.decoder.JSONDecodeError:
    print("El archivo está vacío o no es un JSON válido.")
    exit(1)
except Exception as e:
    print("Error:", type(e))
    exit(1)

nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")

while True:
    try:
        telefono = input("Ingrese el teléfono: ")
        if len(telefono) < 7 or len(telefono) > 15 or not telefono.isdigit():
            raise ValueError
        break
    except ValueError:
        print("El teléfono debe tener entre 7 dígitos a 15.")

formulario = {
    "nombre": nombre,
    "apellido": apellido,
    "telefono": telefono,
}
personas.append(formulario)

with open(RUTA, "w") as f:
    json.dump(personas, f, indent=4)
