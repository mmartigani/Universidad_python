num1=float(input('ingrese el primero nro : '))
op=input('ingrese el operador(+,-,*,/) : ')
num2=float(input('ingrese el segundo nro: '))
if op=='+':
    print(num1+num2)
elif op =='-':
    print(num1-num2)
elif op =='*':
    print(num1*num2)
elif op =='/':
    print(num1/num2)
else:
    print('operador incorrecto')

   