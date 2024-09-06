"""
Manejo de errors con try-except

try:
    bloque de código que puede generar un error
except:
    bloque de código que se ejecuta si hay un error en el bloque try
else:
    (opcionales) bloque de código que se ejecuta si NO HAY un error en el bloque try
finally:
    (opcionales) bloque de código que se ejecuta SIEMPRE, haya o no haya un error en el bloque try
"""

try:
    numero_1 = float(input("Primer número: "))
    numero_2 = float(input("Segundo número: "))
    division = numero_1 / numero_2
except ValueError:
    print("Error: Debes ingresar un número.")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except KeyboardInterrupt:
    print("\nInterrumpido por el usuario")
except Exception as e:
    print("Error:", repr(e))
else:
    print("La división es:", division)
# finally:
#     print("Fin del programa")
