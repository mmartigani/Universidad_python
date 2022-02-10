class Personal:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
class Empleado(Personal):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo=sueldo
Empleado1=Empleado('joaquin',66,7700)
print(f'objeto Empleado:{Empleado1.nombre} {Empleado1.edad} {Empleado1.sueldo}')
    
    