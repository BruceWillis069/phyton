#area de un rectangulo

print ('### calculador el area y perimetro de un rectangulo ###')
base = float(input('Ingrese la base del rectangulo: ')) 
altura = float(input('Ingrese la altura del rectangulo: '))

perimetro = (base+altura)*2
area = base * altura

print(f'El area de el rectangulo es : {area}')
print(f'El perimetro de el rectangulo es : {perimetro}')