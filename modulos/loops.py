#############################################
# Loops o bucles
#

### Ciclos For:
# numeros = [1,2,3,4,5]

# numero = numeros[0]
# print(numero)
# numero = numeros[1]
# print(numero)
# numero = numeros[2]
# print(numero)
# numero = numeros[3]
# print(numero)
# numero = numeros[4]
# print(numero)

# for numero in numeros:
#     print(numero)

# Uso de break:
# for numero in numeros:
#     if numero == 3:
#         print("Numero 3 encontrado en lista numeros! Terminando")
#         break
#     print(numero)
# print("Ciclo For Finalizado!")

# numeros = [1,2,3,4,5]
# # Uso de continue:
# for numero in numeros:
#     if numero == 3:
#         print("Numero 3 encontrado en lista numeros! Saltando al siguiente numero")
#         continue
#     print("hola", numero)

# Loops dentro de loops:
# for numero in numeros:
#     print(f"La variable numero es igual a {numero}")
#     for x in numeros:
#         print(numero, x)
    # for letra in 'abc':ange(0,10)
# for numero in numeros:
#     if numero in [2, 4, 5]:
#         continue
#     for letra in 'abc':
#         print(numero, letra)
    # print("Hola")

# Funcion Range
# rango = range(15,20)
# print(rango)
# # Ver tipo de variable:
# print(type(rango))
# # # Transformar rango a lista:
# print(list(rango))
# # Transformar rango a entero?:
# print(int(rango)) # no se puede!

# rango = range(0,10)
# print(rango)
# print(list(rango))
# rango = range(5,10)
# print(rango)
# print(list(rango))

# rango = range(1,6)
# print("Caso 1:")
# for elemento in rango:
#     print(elemento)

# print("Caso 2:")
# for elemento in range(1,6):
#     print(elemento)

# numeros = ["a", "b", "c", "d", "e"]
# print("Caso basico:")
# for numero in numeros:
#     print(numero)

# print("Caso Range:")
# for indice in range(len(numeros)):
#     print(numeros[indice])


# nombres =   ["Felipe",  "Michael", "Felipe"]
# apellidos = ["Sequeira", "Arredondo", "Tejada"]
# edades =    [26, 17, 28]

# for indice in range(len(nombres)):
#     print(f"{nombres[indice]} {apellidos[indice]} tiene {edades[indice]} años")

# En matematica se suele utilizar como indice u subindice las letras: i, j, k, n, m
# for i in range(0,3):
#     for j in range(15,18):
#         for k in range(30,32):
#             print(i, j, k)


## Ciclos While!
# while en español es equivalente a: "mientras"
# Loop finito:
x = 0
while x < 10:
    if x in [2,4,6]:
        x += 1
        continue
    print(x)
    x += 1
print("Finalizado!")    # x += 1

# x = 10
# condicion = x >= 10
# print(condicion)

# x= 0
# while x < 10:
#     print(x)
#     x += 1
# print("terminado")

# Loop infinito:
# x = 0
# while True:
#     print(x)
    # x+=1

# # While con otra condicion:
# lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# while len(lista_electrica)>0:
#     print(lista_electrica)
#     lista_electrica.pop()
# print(lista_electrica)

# # while dentro de un while:
# x = 0
# lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# while len(lista_electrica)>0:
#     print(lista_electrica)
#     lista_electrica.pop()
#     while x<10:
#         print(x)
#         x = x + 1
#         #x += 1
#     x = 0


# # while con un for:
# lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
# while len(lista_electrica)>0:
#     print(lista_electrica)
#     lista_electrica.pop()
#     for i in range(10):
#         print(i)


# primeros_10_numeros_primos = [2,3,5,7,11,13,17,19,23,29]
# for n in range(31):
#     if n in primeros_10_numeros_primos:
#         print(f"{n} es primo! :D")
#     else:
#         print(f"{n} no es primo :(")

# Imprimir los numeros pares entre 0 y 100
# for n in range(0,101):
#     print(n, n%15)
    # if n%2 == 0:
    #     print(n)
    # print(n, n % 2)

# Imprimir los numeros impares entre 0 y 100
# for n in range(0,101):
#     print(n, n%15)
    # if n%2 == 1:
    #     print(n)
    # print(n, n % 2)
