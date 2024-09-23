#tiket de venta

print('#### Desarrollo de su compra #####')
leche = float(input('Ingrese el valor de la leche:'))
pan = float(input('Ingrese el valor del pan: '))
manzanas = float(input ('Ingrese los kilos de manzanas compradas: '))
lechuga = float(input('Ingrese el precio de la lechuga:'))
descuento = float(input('Ingrese un descuento (%):'))
manzanas *= 40

descuento2 = descuento
subtotal = leche + pan + manzanas + lechuga
descuento /= 100
descuento = subtotal * descuento
iva = (subtotal-descuento) * .16

print(f'El total es: {subtotal}$')
print(f'Descuento {descuento} ({descuento2:.2f}%)')
print(f'Subtotal con descuento: {subtotal - descuento}')
print(f'Precio del iva es {iva }$')
print(f'El total del precio con IVA es {iva + subtotal:.2f}$')