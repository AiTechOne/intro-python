# Clase: es un objeto en python

class Captiano:
    empresa = "Capta Hydro SPA"
    propiedades = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def numeros_hasta_edad(self):
        for n in range(self.edad):
            print(n)

    def agregar_propiedad(self, var_a_agregar):
        if type(var_a_agregar) is str:
            self.propiedades.append(var_a_agregar)
        else:
            print("La propiedad no es un str!")

    def __str__(self):
        return f"El nombre del captiano es {self.nombre} y su edad es {self.edad}"


captiano_1 = Captiano(nombre="Felipe Tejada", edad=28)
print(captiano_1.nombre)
print(captiano_1.edad)
# print(captiano_1.empresa)
# captiano_1.empresa = "La Competencia"
# print(captiano_1.empresa)

# captiano_2 = Captiano(nombre="Wladi", edad=19)
# print(captiano_2.nombre)
# print(captiano_2.edad)

# if captiano_1.edad > captiano_2.edad:
#     print(f"{captiano_1.nombre} es mayor que {captiano_2.nombre}")
# else:
#     print(f"{captiano_1.nombre} no es mayor que {captiano_2.nombre}")

# print(captiano_1.propiedades)

# captiano_1.numeros_hasta_edad()
# captiano_1.agregar_propiedad(var_a_agregar="Jefe del área electrica")
# print(captiano_1.propiedades)

# captiano_1.agregar_propiedad(var_a_agregar=1)
# print(captiano_1.propiedades)

# captiano_1.agregar_propiedad(var_a_agregar="Juego COD")
# print(captiano_1.propiedades)

