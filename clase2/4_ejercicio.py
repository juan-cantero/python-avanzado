"""
Tuplas. Ejercicio 1

Crear una tupla que represente un cajón de verduras
Crear otra tupla que represente un cajón de frutas
Crear una tupla llamada camion, que contenga los dos cajones anteriores
Mostrar los datos
"""

cajon_verduras = ("zanahorias", "papas", "cebollas", "lechugas")
cajon_frutas = ("manzanas", "naranjas", "peras", "bananas")
camion = (cajon_verduras, cajon_frutas)

verduras, frutas = camion
print(f"Cajón de verduras: {verduras}")
print(f"Cajón de frutas: {frutas}")

camion1 = cajon_frutas + cajon_verduras  # Concatenando las tuplas
camion2 = (*cajon_verduras, *cajon_frutas)  # Desempacando las tuplas
print(f"Camión 1: {camion1}")
print(f"Camión 2: {camion2}")