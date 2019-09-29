# Nicolás Troncoso notes about recursion and iteration

"""
Recursión es una estructura en donde dentro de las declaraciones que contiene una función, existe el llamado a la misma función, esto se diferencia de la programación iterativa (que es lo que hemos visto hasta ahora) representada en for loops.
Su estructura necesita iniciar con un caso base, para salir una vez que la recursión llegue al nivel más bajo.
Posterior a esto se declara la misma función con sus operaciones necesarias para que exista un momento en donde llegue ejecutarse el caso base.
Si esto no ocurre, es imposible salir de la función.
"""

# se define la función recursion()
# recibe un número y suma su valor hasta llegar a 1
def recursion(numero):
    # caso base, si llega al 1 devuelve 1
  if(numero <= 1):
      return 1
  # llamado a la función dentro de sí misma
  else:
      suma = numero + recursion(numero-1)
      # imprimir el valor es para depuración y ejemplo
      print(suma)
  return suma

# utilizando la recursión, si entregamos el valor 6, el primer valor que entrega es 1, luego 3 (1+2), luego 6 (3+(1+2)), ...
x = recursion(6)
print("resultado de recursión " + str(x))

"""
A diferencia las funciones iterativas son de mejor entendimiento ya que iterar desde un inicio a un final a través de una secuencia, es un modelo mental que podemos ver en la realidad, además la estructura para iterar la vimos en módulos anteriores, al incorporar los for loops en Python
"""

"""
Para crear funciones que iteren es necesario declarar un for loop dentro de la función
"""

# funcion iterativa
# recibe un numero y suma sus valores desde 0 hasta el numero ingresadp
def iterativa(numero):
    # variable con valor temporal en 0
    suma = 0
    for i in range(numero+1):
        suma += i
        # imprimir el valor es para depuración y ejemplo
        print(suma)
    return suma

# utilizando la función iterativa, entrega 1 y 3, con el ultimo resultado como
x = iterativa(2)
print("resultado de iteración " + str(x))

"""
La recursión es un proceso muy útil, pero debe ser ejecutado sabiendo la cantidad de niveles que se deberá bajar hasta llegar al caso base, en Python la demanda de recursos para funciones recursivas es más alto que en otros lenguajes de programación.

Es posible esrecbir funciones recursivas que no devuelvan un resultado, pero no es el foco de la utilización de este tipo de estructuras.
"""
