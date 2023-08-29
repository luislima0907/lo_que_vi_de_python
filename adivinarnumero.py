#EL programa genera un numero aleatorio en tre 1 y 10 y adivina el numero.
#Debe darle instrucciones el numero es mayor o menor o si acerto
import random

numero = int(input("Ingrese el numero \n"))
numero_aleatorio = random.randint(1, 10)

acerto = False

while(not acerto):
    if numero==numero_aleatorio:
        print("has acertado el numero")
        acerto = True
    if numero > numero_aleatorio:
        print("Estas cerca")
    if numero < numero_aleatorio:
        print("Es menor")
    numero = int(input())