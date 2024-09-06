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
#     print("Fin del programa

def ingresar_numero():  
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
    
    except ValueError:
        print("Error: Debes ingresar un número.")
        return None,None
    
    return n1, n2


def dividir(n1, n2):
    if n2 == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    return n1 / n2

#resultado_division = dividir(n1, n2)

#
# print("La división es:", resultado_division)


def main():
    n1, n2 = ingresar_numero()
    resultado_division = dividir(n1, n2)
    print("La división es:", resultado_division)