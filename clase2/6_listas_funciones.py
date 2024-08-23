# Funciones de las listas

serie_fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# count(elemento)
print(serie_fibonacci.count(1))

# index(elemento)
print(serie_fibonacci.index(144))

# append()
serie_fibonacci.append(233)
print(serie_fibonacci)

# remove(elemento)
serie_fibonacci.remove(144)
if 144 in serie_fibonacci:
    serie_fibonacci.remove(144)
print(serie_fibonacci)

# insert()
serie_fibonacci.insert(0, "principio")
print(serie_fibonacci)

# pop()
serie_fibonacci.pop()
print(serie_fibonacci)
lo_quitado = serie_fibonacci.pop()
print(serie_fibonacci, lo_quitado)

# pop(indice)
serie_fibonacci.pop(3)  # quita el elemento en la posición 3: el 2
print(serie_fibonacci)

# extend(iterable)
mas_numeros = [233, 377, 610, 987, 1597]
serie_fibonacci.extend(mas_numeros)
print(serie_fibonacci)

# sort()
numeros = [1, 10, 4, 76, -1000]
numeros.sort()  # ordena la lista de menor a mayor
print(numeros)

# reverse()
numeros.reverse()  # invierte el orden de la lista
print(numeros)

# clear()
numeros.clear()  # vacía la lista
# numeros = []  # vacía la lista (otra forma, pero se aconseja la otra)
print(numeros)

