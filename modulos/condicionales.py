#############################################
# Condicionales
#
# Tipo de variable "bool" "boolean"
variable_verdadero = True
variable_falso = False

# if en español es 'si'
# else en español es: 'si no'

# if False:
#     print("Condicion es verdadera")
# else:
#     print("Condicion es Falsa")


# var = False
# if var == True:
# # if var:
#     print("Condicion es verdadera")
# else:
#     print("Condicion es falsa")


# Operadores para condiciones:
# igual:                  ==
# diferente:              !=
# mayor que:              >
# menor que:              <
# mayor o igual que:      >=
# menor o igual que:      <=
# identidad del objeto:   is
# elemento "en" objeto:   in

# El resultado de los operadores es: Verdadero o Falso!

# # If y Else:
# nombre = "Felipe2"
# largo_nombre = len(nombre)
# nombre_2 = "Felipe Andres"
# largo_nombre_2 = len(nombre_2)
# #print(largo_nombre > largo_nombre_2)
# print(nombre == nombre_2)
# comparacion = nombre == nombre_2
# print(comparacion)


# if nombre == "Felipe":
#     print("La variable 'nombre' es igual a 'Felipe'")
# else:
#     print("La variable 'nombre' no es igual a 'Felipe'")

# numero = -10
# if numero > 0:
#     print("La variable 'numero' es mayor a cero")
# elif numero == 0:
#     print("La variable 'numero' es igual a cero")
# else:
#     print("La variable 'numero' es menor a cero")

# # If, Elif y Else:
# nombre = 'Pedro'
# if nombre == "Felipe":
#     print("La variable 'nombre' es igual a 'Felipe'")
# elif nombre == 'Giuseppe':
#     print("La variable 'nombre' es igual a 'Giuseppe'")
# else:
#     print("La variable 'nombre' no es igual a 'Felipe' ni 'Giuseppe'")

# # Varios if
# nombre = 'Giuseppe'
# if nombre == "Felipe":
#     print("La variable 'nombre' es igual a 'Felipe'")
# if nombre[0] == 'F':
#     print("La variable 'nombre' es un string que comienza con 'F'")
# if nombre[-1] == 'e':
#     print("La variable 'nombre' es un string que termina con 'e'")


# Varios elif:
# numero = 5
# if numero < 0:
#     print("El numero es negativo")
# elif numero == 0:
#     print("EL numero es igual a cero")
# elif numero > 0 and numero < 10:
#     print("El numero es positivo y menor a 10")
# else:
#     print("El numero es mayor o igual a 10")
# print("Finalizado")

# # Ejemplo más de una condicion:
# condicion_1 = 10<2 # comparacion de enteros
# condicion_2 = 'Feelipe' == 'Felipe'

# print(f"La condicion_1 es = {condicion_1}")
# print(f"La condicion_2 es = {condicion_2}")

# # # Usar operador 'and' (en español 'y')
# #if condicion_1 and condicion_2:
# if (condicion_1==True) and (condicion_2==True):
#     print("Ambas condiciones son verdaderas")
# elif condicion_1:
#     print("Solo la condicion 1 es verdadera")
# elif condicion_2:
#     print("Solo la condicion 2 es verdadera")
# else:
#     print("Ninguna condicion es verdadera!")

# if condicion_1:
#     print("La condicion 1 es verdadera")
# if condicion_2:
#     print("La condicion 2 es verdadera")


# condicion = False

# if condicion:
#     pass
# else:
#     print("1. La condicion es falsa")

# if not condicion:
#     print("2. La condicion es falsa")

# if condicion == False:
#     print("3. La condicion es falsa")


# # Ejemplo más de una condicion:
# condicion_1 = 10<2 # comparacion de enteros
# condicion_2 = 'Felipe' == 'Felipe'

# print(f"La condicion_1 es = {condicion_1}")
# print(f"La condicion_2 es = {condicion_2}")
# # Usar operador 'or' (en español 'o')
# if condicion_1 or condicion_2:
# #if (condicion_1==True) or (condicion_2==True):
#     print("Al menos una de las dos condiciones es verdadera")
# else:
#     print("Ninguna condicion es verdadera!")


# Utilizar condicional "in" (en español: "en") para saber si un elemento existe en una lista, y después eliminarlo
# lista_ejemplo = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# elemento_a_eliminar = "Sequeira"

# if elemento_a_eliminar in lista_ejemplo:
#     lista_ejemplo.remove(elemento_a_eliminar)
#     print("El elemento fue eliminado")
# else:
#     print(f"No existe el elemento {elemento_a_eliminar} en la lista")
# print(lista_ejemplo)


# # Ejemplo con operador != (diferente de):
# nombre = "Sequeira"

# if nombre != "Basilio":
#     print("Nombre no es 'Basilio")
# else:
#     print("Nombre es Basilio")

# Ejemplo con operador is (en español: es). En python es para comparar tipos de objeto
# variable = "10"

# if type(variable) is str:
#     print("'variable' es un string")
# elif type(variable) is int:
#     print("'variable' es un entero")
# elif type(variable) is float:
#     print("'variable' es un decimal")
# elif type(variable) is bool:
#     print("'variable' es de tipo booleana" )
# else:
#     print("'variable' no es un string, entero, booleana ni decimal")