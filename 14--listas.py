nombres=['analisis', 'de','datos','me voy a','convertir']
print(nombres)
print(type(nombres))
print(nombres[0:])
print(nombres[0:1])
print(nombres[:1])
print(len(nombres))
nombres[0]='datos'
print(nombres)
for i in nombres:
    print(i)
    
nombres.append('ingeniero')
print(nombres)
nombres2=['deby','lorenzo', 'marco']
nombres.extend(nombres2)
print(nombres)
nombres.insert(0,'science')
print(nombres)
nombres.remove('science')
print(nombres)
nombres.pop()
print(nombres)
del nombres[0]
print(nombres)
#nombres.clear()limpiamos toda la lista 
#del nombres borra toda la lista 

