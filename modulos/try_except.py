#############################################
# Condicionales
#

# lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# nombre_a_buscar = "dsaewqdsaewq"

# try:
#     print("Buscando...")
#     indice = lista_electrica.index(nombre_a_buscar)
#     print(f"El elemento {nombre_a_buscar} esta en el indice {indice} de la lista_electrica")
# except:
#     print("El elemento buscado no esta en la lista")

# print("Fin del programa")


# Comparacion con el caso del metodo "find" en string -> arroja indice = -1 si el elemento no existe.
# # nombre = 'Felipe'
# indice_l = nombre.find("a")

# if indice_l >= 0:
#     print(f"El caracter 'l' esta en el indice {indice_l} de la variable nombre")
# else:
#     print("El caracter buscado no existe en la variable nombre")

# lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# nombre_a_buscar = "Sequeira"

# try:
#     print("Buscando...")
#     indice = lista_electrica.index(nombre_a_buscar)
#     print(f"El elemento {nombre_a_buscar} esta en el indice {indice} de la lista_electrica")
# except ValueError:
#     print("No esta en la lista")
# except KeyError:
#     print("Fue un error de tipo 'KeyError'")
# except:
#     print("Ocurrio otro error")

# print("Fin del programa")

## Ejemplo sumar variable string con variable entera
# variable_string = "Hola"
# variable_int = 10

# try:
#     print(variable_string + variable_int)
# except TypeError:
#     print("No se puede sumar variables de tipo string con entero")


# # Ejemplo aplicar funcion len a una variable de tipo entero
# variable_int = 10
# try:
#     print(len(variable_int))
# except TypeError:
#     print("No se puede aplicar la funcion len a un entero")


# Ejemplo aplicar funcion len a una variable de tipo entero
# numero = 100
# divisor = 0.0
# try:
#     print(numero / divisor )
# except ZeroDivisionError:
#     print("No se puede dividir un numero por 0")


# try:
#     lista_ejemplo.remove(elemento_a_eliminar)
#     print("El elemento fue eliminado")
# except ValueError:
#     print(f"No se puede eliminar el elemento {elemento_a_eliminar} porque no existe en la lista")