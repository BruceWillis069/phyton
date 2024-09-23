#Sistema de autenticacion

print('**** Sistema de autenticacion ****')
usuario = input('Ingrese el usuario: ').strip()
contra = input('Ingrese la contraseña: ').strip()

usuario = usuario == 'john'
contra = contra == '123456'
autentificaion = contra and usuario

print(f'Los datos son: {autentificaion}')
