precio_de_la_barra_de_pan = 3.50
precio_de_la_barra_de_pan_con_descuento = precio_de_la_barra_de_pan * .6

cantidad_de_barras_de_pan_vendidas = int(input("Ingrese la cantidad de barras de pan que se van a vender \n"))
precio_total_por_las_barras_de_pan = round(float(cantidad_de_barras_de_pan_vendidas * precio_de_la_barra_de_pan_con_descuento))
print(f"El precio normal de la barra de pan es de: {precio_de_la_barra_de_pan}, el descuento que se le hace por no ser fresca es de: {precio_de_la_barra_de_pan_con_descuento}, entonces tu compra tiene un total de: {precio_total_por_las_barras_de_pan}")



cantidad_de_payasos_vendidos = int(input("Ingrese la cantidad de payasos que va a vender \n"))
cantidad_de_muniecas_vendidas = int(input("Ingrese la cantidad de muñecas que va a vender \n"))

peso_del_payaso = 112
peso_de_la_munieca = 75

peso_total_del_paquete = cantidad_de_payasos_vendidos * peso_del_payaso + cantidad_de_muniecas_vendidas * peso_de_la_munieca
print(f"El paquete te pesara: {peso_total_del_paquete} gramos")


inversion_del_usuario = float(input("Ingrese la cantidad que va a invertir \n"))
tasa_de_interes_anual = float(input("Ingrese la tasa de interes anual a calcular \n"))
anios_de_la_inversion = int(input("Ingrese los años que se le deben aplicar al interés \n"))

capital_obtenido_de_la_inversion = inversion_del_usuario / 100 * tasa_de_interes_anual * anios_de_la_inversion
print(f"Su capital es de: {capital_obtenido_de_la_inversion}")


n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))

peso_del_usuario_en_kilogramos = float(input("Ingresa tu peso en kg \n"))
estatura_del_usuario = float(input("Ingresa tu estatura \n"))
indice_de_masa_corporal = round(peso_del_usuario_en_kilogramos / estatura_del_usuario ** 2)
print(f"Tu indice de marca corporal es de: {indice_de_masa_corporal}")


horas_trabajadas_del_usuario = int(input("Ingrese las horas que trabaja \n"))
coste_por_hora = float(input("Ingrese el coste por hora \n"))
total_de_paga = horas_trabajadas_del_usuario * coste_por_hora
print(f"Tu paga será de: {total_de_paga}")


string_hola_mundo = "Hola, Mundo"
print(string_hola_mundo)

string_hola_usuario = "Hola,"
nombre_usuario = input("Ingrese su nombre \n")
print(string_hola_usuario,nombre_usuario)