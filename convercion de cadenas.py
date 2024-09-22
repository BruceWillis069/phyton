cadena1= '51'
cadena2 = int(cadena1)
mult = cadena1 * 4
print(f'LA miltiplicacion de la cedena es:{mult}')#se multiplica las veces que se meciona el 51 y no el numero
mult = cadena2 * 4
print(f'LA miltiplicacion de la cedena es:{mult}')#se multiplica el valor int

cadena3 = float(cadena1)
print(f'Convericon a flotante: {cadena3}')

cadena4 = bool(cadena1)
print(f'Convericon a booleano: {cadena4}')#mientras el valor no sea 0 o la cadena este vacia esto lo marcara como true

cadena5 = 21
cadena6 = str(cadena5)
cadena6 = cadena6 * 4
print(f'convercion de int a string {cadena6}') #al convertirlo al string no multliplica el numero

cadena_vacia=''
cadena_vacia=bool(cadena_vacia)
print(f'el valor booleano de la cadena vacia es: {cadena_vacia}')

cadena_algo='algo'
cadena_algo= bool(cadena_algo)
print(f'la cadena contiene en termminacion booleana es: {cadena_algo}')