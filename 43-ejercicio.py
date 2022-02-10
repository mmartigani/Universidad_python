print('----calculado para dividir una factura de restaurant-----')
factura=float(input('ingrese el monto total de la factura : '))
propina =int(input('ingrese el porcentaje de propina 10,12,15 : '))
personas=int(input('cantidad de personas entre las que se divide : '))
porcentaje=propina/100
subtotal=porcentaje*factura
subtotal2=subtotal + factura
total=subtotal2/personas
print(f'cada persona debe abonar : {total:.2f}')