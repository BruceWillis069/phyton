#funcion input
Nombre = input('Ingrese su nombre:')
nobol = bool(Nombre)
if nobol==True:

 print(f'su nombre es:{Nombre}')
 edad = input('Ingrese su edad:')
 edad = int(edad)
 edad = edad * 4
 print(f'su edad multiplicada por 4 es:{edad}')

else :
 print('es necesario introducir su nombre') 