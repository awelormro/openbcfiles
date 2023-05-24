# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos 
# impares de una lista pasada por parámetro con filter y realizará una suma de todos estos 
# elementos obtenidos mediante reduce.

from functools import reduce

lista=[1,3,4,5,6]


lista=[1,2,3,4,5,6,7,8,9,10]
def mifuncion(x):
    if x%2!=0:
        return True
        return False
resultado=filter(lambda x: x%2!=0,lista)
res=reduce(lambda a,b:a+b,resultado)
print(res)
