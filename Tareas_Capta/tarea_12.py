# Tarea: Crear una lista con el abecedario a partir del 'string_abecedario'.
# 1. Se solicita que las vocales sean almacenadas en mayúsculas.
# 2. Imprimir la lista generada
# 3. Imprimir una frase indicando en que indice está cada vocal. Ej:
# "La vocal <vocal> esta en la posición <n> de la lista abecedario"

string_abecedario = "abcdefghijklmnopqrstuvwxyz"

lista_abecedario= []

for x in string_abecedario:
    if x == "a" or x== "e" or x== "i" or x== "o" or x=="u":
        print(f"La vocal: {x} esta en la posicion: {len(lista_abecedario)}")
        vocal_mayuscula=x.upper()
        lista_abecedario.append(vocal_mayuscula)
    else:
        lista_abecedario.append(x)



print(lista_abecedario)