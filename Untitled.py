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


# ------------------------------------------------------------------------------
# Semana 9 Encapsulamiento, modularidad, economía
# Funciones y parámetros


def nombre_edad(edad=0, nombre="sin nombre"):
    print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años.")


nombre_edad("Nicolas", 25)
nombre_edad("Elena", 2)
nombre_edad("Maria", 19)

# ------------------------------------------------------------------------------
# funcion que devuelve el doble de su valor


def el_doble(numero):
    return 2*numero


d2 = el_doble(2)
d10 = el_doble(10)
print(d2)
print(d10)

# Semana 10 Programación modular


def saludo(nombre):
    print("Hola mi nombre es " + nombre)


def nombre_edad(edad=0, nombre="sin nombre"):
    print("Mi nombre es " + nombre + " y tengo " + str(edad) + " años.")

import creacion_textos

creacion_textos.saludo("nicolas")
