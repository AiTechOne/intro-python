##############
# Diccionarios!

# Los diccionarios que conocemos de niños, son libros que contienen un conjunto de palabras
# y su significado. En python, los diccionarios son algo similar: llaves (keys) y valores (values).

# Para definir una lista se utilizan los "parentesis cuadrados" -> [ ]
# Para definir una tupla se utilizan los "parentesis tipicos/circulares" -> ( )
# Para definir un diccionario se utilizan los "parentesis tipo llave" -> { }

# ejemplo = {}
# print(ejemplo)

# Agregar elementos al diccionario:
# ejemplo["nombre"] = "Felipe"
# print(ejemplo)

# Obs 1: Al imprimir los diccionarios vemos que las llaves y los valores se conectan no con el símbolo
# igual '=', sino que con dos puntos
# {'nombre': 'Felipe'}

# Agregar elementos al crear el diccionario (ojo que hay que utilizar los dos puntos!)
# ejemplo = {"nombre": "Felipe"}
# print(ejemplo)

# Agregamos otra variable:
# ejemplo = {"nombre": "Felipe", "edad": 28}
# print(ejemplo)

# ejemplo = {}
# ejemplo["nombre"] = "Felipe"
# ejemplo["edad"] = 28
# print(ejemplo)

# # Obs 2: es posible definir valores de cualquier tipo válido en python! (enteros, decimales, listas,
# # otro diccionario, tuplas, etc.)
# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"]}
# print(ejemplo["hermanos"])

# Obtener solamente el valor de una llave del diccionario -> Utilizar corchetes cuadrados
# como índices de listas!
# print( ejemplo["nombre"] )
# hermanos_de_felipe = ejemplo["hermanos"]
# print(hermanos_de_felipe)

# # Que pasa si pregunto una llave que no existe? Ustedes lo saben...
ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"]}
# print( ejemplo["correo"] )

# Para evitar errores, se puede utilizar el método "get" (en español 'obtener')
# propio de un diccionario. Si no existe, retorna un None por defecto:
# print( ejemplo.get('dsadsadsa') )

# # Es posible definir un valor predeterminado diferente de None:
# print( ejemplo.get('correo', 'algo@captahydro.com'))

# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"]}
# # Crear o actualizar el valor de una variable del diccionario. Los dos métodos comunes son:
# # 1. Con el indice:
# ejemplo["nombre"] = "Felipe Andres"
# print(ejemplo)
# ejemplo["correo"] = "felipe@captahydro.com"
# print(ejemplo)

# 2. Con el metodo update (actualizar):
# ejemplo.update({"nombre": "Felipe Tejada"})
# print(ejemplo)
# # Este metodo permite actualizar o agregar varias llaves!
# # ejemplo.update({"nombre": "Felipe Tejada Estay", "edad": 29, "correo": "felipe.tejada@pm.me"})
# ejemplo.update(
#         {
#             "nombre": "Felipe Tejada Estay",
#             "edad": 29,
#             "correo": "felipe.tejada@pm.me"
#         }
#     )
# print(ejemplo)


# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"], "correo": "felipe.tejada@pm.me"}
# Eliminar llaves del diccionario -> Dos métodos:
# 1. Método del (delete=eliminar)
# del ejemplo["correo"]
# print(ejemplo)

# Método pop del diccionario:
# ejemplo.pop("hermanos")
# print(ejemplo)

# # Obs: al aplicar pop, es posible almacenar el valor de la llave que se elimina 
# # a una variable. Ejemplo:
# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"], "correo": "felipe.tejada@pm.me"}
# print(ejemplo)
# edad_felipe = ejemplo.pop('edad')
# print(ejemplo)
# print(edad_felipe)

# # La funcion len() también se puede utilizar en un diccionario!
# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"]}
# print(f"El largo del diccinario es: {len(ejemplo)}")
# # len(diccionario) -> numero de llaves!


# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"], "correo": "felipe.tejada@pm.me"}
# # Se puede acceder a un iterable (parecido a una lista) con las llaves del diccionario:
# print(ejemplo.keys())
# # Obs 3: Todos los iterables se pueden recorrer con loops
# for llave in ejemplo.keys():
#     print(llave)

# # # Similar al anterior, se puede acceder a todos los valores del diccionario con:
# print(ejemplo.values())
# for valor in ejemplo.values():
#     print(valor)

# Otro método de los diccionarios es 'items' -> entrega los pares llaves y valor en tuplas:
# print(ejemplo.items())
# for x in ejemplo.items():
#     print(x)
#     print(x[0], x[1])

# # Eliminar todos los elementos de un diccionario -> metodo clear:
# ejemplo.clear()
# print(ejemplo)

# Eliminar la última llave-valor y retornarla en una variable: metodo popitem()
# ejemplo = {"nombre": "Felipe", "edad": 28, "hermanos": ["Daniela", "Matías"]}
# tupla = ejemplo.popitem()
# print(tupla)