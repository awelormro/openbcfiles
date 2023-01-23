class Persona:
    def __init__(self, edad,nombre,telefono):
        self.edad=edad
        self.nombre=nombre
        self.telefono=telefono
    def daredad(self):
        return self.edad
    
class Cliente:
    def __init__(self,dinero,edad,nombre):
        self.edad=Persona.edad
        self.nombre=Persona.nombre
        self.telefono=Persona.telefono
        self.dinero=dinero

Persona.nombre='Agustín'
Persona.edad=33
Persona.telefono=123456
k=Persona(22,'Chicarcas',223344)
# m=Persona(11,'kawamo',2233)
Cliente.dinero=22.50
Cliente.nombre=Persona.nombre
Cliente.telefono=Persona.telefono
Cliente.edad=Persona.edad
# Cliente.nombre=k.nombre
# Cliente.telefono=k.telefono
# Cliente.edad=k.edad
print(Cliente.dinero)
print(Cliente.nombre)
print(Cliente.edad)
print(Cliente.telefono)
