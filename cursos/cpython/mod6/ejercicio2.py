class Alumno():
    nombre='Alex'
    nota=70
    def Aprueba(self):
        if self.nota < 70:
            print('reprobado')
        else:
            print('aprobado')

            
al=Alumno()
al.nombre='Juanito'
al.nota=66
print(al.nombre)
print(al.nota)
al.Aprueba()
al1=Alumno()
al1.nombre= 'Rosita'
al1.nota=100
print(al1.nombre)
print(al1.nota)
al1.Aprueba()
