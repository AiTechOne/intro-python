# Tarea: En una competición entre 10 hombres y mujeres, se puntúa entre 0 y 100 su resultado.
# En la lista resultados se presentan sublistas con el nombre del competidor y su resultado (decimal).

# Utilizando un ciclo for o while, imprima el segundo mejor resultado, y el segundo peor resultado como:
# 'El segundo mejor resultado de la competición lo obtuvo <nombre> con <x> puntos.'
# 'El segundo peor resultado de la competición lo obtuvo <nombre> con <x> puntos.'


resultados = [
    ["Cristobal", 15.6],
    ["Miguel", 64.0],
    ["Cristina", 70.2],
    ["Jorge", 55.6],
    ["Rafael", 44.8],
    ["Francisca", 97.1],
    ["Ignacia", 90.3],
    ["Amparo", 20.6],
    ["Joaquin", 44.9],
    ["Paula", 80.6],
]

nombre_maximo = resultados[0][0]
nombre_segundo_maximo = resultados[0][0]

numero_maximo = resultados[0][1]
segundo_maximo = resultados[0][1]

for sublista in resultados:
    if sublista[1] > numero_maximo:
        segundo_maximo = numero_maximo
        nombre_segundo_maximo = nombre_maximo

        numero_maximo = sublista[1]
        nombre_maximo = sublista[0]
    else:
        if sublista[1] > segundo_maximo:
            segundo_maximo = sublista[1]
            nombre_segundo_maximo = sublista[0]


print(f'El segundo mejor resultado de la competición lo obtuvo {nombre_segundo_maximo} con {segundo_maximo} puntos.')