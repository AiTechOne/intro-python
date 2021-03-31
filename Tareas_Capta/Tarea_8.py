# Tarea: Estandarizar los números telefónicos de la lista "telefonos" para que
# cumplan con el código del país y con el formato:
# "+<codigo pais> <4 numeros> <4 numeros>"
# Ejemplo (consideren los 2 espacios y el símbolo "+"):
# +56 9855 2410
#     +56 -> +<codigo pais>
#     9855 -> "primeros" 4 números
#     2410 -> "segundos" 4 números

# Observación:
# En la lista "telefonos" hay números que ya tienen el código, pero les falta el + y el formato con espacios
# Hay otros numeros que en vez del código, comienzan con un 0. Sobreescribir por el +56 y aplicar formato.
# Finalmente hay números que no tienen ni el 0 ni el código del país, solo los 8 números de teléfono. Agregar +56 y formato.


telefonos = [
    "84779928",
    "078954621",
    "5698756412",
    "5695969878",
    "092776677"
    "5668962878",
    "058923178",
]