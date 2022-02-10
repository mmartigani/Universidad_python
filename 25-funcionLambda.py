#la funcion lambda no tiene parentesis, 
#no se usa return 
#se utiliza la palabra reservada lambda 

miFuncion_lambda=lambda a,b:a+b
resultado=miFuncion_lambda(4,4)
print(f'el resultado de la funcion lambda:{resultado}')


print('-----fin de la priemra funcion-----')

myfuncion_lambda1=lambda:'sin argumentos con string'
print(f'sin argumentos: {myfuncion_lambda1()}')
