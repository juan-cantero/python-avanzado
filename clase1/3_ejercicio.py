"""
Consigna: mostrar por la terminal el mensaje:
"La función upper() sirve para poner en mayúsculas las cadenas"
La variable comando tiene 7 caracteres"
Para el primer print, usar las 3 formas concatenación, +, coma, f-string
El valor upper() debe ser guardado en una variable
"""

comando = "upper()"
print("La función " + comando + " sirve para poner en mayúsculas las cadenas")
print("La función", comando, "sirve para poner en mayúsculas las cadenas")
print(f"La función {comando} sirve para poner en mayusculas las cadenas")
# Esta última es cada vez menos usada
print("La función {} sirve para poner en mayusculas las cadenas".format(comando))

