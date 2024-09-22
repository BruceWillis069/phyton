
print('### Sistema generador de EMAILS\'s ####')
nombre = input('Ingrese su nombre : ')
apellido= input('Ingrese sus apellido: ')
empresa = input('Ingrese el nombre de la empresa: ')
dominio = input('Ingrese el dominio:')

nombre = nombre.replace(" ",".").lower()
apellido = apellido.replace(" ",".").lower()
empresa = empresa.replace(" ","").lower()

email = nombre +'.'+ apellido + '@'+ empresa + dominio
print('\nTu email se ah generado exitosamente y es:')
print(f'\t su correo es: {email}')
