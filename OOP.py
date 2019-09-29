# Nicolás Troncoso notes about Object Oriented Programming

"""
Python es un lenguaje orientado a objetos.
Un objeto se define como una entidad que tiene métodos y atributos particulares, los cuales son creados dentro de una Clase.
Por lo tanto una Clase contiene todo lo necesario para que un objeto de se genere.
Una Clase encapsula variables, como atributos; y funciones, como métodos.
Para acceder tanto a atributos como métodos, se realiza a traǘes de la sintásis de punto.
"""


"""
La creación de una clase tiene una estructura similar en otros lenguajes de programación, ya que no sirve solamente encapsular variables y funciones, y cambiarles el nombre, se debe pensar conceptualmente diferente.

La estructura llamada Constructor permite inicializar la clase, en esta estructura se asignan valores a los atributos y también se puedenincorporar otras operaciones que sean necesarias cuando el objeto está siendo creado
"""

"""
Estructura de una Clase
nombre es importante notar que el nombre es con mayúscula
En este ejemplo la clase tiene un solo atributo llamado x el cual acederemos por medio del punto . una vez creado el objeto obj. Por medio del Csontructor definimos ese valor cada vez que inicializamos una variable de tipo Clase.
El primer parámetro de cada función dentro de una clase debe ser este "self", su nombre es por convención.
También por convención las clases se escriben en un arcivo independiente.
"""
# clase MiClase
class MiClase:
    # el Constructor se define igual que cualquier función, con la diferencia que se llama __init__ y su primer parámetro es self.
    def __init__(self, valor):
        self.valor = valor

obj = MiClase(5)
print(obj.valor)

"""
Se pueden modificar los atributos de un objeto sobre escribiendo.
También se pueden borrar atribujos y objetos completos por medio de la palabra del
"""
obj.valor = 10
print(obj.valor)
del obj.valor
# la siguiente línea dará un error si la ejecutamos
# print(obj.valor)
obj2 = MiClase(100)
print(obj2.valor)
del obj2

"""
Una clase típica de calculadora tiene métodos:
Suma, Resta, Multiplicación, División.
Crea una clase de alumno, que tenga nombre completo, tres asignatiras, con 10 notas cada una, y la posibilidad de saber el promedio de final en cada asignatura y el promedio final.
"""
