class Rectangulo:
    def __init__(self,base,altura) :
        self.base=base
        self.altura=altura
    def calcular_rectangulo(self):
        return self.base* self.altura
    
base=int(input("ingrese la base: "))
altura=int(input("ingrese la altura: "))
Rectangulo1=Rectangulo(base,altura)
print(f'el area de un rectangulo es : {Rectangulo1.calcular_rectangulo()}')