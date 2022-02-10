class Persona:
    def __init__(self, nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        
    def mostrar_Detalle(self):
        print(f'persona:{self.nombre}{self.apellido}{self.edad}')  
    
Persona1=Persona('marco','martigani',41)
print(f'objeto persona1:{Persona1.nombre} {Persona1.apellido} {Persona1.edad}')      
Persona1.telefono=156748747
print(Persona1.telefono)   
Persona1.apellido='musk'
print(f'objeto persona1:{Persona1.nombre} {Persona1.apellido} {Persona1.edad}')

Persona1.mostrar_Detalle()

Persona2=Persona('bill','gates',66)
print(f'objeto persona2:{Persona2.nombre} {Persona2.apellido} {Persona2.edad}')
