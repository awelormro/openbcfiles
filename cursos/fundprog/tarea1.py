"""
File: tarea1.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Función de tres parámetros para ser sumados y una clase auto.
"""
def suma(a,b,c):
    """docstring for suma"""
    a1=int(a)
    b1=int(b)
    c1=int(c)
    return a1+b1+c1
print(suma(1,2,3))

class Coche:
    """docstring for coche"""
    def __init__(self, puertas):
        self.puertas = puertas

cosa=Coche(2)
print(cosa.puertas)
