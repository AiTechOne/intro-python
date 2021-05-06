# Leer un archivo con python:

# Para abrir un archivo con python se utiliza el metodo open(). Existen diferentes modos de abrir un archivo. Los principales son:
# Leer (read -> 'r') para solamente cargar el archivo y ver su contenido.
# Escribir (write -> 'w') para crear un archivo (si no existe) o sobreescribirlo y escribir cosas.
# Agregar (append -> 'a') para crear un archivo (si no existe) o agregarle nuevas cosas (al final).

################
# Leer archivos: similar al método input(), los archivos al leerlos los tendremos que tratar como strings. Si hay números
# en el texto, podemos transformarlos utilizando el método int o float, pero eso lo veremos con el tiempo.

# Obs: utilizaremos el método especial 'with' y 'as' de python para simplificar y asegurar el correcto manejo
# del archivo. Después les explicaré mejor esta parte.

# 1. Uso metodo open para guardar todo el texto del archivo en una variable llamada 'texto_archivo'
# nombre_archivo_a_abrir = 'prueba.txt'
# with open(nombre_archivo_a_abrir, mode='r') as archivo:
#     texto_archivo = archivo.read()
# print(texto_archivo)

# # 2. Uso del método open para leer una linea( del archivo (la primera)
# nombre_archivo_a_abrir = 'prueba.txt'
# with open(nombre_archivo_a_abrir, mode='r') as archivo:
#     linea = archivo.readline()
#     print(linea)
#     # Podemos crear un while para ir leyendo las lineas siguientes como:
#     while linea:
#         linea = archivo.readline()
#         print(linea)

# ################
# # Escribir archivos: similar a lo anterior, ahora cambiaremos el mode a 'w' o 'a'.

# 1. Crear un archivo: este codigo crea un nuevo archivo y le escribe el texto de la variable "texto_a_guardar"
# nombre_nuevo_archivo = 'nuevo_archivo.txt'
# texto_a_guardar = f'Esta es una linea de texto que sera almacenada en el archivo {nombre_nuevo_archivo}'
# with open(nombre_nuevo_archivo, mode='w') as nuevo_archivo:
#     nuevo_archivo.write(texto_a_guardar)

# with open(nombre_nuevo_archivo, mode='r') as nuevo_archivo:
    # print(nuevo_archivo.read())

# # 2. Agregar elementos a un archivo:
# nombre_nuevo_archivo = 'nuevo_archivo.txt'
# texto_a_Agregar = f'Esta es una DSADSADAS linea de texto que sera almacenada en el archivo {nombre_nuevo_archivo}\n'
# with open(nombre_nuevo_archivo, mode='a') as nuevo_archivo:
#     nuevo_archivo.write(texto_a_Agregar)
