from pathlib import Path

BASE_DIR = Path(__file__).parent
ARCHIVO = "prueba.txt"
RUTA = BASE_DIR / ARCHIVO

# archivo = open(RUTA, "w")
# archivo.write("Juan\n")
# archivo.write("Julio\n")
# archivo.close()

with open(RUTA, "w") as archivo:
    archivo.write("Juan\n")
    archivo.write("Julio\n")

# archivo = open(RUTA)
# print(archivo.read())
# archivo.close()

with open(RUTA) as f:
    print(f.read())
