"""
A partir de la siguiente lista:
matriz:

matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

Sumar los elementos de cada lista y agregar el resultado
al final de cada lista. Debe quedar de la siguiente forma:

matriz = [
    [1, 20, 3, 24],
    [4, 3, 2, 9],
    [10, 4, 1, 15],
]
Puedes usar la función sum(<lista>)
>>> print(matriz)
[[1, 20, 3, 24], [4, 3, 2, 9], [10, 4, 1, 15]]
"""
matriz = [
    [1, 20, 3],
    [4, 3, 2],
    [10, 4, 1],
]

# print(len(matriz))

# Solución 1:
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
print(matriz)

# Solucion 2:
# matriz[0] += [sum(matriz[0])]
# matriz[1] += [sum(matriz[1])]
# matriz[2] += [sum(matriz[2])]
# print(matriz)

# Solución 3:
# matriz[0] += [matriz[0][0] + matriz[0][1] + matriz[0][2]]
# matriz[1] += [matriz[1][0] + matriz[1][1] + matriz[1][2]]
# matriz[2] += [matriz[2][0] + matriz[2][1] + matriz[2][2]]
# print(matriz)