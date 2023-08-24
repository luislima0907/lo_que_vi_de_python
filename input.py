#Datos de entrada o inputs en python, los inputs siempre nos devolverán como dato de salida del proceso, un texto o una string

#El dato que le ingresemos al input, se guardará en la variable que declaremos, en este caso nombre.
#nombre = input("Brooo, Escribe tu nombre xd \n")
#print("che este es tu nombre xd", nombre)

#numero = input("ingrese un número xddd \n")
#print(f"Este es el numero que ingresaste: {numero}")

#En caso de operar con valores númericos debemos de especificarle a python que tipo de valor vamos a ingresar, ya sea int o float.
#Y esto porque los input siempre nos van a devolver como dato de salida, una string o texto.
#Para evitar le declaramos el tipo de dato y luego adentro de unos paréntesis colocamos el input con sus debidos parámetros.

#numero_random = int(input("che ingresa el número xdd \n"))
#operacion_multiplicacion = numero_random * 2
#print(f"Este es el resultado de multiplicar el número que ingresaste x 2: {operacion_multiplicacion}")

numero_ingresado = float(input("ingresa el primer número boludoooo \n"))
numero_ingresado_dos = float(input("Ingresa el segundo numero crack \n"))
resultado_de_la_suma = int(numero_ingresado + numero_ingresado_dos)
print(f"che aqui esta el resultado de tu suma bro: {resultado_de_la_suma}")