#descuento VIP

print('#### Bienvenido a Wallmart ####')
numero = int(input('cuantos productos compro? '))
miembro = input('es miembro? (si/no):')

miembro = miembro.lower() =='si'
descuento = 10
vip = (numero >= descuento)

print(f'Es aspirante al descuente : {vip and miembro}')


