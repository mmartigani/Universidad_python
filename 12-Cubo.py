class Cubo:
    def __init__(self,ancho,alto,profundo):
        self.ancho=ancho
        self.alto=alto
        self.profundo=profundo
    def calcular_Cubo(self):
        return self.ancho*self.alto*self.profundo
        
ancho=int(input("ingrese le ancho: "))
alto=int(input("ingrese el alto: "))
profundo = int(input("ingrese la profundidad: "))
Cubo1=Cubo(ancho,alto,profundo)
print(f'el volumen es: {Cubo1.calcular_Cubo()}')
