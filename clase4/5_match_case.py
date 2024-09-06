def prueba(listado: list) -> None:
    match listado:
        case []:
            print("La lista está vacía")
        case [x]:
            print(f"La lista tiene un elemento: {x}")
        case [x, y]:
            print(x + y)
        case [x, y, *resto]:
            print(f"La lista tiene más de dos elementos: {x}, {y}, y {len(resto)} más")
        case _:
            print("Esto no debería pasar jamás")
    ...


prueba([2, 4])
prueba([2, 4, 6])
prueba([])
prueba([2, 4, 6, 10, 10])
