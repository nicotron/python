# Nicolás Troncoso notes about modules

"""
Un módulo es los mismo a una biblioteca, tengo cada elemento a mi disposición, y como lo vimos anteriormente en las funciones, si ellas están bien escritas, y manejan correctamente errores, puedo ir construyendo un programa robusto que no tiene fallas, es diverso, y puede ser compartido o empaquetado en módulos.
"""
"""
Para crear un módulo es un archivo.py dentro de la misma carpeta.
Para utilizarlo en nuestro archivoPrincipal.py, tendremos que importar el módulo, y usar las funciones con la sintáxis de punto: forma de acceder a las funciones dentro de un archivo.
Los módulos pueden contener funciones, arrays, dictionaries, objects etc
"""

# importar el modulo "modulo.py"
import modulo

#usar la función saludos
modulo.saludos("Elena")


"""
Es probable que en desarrollo de un programa, éste se complejice y la cantidad de funciones que pueda tener un módulo sean muchas, para lo cual se utiliza la función de Python dir(), con esto tendremos todos los nombres.
Las funciones con doble guión bajo son aquellas inherentes a Python.
"""
# importar el modulo "modulo.py"
import modulo

#usar la función saludos
modulo.saludos("Elena")
# imprimr directorio de funciones del módulo
print(dir(modulo))


"""
Otra funcionalidad para tener un programa más legible, generando un alias por medio de la palabra clave as
"""

# importar el modulo "modulo.py"
import modulo as m

#usar la función saludos
m.saludos("Elena")
# imprimr directorio de funciones del módulo
print(dir(m))


"""
Actividad: Escribir un módulo con funciones que permitan escribir un cuento, en donde las variables del cuento serán listas, diccionarios, tuples.
Tienen que buscar información de como se escriben diccionarios en Python
"""
