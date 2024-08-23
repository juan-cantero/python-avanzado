# Tuplas

# *** Definición: Colección inmutable de objetos

# *** Declaración
tupla = (1, 2, 3, "hola", 4.5, True)
# tupla = ()  # tupla vacía
# tupla = (1,)  # tupla de un solo elemento
print(tupla)

# *** Representación
print(type(tupla))  # tuple

# *** Longitud
print(len(tupla))

# *** Acceso a elementos
print(tupla[0])  # 1
hola = tupla[3] 
print(hola)

# *** Crear elementos
# no tiene funciones

# *** Actualizar elementos
# no tiene funciones

# *** Eliminar elementos
# no tiene funciones

# Desempaquetado de tuplas
numeros_primos = (2, 3, 5)
# primero = numeros_primos[0]
# segundo = numeros_primos[1]
# tercero = numeros_primos[2]
# print(primero, segundo, tercero)
primero, segundo, tercero = numeros_primos
print(primero, segundo, tercero)