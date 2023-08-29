#Desempaquetar valores de una tupla o variables, aquí estamos creando una tupla con tres valores, pero cuando nosotros queremos
#almacenar un elemento que contenga la tupla en una variable aparte lo que debemos de hacer es crear una variable para cada elemento
#de preferencia con un nombre que las identifique para no confundirnos y al final le asignamos el nombre de la variable que contiene la tupla

datos = ("Luis", "Lima", 1000)
#Cabe recordar que se deben de crear la misma cantidad de variables para poder almacenar cada elemento de la tupla
nombre,apellido,suscriptores = datos
print(nombre)

#Esto se puede hacer con las listas, conjuntos, diccionarios, etc.
datos_en_lista = ["Carlos", "Perez", 18]
segundo_nombre,segundo_apellido,anios = datos_en_lista
print(segundo_apellido)