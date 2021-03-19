# Lista de ejemplo:
lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# print("Para crear una lista hay que utilizar los corchetes [ y ]")
# print("Los elementos de una lista se separan con comas!")
# print(f"La lista_electrica tiene los siguientes elementos: {lista_electrica}")
# print(f"Al imprimir una lista siempre aparecen los corchetes en los extremos: [..., ... , ... ]")

# # Largo de la lista con len():
# print(f"La lista_electrica tiene {len(lista_electrica)} elementos originalmente")

# # # Accediendo a elementos de la lista por [indice]
# print(f"El primer elemento de la lista es: {lista_electrica[0]} - {type(lista_electrica[0])}")
# print(f"El segundo elemento de la lista es: {lista_electrica[1]} - {type(lista_electrica[1])}")
# print(f"El tercer elemento de la lista es: {lista_electrica[2]} - {type(lista_electrica[2])}")
# print(f"El cuarto elemento de la lista es: {lista_electrica[3]} - {type(lista_electrica[3])}")
# print(f"El quinto elemento de la lista es: {lista_electrica[4]} - {type(lista_electrica[4])}")
# print(f"El sexto elemento de la lista es: {lista_electrica[5]} - {type(lista_electrica[5])}")
# print(f"El último elemento de la lista es: {lista_electrica[-1]} - {type(lista_electrica[-1])}")

# print(f"Los primeros 2 elementos de la lista son: {lista_electrica[:2]} - {type(lista_electrica[:2])}")
# print(f"El segundo y tercer elementos de la lista son: {lista_electrica[1:3]} - {type(lista_electrica[1:3])}")
# print(f"Los elementos desde el tercer indice en adelante de la lista son: {lista_electrica[2:]} - {type(lista_electrica[2:])}")

# Crear variable auxiliar de sublista:
# primeros_dos = lista_electrica[:2]
# print(f"Los primeros 2 elementos de la lista son: {lista_electrica[:2]} - {type(lista_electrica[:2])}")
# print(f"Los primeros 2 elementos de la lista son: {primeros_dos} - {type(primeros_dos)}")


# # Agregar elementos al final de la lista:
# print(f"La lista_electrica tiene los siguientes elementos: {lista_electrica}")
# lista_electrica.append("Villarroel")
# print(f"Al utilizar append, se agrega al final de la lista Villarroel -> {lista_electrica}")
# print(f"La lista_electrica tiene {len(lista_electrica)} elementos")

# # Agregar elementos en un indice específico de la lista:
# lista_electrica.insert(0, "De La Jara")
# print(f"Al insertar en el indice 0, se agrega De La Jara al inicio de la lista -> {lista_electrica}")

# # Eliminar elemento especifico de la lista:
# lista_electrica.remove("De La Jara")
# print(f"Eliminado De La Jara de la lista_electrica -> {lista_electrica}")
# lista_electrica.remove("De La Jara")

# # Eliminar el último elemento de la lista
# lista_electrica.pop()
# print(f"Al aplicar pop, se elimina el ultimo elemento de la lista, por lo que la nueva lista es: {lista_electrica}")

# # Ordenar por orden alfabetico:
# lista_electrica.sort()
# print(f"La lista ordenada es: {lista_electrica}")

# Buscar el indice de un elementos de la lista
# OJO: buscar algo que no existe en la lista, entrega un error! no un -1 (como lo hace el metodo find con los strings)
# print(lista_electrica)
# nombre_a_buscar = "Dusadnsandjs"
# indice = -1

# print(f"El indice de {nombre_a_buscar} en la lista_electrica es {indice}")
# print(lista_electrica[indice])

# string = "Felipe"
# buscar = "o"
# indice = string.find(buscar)
# print(indice)

# # Eliminar todos los elementos de la lista
# print(lista_electrica)
# lista_electrica.clear()
# print(lista_electrica)

# # Dar vuelta elementos de una lista:
# print(lista_electrica)
# lista_electrica.reverse()
# print(lista_electrica)

# Concatenar con otra lista:
# lista_mecanica = ["Carilao", "Echeverria"]

# Concatenar listas:
# lista_electrica_mecanica = lista_electrica + lista_mecanica
# print(f"La nueva lista mecanica y electrica es: {lista_electrica_mecanica}")

# lista_electrica_mecanica = lista_electrica + lista_mecanica + "string_prueba"
# lista_electrica_mecanica = lista_electrica + lista_mecanica + 10
# lista_electrica_mecanica = lista_electrica + lista_mecanica + ["elemento1", "elemento2"]
# print(lista_electrica_mecanica)


# ## Las listas pueden mezclar elementos de diferentes tipos: int, floats, strings, boolean, None, listas, etc
# lista_mixta = ["1231321", 5435, 10.5, "Capta Hydro", lista_electrica, True, False, None]
# print(f"La lista_mixta contiene los siguientes elementos: {lista_mixta}")
# print(f"El largo de la lista_mixta es {len(lista_mixta)}")

# print(f"El elemento 1 de la lista_mixta es {lista_mixta[0]} y es de clase {type(lista_mixta[0])}")
# print(f"El elemento 2 de la lista_mixta es {lista_mixta[1]} y es de clase {type(lista_mixta[1])}")
# print(f"El elemento 3 de la lista_mixta es {lista_mixta[2]} y es de clase {type(lista_mixta[2])}")
# print(f"El elemento 4 de la lista_mixta es {lista_mixta[3]} y es de clase {type(lista_mixta[3])}")
# print(f"El elemento 5 de la lista_mixta es {lista_mixta[4]} y es de clase {type(lista_mixta[4])}")
# print(f"El elemento 6 de la lista_mixta es {lista_mixta[5]} y es de clase {type(lista_mixta[5])}")
# print(f"El elemento 7 de la lista_mixta es {lista_mixta[6]} y es de clase {type(lista_mixta[6])}")
# print(f"El elemento 8 de la lista_mixta es {lista_mixta[7]} y es de clase {type(lista_mixta[7])}")

# Acceder a elementos de una sublista:
# lista_mixta[4] = lista_electrica
# lista_electrica[0]
# => lista_mixta[4][0]
# print(f"El elemento 5 de la lista_mixta es {lista_mixta[4]} y el subelemento 1 de esta lista es: {lista_mixta[4][0]} - tipo: {type(lista_mixta[4][0])}")
# print(f"El elemento 5 de la lista_mixta es {lista_mixta[4]} y el subelemento 2 de esta lista es: {lista_mixta[4][1]}")
# print(f"El elemento 5 de la lista_mixta es {lista_mixta[4]} y el subelemento 3 de esta lista es: {lista_mixta[4][2]}")

# print(f"El elemento 4 de la lista_mixta es {lista_mixta[3]} y es de tipo {type(lista_mixta[3])}")
# hydro = lista_mixta[3][5:]
# print(f"Basilio y Sequeira dicen que Hydro es: {hydro} - {len(hydro)}")
# hydro = lista_mixta[3][6:]
# print(f"Lavado dice que Hydro es: {hydro} - {len(hydro)}")
# hydro = lista_mixta[3][-5:]
# print(f"Lavado dice que Hydro es: {hydro} - {len(hydro)}")


