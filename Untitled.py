# Semana 3 unidad 7: control de ciclos for while loops, y elementos ordenados

# While loop == Mientras
# For loop

condicion = 1

while condicion < 10:
    print("Dentro del While loop")

print("Siguente línea del programa")


# --------------------------
# Semana 3 unidad 7: control de ciclos for while loops, y elementos ordenados
# Semana 3 unidad 7: control de ciclos for while loops, y elementos ordenados

# While loop == Mientras
# For loop

condicion = 0

while condicion < 10:
    condicion += 1
    if (condicion == 5):
        continue
    else:
        print(condicion , "Dentro del While loop")


print("Siguente línea del programa")

# For loop
# intera en secuencia según tipo de variable list, tuple, diccionary, set, o string.

lista = [6,0,0,8,0,0,10]
for elementos in lista:
    print(elementos)

for elementos in "lista":
    print(elementos)

for elementos in lista:
    print(elementos)
    if (elementos == 8):
        break

for elementos in lista:
    if elementos == 8:
        continue
    print(elementos)


colores = ["rojo", "blanco", "cafe", "azul", "negro", "cafe"]
for color in colores:
    print(color)
print("------------")

#agregar un color
colores.append("amarillo")
for color in colores:
    print(color)
print("------------")

# remover por el lugar de la lista.
ultimoElemento = len(colores)
print(ultimoElemento)
colores.pop(ultimoElemento-1)
for color in colores:
    print(color)
print("------------")

# remover un elemento = cafe
colores.remove("cafe")
for color in colores:
    print(color)
print("------------")
