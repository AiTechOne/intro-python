# 1. Imprimir el elemento siguiente de cada NUMERO ENTERO par de la lista
# 2. Imprimir el elemento anterior de cada NUMERO ENTERO par de la lista
lista = [
    "hola",
    6,
    True,
    "Esto se deberia imprimir?",
    False,
    40,
    3,
    2,
    1,
    None,
    2020,
    ["1","2","3","Esto que onda?"],
    "que tal",
    4,
    19,
    32
]

# # # Identificar numero par
# imprimir_siguiente = False
# for elemento in lista:
#     # print(f"(antes del if) imprimir_siguiente = {imprimir_siguiente}")
#     if imprimir_siguiente == True:
#         print(f"Imprimiendo elemento -> {elemento}")
#         imprimir_siguiente = False
#     # print(f"(despues del if) imprimir_siguiente = {imprimir_siguiente}")

#     # print(f"Analizando elemento = {elemento}")
#     if (type(elemento) is int) and (elemento%2==0):
#         # print(f"El elemento analizado es par! ({elemento}). Debemos imprimir el siguiente!")
#         imprimir_siguiente = True

# # Solucion con index:
# # indices_a_imprimir = []
# for elemento in lista:
#     if (type(elemento) is int) and (elemento%2==0):
#         indice = lista.index(elemento)
#         indice_siguiente = indice + 1
#         if indice_siguiente < len(lista):
#             print(lista[indice_siguiente])
#             # indices_a_imprimir.append(indice+1)

# print(f"Los indices a imprimir son: {indices_a_imprimir}")
# for indice in indices_a_imprimir:
#     print(lista[indice])

# lista.reverse()
# for elemento in lista:
#     print(elemento)


imprimir_siguiente = False
lista.reverse()
lista_nueva = []
for elemento in lista:
    # print(f"(antes del if) imprimir_siguiente = {imprimir_siguiente}")
    if imprimir_siguiente == True:
        lista_nueva.insert(0,elemento)
        imprimir_siguiente = False
    # print(f"(despues del if) imprimir_siguiente = {imprimir_siguiente}")

    # print(f"Analizando elemento = {elemento}")
    if (type(elemento) is int) and (elemento%2==0):
        # print(f"El elemento analizado es par! ({elemento}). Debemos imprimir el siguiente!")
        imprimir_siguiente = True

# lista_nueva.reverse()
for elemento in lista_nueva:
    print(f"Imprimiendo elemento -> {elemento}")