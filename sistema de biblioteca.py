print('#### Bienvenido a la biblioteca nacional ####')
credencial = input('\nCuenta con credencial de estudiante? (si/no) : ')
cerca = int(input('a cuantos km vive de la biblioteca?:'))

credencial = credencial.lower() =='si'
km=3
cerca = (cerca ==km)

if cerca or credencial ==True:
    print('Usted puede tomar libros de la biblioteca ')
else:
    print('usted no puede tomar libros de la biblioteca')

