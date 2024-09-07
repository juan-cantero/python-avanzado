"""
✨ EJERCICIO ✨
Crea dos clases: Libro y Biblioteca.
    - La clase Libro debe tener los atributos titulo, autor y año.
    - La clase Biblioteca debe tener un atributo nombre y una lista de libros llamada libros.

- Implementa el método agregar_libro en la clase Biblioteca,
    que reciba un objeto Libro como parámetro y lo agregue a la lista de libros.
- Implementa el método eliminar_libro en la clase Biblioteca,
    que reciba un objeto Libro como parámetro y lo elimine de la lista de libros.
- Implementa el método listar_libros en la clase Biblioteca,
    que imprima en pantalla los libros disponibles en la biblioteca, mostrando el título, autor y año de cada libro.

- Crea varios objetos de la clase Libro y agrégalos a la biblioteca mediante el método agregar_libro.
- Llama al método listar_libros para mostrar los libros en la biblioteca.
- Elimina un libro de la biblioteca utilizando el método eliminar_libro.
- Vuelve a llamar al método listar_libros para mostrar los libros actualizados en la biblioteca.
"""


class Libro:
    def __init__(self, titulo: str, autor: str, año: int) -> None:
        self.titulo = titulo
        self.autor = autor
        self.año = año


class Biblioteca:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro) -> None:
        pass

    def eliminar_libro(self, libro: Libro) -> None:
        pass

    def listar_libros(self) -> None:
        pass


libro1 = Libro(titulo="El Principito", autor="Antoine Saint E.", año=1940)
libro2 = Libro(titulo="1984", autor="Orwel", año=1950)
libro3 = Libro(titulo="Órganon", autor="Aristóteles", año=-384)
