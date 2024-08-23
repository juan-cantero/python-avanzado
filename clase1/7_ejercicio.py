"""
A partir de dos variables llamadas nombre y edad:
crear una variable que almacene si se cumplen las siguientes condiciones,
y mostrar al usuario True o False:
    - nombre sea diferente de cuatro asteriscos ****
    - edad sea mayor que 5 y a su vez menor que 20
    - Que la longitud de nombre sea mayor o igual a 4 pero a la vez menor que 8
    - edad multiplicada por 3 sea mayor que 35
    - Debes ingresar los datos con input():
    - No debes usar funciones, condicionales, bucles o cualquier
    - otra instrucción que no hayamos visto
"""

# Ingresos
nombre = "Cintia"
edad = 12

# Operaciones
# x = (nombre != "****") and (edad > 5 and edad < 20) and (len(nombre) >= 4 and len(nombre) < 8) and (edad * 3 > 35)
validacion_nombre = nombre != "****"
validacion_nombre_len = len(nombre) >= 4 and len(nombre) < 8
validacion_edad = edad > 5 and edad < 20
validacion_edad_operacion = edad * 3 > 35
validar = (
    validacion_nombre
    and validacion_nombre_len
    and validacion_edad
    and validacion_edad_operacion
)


# Salida de datos
print(validar)