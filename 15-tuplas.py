tupla=('hola', 'esta', 'es','una','tupla')
print(tupla)
print(type(tupla))

#la diferencia con la lista es que la tupla 
#no se puede modificar 
#los demas sentencias son iguales a ala lista 
#debemos convertir a lista para poder hacerlo 

convertir=list(tupla)
convertir[0]='hello'
tupla=tuple(convertir)
print(tupla)
