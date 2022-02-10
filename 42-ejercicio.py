print('-----calcular cuanto me queda hasta los 90 años----')
print('----segun mi edad actual----')
edad_actual=input('ingrese su edad actual: ')
edad_entera=int(edad_actual)
años=90-edad_entera
semanas=años*52
meses=años *12
dias =años*365
mensaje =(f'A Ud.le quedan : {meses} meses {semanas} semanas {dias} dias')
print(mensaje)