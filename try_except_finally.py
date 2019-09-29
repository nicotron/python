# Nicolás Troncoso notes about try, except, finally

"""
Errores en los programas como por ejemplo, un cálculo que no existe; ingresar texto en variables numéricas, etc, hacen caer al programa. Existe una estructura que puede manejar el programa en caso de error y no cometer un "Error en tiempo de ejecución", así el programa seguirá con la ejecución del resto del código.

Si tengo una instrucción para ingresar información y existe la posibilidad de que se ingrese otro, primero debo saber cual es el error, mientras diseño el programa

"""
# imprimir  x da error de tipo NameError: name 'x' is not defined
# no existe la variable x
# print(x)


"""
Para esto puedo indentar esa línea que se ejecutará, dentro de un try: que la primera parte de la estructura de manejo de errores. Como ya sabemos que print(x) dará error podemos continuar con el manejo de ese error
"""

# imprimir x da error de tipo NameError: name 'x' is not defined
# no existe la variable x
try:
  print(x)
except NameError:
  print("No existe la variable x")


"""
De esta manera si hay un error, será manejado y el programa seguirá en ejecución. Si en el caso que no exista error, el programa sigue sin problemas, es posible que se requiera ejecutar más líneas cuando se utilice try, para esto es necesario escribir finally.
Es la última declaración en la estructura de control de errores, finally permite cerrar el try.
"""

try:
    print(x)
except NameError:
    print("No existe la variable x")
finally:
    print("Fin del proceso")
