# Conjuntos

# *** Definición de conjuntos: Colección mutable de elementos, únicos, desordenados

# *** Declaración
conjunto = {1, 2, 3, "hola", 4.5, True, 1, 2}
# conjunto = set()  # conjunto vacío
# conjunto = {1}  # conjunto de un solo elemento
print(conjunto)

# *** Representación
print(type(conjunto))  # 

# *** Longitud
print(len(conjunto))

# *** Acceso a elementos
# print(conjunto[0])  # Error: 'set' object is not subscriptable

# *** Crear elementos
# Podemos crear pero con funciones

# *** Actualizar elementos
# Podemos actualizar pero con funciones

# *** Eliminar elementos
# Podemos eliminar pero con funciones

# # Desempaquetado de conjuntos
numeros_primos = {2, 3, 5}
# > Tener cuidado porque los conjuntos son una colección desordenada
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)