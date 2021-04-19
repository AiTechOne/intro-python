# Para importar un archivo, hay que utilizar la palabra mágica 'import'. Luego, se puede agregar modulos que vienen ya instalado 
# en python, u otros archivos .py que esten en el mismo directorio de este archivo (o el archivo principal que vas a ejecutar).

#########################3
# Ejemplo 1: modulo time (tiempo)
#
# import time

# # la funcion time.time() entrega la cantidad de segundos desde el 'inicio de los tiempos de programación'.
# tiempo_inicio = time.time()

# for i in range(10):
#     print(i)
#     # La funcion time.sleep(x) duerme el código por x segundos.
#     time.sleep(1)

# tiempo_final = time.time()
# # Al restar tiempo_final con tiempo_inicio, estamos calculando la cantidad de segundos que demoró en correr nuestro codigo:

# print(tiempo_final - tiempo_inicio)


#########################3
# Ejemplo 2: modulo datetime (fecha y tiempo)
#
#

# import datetime as dt
# # El modulo datetime tiene varios submodulos. El primero que nos interesa es el submodulo datetime, el cual tiene algunos metodos
# # como now() que proporcionan un objeto datetime que tiene la fecha y el tiempo actual.
# fecha_hora = datetime.datetime.now()

# ## Podemos acceder a variables de año, mes, dia, hora, minuto y segundo del objeto datetime como:
# print(fecha_hora.year)
# print(fecha_hora.month)
# print(fecha_hora.day)
# print(fecha_hora.hour)
# print(fecha_hora.minute)
# print(fecha_hora.second)

# # Otro submodulo da datetime es timedelta, que permite crear un objeto tipo timedelta para poder operarlo con objetos datetime y así
# # sumar o restar dias, años, segundos, etc.

# # Ej: objeto timedelta de 2 segundos
# delta_segundos = datetime.timedelta(seconds=2)

# # Podemos operar entonces con + o - como:
# print(fecha_hora + delta_segundos)

# # Ejemplo condicion while con tiempo:
# contador = 0
# while fecha_hora+delta_segundos > datetime.datetime.now():
#     #print("Aun no pasan 5 segundos")
#     contador += 1
# print(f"Contador = {contador}")

#########################3
# Ejemplo 3: modulo tarea_4 tiene que estar en el mismo directorio que este archivo !! si no, tirara error
#

# import tarea_4
# print(tarea_4.lista_electrica)
# print(tarea_4.usa_lentes)
# print(tarea_4.tiene_licencia)
# print(tarea_4.edades)
# print(tarea_4.meses_en_capta)

# print(tarea_4.lista_electrica)
# tarea_4.lista_electrica.append("Nuevo integrante")
# print(tarea_4.lista_electrica)


## Palabra from (en españo 'desde') antes de un import para especificar de que archivo queremos
## importar que cosa (variable, funcion, clase, etc)

# import tarea_4
# print(tarea_4.lista_electrica)

# from tarea_4 import lista_electrica
# print(lista_electrica)

## Palabra as (en españo 'como') despues de un import para cambiar el nombre del objeto importado a algo que nos acomode
## mas

# import tarea_4 as t4
# print(t4.lista_electrica)
# print(t4.usa_lentes)
# print(t4.tiene_licencia)
# print(t4.edades)
# print(t4.meses_en_capta)

## Mezcla de from y as:
# from tarea_4 import lista_electrica as le
# print(le)

## Utilizando from y as con modulo datetime:

# from datetime import datetime as dt
# from datetime import timedelta as td

# fecha_hora_ahora = dt.now()
# print(fecha_hora_ahora)
# delta_tiempo_1_semana = td(weeks=1)
# print(delta_tiempo_1_semana)

# print(fecha_hora_ahora - delta_tiempo_1_semana)
# print(fecha_hora_ahora + delta_tiempo_1_semana)


## Es posible importar más de un submodulo en una sola linea! Ejemplo:
# from datetime import timedelta
# from datetime import datetime
# # Es equivalente a:
# from datetime import datetime, timedelta
