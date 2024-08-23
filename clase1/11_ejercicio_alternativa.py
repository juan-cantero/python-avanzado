# Ingreso de datos
edad = int(input("Ingrese la edad del cliente: "))
antiguedad = int(input("Ingrese la antigüedad en el sistema financiero (en años): "))
ingreso = float(input("Ingrese el ingreso mensual del cliente: "))

# Operaciones
# Uso de la técnica de bandera o flag
# 1. Se inicializa la variable bandera en False
# 2. Se verifica la condición, si se cumple se cambia el valor de la bandera a True
# 3. Se utiliza el valor de la bandera para tomar decisiones

credito_aprobado = False  # Bandera o flag

if edad >= 18:
    if antiguedad >= 3 and ingreso >= 2500:
        credito_aprobado = True
    elif ingreso >= 4000:
        credito_aprobado = True

# Salida
if credito_aprobado:  # if credito_aprobado == True
    print("El crédito ha sido aprobado.")
else:
    print("El crédito no ha sido aprobado.")