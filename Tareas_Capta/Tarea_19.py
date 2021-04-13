# Tarea: crear un diccionario con la info de los miembros del área eléctrica utilizados en la Tarea 4:

lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
edades = [19, 17, 24, 25, 26, 28]
usa_lentes = [False, False, False, False, True, True]
tiene_licencia = [False, False, True, False, False, False]
meses_en_capta = [3, 2, 1, 5, 5, 36]

# El diccionario debe tener la info de cada uno de los miembros, de tal forma que si se pregunta:
# diccionario["Lavado"] esto entregue un diccionario con la edad, si usa lentes, tiene licencia 
# # y los meses en capta

# Al terminar, printea el diccionario completo

captianos_electricos = {}
for i in range(len(lista_electrica)):
    captianos_electricos[lista_electrica[i]] = {}
    captianos_electricos[lista_electrica[i]]["edad"] = edades[i]
    captianos_electricos[lista_electrica[i]]["usa_lentes"] = usa_lentes[i]
    captianos_electricos[lista_electrica[i]]["tiene_licencia"] = tiene_licencia[i]
    captianos_electricos[lista_electrica[i]]["meses_en_capta"] = meses_en_capta[i]

# print(captianos_electricos)

print(captianos_electricos["Arredondo"])


dicc = {
    "Lavado": {
        "edad": edades[0],
        "usa_lentes": usa_lentes[0]
    },
    "Arredondo":{
        "edad": edades[1],
        "usa_lentes": usa_lentes[1]
    },
    "Basilio":{
        "edad": edades[2],
        "usa_lentes": usa_lentes[2]
    }
}