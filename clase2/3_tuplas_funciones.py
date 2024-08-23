# Funciones de tuplas

serie_fibonacci = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144)

# count()

print(serie_fibonacci.count(1))
print(serie_fibonacci.count(2))
print(serie_fibonacci.count(10))

# index()

valor = 13
indice = serie_fibonacci.index(valor)
print(f"El índice del valor {valor} en la tupla es {indice}")