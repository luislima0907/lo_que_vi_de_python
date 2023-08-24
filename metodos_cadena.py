#Las funciones en python toman un valor que le brindemos en el parentesis () y luego hace algo con ello, es importante recordar que hay diversas funciones.

string_uno = "Hola mundo"
numero_uno = 4
numero_dos = 3.12
lista = ["Hola Xdd", 4, 67.9]
tupla = ("alo", 56, 90.2)
conjunto = {"ula", 90, 23.7}
diccionario = {
    "nombre": "Luis",
    "apellido": "Lima",
    "estatura": "1.50"
}
booleano_uno = True

#palabra clave dir, con esta función podemos hacer que nos brinde la cantidad de atributos que le podemos aplicar a un objeto, ya sea un texto, un número, un decimal, una lista, etc.
#Esto lo podemos tomar como una especie de guía para poder recordar los atributos que podemos aplicar hacia algo en específico.
#para ejecutarlo debemos de poner un print y luego adentro de los parentésis la palabra dir y luego adentro de otros paréntesis, le colocamos los el objeto o valor que queremos analizar.
#y automáticamente nos mostrará los atributos que podemos aplicar hacia el mismo.
#podemos almacenar un dir dentro de una variable para luego imprimirla, asi se sentiria mas ordenado, ya que el dir deja los valores sueltos, por lo tanto, sería necesario guardarlos dentro de una variable.

#print(dir(string_uno))
#atributos de texto o strings
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


#print(dir(numero_uno))
#atributos de un número entero (int)
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

#print(dir(numero_dos))
#atributos de un número flotante o decimal (float)
#['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

#print(dir(lista))
#atributos de una lista
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

#print(dir(tupla))
#atributos de una tupla
#['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

#print(dir(conjunto))
#atributos de un conjunto
#['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

#print(dir(diccionario))
#atributos de un diccionario
#['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#print(dir(booleano_uno))
#atributos de un boleano
#['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']

#Los métodos en python, primero va el nombre o el valor del dato, luego un punto ( . ) y de último el nombre del método seguido de un paréntesis () que puede contener o no un parametro.

#ejemplo
texto_uno = "Que onda vos"
texto_dos = "kIONDA"
texto_tres = "hola como estas"

#método upper, convierte cada letra de un texto o string en MAYUSCULAS
prueba_de_metodo = texto_uno.upper()
print(prueba_de_metodo)

#método lower, convierte cada letra de un texto o string en minúsculas
prueba_de_metodo_dos = texto_dos.lower()
print(prueba_de_metodo_dos)

#método capitalize, convierte la primera letra de un texto o string en inicial mayúscula
prueba_de_metodo_tres = texto_tres.capitalize()
print(prueba_de_metodo_tres)

#método find, este encuentra la posición de un elemento dentro de un objeto, puede ser una string, lista, etc.
#para especificar que valor queremos encontrar, debemos de darle el parámetro dentro de los paréntesis.
#cuando este método no encuentra la posición de un elemento, nos dará como resultado -1 
prueba_de_metodo_cuatro = texto_uno.find("s")
print(prueba_de_metodo_cuatro)

#metodo index, funciona casi igual al find solo que este cuando no encuentra un elemento da error, porque funciona como manejo de excepciones.

#Esto da error y el programa se detiene.
#prueba_de_metodo_cinco = texto_dos.index("5")
#print(prueba_de_metodo_cinco)

#Debemos de escribir correctamente el valor dentro de los parámetros para poder encontrar su posición.
lista_de_prueba = ["jaja", "hola"]
prueba_de_metodo_cinco = lista_de_prueba.index("hola")
print(prueba_de_metodo_cinco)

#método isnumeric, esta función encuentra un elemento númerico dentro de una string y dará como resultado True si lo llegará a encontrar.
#cabe recordar que no le podemos dar un parametro, ya sea un número o cáracter, ya que esta función no está buscando el índice o posición del número.
#sino mas bien, solo nos indicará si toda la string tiene elementos númerico con true o false.
string_numerica = "8923140asdfjag"
prueba_de_funcion = string_numerica.isnumeric()
print(prueba_de_funcion)

#método isalpha, esta función nos dará como resultado verdadero si encuentra una string que no tenga espacios o carácteres especiales.
#como lo pueden ser los espacios o símbolos, etc, también no tienen que haber números dentro de la string, va a ser verdadera si la string solo es de las letras del abecedario A-Z.
string_de_solo_letras = "aksdjfjqwfaskdfhoqv"
prueba_de_funcion_dos = string_de_solo_letras.isalpha()
print(prueba_de_funcion_dos)

#método count, esta función cuenta las veces que se repite un elemento dentro de una string. Debemos de definir un parámetro para determinar el número de coincidencias.
#si no encuentra ninguna repetición o coincidencia, se mostrará un 0.
string_de_coincidencias = "hola como estas amigo"
prueba_de_funcion_tres = string_de_coincidencias.count("o")
print(prueba_de_funcion_tres)

#método len, esta función muestra la cantidad de caráteres de una string.

string_de_caracteres = "Hola, mundo."
prueba_de_metodo_cinco = string_de_caracteres.__len__()
print(prueba_de_metodo_cinco)


#método startswith, este método nos dará como resultado verdadero si dentro del parámetro le colocamos las iniciales de nuestra string.

string_de_iniciales = "Hola wachin kionda"
prueba_de_metodo_seis = string_de_iniciales.startswith("Hol")
print(prueba_de_metodo_seis)

#método endswith, este método es similar al anterior, solo que este evalúa los caráteres que conformen el final de nuestra string.

string_de_finales = "Quiero aprender word"
prueba_de_metodo_siete = string_de_finales.endswith("rd")
print(prueba_de_metodo_siete)

#método replace, este método remplaza carácteres de nuestra string. Primero debemos de darle el primer parámetro o parte que queremos modificar en nuestra string en comillas y luego lo separamos por una coma.
#una vez hecho eso, ya podemos definir el remplazo dentro de comillas.
#cabe recordar que primero debemos de escribir bien la coincidencia o repeticion de nuestra string vieja para poder asignarle un nuevo valor despues, en caso de que no lo cumplamos, nos devolverá la string original.

string_reemplazable = "Que buena onda" 
string_nueva = string_reemplazable.replace("Que", "Gracias")
print(string_nueva)

#método split, este método separa las strings por medio del valor que le ingresemos en el parámetro.
#el valor que pongamos dentro del parámetro se remplazará por una coma

string_separable = "Yutu morado"
prueba_de_metodo_ocho = string_separable.split(" ")
print(prueba_de_metodo_ocho)