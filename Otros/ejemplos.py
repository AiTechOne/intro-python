numeros = [55, 91, 70, 64, 12, 32, 64, 35, 88, 98, 100, 3, 5, 101]

# print("Caso 1")
# print(max(numeros))
# print(min(numeros))
# print(sum(numeros))

# print("Caso 2")
numero_maximo = numeros[0]
segundo_maximo = numeros[0]
for numero in numeros:
    if numero > numero_maximo:
        segundo_maximo = numero_maximo
        numero_maximo = numero
    else:
        if numero > segundo_maximo:
            segundo_maximo = numero



    # if numero < numero_minimo:
    #     numero_minimo = numero
    # else:
    #     if numero < segundo_menor:
    #         segundo_menor = numero

    # suma_numeros += numero


# print(f"Maximo: {numero_maximo}")
# print(f"Segundo mayor: {segundo_maximo}")
# print(f"Minimo: {numero_minimo}")
# print(f"Segundo minimo: {segundo_menor}")
# print(f"Suma: {suma_numeros}")


for numero in numeros:
    print(f"Analizando el número: {numero}")
    print(f"    Maximo = {numero_maximo} y Segundo Maximo = {segundo_maximo}")
    if numero > numero_maximo:
        print(f"       Mayor: {numero} > {numero_maximo} -> numero_maximo = {numero}")
        print(f"       Segundo Mayor: {numero_maximo} => {segundo_maximo} -> segundo_maximo = {numero_maximo}")
        segundo_maximo = numero_maximo
        numero_maximo = numero
    else:
        if numero > segundo_maximo:
            print(f"       Segundo mayor: {numero} > {segundo_maximo} -> segundo_maximo = {numero}")
            segundo_maximo = numero
