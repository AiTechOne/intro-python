####
# # Metodo 1:
# lista_strings = ["ebcde", "hbc", "cb", "abcd", "jbcdee", "a", "zbcde"]
# lista_auxiliar = []
# for string in lista_strings:
#     auxiliar = [ len(string), string ]
#     lista_auxiliar.append(auxiliar)

# print(lista_auxiliar)
# lista_auxiliar.sort()
# print(lista_auxiliar)
# string_corto = lista_auxiliar[0]
# string_largo = lista_auxiliar[-1]

# print(f"El string mas corto es {string_corto}")
# print(f"El string mas largo es {string_largo}")

####
# Metodo 2:
lista_strings = ["ewqewqewq", "bcd", "ebcde", "hbc", "cb", "abcd", "jbcdee", "a", "zbcde"]

auxiliar_mas_corto = 'ewqewqewq'
auxiliar_mas_largo = "ewqewqewq"

for string in lista_strings:
    #print(f"Analizando el string: {string}")
    if len(auxiliar_mas_corto) > len(string):
        #print(f"   El string={string}({len(string)}) es más corto que auxiliar_mas_corto={auxiliar_mas_corto}({len(auxiliar_mas_corto)})")
        auxiliar_mas_corto = string
        #print("    ---> SOBREESCRIBIENDO!")
    #else:
        #pass
        #print(f"   El string={string}({len(string)}) NO ES MAS corto que auxiliar_mas_corto={auxiliar_mas_corto}({len(auxiliar_mas_corto)}). Siguiendo con el siguiente")

    if len(auxiliar_mas_largo) < len(string):
        auxiliar_mas_largo = string

print(f"String mas corto: {auxiliar_mas_corto} ")
print(f"String mas largo: {auxiliar_mas_largo} ")