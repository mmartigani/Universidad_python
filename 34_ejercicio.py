edad=int(input('ingrese su edad: '))
mensaje=None
if edad >= 0 and edad <10:
    mensaje='infancia'
elif edad >=10 and edad <20:
    mensaje='estudiando'
elif edad >=20 and edad <30:
    mensaje='adulto'
else:
    mensaje='descansa'
print(f'tu edad es :{edad}:eres {mensaje}')