numero=int(input("ingrese un nro del 1 al 3:"))
numero_texto=""
if numero ==1:
    numero_texto="numero uno"
elif numero==2:
    numero_texto='numero dos'
elif numero==3:
    numero_texto="numero tres"
else:
    numero_texto='numero fuera de rango'
print(f'numero ingresado es : {numero} convertido a texto es : {numero_texto}')