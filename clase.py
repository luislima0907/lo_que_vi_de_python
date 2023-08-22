#importamos el modulo sis
import sys
#El primer argumento siempre es el 0
print(sys.arg[0])

argumento = sys.arg[1]

if argumento == "ayuda" or argumento == "help":
    print("""Para ejecutar el programa debe ingresar el argumento 1
          python examen_valores_por_argumento.py""")
    sys.exit()
    
monto = float(argumento)
descuento = 0