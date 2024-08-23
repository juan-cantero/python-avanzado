"""
Partiendo de:
cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"
Crea una nueva cadena con el siguiente contenido:
"PYTHON es un lenguaje de programación versátil"
Usar f-strings, y la función upper() con cadena_2
"""

cadena_1 = "versátil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programación"

cadena_final = f"{cadena_2.upper()} {cadena_3} {cadena_4} {cadena_1}"
print(cadena_final)