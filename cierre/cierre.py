# Leer desde carpeta con archivos
import os   # lee carpetas
import csv  # lee archivos

# imprime el direcotorio
print(os.fspath("/Users/N/Documents/2Work/python/cierre"))
# la variable path tiene la dirección de los archivos
path = os.fspath("/Users/N/Documents/2Work/python/cierre")

# escanear el directorio path como listaArchivos
# iterar por toda la lista, imprimiento el nombre del archivo
print("LA LISTA DE LOS ARCHIVOS: -------------------------------------------")
with os.scandir(path) as listaArchivos:
    for archivo in listaArchivos:
        print(archivo.name)
print("---------------------------------------------------------------------")
# ocupar el mismo algoritmo y ahora filtrar por archivos que sean con estensión
# csv
with os.scandir(path) as listaArchivos:
    # lista general que tiene todas las otras listas
    listas = []
    for archivo in listaArchivos:
        # si el archivo no comienza con punto y además es archivo
        # imprimir el nombre del archivo
        if not archivo.name.startswith('.') and archivo.is_file() and archivo.name.endswith('.csv'):
            # creación de listas con cada uno de las rows
            listaTemp = []
            with open(archivo.name, newline='') as csvfile:
                print("ARCHIVO: ", archivo.name)
                reader = csv.reader(csvfile)
                # por cada archivo concatenar sus filas separadas por -
                for row in reader:
                    print(row)
                    # cada fila se suma a la lista temporal
                    listaTemp.append(row)
            # toda la lista temporal se suma a la lista general
            listas.append(listaTemp)

# iterar por todas las listas para saber su tamaño
print("Imprime el primer item de cada lista ---------------------------------")
numeroLista = 0
for l in listas:
    print("lista: l[", numeroLista, "]", l[0])
    numeroLista += 1


print("Creando una lista de alumnos con campos vacios")
# importar la clase
from Alumno import Alumno
# lista de todos los alumnos con objetos Alumno
alumnosTodos = []
# iterar por la lista l[4] y llenar con nombre apellido y id, con el resto vacío
listaAlumnos = listas[4]
for alumno in listaAlumnos:
    nombre = alumno[0]
    apellido = alumno[1]
    id = alumno[2]
    cursoA = []
    cursoB = []
    alumnosTodos.append(Alumno(nombre, apellido, id, cursoA, cursoB))

for a in alumnosTodos:
    for b in listas[0]
    print(a.nombre)
