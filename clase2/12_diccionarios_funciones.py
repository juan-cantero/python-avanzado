# Funciones de diccionarios

diccionario = {"nombre": "Juan", "edad": 30, "ciudadanías": ["España", "Italia"]}

# *** get()
nombre = diccionario.get("nombre")  # diccionario["nombre"]
# print(nombre)
# apellido = diccionario.get("apellido")
apellido = diccionario.get("apellido", "No existe el valor")
# apellido = diccionario["apellido"]  # ¡Esto generará un KeyError si "apellido" no está en el diccionario!
# print(apellido)

# *** update(diccionario)
diccionario.update({"nombre": "Pedro", "apellido": "García", "altura": 1.75})
# print(diccionario)

# *** pop(clave)
diccionario.pop("edad")
# print(diccionario)

# *** keys()
print(diccionario.keys())

# *** values()
print(diccionario.values())

# *** items()
print(diccionario.items())

# *** clear()
diccionario.clear()
print(diccionario)