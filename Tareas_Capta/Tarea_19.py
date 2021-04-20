# Tarea: crear un diccionario con la info de los miembros del área eléctrica utilizados en la Tarea 4:

lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
edades = [19, 17, 24, 25, 26, 28]
usa_lentes = [False, False, False, False, True, True]
tiene_licencia = [False, False, True, False, False, False]
meses_en_capta = [3, 2, 1, 5, 5, 36]

# El diccionario debe tener la info de cada uno de los miembros, de tal forma que si se pregunta:
# diccionario["Lavado"] esto entregue un diccionario con la edad, si usa lentes, tiene licencia
# y los meses en capta

# Al terminar, printea el diccionario completo

# diccionario = {}
# diccionario["lavado"] = {}
# diccionario["lavado"]["edad"] = edades[0]
# diccionario["lavado"]["usa_lentes"] = usa_lentes[0]
# diccionario["lavado"]["tiene_licencia"] = tiene_licencia[0]

# diccionario["arredondo"] = {}
# diccionario["arredondo"]["edad"] = edades[1]
# diccionario["arredondo"]["usa_lentes"] = usa_lentes[1]
# diccionario["arredondo"]["tiene_licencia"] = tiene_licencia[1]

# diccionario["basilio"] = {}
# diccionario["basilio"]["edad"] = edades[2]
# diccionario["basilio"]["usa_lentes"] = usa_lentes[2]
# diccionario["basilio"]["tiene_licencia"] = tiene_licencia[2]

diccionario = {}
for indice in range(len(lista_electrica)):
    diccionario[ lista_electrica[indice] ] = {}
    diccionario[ lista_electrica[indice] ]["edad"] = edades[indice]
    diccionario[ lista_electrica[indice] ]["usa_lentes"] = usa_lentes[indice]
    diccionario[ lista_electrica[indice] ]["tiene_licencia"] = tiene_licencia[indice]
    diccionario[ lista_electrica[indice] ]["meses_en_capta"] = meses_en_capta[indice]

# print(diccionario)
