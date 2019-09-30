# Nicolás Troncoso notes about OOP Inheritance
"""
Herencia (Inheritance) permite definir una clase que hereda los atributos y métodos de otra clase, en esta figura, existe la clase Padre (Parent), y la clase Hijo (Child).
class Padre es de quién se hereda
class Hijo es quién hereda

Clase Padre:
Cualquier clase se puede convertir en una clase padre, recibe su denominación de Padre al momento de ser referenciada en la clase Hijo
"""

# una clase cualquiera
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def nombreCompleto(self):
        print(self.nombre + " " + self.apellido)

persona1 = Persona("Elena", "Troncoso", 0.45)
persona1.nombreCompleto()


"""
Para crear una clase Hijo desde la clase Padre y entonces generar herencia entre clases, se debe hacer con la siguiente sintaxis:
class Hijo(Padre):

Si queremos que la clase no tenga ninguna diferencia con la clase de la que heredó propiedades, debemos declarar la palabra pass
"""

#clase Hijo(Padre) sin modificación de las características completas de la clase Padre
class Estudiante(Persona):
    pass

persona2 = Persona("Elena", "Troncoso", 0.45)
persona2.nombreCompleto()
estudiante1 = Estudiante("Nicolás", "Troncoso", 37)
estudiante1.nombreCompleto()


"""
Si la clase Hijo no tiene modificaciones, entonces no es óptimo realizar este proceso. La clase Estudiante debe tener otros atributos y métodos que la clase Persona, por lo que es necesario construirla como una clase normal, por ejemplo la carrera del Estudiante.
Entonces escribimos el atributo necesario dentro del Constructor, __init__() sobre escribe la función __init__() de la clase Padre, por lo que tenemos que hacer es llamar a esa función una vez estemos diseñando el Constructor
"""
# Crear una clase heredada por completo
# 1:4 El Constructor debe tener la misma cantidad de parámetros que la clase Padre menos el self- Persona(), luego los paámetros específicos de la clase
class Estudiante(Persona):
    def __init__(self, nombre, apellido, edad, carrera):
# 2:4 A través del método super() podemos decirdir qué atributos pasamos desde la clase Padre a Hijo.
# super() supone que es una sola clase desde la que se hereda
        super().__init__(nombre, apellido, edad)
# 3:4 Ahora podemos agregar los atributos específicos de la clase
# en este caso
        self.carrera = carrera

# 4:4 Finalmente podemos agregar métodos en la clase
# método para carrera
    def estudios(self):
        print(self.carrera)

# creación de un estudiante con nombre, apellido, edad, y carrera
estudianteCompleto = Estudiante("Estaban", "Riquelme", 24, "Botánica")
# método de la clase Persona heredado
estudianteCompleto.nombreCompleto()
# método de la clase Estudiante
estudianteCompleto.estudios()
