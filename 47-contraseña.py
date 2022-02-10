import random 
contraseña=int(input('ingrese la longuitud de su contraseña : '))
a='ABCDEFGHIJKLMNOPQWSZXabcdefghijklmnopzxw$%&/?¿123456789'
b=''.join(random.sample(a,contraseña))
print(b)