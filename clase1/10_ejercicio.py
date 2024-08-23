"""
Una empresa debe aprobar o no un crédito para un cliente.
Las condiciones son las siguientes:
    - El cliente debe ser mayor de edad.
    - Debe tener una antigüedad en el sistema financiero mínimo de 3 años
    y un ingreso mayor a 2500 dólares.
    - En caso de que no tenga la antigüedad suficiente,
    su ingreso mensual debe ser como mínimo 4000 dólares.
Si no cumple ninguna de las condiciones, no se aprueba el crédito.
"""

# Ingreso de datos
edad = int(input("Ingrese la edad del cliente: "))
antiguedad = int(input("Ingrese la antigüedad en el sistema financiero (en años): "))
ingreso = float(input("Ingrese el ingreso mensual del cliente: "))

# Operaciones
mayor_edad = edad >= 18
caso_1 = mayor_edad and (antiguedad >= 3) and (ingreso > 2500)
caso_2 = mayor_edad and (ingreso >= 4000)

# Salida de datos
if caso_1 or caso_2:
    print("El crédito se aprueba.")
else:
    print("El crédito no se aprueba.")