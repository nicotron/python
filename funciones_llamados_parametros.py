# Nicolás Troncoso notes about funcionts

"""
Funciones son estructuras de código que solo corren una vez que se llaman, en el llamado se puede ingresar información de manera de parámetros.
De esta forma existe la modularidad dentro de Python y con ello, economía de espacio y memoria, reutilización sin perdida y diversidad dentro del ámbitos totales de los parámetros
"""

#palabra clave para construir una funcion def
def mi_funcion():
    print("Resultado de una función sin parámetros")

"""
Los parámetros son variables que ingresan en los paréntesis siguientes al nombre de la función, la cantidad de parámetros da más diversidad a la función, y el orden debe ser respetado absolutamente
"""

#funcion con parámetros para saludar con nombre propio
def hola_soy(nombre):
    print("Hola, mi nombre es " + nombre)

hola_soy("Nicolás")
hola_soy("María José")
hola_soy("Elena")

"""
Es posible generar que la misma función pueda responder a un llamado en donde no hay parámetros
"""
#funcion con parámetros para saludar con nombre propio
def hola_soy(nombre = "Julia"):
    print("Hola, mi nombre es " + nombre)

hola_soy("Nicolás")
hola_soy("María José")
hola_soy("Elena")
hola_soy()

"""
Es posible que un parámetro sea una lista ordenada para esto debemos iterar dentro de la función
"""
#funcion con parámetro lista
def hola_soy(lista):
    for nombre in lista:
        print("Hola, mi nombre es " + nombre)

listadeNombres = ["Nicolás", "María José", "Elena"]
hola_soy(listadeNombres)

"""
Otra característica de las funciones es que pueden devolver la información luego de un proceso. El modelo mental matemático de f(x) en donde el resultado variaba dependiendo el valor de x, es lo que se traspasa a esta variación de las listas ordenadas
"""
# funcion que devuelve el doble de su valor
def elDoble(numero):
    return 2*numero

print(elDoble(2))
print(elDoble(10))

# funcion que devuelve el texto de cualquier numero que entre
def numero_texto(numero):
    return  str(numero)

print(numero_texto(2) + " ahora es el texto 2")
print(numero_texto(10) + " ahora es el texto 10")
