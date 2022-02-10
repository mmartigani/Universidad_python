print('---ingrese los datos del libro---')
nombre=input('ingrese el nombre del libro : ')
idd=int(input('ingrese el idd del libro : '))
precio =float(input('ingrese el precio: '))
envioGratis=input('indique si el envio es gratis o tiene costo con True/False: ')
if envioGratis=='True':
    envioGratis=True
elif envioGratis=='False':
    envioGratis=False
else:
    envioGratis='debe escribir True or False'
print(f'''
      nombre:{nombre}
      idd:{idd}
      precio:{precio}
      envioGratis:{envioGratis}''')