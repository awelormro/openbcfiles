class Vehiculo():
    color='Verde'
    ruedas=2
    puertas=2

class Coche(Vehiculo):
    velocidad=200
    cilindrada=3

p=Coche()
p.puertas=4
p.cilindrada=5
print(p)
