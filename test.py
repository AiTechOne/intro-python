lista = [
    "nada",
    "nada",
    "nada",
    "medir",
    "nada",
    "nada",
    "nada",
    "medir",
    "nada",
    "nada",
    "nada",
    "medir",
    "nada",
    "nada",
    "nada",
    "medir",
    "medir",
    "medir"
    ]


def medir():
    print(1231321321)

medir_ahora = False
for accion in lista:
    if accion == 'nada':
        print("No hay nada que hacer")
    if accion == 'medir':
        print("Preparandonos para medir... -> medir_ahora = True")
        medir_ahora = True
    if medir_ahora == True:
        medir()
        medir_ahora = False


# timer = 30 segundos
# comandos_entrantes = False
# while True:
#     escuchar_amaru()
#
#     if comandos_entrantes == True:
#         procesar_comando()
#         comandos_entrantes = False
#
#     if timer_agotado():
#         medir_sensor()
#         reset_timer()