# Cadenas

texto = "hola"
for letra in texto:
    print(letra)

# Tuplas, listas, conjuntos

lista = ["a", "b", "c", "d"]
for elemento in lista:
    print(elemento)

# Diccionarios
diccionario = {
    "nombre": "Augusto",
    "edad": 25,
}

print("DICCIONARIOS - CLAVE")
for clave in diccionario.keys():
    print(clave)

print("DICCIONARIOS - VALOR")
for valor in diccionario.values():
    print(valor)

print("DICCIONARIOS - CLAVE VALOR")
for clave, valor in diccionario.items():
    print(f"La clave es {clave}. Su valor es {valor}")