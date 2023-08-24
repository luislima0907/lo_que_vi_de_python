contraseña_establecida = "Contraseña"
contraseña_ingresada = input("Ingrese la contraseña, por favor \n")

if contraseña_ingresada == contraseña_establecida:
    print("Iniciando sesión...")
else:
    print("Error, contraseña no válida, ingreselá de nuevo.")
    
primer_numero_ingresado = float(input("Ingrese el primer numero \n"))
segundo_numero_ingresado = float(input("Ingrese el segundo numero \n"))

if segundo_numero_ingresado == 0:
    print("Error, No puedes dividir en 0")
else:
    resultado_de_la_division = primer_numero_ingresado / segundo_numero_ingresado
    print(f"Aqui esta el resultado de tu division {resultado_de_la_division}")
    
numero_entero_ingresado = int(input("Escriba un numero y le diremos si es par o impar \n"))
conversion_a_par_o_impar = numero_entero_ingresado % 2

if conversion_a_par_o_impar == 0:
    print("tu numero es par")
else:
    print("tu numero es impar")
