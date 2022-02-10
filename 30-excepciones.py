resultado=None
try:
    a=int(input('ingrese el primer nro: '))
    b=int(input('ingrese el segundo nro: '))
    resultado=a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError:Ocurrio un error:{e}')
except TypeError as e:
    print(f'TypeError:ocurrio un error:{e}')
except Exception as e:
    print(f'Ocurrio un error:{e}')
else:
    print('no se arroja ninguna excepcion de error')
finally:
    print('se ejecuta el finally')
print(f'el resultado es :{resultado}')
