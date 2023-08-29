#creando un conjunto con la palabra clave o función set, funciona igual que la tuple, le damos una lista dentro de los parámetros de la función.
conjunto = set(["Dato 1", "Dato 2"])
print(conjunto)

#anidando o juntando conjuntos entre si con la palabra clave o función frozenset, esta función nos servirá para poder anidar conjuntos.
#debemos de declarar una variable que contenga el conjunto que vamos a anidar, luego escribimos la palabra clave y dentro de los parámetros ponemos un conjunto normal, siempre utilizando una lista normal para que luego se modifique a un conjunto.

conjunto_uno = frozenset(["Dato 3", "Dato 4"])
conjunto_dos = {conjunto_uno, "Dato 5"}
print(conjunto_dos)

#Teoría de conjuntos

conjunto_tres = {1,3,5,7}
conjunto_cuatro = {1,3,7}

#Aqui lo que estamos haciendo es de el programa nos diga si un conjunto es subconjunto de otro, o en palabras simples, tienen una intersección entre los mismos conjuntos, esto nos puede devolver True o False.
interseccion_subconjuntos_de_los_ejemplos = conjunto_cuatro.issubset(conjunto_tres)
print(interseccion_subconjuntos_de_los_ejemplos)

#Otra forma de averiguar si hay un subconjunto entre dos o más conjuntos es usando los operadores (<=)
#con este ejemplo decimos que, si el primer conjunto tiene la misma o menor cantidad de elementos iguales al segundo conjunto.
interseccion_subconjuntos_de_los_ejemplos_dos = conjunto_cuatro <= conjunto_tres
print(interseccion_subconjuntos_de_los_ejemplos_dos)

#Para saber si hay un superconjunto entre dos o más conjuntos, debemos de usar el método issuperset de la misma manera que el primero, nos devolverá true o false
interseccion_superconjuntos_de_los_ejemplos_uno = conjunto_tres.issuperset(conjunto_cuatro)
print(interseccion_superconjuntos_de_los_ejemplos_uno)

#Podemos usar los comparadores (>=) de la misma manera que con el subconjunto
#con este ejemplo decimos que, si el primer conjunto tiene la misma o mayor cantidad de elementos iguales al segundo conjunto.
interseccion_superconjuntos_de_los_ejemplos_dos = conjunto_tres >= conjunto_cuatro
print(interseccion_superconjuntos_de_los_ejemplos_dos)

#Aunque lo podemos simplicar sin necesidad de escribir el (=), podemos verificarlo con un (<) o (>) esto solo aplica para los superconjuntos.

#Si queremos verficar que un conjunto no tenga elementos en común con otro conjunto, debemos de usar el método isdisjoint
#cabe mencionar que si almenos un elemento es común entre los conjuntos, nos dará como resultado false
conjunto_cinco = {0,1,2,3}
conjunto_seis = {4,5,6,7}

elementos_no_comunes = conjunto_cinco.isdisjoint(conjunto_seis)
print(elementos_no_comunes)