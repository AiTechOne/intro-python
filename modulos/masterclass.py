# Resumen general de lo estudiado hasta ahora en Python3

# variable = 10302
# print(f"La variable {variable} es de tipo {type(variable)}")

# variable = 10302.321321321
# print(f"La variable {variable} es de tipo {type(variable)}")

# variable = True
# print(f"La variable {variable} es de tipo {type(variable)}")

# variable = False
# print(f"La variable {variable} es de tipo {type(variable)}")

# variable = None
# print(f"La variable {variable} es de tipo {type(variable)}")

# variable = [1,2,3,"lista","objeto"]
# print(f"La variable {variable} es de tipo {type(variable)}")

# Operaciones entre variables:
# Los numeros (enteros o decimales) se pueden sumar, restar, multiplicar o dividir
# con los símbolos + - * / respectivamente

# operacion = 2*3 + 5
# print(f"El resultado de la operacion de numeros (directamente) es {operacion}")


# numero_1 = 10
# numero_2 = 30
# operacion = numero_2 - numero_1
# print(f"El resultado de la operacion entre variables es {operacion}")

# Los strings o textos solo pueden utilizar el operador + para concatenarse:
# string_1 = "Felipe"
# string_2 = "Sequeira"

# nombre = string_1 + " " + string_2 + " trabaja en Capta Hydro desde noviembre del 2020"
# print(f"El joven {nombre}")

# Listas:
# colores = ["rojo", "verde", "azul", "amarillo", "blanco", "negro", "morado"]

# print(f"El primer elemento de la lista es {colores[0]}")
# print(f"El tercer elemento de la lista es {colores[2]}")
# print(f"El ultimo elemento de la lista es {colores[-1]}")

# color_rojo = colores[0] + " es un color bonito"
# print(color_rojo)

# Cuantos elementos tiene la lista colores: utilizamos la funcion len()
# print(f"La lista colores tiene un total de {len(colores)}")


# Condicionales: Hacer algo si se cumple una condicion!
# condicion = (-1 > 0)
# print(f"El valor de condicion es {condicion}")

# condicion = ("Felipe" == "felipe")
# print(f"El valor de condicion es {condicion}")

# condicion = type(123) is int
# print(f"El valor de condicion es {condicion}")


# if type(123) is int:
#     print("La condicion es verdadera")
# else:
#     print("La condicion es falsa")

# numero = 3
# if numero > 10000:
#     print("El numero es mayor a 10000")
# elif numero > 1000:
#     print("El numero es mayor a 1000")
# elif numero > 100:
#     print("El numero es mayor a 100")
# elif numero > 10:
#     print("El numero es mayor a 10")
# else:
#     print("Ninguna de las condiciones anteriores")

# numero = 30000000
# if numero > 10000:
#     print("El numero es mayor a 10000")
# if numero > 1000:
#     print("El numero es mayor a 1000")
# if numero > 100:
#     print("El numero es mayor a 100")
# if numero > 10:
#     print("El numero es mayor a 10")
# if type(numero) is int:
#     print("El numero es un entero")
# if type(numero) is float:
#     print("El numero es un decimal")

# Ciclos:
# colores = ["rojo", "verde", "azul", "amarillo", "blanco", "negro", "morado"]

# recorrer la lista colores:
# Metodo 1:
# for color in colores:
#     print(color)

# Metodo "manual":
# print(f"El elemento 1 de la lista es {colores[0]}")
# print(f"El elemento 2 de la lista es {colores[1]}")
# print(f"El elemento 3 de la lista es {colores[2]}")
# print(f"El elemento 4 de la lista es {colores[3]}")
# print(f"El elemento 5 de la lista es {colores[4]}")
# print(f"El elemento 6 de la lista es {colores[5]}")
# print(f"El elemento 7 de la lista es {colores[6]}")

# for i in range(0, len(colores)):
#     print(f"El elemento {i+1} de la lista es {colores[i]}")

# rango = range(0, len(colores))
# print(list(rango))

# Mezcla de metodos:
# varias_cosas = [25, "Felipe", "Capta Hydro", False, True, None, 3.1415, "Arturo", "Andres", 1, 3, 2]

# suma_de_strings = ""
# suma_de_enteros = 0
# for elemento in varias_cosas:
#     if type(elemento) is str:
#         # print(f"Vamos a agregar {elemento} al string concatenado que por ahora es = {suma_de_strings}")
#         suma_de_strings += elemento + " "
#     if type(elemento) is int:
#         # print(f"Vamos a agregar {elemento} al total de la suma que va en = {suma_de_enteros}")
#         suma_de_enteros += elemento

# print(suma_de_strings)

varias_cosas = [1, "Felipe", "Capta Hydro", False, True, None, 3.1415, "Arturo", "Andres", 2, 3, 4, "a", 5, 6,7,8,9,10]

suma_de_strings = ""
string_largo = "Felipe"
string_corto = "Felipe"

suma_de_enteros = 0
numero_de_bools = 0
numero_de_enteros = 0

for i in range(len(varias_cosas)):
    print(f"Iteracion numero {i} -> Analizando {varias_cosas[i]}")
    if type(varias_cosas[i]) is str:
        if len(string_corto) > len(varias_cosas[i]):
            string_corto = varias_cosas[i]
        if len(string_largo) < len(varias_cosas[i]):
            string_largo = varias_cosas[i]
        # print(f"Vamos a agregar {varias_cosas[i]} al string concatenado que por ahora es = {suma_de_strings}")
        suma_de_strings += varias_cosas[i] + " "
    if type(varias_cosas[i]) is int:
        # print(f"Vamos a agregar {varias_cosas[i]} al total de la suma que va en = {suma_de_enteros}")
        suma_de_enteros += varias_cosas[i]
        numero_de_enteros += 1
    if type(varias_cosas[i]) is bool:
        numero_de_bools += 1

print(f"El promedio de los enteros de la lista es: {suma_de_enteros/numero_de_enteros}")

