# Funciones de conjuntos

serie_fibonacci = {1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144}

# add(elemento) - Agrega un elemento al conjunto
serie_fibonacci.add(233)
print(serie_fibonacci)

# pop() - Elimina y devuelve un elemento aleatorio del conjunto
cual_quito = serie_fibonacci.pop()
print(serie_fibonacci, cual_quito)
cual_quito = serie_fibonacci.pop()
print(serie_fibonacci, cual_quito)
cual_quito = serie_fibonacci.pop()
print(serie_fibonacci, cual_quito)

# remove(elemento) - Elimina un elemento específico del conjunto.
# Si el elemento no está presente, lanza una excepción KeyError
serie_fibonacci.remove(34)
# serie_fibonacci.remove(34)  # error
print(serie_fibonacci)

# discard(elemento) - Elimina un elemento específico del conjunto
# Si el elemento no está presente, no lanza un error
serie_fibonacci.discard(89)
serie_fibonacci.discard(89)
print(serie_fibonacci)

# union(conjunto) - Devuelve un nuevo conjunto que es la unión de dos conjuntos
conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}
union_AB = conjunto_A.union(conjunto_B)
print(union_AB)

# intersection(conjunto) - Devuelve un nuevo conjunto que es la intersección de dos conjuntos
conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}
interseccion_AB = conjunto_A.intersection(conjunto_B)
print(interseccion_AB)

# symmetric_difference(conjunto)
conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}
print(conjunto_A.symmetric_difference(conjunto_B))


# update(conjunto) - Actualiza el conjunto con la unión de otro conjunto
conjunto_A.update(conjunto_B)
print(conjunto_A, conjunto_B)

# diffence(conjunto) - Devuelve un nuevo conjunto que contiene los elementos 
# que están en el primer conjunto pero no en el segundo
conjunto_A = {1, 2, 3}
conjunto_B = {3, 4, 5}
diferencia_AB = conjunto_A.difference(conjunto_B)
print(diferencia_AB)

