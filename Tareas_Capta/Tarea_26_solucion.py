# Crear un codigo que entregue la fecha de hoy y la de los siguientes "x" días utilizando un ciclo for.
# Imprimir con f-string: 'En <n> dias a partir de hoy, la fecha sera <dias-mes-año>'.
# Considera que n debe partir en 1 y debe llegar hasta el valor de X, por tanto tendrás que imprimir x lineas.

from datetime import datetime as dt
from datetime import timedelta as td

fecha_hoy = dt.now().date()
dias_a_analizar = int(input("Ingrese el numero de dias a analizar: "))
for n in range(1,dias_a_analizar+1):
    fecha_nueva = fecha_hoy + td(days=n)
    print(f"En {n} dia(s) a partir de hoy, la fecha sera {fecha_nueva}")