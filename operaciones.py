# operaciones 

a = 5
b = 40
suma = a+b
multiplicaion = a * b
division = a/b
division_entera= a//b
potencia = a**b
residuo = a%b

print (f'suma: {suma}\ndivision: {division}\nmultiplicacion: {multiplicaion}\ndivision entera: {division_entera}\npotencia: {potencia}\nresiduo: {residuo}')#flojera

#asigancion ecadenada 
c,e,f = 4,5,8
print(f'Los valores de la variables c:{c},e:{e},f:{f}')

#asignacion encadenada 
g=h=j=k=10
print(f'los valores de g:{g},h:{h},j:{j},k:{k}')

nombre,apellido = input('Ingrese su nombre y apellido separado por una coma:').split(',')
print(f'su nombre es {nombre} y su apellido es: {apellido}')

#OPERADOR DE ASIGNACION COMPUESTA 

a+=b
print(f'la suma de los valores a+=b es : {a}')
a=5
a-=b
print(f'La resta de los valores es a-=b : {a} ')
a=5
a*=b
print(f'La multiplicaion de los valores es a*=b : {a} ')

#Operadores condicionales 
a=5
print(f'a es mayor o igual que b? {a>=b}')
print(f'a es igual que b? {a==b}')
print(f'a es diferente que b? {a!=b}')
print(f'b es mayor que a? {b>a}')

#operador And

entrada1= True
entrada2= False

operador= entrada1 and entrada2

print(f'La entrada {entrada1} y la entrada 2 {entrada2} es igual a ={operador}')

#operador or

entrada1= True
entrada2= False

operador= entrada1 or entrada2

print(f'La entrada {entrada1} y la entrada 2 {entrada2} es igual a ={operador}')

#condicion not
condicion1 = True
resultado = not condicion1
print(f'Operador not sobre {condicion1}: {resultado}')

# Revisar si una variable es cadena vacia
nombre = ''
es_cadena_vacia = not nombre
print(f'\nLa variable NO tiene ningún valor? {es_cadena_vacia}')

# Revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable
print(f'\nLa variable NO tiene ningún valor asignado? {es_variable_sin_valor}')

dato = int(input('Escribe un valor entero: '))

rango = 1<= dato <= 10

if rango ==True:
    print('Tu dato esta en el rango')
else:
    print('tu dato esta fuera de rango')
