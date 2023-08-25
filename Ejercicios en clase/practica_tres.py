print("Este es mi primer programa")

import sys
print(sys.argv[0])
argumento_de_ayuda = sys.argv[1]
edad_del_usuario = sys.argv[2]

if argumento_de_ayuda == "ayuda" or argumento_de_ayuda == "Ayuda" or argumento_de_ayuda == "help" or argumento_de_ayuda == "Help":
    print("""Para ejecutar el programa debe escribir el comando de esta forma
python .\practica_tres.py SU_EDAD""")
    sys.exit()

if edad_del_usuario >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
