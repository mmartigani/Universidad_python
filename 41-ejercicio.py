from lib2to3.pytree import convert


altura=input ('ingrese su altura: ')
peso=input('ingrese su peso : ')
bmi=int(peso)/float(altura)**2
convertir=int(bmi)
print(f'su indice de bmi es :{convertir}')