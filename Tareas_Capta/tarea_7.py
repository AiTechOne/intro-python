## Tarea: encontrar el promedio de notas de cada alumno, almacenado en sublistas de la lista "general"

# OJO: cada elemento de la lista es una sublista con el nombre y las 3 notas acumuladas por el alumno como:
# ['nombre', nota1, nota2, nota3]

# Aproximar el promedio al primer decimal.
# Imprimir el resultado utilizando f-strings como:
# "El alumno <x> promedio <y> en el ramo.

general = [
    ['Jose', 6.3, 4.5, 1.6],
    ['Miguel', 5.3, 6.3, 1.2],
    ['Mario', 5.2, 2.6, 2.2],
    ['Pedro', 1.2, 5.1, 2.2],
    ['Rodrigo', 4.3, 3.5, 4.1],
    ['Emilio', 1.3, 5.5, 2.6],
    ['Ricardo', 5.3, 2.2, 1.2],
    ['Roberto', 4.3, 3.6, 2.6],
    ['Rafael', 1.5, 2.2, 1.6],
    ['Alonso', 3.6, 1.4, 2.3]
]

# class Curso:
class Alumno:
    promedio = "No se ha calculado el promedio del alumno aun!"

    def __init__(self, sublista_alumno):
        self.nombre = sublista_alumno[0]
        self.nota_1 = sublista_alumno[1]
        self.nota_2 = sublista_alumno[2]
        self.nota_3 = sublista_alumno[3]

    def calcular_promedio(self):
        self.promedio = (self.nota_1 + self.nota_2 + self.nota_3)/3


alumno_1 = Alumno(sublista_alumno=general[0])
print(alumno_1.promedio)
alumno_1.calcular_promedio()
print(alumno_1.promedio)