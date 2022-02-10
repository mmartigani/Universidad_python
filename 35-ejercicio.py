mes=int(input('ingrese un mes entre 1 y 12: '))
estacion =None 
if mes ==1 or mes ==2 or mes ==3:
    estacion = 'verano'
    print(f'el mes es : {mes} y la estacion es : {estacion}')
elif mes ==4 or mes ==5 or mes ==6:
    estacion = 'otoño'
    print(f'el mes es : {mes} y la estacion es : {estacion}')
elif mes ==7 or mes ==8 or mes ==9:
    estacion='invierno'
    print(f'el mes es : {mes} y la estacion es : {estacion}')
elif mes ==10 or mes ==11 or mes ==12:
    estacion = 'primavera'
    print(f'el mes es : {mes} y la estacion es : {estacion}')
else:
    estacion ='no existe'
    print(f'el mes es : {mes} y la estacion es : {estacion}')
