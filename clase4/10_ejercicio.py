"""
Crear un archivo que contenga los elementos de una lista.
La lista consiste en 5 elementos.
Usar for range para pedir los elementos para la lista
Usar for para iterar la lista y escribir sobre el archivo
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent
ARCHIVO = "ejercicio.txt"
RUTA = BASE_DIR / ARCHIVO

# Crear una lista vacía para almacenar los elementos
lista_elementos: list[str] = []

# Ingresar los datos
for i in range(5):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    lista_elementos.append(elemento)

# Escribir los datos en el archivo
with open(RUTA, "w") as f:
    for elemento in lista_elementos:
        f.write(elemento + "\n")

# Salida de datos en pantalla
print(f"Archivo '{RUTA}' creado con éxito")
