##################
# Funciones o metodos

# Metodos de elementos o propios de python
# type()
# int()
# len()
# range()
# string.replace()
# lista.pop()
# lista.insert()
# lista.append()

# lista = [1,2.0,3]
# lista.append("hola")
# print(lista)
# lista.pop()
# print(lista)

# def sumar(x, y):
#     if type(y) is int:
#         return x+y
#     else:
#         return "la variable 'y' no es un entero!"

# def restart(x, y):
#     return x-y

# def es_par(x):
#     if x%2 == 0:
#         return "Es par!"
#     else:
#         return "No es par!"


# lista = [1,2,3]
# resultado_suma = sumar(x=5, y=lista[1])
# print(resultado_suma)



# Tarea: Crear un codigo que imprima todos los números del 1 al "x"
# "X" debe ser una variable a definir y que pueda ser modificada en el futuro


# x = 8
# for n in range(x):
#     print(n)

# def print_hasta(x):
#     for n in range(x):
#         print(n)

# print_hasta(x=2)
# print("")
# print_hasta(x=5)
# print("")
# print_hasta(x=3)
# print("")
# print_hasta(x=1)


# lista = list(range(15))
# lista.append("String")
# print(lista)
# resultado = sumar(x=lista[-1], y=lista[1])
# print(resultado)

# print(lista)

# def suma_lista(lista_a_sumar):
#     suma = 0
#     for elemento in lista_a_sumar:
#         if type(elemento) is int:
#             suma += elemento
#     return suma

# resultado = suma_lista(lista_a_sumar=lista)
# print(resultado)
# print(sum(lista))

# lista_verduras_1 = ["papas", "cebolla", "tomate"]
# lista_verduras_2 = ["pepino", "lechuga", "tomate"]

# def modificar_lista(lista):
#     for elemento in lista:
#         x = elemento[0:2] + "X" + elemento[2:]
#         print(x)

# modificar_lista(lista=lista_verduras_1)
# modificar_lista(lista=lista_verduras_2)

# lista_numeros = list(range(5))
# print(lista_numeros)

# def estadisticas(lista):
#     return sum(lista), min(lista), max(lista)

# r = estadisticas(lista=lista_numeros)
# print(f"La suma total de la lista es {r[0]}")
# print(f"El minimo de la lista es {r[1]}")
# print(f"El maximo de la lista es {r[2]}")

# suma, minimo, maximo = estadisticas(lista=lista_numeros)
# print(f"La suma total de la lista es {suma}")
# print(f"El minimo de la lista es {minimo}")
# print(f"El maximo de la lista es {maximo}")