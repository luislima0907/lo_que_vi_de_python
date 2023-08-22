#suma y resta (+ -)
suma = 3 + 3
resta = 7 - 6

#multiplicación y división (* /)
multiplicacion = 9 * 2
division = 10 / 2 #nos devuelve un dato float (decimal)

#potenciación (exponente) (**)
potencia = 2 ** 3

#división baja (//)
division_baja = 12 // 5 #devuelve un entero redondeado hacia abajo

#resto o modulo de la división (%)
resto = 37 % 2

#La impresión de los resultados de los operadores
print(suma, resta, multiplicacion, division, potencia, division_baja, resto)

#Con la palabra clave "type" y después encerramos entre parentésis algún dato o datos almacenados en una lista, tupla, etc, a la hora de imprimirlo nos mostrará que tipo de dato es para python
#Ejemplo: (Para un entero): <class 'int'> (Para una cadena de texto o cáracter): <class 'str'> (Para un decimal): <class 'float'> (Para un booleano): <class 'bool'>
#Ejemplo_dos: (Para una lista): <class 'list'> (Para una tupla): <class 'tuple'> (Para un conjunto): <class 'set'> (Para un diccionario): <class 'dict'>

tipos_de_datos = type(5)
tipos_de_datos_dos = type('Hola mundo')
tipos_de_datos_tres = type(3.2)
tipos_de_datos_cuatro = type(True)
tipos_de_datos_lista = type([1, "hola XDD", False])
tipos_de_datos_tupla = type((3, "XDDD", True))
tipos_de_datos_conjunto = type({"DX", 45, False})
tipos_de_datos_diccionario = type({
    "XD?": "marvin no paso copia",
    "chisme?": "NO",
    "porque?": "porque si"
})

print(tipos_de_datos, tipos_de_datos_dos, tipos_de_datos_tres, tipos_de_datos_cuatro)
print(tipos_de_datos_lista, tipos_de_datos_tupla, tipos_de_datos_conjunto, tipos_de_datos_diccionario)