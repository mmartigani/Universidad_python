import re


def hola(mensaje):
    return mensaje
print(hola('como estas!'))

def datos (nombre,apellido):
    return nombre,apellido
print(datos('marco','martigani'))

def plus(a):
    resultado= a+10
    return resultado
print(plus(3))

def salario(horas):
    return horas *25
def extra(horas):
    return salario(horas)+50
print(salario(4),(extra(4)))
