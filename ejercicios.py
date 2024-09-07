"""
- Crear una clase Persona
  que contenga los atributos:
    - nombre: str
    - edad: str
- Crear 3 instancias de Persona
- Mostrar por pantalla un mensaje más elaborado
"""

class Persona:
  def __init__(self, nombre, edad) ->None:
    self.nombre = nombre
    self.edad = edad
  def __str__(self):
    return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} anios"


persona1 = Persona("Cintia", 18)
persona2 = Persona("Maria", 23)
persona3 = Persona("Fernando", 25)

print(persona1)
print(persona2)
print(persona3)

class Especie:
    def __init__(self, nombre: str):
        self.nombre = nombre
class Animal:
    def __init__(self, especie: Especie, nombre: str, sonido: str) -> None:
        self.especie = especie
        self.nombre = nombre
        self.sonido = sonido
    def hacer_sonido(self) -> None:  # método de instancia
        print(f"{self.nombre} hace '{self.sonido}'")
    def andar(self, pasos: int = 0) -> None:
        print(f"{self.nombre} ha andado {pasos} pasos")



canis = Especie("Canis")
felis = Especie("Felis")
animal_1 = Animal(canis, "Fido", "Guau")
animal_2 = Animal(felis, "Garfield", "Miau")
animal_1.hacer_sonido()
animal_2.hacer_sonido()
animal_1.andar(5)

"""
✨ EJERCICIO ✨
Utilizar las clases Especie y Animal
Agregar a Animal el método de instancia: andar()
andar() recibe un entero, son los pasos que puede dar el animal
Cuando se invoque andar(), se mostrará por pantalla el nombre del animal,
el nombre de la especie y cuántos pasos anduvo
Si no agregan 'pasos' , se entenderá que el animal no dio pasos.
"""


"""
✨ EJERCICIO ✨
A partir de la siguiente clase
class Usuario:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
Crear una variable de clase que consista en una lista de instancias de la misma clase Usuario
(dentro del método constructor llamar a la variable de clase 
y con append agregar el mismo objeto: self)
"""

class Usuario:
   usuarios = []

   def __init__(self, username: str, password: str) -> None:
       self.username = username
       self.password = password
       Usuario.usuarios.append(self)


admin = Usuario("admin", "admin")
for user in Usuario.usuarios:
    print(user.username)