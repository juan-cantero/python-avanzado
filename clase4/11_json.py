import json
from pathlib import Path

BASE_DIR = Path(__file__).parent
ARCHIVO = "11_mi_json.json"
RUTA = BASE_DIR / ARCHIVO

base_datos = {
    "articulos": {
        1: {"nombre": "Teclado", "precio": 100.00, "disponible": True},
        2: {"nombre": "Mouse", "precio": 50.00, "disponible": True},
        3: {"nombre": "Monitor", "precio": 200.00, "disponible": False},
    },
    "proveedores": {
        1: {"nombre": "Proveedor1", "telefono": "1234567890"},
        2: {"nombre": "Proveedor2", "telefono": None},
    },
}

with open(RUTA, "w") as f:
    json.dump(base_datos, f, indent=4)


with open(RUTA, "r") as f:
    base_datos = json.load(f)
    precio_teclado = base_datos["articulos"]["1"]["precio"]
    print(precio_teclado)
