## Inspeccionando el modulo datetime:
# import datetime

# # La funcion dir entrega todas las propiedades de un objeto. Estas propiedades pueden ser variables
# # (string, int, listas, etc), otros objetos, y funciones o métodos.
# print("Contenido del modulo datetime (funcion dir): ", dir(datetime))
# # print(type(datetime.MAXYEAR))
# # print(datetime.MAXYEAR)
# # print(datetime.MINYEAR)

# print("\n")
# print("Contenido del submodulo datetime: ",dir(datetime.datetime))

# print(datetime.datetime.now())

# # print("\n")
# print("Contenido del submodulo timedelta: ",dir(datetime.timedelta))


###############################
# Comentar el primer import de datetime para no tener problemas de aqui en adelante:
# from datetime import datetime as dt

# # Recordando lo visto en la clase modulos:
# fecha_hora = dt.now()
# print(f"El tipo de objeto de fecha_hora es: {type(fecha_hora)}")
# print("Objeto datetime fecha_hora es:", fecha_hora)
# print("Año: ",fecha_hora.year)
# print("Mes: ",fecha_hora.month)
# print("Dia: ",fecha_hora.day)
# print("Hora: ",fecha_hora.hour)
# print("Minuto: ",fecha_hora.minute)
# print("Segundo: ",fecha_hora.second)
# print("Dia de la semana: ",fecha_hora.weekday())


# # Timestamp es una estampa de tiempo, equivalente a datetime, solo que entrega la fecha y hora como un decimal
# # que equivale a la cantidad de segundos desde "el inicio de la programacion" (por decirlo de un modo simplificado)
# import time
# from datetime import datetime as dt

# timestamp = time.time()
# print("El timestamp es:", timestamp)

# # El modulo datetime tiene un metodo llamado fromtimestamp() que puede traducirse como "desde estampa de tiempo",
# # que transforma un objeto time.time() (timestamp) en un objeto datetime (fecha y hora)
# timestamp_a_dt = dt.fromtimestamp(timestamp)
# print("El timestamp_a_dt es: ", timestamp_a_dt)

# timestamp_a_dt = dt.fromtimestamp(0)
# print("El timestamp_a_dt es: ", timestamp_a_dt)


#################
# Transformar un objeto datetime en un string con un formato especial que nos sirva para nuestra aplicación
# from datetime import datetime as dt

# fechahora_actual = dt.now()
# print("Fecha y hora actual: ",fechahora_actual)

# solo_hora = fechahora_actual.strftime("%H:%M:%S")
# print("solo_hora es: ", solo_hora)

# solo_fecha = fechahora_actual.strftime("%d/%m/%Y")
# print("solo_fecha es: ",solo_fecha)

# fecha_y_hora = fechahora_actual.strftime("%Y-%m-%d %H:%M:%S")
# print("fecha_y_hora es: ",fecha_y_hora)

# fecha_y_dia = fechahora_actual.strftime("%A, %d-%m-%Y")
# print("fecha_y_dia es: ",fecha_y_dia)

# fecha_hora_utc = dt.utcnow()
# print("fecha_hora_utc es: ",fecha_hora_utc)

# # Tabla resumen con todos las opciones de atributos en strftime
# # %a	Weekday name, short version	Sun
# # %A	Weekday name, full version	Sunday
# # %w	Weekday as number, 0 is Sunday	0 - 6
# # %b	Month name, shot version	Jan
# # %B	Month name, full versuib	January
# # %m	Month	01-12
# # %d	Day of the month	01 - 31
# # %Y	Four-digit year, full version	2019
# # %y	Two-digit year, short version	19
# # %H	Hour, in 24-hour format	00 - 23
# # %I	Hour, in 12-hour format	01 - 12
# # %p	AM or PM	AM, PM
# # %M	Minutes	00 - 59
# # %S	Seconds	00 - 59
# # %Z	Timezone	IST
# # %c	Local version of date and time	Thu 11 Jun 2020 08:42:30 AM IST>/code>
# # %X	Local version of time	08:43:07 AM
# # %x	Local version of date	06/11/2020



#################
# Transformar un string en un objeto datetime para poder utilizar las propiedades de un objeto datetime
from datetime import datetime as dt
string_fecha = "06/02/2020"

print("string_fecha es: ",string_fecha)
print("El tipo de dato de string_fecha es: ",type(string_fecha))
print("")

# Crear objeto dt:
nuevo_objeto_dt = dt.strptime(string_fecha, "%m/%d/%Y")
print("Objeto datetime con fecha de string fecha: ",nuevo_objeto_dt)
print("Tipo de dato de nuevo_objeto_dt: ",type(nuevo_objeto_dt))

print("El año del nuevo_objeto_dt es: ", nuevo_objeto_dt.year)
print("El mes del nuevo_objeto_dt es: ", nuevo_objeto_dt.month)
print("El dia del nuevo_objeto_dt es: ", nuevo_objeto_dt.day)
