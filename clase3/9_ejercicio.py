"""
A partir de la siguiente lista de diccionarios,
iterar sobre la lista y mostrar la siguiente oración para cada elemento:
Por ej: "Buenos Aires es una ciudad de Argentina"
"""

ciudades_latinoamerica: list[dict] = [
    {"nombre": "Buenos Aires", "pais": "Argentina"},
    {"nombre": "Ciudad de México", "pais": "México"},
    {"nombre": "São Paulo", "pais": "Brasil"},
    {"nombre": "Rio de Janeiro", "pais": "Brasil"},
    {"nombre": "Lima", "pais": "Perú"},
    {"nombre": "Bogotá", "pais": "Colombia"},
    {"nombre": "Santiago", "pais": "Chile"},
    {"nombre": "Montevideo", "pais": "Uruguay"},
    {"nombre": "Caracas", "pais": "Venezuela"},
    {"nombre": "La Habana", "pais": "Cuba"},
]

for diccionario in ciudades_latinoamerica:
    print(f"{diccionario['nombre']} es una ciudad de {diccionario['pais']}")

print("\n*** ahora con get() ***")

for diccionario in ciudades_latinoamerica:
    nombre = diccionario.get("nombre")
    pais = diccionario.get("pais")
    print(f"{nombre} es una ciudad de {pais}")
