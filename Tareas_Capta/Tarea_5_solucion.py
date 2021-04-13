# El objetivo de esta tarea es realizar un conjunto de divisiones de forma automatizada y almacenar los cociente, para
# posteriormente imprimir que operación se realizó y qué resultado se obtuvo. SE PIDE REDONDEAR A 2 DECIMALES LOS RESULTADOS!
# Para esto, se presentan las siguientes listas con dividendos y divisores:

dividendos = [1,2,3,4,5,6,7,8,9,10,11,12,1300,140,15,16,170,18,190,20]
divisor = [5,4,0,2,1,0,7,5,0,2,1,3,4,60,7,8,9,0,0,1.5]

# Observación 1: Si en una división de entre <x> e <y> (ó x/y) se obtiene <z>, se denomina:
#     x: dividendo
#     y: divisor
#     z: cociente

# Observación 2: en caso de que el divisor sea igual a 0, entonces el cociente debe ser "Indeterminado" (si, un string)
# ya que un número que se divide por cero tiende al infinito (confien en mi, y se los explicaré después)

# Se solicita crear una lista llamada resultados la cual tendrá cuantas sublistas como divisiones se deben realizar,
# y cada sublista se compone de 3 variables: dividendo, divisor y cociente. Entonces, la lista resultados debe comenzar y terminar como:
#     resultados = [ [1, 5, 0.2], ... ... ... , [20, 1.5, 13.33] ]
# Cada sublista de resultados es entonces simplemente:
#     [x, y, z]

# Finalmente, imprimir todos los resultados utilizando un ciclo for y f-strings como:
# 'La división entre <x> y <y> es igual a <z>'

# Forma optimizada:
resultados = []
for i in range(len(dividendos)):
    if divisor[i] == 0:
        z = "Indeterminado"
    else:
        z = round( dividendos[i] / divisor[i], 2)
    resultados.append([dividendos[i], divisor[i], z])
    print(f"La división entre {dividendos[i]} y {divisor[i]} es igual a {z}")


# # Forma simple con 2 for:
# cocientes = []
# for i in range(len(dividendos)):
#     if divisor[i] == 0:
#         cocientes.append("Indeterminado")
#     else:
#         resultado_auxiliar = round( dividendos[i] / divisor[i], 2)
#         cocientes.append(resultado_auxiliar)

#     # print(i)
#     # print(f"Dividendo = {dividendos[i]}")
#     # print(f"Divisor = {divisor[i]}")
#     # print(f"Cociente = {dividendos[i] / divisor[i]}")
#     # print("")

# resultados = []
# for i in range(len(dividendos)):
#     resultados.append([dividendos[i], divisor[i], cocientes[i]])
#     print(f"La división entre {dividendos[i]} y {divisor[i]} es igual a {cocientes[i]}")
