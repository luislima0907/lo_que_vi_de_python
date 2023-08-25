#importamos el modulo sis
import sys
#El primer argumento siempre es el nombre del programa
print(sys.argv[0])

monto_texto = sys.argv[1]

if monto_texto == "":
    exit

monto = float(monto_texto)
descuento = 0

if monto >= 500 and monto <= 1000:
    descuento = monto * .05
elif monto > 1000:
    descuento = monto * .1
print("El monto del descuento es", str(monto - descuento))