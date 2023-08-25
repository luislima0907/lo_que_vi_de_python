decision_de_la_pizza = input("¿Quiere una pizza vegetariana?\n")
ingredientes_de_la_pizza_vegetariana = "Pimiento y Tofu"
ingredientes_de_la_pizza_no_vegetariana = "Peperoni, Jamón y Salmón"
ingredientes_de_la_pizza_normal = "Tomate, Mozzrella"

if decision_de_la_pizza == "":
    print("Por favor, escriba (si) o (no) para determinar el sabor de la pizza")
    decision_de_la_pizza = input("¿Quiere una pizza vegetariana?, puede responder (si) o (no) \n")

if decision_de_la_pizza == "si" or decision_de_la_pizza == "Si":
    print(f"""Estos son los ingredientes de la pizza vegetariana: {ingredientes_de_la_pizza_vegetariana}. Y además están los ingredientes que toda pizza tiene: {ingredientes_de_la_pizza_normal}.
Debes elegir solo uno de ellos para implementarlo en tu pizza, por favor escoge un ingrediente \n""")
    ingrediente_elegido = input()
    if ingrediente_elegido == "Pimiento" or ingrediente_elegido == "pimiento" or ingrediente_elegido == "Tofu" or ingrediente_elegido == "tofu":
        print(f"Has elegido una pizza vegetariana con: {ingredientes_de_la_pizza_normal} y {ingrediente_elegido}.")
    else:
        print("Ese no es un ingrediente a escoger, por favor intentelo de nuevo.")

if decision_de_la_pizza == "no" or decision_de_la_pizza == "No":
    print(f"""Estos son los ingredientes de la pizza no-vegetariana: {ingredientes_de_la_pizza_no_vegetariana}. Y además están los ingredientes que toda pizza tiene: {ingredientes_de_la_pizza_normal}.
Debes elegir solo uno de ellos para implementarlo en tu pizza, por favor escoge un ingrediente \n""")
    ingrediente_elegido = input()
    if ingrediente_elegido == "Peperoni" or ingrediente_elegido == "peperoni" or ingrediente_elegido == "Jamón" or ingrediente_elegido == "jamón" or ingrediente_elegido == "Salmón" or ingrediente_elegido == "salmón":
        print(f"Has elegido una pizza no-vegetariana con: {ingredientes_de_la_pizza_normal} y {ingrediente_elegido}.")
    else:
        print("Ese no es un ingrediente a escoger, por favor intentelo de nuevo.")


edad_del_cliente = int(input("Ingrese su edad para determinar lo que debe de pagar para entrar a la sala de juegos \n"))

if edad_del_cliente < 4:
    print("Puedes pasar sin pagar")
elif edad_del_cliente <= 18:
    print("Debes pagar 5 pesos wey")
else:
    print("Debes pagar 10 pesos wey")


puntuacion_del_empleado_ingresada = float(input("Ingrese la puntuacion del empleado \n"))

if puntuacion_del_empleado_ingresada == 0.0 or puntuacion_del_empleado_ingresada == 0.4 or puntuacion_del_empleado_ingresada >= 0.6:
    cantidad_de_dinero_conseguida = puntuacion_del_empleado_ingresada * 2400
    if cantidad_de_dinero_conseguida == 0:
        print(f"Tu nivel es inaceptable, la cantidad de dinero que te corresponde es de: {cantidad_de_dinero_conseguida}")
    if cantidad_de_dinero_conseguida == 960:
        print(f"Tu nivel es aceptable, la cantidad de dinero que te corresponde es de: {cantidad_de_dinero_conseguida}")
    if cantidad_de_dinero_conseguida >= 1440:
        print(f"Tu nivel es Meteorito, la cantidad de dinero que te corresponde es de: {cantidad_de_dinero_conseguida}")
elif puntuacion_del_empleado_ingresada > 0 or puntuacion_del_empleado_ingresada < 0.0 or puntuacion_del_empleado_ingresada == 0.1 or puntuacion_del_empleado_ingresada == 0.2 or puntuacion_del_empleado_ingresada == 0.3 or puntuacion_del_empleado_ingresada == 0.5:
    print("Esta puntuación no pertenece a algún nivel")


renta_anual_del_usuario = float(input("Ingrese su renta anual, por favor \n"))

if renta_anual_del_usuario < 10000:
    resultado_del_porcentaje_de_tipo_impositivo = renta_anual_del_usuario * .05
    print(f"Te corresponde el tipo impositivo del 5% {round(resultado_del_porcentaje_de_tipo_impositivo)}")
if renta_anual_del_usuario >= 10000 and renta_anual_del_usuario <=20000:
    resultado_del_porcentaje_de_tipo_impositivo = renta_anual_del_usuario * .15
    print(f"Te corresponde el tipo impositivo del 15% {round(resultado_del_porcentaje_de_tipo_impositivo)}")
if renta_anual_del_usuario >= 20000 and renta_anual_del_usuario <= 35000:
    resultado_del_porcentaje_de_tipo_impositivo = renta_anual_del_usuario * .20
    print(f"Te corresponde el tipo impositivo del 20% {round(resultado_del_porcentaje_de_tipo_impositivo)}")
if renta_anual_del_usuario >= 35000 and renta_anual_del_usuario <= 60000:
    resultado_del_porcentaje_de_tipo_impositivo = renta_anual_del_usuario * .30
    print(f"Te corresponde el tipo impositivo del 30% {round(resultado_del_porcentaje_de_tipo_impositivo)}")
if renta_anual_del_usuario >= 60000:
    resultado_del_porcentaje_de_tipo_impositivo = renta_anual_del_usuario * .45
    print(f"Te corresponde el tipo impositivo del 45% {round(resultado_del_porcentaje_de_tipo_impositivo)}")


edad_del_usuario = int(input("Ingrese su edad, por favor \n"))
ingresos_del_usuario = int(input("Escriba sus ingresos mensuales, por favor \n"))

if edad_del_usuario > 16 and ingresos_del_usuario >= 1000:
    print("Es necesario que tribute")
else:
    print("No tienes que tributar")

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

