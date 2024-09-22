from random import randint
print('### Sistema generador de Id\'s ####')
nombre = input('Ingrese su nombre : ')
apellido= input('Ingrese su apellido paterno : ')
nacimiento = input('Ingrese su ano de nacimiento (YYYY): ')

nombreid= nombre [0:2].upper()
apellidoid= apellido [0:2].upper()
nacimientoid = nacimiento [0:2]
numero1= str(randint(1000,9999))


id = nombreid + apellidoid + nacimientoid +numero1 

print(f'\nHola {nombre}')
print(f'\tTu numero de identificacion se ah generado en el sistema es :')
print(f'\tsu ID es {id}')