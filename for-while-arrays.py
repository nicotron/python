# código desde pP03 Control de flujo
# hacer comparaciones desde PSEint Mientras, Repetir, y Para

"""
 En Python existen dos tipos de loops, While loop y For loop.
 El While loop tiene la misma estructura que el Mientras en PSEint
 La sintaxis es la siguente:

 En donde debe existir una condición verdadera para que se ejecute el código indentado en el loop.
 Si no se cambia la condición, no se podrá salir del loop
"""

condicion = 1

while condicion < 10:
    print(condicion, " Texto dentro de la condición")
    condicion += 1
print("Fin del programa")

"""
Hay modificaciones al While loop para dar una mayor flexibilidad esta estructura.
La declaración Break permite detener el loop a pesar que la condición la que se ejecuta el verdadera
"""

# condicion = 1

# while condicion < 10:
#     print(condicion, " Texto dentro de la condición")
#     condicion += 1
#     # uso de declaración break
#     if(condicion == 4):
#         break
# print("Fin del programa")

condicion = 1

while condicion < 10:
    condicion += 1
    # uso de declaración break
    if(condicion == 4):
        continue
    print(condicion, " Texto dentro de la condición")
print("Fin del programa")


"""
También se puede utilizar else al igual que en la estructura condicional, se escribe luego de terminado el código del While loop, y esta se ejecuta una sola vez
"""

condicion = 1

while condicion < 10:
    condicion += 1
    # uso de declaración break
    if(condicion == 4):
        continue
    print(condicion, " mientras la condicion While es verdadera")
else:
    print("Esta condición cuando el While es falso")
print("Fin del programa")



"""
Otro tipo de loop es el for loop, el cual itera sobre una secuencia, esta secuencia puede ser del tipo, list, tuple, diccionary, set, o string.
A diferencia de otras estructuras de for loop en otros lenguajes de programación el for loop en Python sirve como un método iterador, por lo cual se ejecutarán una serie de declaraciones, una por cada elemento de la lista, tuple, set, etc
El siguente código muestra los elementos de una lista
"""

# iterar por los elementos de una lista
lista = [6,0,0,8,0,0,100]
# iterar por todos ellos
for elementos in lista:
    print(elementos)


# iterar por los elementos de un string
# iterar por todos ellos
for elementos in "lista":
    print(elementos)


"""
Se puede utilizar la declaración break para salir del loop una vez que la condición creada sea verdadera
"""

# iterar por los elementos de una lista
lista = [6,0,0,8,0,0,100]
# iterar por todos ellos
for elementos in lista:
    print(elementos)
    if elementos == 8:
        print("salir")
        break


"""
De la misma forma se puede implementar la declaración continue
"""
# iterar por los elementos de una lista
lista = [6,0,0,8,0,0,100]
# iterar por todos ellos
for elementos in lista:
    if elementos == 8:
        continue
    print(elementos)


# ==============================================================================

"""
Elementos Ordenados
Son variables que almacenan multiples valores en sí misma.
Se crean con corchetes después del nombre de la variable, y en su interior se pueden almacenar las variables.
Son de tamaño dinámico por lo que para agregar o disminuir, existen los métodos:
apped() para agregar
pop() para eliminar por índicie
remove() para eliminar por nombre del elemento dentro de la lista
"""

# creacion de una lista de colores
colores = ["rojo", "blanco", "cafe", "azul", "negro"]
# iterar por todos los elementos de la lista
for color in colores:
    print(color)
# agregando un color
colores.append("amarillo")
# iterar por todos los elementos de la lista
for color in colores:
    print(color)
# remover el ultimo elemento, necesitamos saber el tamaño para luego saber la ultima posicion
ultimo = len(colores)
colores.pop(ultimo-1)
# remover el elemento "negro"
colores.remove("negro")
# iterar por todos los elementos de la lista
for color in colores:
    print(color)

"""
Existen una serie de otros métodos dentro de la estructura de Elementos Ordenados:
append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()
"""
