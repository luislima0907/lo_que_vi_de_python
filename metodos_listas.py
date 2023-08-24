#Crear una lista con la función list, debemos de darle los parámetros de una lista normal

lista = list(["Hola", 34, 56.7])
print(lista)

#Contar la cantidad de elementos de una lista con la función len.

lista_dos = list(["jajaja", "xd", 45, 90.8])
conteo_de_elementos = len(lista_dos)
print(conteo_de_elementos)

#agregar un elemento a una lista con el método append. Aquí no es necesario guardar el resultado dentro de una variable, ya que este método solo agrega un elemento a la lista original.

lista_tres = ["hola", "mundo", "como estan"]
lista_tres.append("soy ese")
print(lista_tres)

#Agregar un elemento a una lista con el método insert. Este funciona cuando le indicamos el índice específico dónde queremos agregar un elemento y luego agregamos el valor, puede ser de cualquier tipo.
#El elemento se va a agregar normalmente y correrá un espacio más adelante el elemento que ocupaba esa posición anteriormente.

lista_cuatro = ["yulia", 90, False, True]
lista_cuatro.insert(3, 78)
print(lista_cuatro)

#Agregar varios elementos con el método extend. Con este agregamos uno o varios elementos a una lista, pero debemos de poner adentro de los parámetros los corchetes [] para que sepa que es una lista la que estamos modificando.

lista_cinco = ["ula", "ola", 78, True, False, 67.3]
lista_cinco.extend(["kionda", "xd", 100])
print(lista_cinco)

#Eliminar un elemento de una lista con el método pop. Aquí debemos de especifcar el índice que queremos eliminar dentro de la lista, esto lo hacemos adentro de los parámetros.
#Pero si queremos eleminar el último elemento de la lista, solo escribimos el -1 dentro de los parámetros del método. Y si queremos elminar el penúltimo de la lista escribimos -2 y así sucesivamente.

lista_seis = ["ctm", "yutu", True, False, 56, 89, 100.01]
print(len(lista_seis))
lista_seis.pop(1)
lista_seis.pop(-1)
print(lista_seis)
print(len(lista_seis))

#remover un elemento de una lista con el método remove. Aquí debemos de especificar dentro de los parámetros cual va a ser el elemento que queremos eliminar, lo debemos de escribir bien para que se puede ejecutar sin errores.

lista_siete = ["carlos", "perez", 90, 676.23]
lista_siete.remove("carlos")
print(lista_siete)

#Eliminar todos los elementos de una lista con clear.

lista_ocho = ["19831290", 78, "18273djakdja"]
lista_ocho.clear()
print(lista_ocho)

#ordenar de manera ascendente (de menor a mayor) los elementos númericos o booleanos en una lista con el método sort.
#cabe destacar que se ordenan así: false, true, 1, 2, 3 ......
#Aparte de eso, podemos revertir el orden con el parámetro reverse= y el valor del elemento de la lista, esto los ordenará de manera descendiente (de mayor a menor)

lista_nueve = [90, 17, 23, 87,True, False]
lista_nueve.sort()
print(lista_nueve)
lista_nueve.sort(reverse=90)
print(lista_nueve)

#revertir el orden de una lista con el método reverse. Esto no lo ordena de mayor a menor solo le cambia el orden, es decir, el último elemento pasa a ser el primero, el penúltimo elemento pasa a ser el segundo y asi sucesivamente.

lista_diez = [90, False, True, False,True, 8192, 2023]
lista_diez.reverse()
print(lista_diez)
