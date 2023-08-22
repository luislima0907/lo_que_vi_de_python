edad = 17

#Condicional if - else (Si - Sino) esta condición evalua las comparaciones que determinemos en las variables o datos.
#Si la condición que determinamos en el If se cumple, entonces nos ejecutará el código que tengamos arriba.
#Si no se cumple entonces nos ejecutará el código de abajo
if edad < 18:
    print("Sos menor de edad")
else:
    print("Sos mayor de edad")

#las condiciones siempre deben de terminar con los dos puntos " : "    
contraseña_almacenada = "LolXDDD"
contraseña_escrita = "lolxddd"
    
if contraseña_almacenada == contraseña_escrita:
    print("Iniciando sesión")
else:
    print("Contraseña equivacada, intente de nuevo")
    
#condicional elif
#con esta condicional estamos determinando una subcondición en caso de que no se cumpliera la primera condición, es decir, si no se cumple la primera.
#evalua una subcondición que esta vinculada a la condicion principal para poder ver si puede ser verdadera, y en caso de que no.
#ejecuta el Sino que hay de último en el If principal
ingreso_mensual = 5000

#condición uno (si se cumple la primera condicion es un if normal)
if ingreso_mensual > 10000:
    print("Estas bien económicamente en cualquier parte del mundo")
#condición dos (en caso de que la primera sea falsa esta puede actuar como un escape en caso de que quisieramos algo en concreto)
elif ingreso_mensual > 1000:
    print("Estas bien de economía en latam")
#Se pueden poner varios elif, igualemente if, solo los else deben estar anidados a un if siempre que lo vayamos a declarar
elif ingreso_mensual > 500:
    print("Estas bien de economía en Guatemala")
elif ingreso_mensual > 100:
    print("Estas bien de economía en Jalapa")
#condicion tres (si las dos anteriores son falsas, ahora si, ejecuta el else)
else:
    print("Eres pobre XDDDD")

#Ejemplo 2 con if anidados, recordemos que primero se evualuan los if, luesgo los elifs (si es que los hay) y de ultimo los else.    
ingreso_mensual_dos = 6000
gasto_mensual = 6000

if ingreso_mensual_dos >= 5000:
    if gasto_mensual <= 3000:
        print("tamos bien brooooo")
    else:
        print("tamos mal broooo")
    if ingreso_mensual_dos - gasto_mensual <= 0:
        print("nmms estamos condenados")
    elif ingreso_mensual_dos - gasto_mensual <= 2000:
        print("estoy cansado jefe :c")
    else:
        print("La chamba nos da frutos")
elif ingreso_mensual_dos >= 10000:
    print("tamos excelentes broooooo")
else:
    print("La chamba no da lo suficiente >:c")