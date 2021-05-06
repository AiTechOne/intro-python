# Tarea: dado el diccionario de ejemplo a continuación, elimina todas las llaves presentes
# en la lista de llaves_a_eliminar. El proceso debe ser realizado utilizando un ciclo for o
# while. Imprime el diccionario final luego de aplicar las eliminaciones correspondientes.

original = {
    "lista_nombres": ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"],
    "lista_colores": ["rojo", "verde", "azul"],
    "nota" : 7.0,
    "ciudad": "Santiago",
    "comunas": ["Peñalolen", "Maipu", "Ñuñoa", "Renca"],
    "direccion": "Carrera Pinto 12321421"
}

llaves_a_eliminar = ["nota", "ciudad", "direccion"]

for llave in llaves_a_eliminar:
    print("Eliminando llave", llave)
    original.pop(llave)
print(original)

# n = 0
# while n < len(llaves_a_eliminar):
#     print("Eliminando llave", llaves_a_eliminar[n])
#     original.pop(llaves_a_eliminar[n])
#     n+=1
# print(original)

# while len(llaves_a_eliminar) > 0 :
#     print("Eliminando llave", llaves_a_eliminar[-1])
#     original.pop(llaves_a_eliminar[-1])
#     llaves_a_eliminar.pop()
#     print(llaves_a_eliminar)
# print(original)