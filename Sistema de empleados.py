#Sistema de empleados
print('#### Sistema de datos de empleadores ####')
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad:')
salario= input('Ingrese su salario:')
jefe = input('Ingrese si es jefe de departamente si/no :')

edad = int(edad)
salario = str(salario)
jefe= jefe.lower()=='si'

print('#### captura de datos exitosa ####')
print(f'su nombre es: {nombre}')
print(f'su edad es: {edad}')
print(f'cuenta con un slario de : {salario}')
print(f'jefe de departamento: {jefe}')