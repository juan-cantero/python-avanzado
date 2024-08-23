"""
Tienes dos listas de invitados a una fiesta. 
La primera lista contiene los nombres de los invitados confirmados 
que asistirán a la fiesta, 
y la segunda lista contiene los nombres de las personas que se unieron 
a la fiesta en el último minuto sin confirmar previamente. 
Tu tarea es usar conjuntos para realizar las siguientes operaciones:

1. Encuentra el conjunto de invitados únicos, es decir, 
todos los invitados que asistirán a la fiesta, independientemente de si confirmaron o no.
2. Encuentra el conjunto de personas que confirmaron su asistencia, 
pero al final no asistieron a la fiesta.
3. Encuentra el conjunto de personas que se unieron a la fiesta sin confirmar previamente.

# Lista de invitados confirmados
invitados_confirmados = {"Ana", "Carlos", "Luis", "Marta", "Pedro"}

# Lista de personas que se unieron a la fiesta sin confirmar
invitados_sorpresa = {"Luis", "Marta", "Javier", "Sofía", "Beatriz"}
"""

# Lista de invitados confirmados
invitados_confirmados = {"Ana", "Carlos", "Luis", "Marta", "Pedro"}

# Lista de personas que se unieron a la fiesta sin confirmar
invitados_sorpresa = {"Luis", "Marta", "Javier", "Sofía", "Beatriz"}

# 1. Invitados únicos que asistirán a la fiesta
invitados_totales = invitados_confirmados.union(invitados_sorpresa)
print("Todos los que asistieron:", invitados_totales) 

# 2. Personas que confirmaron pero no asistieron
no_asistieron = invitados_confirmados.difference(invitados_sorpresa)
print("Confirmaron pero no asistieron:", no_asistieron)

# 3. Personas que se unieron a la fiesta sin confirmar
sin_confirmar = invitados_sorpresa.difference(invitados_confirmados)
print("Se unieron sin confirmar:", sin_confirmar)