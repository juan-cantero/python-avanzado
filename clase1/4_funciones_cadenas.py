cadena = " esta es una prueba con Pithon  🔥 🔥  "
#         012345678      
print("Longitud de cadena", len(cadena))

print(cadena.upper())
print(cadena.lower())
print(cadena.strip())
print(cadena.strip().capitalize())
print(cadena.count(" "))
print(cadena.strip().count(" "))
print(cadena.strip().count("es"))
print(cadena.title())
print("0123456789".isdigit())
print("0123456789aaa".isdigit())
print(cadena.replace("e", "3"))
print(cadena.replace("Pithon", "Python"))
print(cadena.find("t"))

indice = cadena.find("P")
print(cadena[indice])
print(cadena[0:3])
print(cadena[1:3])
print(cadena[1:])
print(cadena.strip()[-1])
print(cadena[1:])
print(cadena[0:10:2]) # inicio : paro : paso
print(cadena[::-1])
