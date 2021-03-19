lista_electrica = ["Lavado", "Arredondo", "Basilio", "Sequeira", "Carrasco", "Tejada"]
nombre_a_buscar = "Tejada"
try:
    #raise IOerror
    indice = lista_electrica.index(nombre_a_buscar)
    print("El elemento buscado si existe en lista")
except KeyError:
    print("Fue un error de tipo 'KeyError'")
except ValueError:
    print("No esta en la lista")
except Exception as error:
    print("Fue otro error, pero no tiene que ver con si estaba o no en la lista")
