#con el primer igual después de la variable le estamos asignando un valor a la misma, pero con dos iguales "==" estamos comparando el valor de la vairable con otro valor
#Y esto a la hora de ejecutarlo nos puede dar verdadero o falso, dependiendo del tipo de dato que hemos comparado
es_igual_que = 5 == 6

#Aquí estamos diciendo que el 3 es distinto al 4, siguiendo la misma formula de asignación y comparación del primer ejemplo.
#Nos puede dar verdadero o falso igualmente.
#con operador de distinto "!="
es_distinto_que = 3 != 4

#con operador mayor que ">"
es_mayor_que = 6 > 2

#con operador menor que "<"
es_menor_que = 40 < 100

#con operador mayor o igual que ">="
es_mayor_o_igual_que = 7 >= 8

#con operador menor o igual que "<="
es_menor_o_igual_que = 1 <= 10

print(es_igual_que, es_distinto_que, es_mayor_que, es_menor_que, es_mayor_o_igual_que, es_menor_o_igual_que)

#Ejercicio de calculos combinados

a = 10
b = 15
c = 30

comparacion = a + b == c

print(comparacion)

#Ejercicio de comparar nombres de usuario

contraseña_almacenada = "LolXDDD"
contraseña_escrita = "lolxddd"

contraseña_almacenada_dos = "MaicraGamer"
contraseña_escrita_dos = "MaicraGamer"

#tambien podemos hacer comparaciones dentro de un print (imprimir)
print(contraseña_almacenada == contraseña_escrita)
print(contraseña_almacenada_dos == contraseña_escrita_dos)

