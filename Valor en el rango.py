#Valor en el rango

valor_min = 0
valor_max = 5

valor = int(input('Ingresa un valor dentro del rango: '))
condicion = (valor_min <= valor <= valor_max)

print(f'El valor esta en rango? {condicion}')
