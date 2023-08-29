#Creando diccionarios con la función dict, debemos de brindarle variables que contengan un valor dentro de los parámetros de la función, cada clave y valor, o variable y elemento, lo debemos separar por una coma.
diccionario = dict(nombre = "Danilo", Apellido = "Ucelo")
print(diccionario)

#las palabras claves para crear las listas, tuplas, conjuntos, diccionarios, etc, nos pueden servir para crear cosas así pero que estén vacías, de lo contrario no las podemos crear vacías.

#También podemos hacer que una tupla actue como una clave de un diccionario, también podemos añadir una lista a un diccionario, pero usando frozenset

diccionario_dos = {("nombre", "apellido"): "fjaskdf"}
diccionario_tres = {frozenset(["Hola XDD", "Mundo xddd"]): 0}

print(diccionario_dos)
print(diccionario_tres)

#Creando diccionarios con el método de fromkeys, una cosa a tomar en cuenta es que para que no nos iteré las claves, debemos de crear una lista dentro de los parámetros para darle nombre a las claves, y afuera de esa lista debemos de poner los valores separados por una coma
diccionario_cuatro = dict.fromkeys(["Nombre", "Apellido"])
print(diccionario_cuatro)

diccionario_cinco = dict.fromkeys(["Nombre", "Apellido"], "Saber")
print(diccionario_cinco)