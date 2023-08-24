#Mostrar las claves o keys de los diccionarios con el método keys. Al ejecutarlo nos mostrará todas las claves o keys que contiene nuestro diccionario, pero no mostrará sus valores.

diccionario = {
    #clave - Valor
    #key  -   Value
    "nombre": 'Carlos',
    'apellido': 'Pérez',
    'amigos': 10,
}

claves = diccionario.keys()
print(claves)

#Mostrar el valor de una clave o key con el método get, debemos de escribir adentro de los parámetros el nombre de la clave que queremos saber su valor.

claves_get = diccionario.get("apellido")
print(claves_get)

#borrar un diccionario con el método clear.

diccionario_dos = {
    #clave - Valor
    #key  -   Value
    "Nombre": 'carlos',
    'Apellido': 'pérez',
    'Amigos': 0
}

diccionario_dos.clear()
print(diccionario_dos)

#borrar un elemento del diccionario con el método pop, para eso debemos de escribir la clave del elemento que queremos eliminar. Esto se hace dentro de los parámetros.
#Si queremos eliminar varios elementos, podemos escribir sus claves entre comillas y separadas con una coma ,

diccionario_tres = {
    "Nombre": 'Luis',
    'apellido': 'Lima',
    'amigos': 5
}

diccionario_tres.pop('amigos')
print(diccionario_tres)

#Iterar los elementos y claves de un diccionario con el método items

diccionario_iterado = diccionario_tres.items()
print(diccionario_iterado)