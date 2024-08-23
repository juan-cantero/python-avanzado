"""
A partir del siguiente diccionario, realizar los ejercicios propuestos:

inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "peras": 8
}

# Agregar 5 manzanas más al inventario

# Se vendieron 3 naranjas, actualizar el inventario

# Se agregaron 5 uvas

# Solicitar al usuario qué producto está buscando,
# si está disponible, pedir la cantidad, venderlo y mostrar el inventario

# Crear un nuevo diccionario con 3 productos, agregarlos al diccionario original

# Calcular el número total de productos en el inventario

"""

inventario = {"manzanas": 10, "naranjas": 5, "peras": 8}

# Agregar 5 manzanas más al inventario
# inventario["manzanas"] = inventario["manzanas"] + 5
inventario["manzanas"] += 5
print(inventario)

# Se vendieron 3 naranjas, actualizar el inventario
inventario["naranjas"] -= 3
print(inventario)

# Se agregaron 5 uvas
inventario["uvas"] = 5
print(inventario)

# Solicitar al usuario qué producto está buscando,
# si está disponible, pedir la cantidad, venderlo y mostrar el inventario
entrada = input("Qué desea comprar? ")
if entrada in inventario:
    cantidad = int(input("Cuántas unidades desea comprar? "))
    if cantidad > inventario[entrada]:
        print("No hay suficientes unidades disponibles")
    else:
        inventario[entrada] -= cantidad
        print(f"Usted ha comprado {cantidad} unidades de {entrada}.")
        print(f"Quedan {inventario[entrada]} unidades de {entrada} disponibles.")
else:
    print("El producto no se encuentra disponible.")

# Crear un nuevo diccionario con 3 productos, agregarlos al diccionario original
mas_productos = {
    "limones": 12,
    "sandías": 3,
    "melones": 5,
}

inventario.update(mas_productos)
print(inventario)

# Calcular el número total de productos en el inventario
total_productos = sum(inventario.values())
print(f"Número total de productos en el inventario:", total_productos)