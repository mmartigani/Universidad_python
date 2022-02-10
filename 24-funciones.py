from itertools import product


def mensaje():
    print('hello world')
mensaje()

def mensaje2(nombre, apellido):
    print('hello')
    print(f'como estas : {nombre} , {apellido}')
mensaje2('marco', 'martigani')

def sumar(a,b):
    return a+b
    
resultado=sumar(7,3)
print(resultado)

listar=['juan','esteban']
def nombres(*nombre):
    if listar in nombre:
        print(listar)
print(nombres(listar))


def ListarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')
ListarTerminos(data='analisis', analisis='ingeniero')