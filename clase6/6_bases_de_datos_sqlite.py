import sqlite3

conexion = sqlite3.connect("base.db")
cursor = conexion.cursor()


def crear_tabla_pais():
    cursor.execute("""
        CREATE TABLE Pais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    print("Tabla creada")


def crear_tabla_producto():
    cursor.execute("""
        CREATE TABLE Producto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE
        )
    """)
    print("Tabla creada")


def crear_tabla_cliente():
    cursor.execute("""
    CREATE TABLE Cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        nacimiento TEXT,
        pais_origen_id INTEGER REFERENCES Pais(id) ON DELETE SET NULL
        )
    """)
    print("Tabla creada")


def crear_tabla_venta():
    cursor.execute("""
    CREATE TABLE Cliente_Producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER REFERENCES Cliente(id) ON DELETE CASCADE,
        producto_id INTEGER REFERENCES Producto(id) ON DELETE CASCADE
        )
    """)
    print("Tabla creada")


def crear_paises():
    sql = "INSERT INTO Pais (nombre) VALUES (?)"
    # cursor.execute(sql, ("Argentina",))
    paises = ["Brasil", "Chile", "México", "Ecuador", "Colombia", "Uruguay"]
    for pais in paises:
        cursor.execute(sql, (pais,))
    conexion.commit()
    print("Paises creados")


def ver_paises():
    cursor.execute("SELECT * FROM Pais")
    print(cursor.fetchall())
    # print(cursor.fetchone())  # devuelve una tupla
    # print(cursor.fetchmany(3))  # devuelve una lista de tuplas


def crear_productos():
    productos = [("azúcar",), ("leche",), ("queso",)]
    sql = "INSERT INTO Producto (nombre) VALUES (?)"
    cursor.executemany(sql, productos)
    conexion.commit()
    print("Productos creados")


def ver_productos():
    cursor.execute("SELECT * FROM Producto")
    items = cursor.fetchall()
    for item in items:
        print(item[0], item[1])


def crear_clientes():
    print("CREANDO CLIENTE")

    nombre = input("Nombre: ")
    if nombre == "":
        nombre = None
    apellido = input("Apellido: ")
    if apellido == "":
        apellido = None
    nacimiento = input("Fecha de nacimiento (aaaa-mm-dd): ")

    # SELECT
    print("País de origen:")
    cursor.execute("SELECT * FROM Pais")
    items = cursor.fetchall()
    for item in items:
        print(f"\t{item[0]}: {item[1]}")

    while True:
        entrada = int(input("Seleccione opción: "))
        if entrada in [x[0] for x in items]:
            break
        else:
            continue
    pais_origen_id = entrada

    # INSERT
    sql = "INSERT INTO Cliente (nombre, apellido, nacimiento, pais_origen_id) VALUES (?,?,?,?)"
    cursor.execute(sql, (nombre, apellido, nacimiento, pais_origen_id))
    conexion.commit()
    print("Cliente creado")


def ver_clientes():
    cursor.execute("""
            SELECT Cliente.id, Cliente.nombre, apellido, nacimiento, Pais.nombre
            FROM Cliente INNER JOIN Pais ON Cliente.pais_origen_id = Pais.id
        """)
    items = cursor.fetchall()
    encabezado = (
        f"{'ID':<5} | {'NOMBRE':<10} | {'APELLIDO':<15} | {'NACIMIENTO':<15} | {'PAIS ORIGEN':<15}"
    )
    print(encabezado + "\n" + len(encabezado) * "=")
    for item in items:
        print(f"{item[0]:<5} | {item[1]:<10} | {item[2]:<15} | {item[3]:<15} | {item[4]:<15}")


def crear_venta():
    print("CLIENTE COMPRA PRODUCTO")
    # SELECT
    print("Clientes:")
    cursor.execute("SELECT * FROM Cliente")
    items = cursor.fetchall()
    for item in items:
        print(f"\t{item[0]}: {item[1]} {item[2]}")

    while True:
        entrada = int(input("Seleccione opción: "))
        if entrada in [x[0] for x in items]:
            break
        else:
            continue
    if entrada == "":
        entrada = None
    cliente_id = entrada

    print("Productos:")
    cursor.execute("SELECT * FROM Producto")
    items = cursor.fetchall()
    for item in items:
        print(f"\t{item[0]}: {item[1]}")

    while True:
        entrada = int(input("Seleccione opción: "))
        if entrada in [x[0] for x in items]:
            break
        else:
            continue
    if entrada == "":
        entrada = None
    producto_id = entrada

    # INSERT
    sql = "INSERT INTO Cliente_Producto (cliente_id, producto_id) VALUES (?,?)"
    cursor.execute(sql, (cliente_id, producto_id))
    conexion.commit()
    print("Cliente - Producto creado")


def main():
    # crear_tabla_pais()
    # crear_tabla_producto()
    # crear_tabla_cliente()
    # crear_tabla_venta()
    # crear_paises()
    # ver_paises()
    # crear_productos()
    # ver_productos()
    # crear_clientes()
    # ver_clientes()
    crear_venta()


main()
