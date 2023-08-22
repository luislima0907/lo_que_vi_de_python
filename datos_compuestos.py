#Este es un ejemplo de un dato compuesto, básicamente contiene un arregllo dónde cada elemento del arreglo tiene un
#índice que inicia desde el 0 hasta el 9, por lo tanto, el primer elemento va ser el índice 0 y así sucesivamente.
#Una lista puede ser modificable, es decir, sus valores pueden cambiar y esta se identifa cuando lleva corchetes[]
#Para encerrar a los elementos

#Para querer mostrar el elemento que este en un índice siempre debemos de poner el número del índice dentro de corchetes[]
#Por defecto python elimina la necesidad de escribir el índice cada vez que vayamos a nombrar un elemento, a diferencia del diccionario dónde si es necesario escribir un nombre para identificar los elementos.

lista = ["Luis Lima", "Soy Carlos", False, 1.60]
print(lista[0])

#Esto es válido
lista[3] = "Marvin"
print(lista[3])

#La diferencia entre una lista y una tupla es de que los elementos que estén dentro de ella no se pueden modificar.
#Los elementos dentro de una tupla van entre parentésis().
tupla = ("Carlos Pérez", "Soy Luis", True, 1.50)
print(tupla[0])

#Esto no es válido
#tupla[3] = 'Marco'
#print(tupla[3])

#Creación de Conjuntos

#Los elementos que esten dentro de un conjunto se deben de encerrar en llaves{}
#La ventaja de los elementos de los conjuntos es que pueden cambiar de lugar y no son fijos como lo pueden ser las tuplas o las listas.
#Son casi igual que las listas solo que los elementos en un conjunto no se pueden modificar, pero si se puede crear otra vez el conjunto u otro conjunto para modifcarlo.
#Tampoco podemos repetir valores dentro de un conjunto porque a la hora de ejecutarlo solo nos mostrará un solo elemento de los repetidos.

conjunto = {"Hola", "¿Cómo estás?", False, 1.20}

#Esto no es válido
#conjunto[1] = 'Luisa'
#print(conjunto[1])

#Esto si es válido
conjunto = {"Jajajaj te chingue XDDDD"}
print(conjunto)

#Los diccionarios
#Son parecidos a las listas, pero con la diferencia que aqui los elementos no tienen un índice, sino un nombre que los contiene.
#Para crear un diccionario debemos de hacer dentro de llaves, pero dejando un espacio entre arriba y abajo para poder escribir los elementos en el centro, como si fuera una función o CSS.
#Para separar las keys juntos a sus values debemos de poner una coma " , "

diccionario = {
    #clave - Valor
    #key  -   Value
    "Hola": 'Hola mundo',
    'soy ese': 'cerebron',
    'Estoy emocionado': True,
    'mido': 2.00,
    "dato_duplicado": 'cerebron'
}

print(diccionario["soy ese"])
print(diccionario["mido"] + 10)