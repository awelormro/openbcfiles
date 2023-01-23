"""
File: tarea3.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Creación de la clase persona, pedir y dar archivos.
"""
class Persona:
    """Creación de la clase persona."""
    def __init__(self, edad,nombre,telefono):
        self.edad=edad
        self.nombre=nombre
        self.telefono=telefono

Persona.telefono=333333
Persona.edad=23
Persona.nombre='abu'
print(Persona.edad)
print(Persona.nombre)
print(Persona.telefono)
