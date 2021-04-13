# Tarea: Accede y guarda en una variable llamada "nota_historia" el valor
# de la sub-llave historia del diccionario presente más abajo.

# Luego, imprime en un f-string la nota de Pedrito en Historia utilizando "nota_historia"

# Finalmente, actualiza el valor de la llave a un 7.0 e imprime las notas de todos
# los ramos del alumno con un ciclo for o uno while. Puedes utilizar los métodos
# items(), keys() o values() si te facilitan la vida.

diccionario = {
    "alumnos":{
        "Pedrito":{
            "curso":"2°D",
            "notas":{
                "matematica": 5.5,
                "lenguaje": 4.8,
                "biologia": 6.0,
                "quimica": 6.8,
                "fisica":4.5,
                "historia":6.5
            }
        },
        "Jose":{
            "curso":"2°D",
            "notas":{
                "matematica": 5.5,
                "lenguaje": 4.8,
                "biologia": 6.0,
                "quimica": 6.8,
                "fisica":4.5,
                "historia":1.0
            }
        }
    }
}

print(diccionario["alumnos"]["Jose"]["notas"]["historia"])