# Diccionarios

# *** Definición de diccionario: Colección mutable, desordenada y no indexada,
# de pares clave-valor. Las claves deben ser únicas e inmutables (cadenas, números, tuplas).

# *** Declaración
diccionario = {"nombre": "Juan", "edad": 30, "ciudadanías": ["España", "Italia"]}
# diccionario = {} # diccionario vacío
# diccionario = {1: "uno"}  # diccionario de un solo elemento
# print(diccionario)

# *** Representación
print(type(diccionario))  # dict

# *** Longitud
print(len(diccionario))

# # *** Acceso a elementos
# print(diccionario["nombre"])
# print(diccionario["edad"])
# print(diccionario["ciudadanías"])

# *** Crear elementos
diccionario["altura"] = 1.75
# print(diccionario)

# # *** Actualizar elementos
diccionario['edad'] = 31
# print(diccionario)

# # *** Eliminar elementos
# del diccionario["altura"]
diccionario["altura"] = None
# print(diccionario)

# # Desempaquetado de diccionarios
diccionario1 = {"nombre": "Juan", "edad": 30, "ciudadanías": ["España", "Italia"]}
diccionario2 = {"idiomas": ["español", "italiano", "inglés"]}
personas = {**diccionario1, **diccionario2}
print(personas)
