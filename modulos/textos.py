#############################################
# Tutorial de textos!!
# Link en ingles: https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=2
#

# Funciones matematicas: y = f(x)
# Print también es una funcion! y se aplica sobre una variable


## Printeo basico
# x = "Hola Mundo"
# print(x)
# print("Hola Mundo")

## Printeo de una variable con diferentes comillas:
# mensaje = "Hola Mundo en comillas dobles"
# mensaje = 'Hola Mundo en comillas simples'
# mensaje = """Hola Mundo en triple-comillas dobles"""
# mensaje = '''Hola Mundo en triple-comillas simples'''
# mensaje = """Esta es la ventaja
# de las comillas
# triples (dobles o simples)
# """
# print(mensaje)


## Acceder a letras del string:
# var = "Felipe Tejada"
# Primera letra:
# print(var[0])
# Segunda letra:
# print(var[1])
# Letra numero 100 (no existe!!)
# print(var[100])
# Conjunto de letras: del 0 al 6 (al 5 realmente)
# print(var[0:6])
# Conjunto de letras: del 6 en adelante! (hasta el final)
# print(var[6:])
# Conjunto de letras: Igual que antes pero saltando el espacio:
# print(var[7:])
# imprimir desde el final hacia adelante:
#print(var[-6:])

# Almacenar substrings:
# nombre = var[0:6]
# apellido = var[7:]
# print(nombre)
# print(apellido)


# Len => lenght que es largo en ingles:
# texto = "este texto tiene muchas letras y no sabemos cuantas realmente son"
# print(texto)
# largo_texto = len(texto)
# print(largo_texto)


### Metodos especiales para strings:

# Contar:
# texto = "Felipe Tejada Felipe"
# buscar_espacios = texto.count(" ")
# buscar_felipe = texto.count("Felipe")
# buscar_e = texto.count("e")
# print(texto)
# print(buscar_espacios)
# print(buscar_felipe)
# print(buscar_e)
# print(texto.count("Felipe"))

# Buscar:
# texto = "Mi nombre es Felipe cosas varias"
# indice = texto.find("Felipe")
# print(indice)
# nombre = texto[:indice]
# print(nombre)
# Indice de algo que no existe = -1
# indice = texto.find("Tejada")
# if indice >= 0:
#     print(texto[indice:])
# else:
#     print("No se encuentra la palabra buscada")

# Reemplazar:
# text = "Mi apellido es Felipe ojo cabeza murcielago"
# print(text)
# # Ojo: "reutilizar" la variable para aplicar todas las reglas a la misma. En este caso: texto_reemplazado
# texto_reemplazado = text.replace("e", "i")
# print(texto_reemplazado)
# texto_reemplazado = texto_reemplazado.replace("a", "i")
# print(texto_reemplazado)
# texto_reemplazado = texto_reemplazado.replace("o", "i")
# print(texto_reemplazado)
# texto_reemplazado = texto_reemplazado.replace("u", "i")
# print(texto_reemplazado)

## lower y upper (mayusculas y minusculas):
# mayusculas = "eSTO ESTA EN MAYUSCULAS"
# minusculas = "Esto esta en minusculas"
# print(mayusculas)
# print(mayusculas.lower())
# print(mayusculas.upper())
# print(minusculas)
# print(minusculas.lower())
# print(minusculas.upper())

## capitalize (primera letra en mayuscula siempre):
# texto = "habia una vez..."
# print(texto.capitalize())


### Sumar strings:
# string_1 = "felipe"
# string_2 = "tejada"
# suma_strings = string_1 + string_2
# print(suma_strings)

# suma_strings_2 = string_1 + " " + string_2
# print(suma_strings_2)

# suma_strings_2 = "Bienvenido " + string_1.capitalize() + " " + string_2.capitalize()
# print(suma_strings_2)

# metodo_especial = f"Bienvenido {string_1} {string_2}"
# print(metodo_especial)
# print(f"Bienvenido {string_1} {string_2}")

# metodo_especial = "Bienvenido {} {} {}".format(string_1, string_2, "otra variable")
# print(metodo_especial)

# suma de sub-strings:
# metodo_especial = f"Bienvenido {string_1[0:3]} {string_2[0:3]}"
# print(metodo_especial)

# mezclando metodos:
# metodo_especial = f"Bienvenido {string_1[0:3].upper()} {string_2[0:3].upper()}"
# print(metodo_especial)
# metodo_especial = f"Bienvenido {string_1.capitalize()} {string_2[0].upper()}."
# print(metodo_especial)

# Mezclando fstrings con count
# texto = "Felipe Tejada"
# print(f"El texto original es: {texto}")
# contar_e = texto.count("e")
# print(contar_e)
# auxiliar = f"La letra 'e' sale en la variable 'texto' {contar_e} veces"
# print(auxiliar)

# Ejemplo para cambiar todas las letras p de texto en mayusculas:
# texto_nuevo = ""
# for caracter in texto:
#     if caracter == "p":
#         # texto_nuevo = texto_nuevo + "P"
#         # texto_nuevo = texto_nuevo + caracter.capitalize()
#         texto_nuevo = texto_nuevo + caracter.upper()
#     else:
#         texto_nuevo = texto_nuevo + caracter
# print(f"El texto nuevo es: {texto_nuevo}")


### OJO: textos pueden tener numeros, pero estos no se pueden sumar matematicamente! se suman como texto:
# a = "1"
# b = "2"
# suma = a + b
# print(suma)

# a = 1
# b = 2
# suma_2 = a+b
# print(suma_2)

# a = "1"
# b = 2
# suma_3 = a+b


# Se pueden transformar textos a numeros si solo contienen numeros!
# a = "1"
# print(type(a))
# a_entero = int(a)
# print(type(a_entero))
# b = 2
# print(a_entero+b)

# Funciones matematicas: y = f(x)
# Print también es una funcion! y se aplica sobre una variable
# Si f = int y x = a => int(a) es aplicar la funcion entero en variable a.