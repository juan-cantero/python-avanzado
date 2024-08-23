# Listas

# *** Definición de listas: Colección mutable y ordenada de elementos.

# *** Declaración
lista = [1, 2, 3, "hola", 4.5, True]
# lista = []  # lista vacía
# lista = [1]  # lista de un solo elemento
print(lista)

# *** Representación
print(type(lista))  # list

# *** Longitud
print(len(lista))

# *** Acceso a elementos
print(lista[0])  # 1
hola = lista[3] 
print(hola)

# *** Crear elementos
lista += [None]
print(lista)

# *** Actualizar elementos
lista[0] = 1000
print(lista)

# *** Eliminar elementos
del lista[-1]
print(lista)

# Desempaquetado de listas
numeros_primos = [2, 3, 5]
primero = numeros_primos[0]
segundo = numeros_primos[1]
tercero = numeros_primos[2]
print(primero, segundo, tercero)
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)