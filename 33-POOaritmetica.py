import re
from tkinter.messagebox import RETRY


class Aritmetica:
    def __init__(self,opa,opb):
        self.opa=opa
        self.opb=opb
    def sumar(self):
        return self.opa +self.opb
    def restar(self):
        return self.opa - self.opb
    def producto(self):
        return self.opa * self.opb
    def division(self):
        return self.opa /self.opb
Aritmetica1=Aritmetica(15,2)
print(f'la suma es :{Aritmetica1.sumar()}')
print(f'la restar es :{Aritmetica1.restar()}')
print(f'la producto es :{Aritmetica1.producto()}')
print(f'la division es :{Aritmetica1.division():.2f}')
