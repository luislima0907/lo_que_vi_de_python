#And ( & ), aqui las dos condiciones comparadas tienen que ser verdad para que sea verdadero de lo contrario, es falso

resultado_and_uno = True & True #Devolver True
resultado_and_dos = True & False #Devolver False
resultado_and_tres = False & False #Devolver False
resultado_and_cuatro = False & True #Devolver False

#Or ( | ), aqui es verdadero cuando haya una condicion verdadera, de lo contrario es falso

resultado_or_uno = True | True #Devolver True
resultado_or_dos = True | False #Devolver True
resultado_or_tres = False |False #Devolver False
resultado_or_cuatro = False | True # Devolver True

#Not, aqui se cambia el valor, de verdadero a falso y de falso a verdadero

resultado_not_uno = not True
resultado_not_dos = not False