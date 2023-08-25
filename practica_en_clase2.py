import sys

print(sys.argv[0])

argumento = sys.argv[1]

if argumento == "ayuda":
    print("""Para ejecutar el programa debe escribir el comando de esta forma
python .\clase.py monto_a_calcular""")
    sys.exit()
    
monto = float(argumento)
descuento = 0

if monto >= 500 and monto <= 1000:
    descuento = monto * .05
elif monto > 1000:
    descuento = monto * .1
print("El monto del descuento es", str(monto - descuento))