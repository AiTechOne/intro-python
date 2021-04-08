rango = range(4,10)

# print(list(rango))

verduras = ["pimenton", "zapallo", "repollo", "platano", "durazno", "palta"]
colores = ["rojo", "azul", "verde", "amarillo", "blanco", "negro"]

# for color in colores:
#     # print(color)
#     for verdura in verduras:
#         print(color, verdura)

# print("")
dividendos = [1,2,3]
divisores = [0,6,7]

c = []
for indice in range(len(dividendos)):
    if divisores[indice] == 0:
        z = "Indeterminado"
    else:
        z = dividendos[indice] / divisores[indice]

    # try:
    #     z = dividendos[indice] / divisores[indice]
    # except:
    #     z = "Indeterminado"

    c.append(z)

print(c)



