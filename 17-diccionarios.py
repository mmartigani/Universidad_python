from this import d


diccionario={'hola':1,'como':2,'estas':3,'llave':'valor'}
print(diccionario)
print(type(diccionario))
print(len(diccionario))
print(diccionario['hola'])
diccionario['hola']=7
print(diccionario)
for termino, valor in diccionario.items():
    print(termino, valor)
for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print(valor)
    
print('holaa'in diccionario)
