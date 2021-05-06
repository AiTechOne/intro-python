from datetime import datetime as dt
from datetime import timedelta as td
import time

fecha_hora = dt.now()
# print(dir(fecha_hora))

# print( fecha_hora.date() )
# print( fecha_hora.time() )
# print( fecha_hora.weekday() )
# print( fecha_hora.year )
# print( fecha_hora.month )
# print( fecha_hora.day )
# print( fecha_hora.hour )
# print( fecha_hora.minute )
# print( fecha_hora.second )

delta_tiempo = td(days=5, minutes=10, seconds=30)
print(delta_tiempo)

print(fecha_hora + delta_tiempo)