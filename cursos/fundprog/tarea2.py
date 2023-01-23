"""
File: tarea2.py
Author: yourname
Email: yourname@email.com
Github: https://github.com/yourname
Description: Genera sistemas de bucles
"""

# En este ejercicio practicarás las estructuras de control, para ello deberás crear:

# Usando un if, crear una condición que compare si la variable numeroIf
# es positivo, negativo, o 0.
# Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
def numif(numeroIf):
    """docstring for numif"""
    if numeroIf>0:
        print("positivo")
    elif numeroIf<0:
        print("negativo")
    else:
        print("cero")
# Crea un bucle While, este bucle tendrá que tener como condición que
# la variable numeroWhile sea inferior a 3, el bloque
# de código que tendrá el bucle deberá:
# Incrementar el valor de la variable en uno cada vez que se ejecute.
# Mostrarlo por pantalla cada vez que se ejecute.

def numwh(numwh):
    """docstring for numwh"""
    while numwh<3:
        numwh+=1
        print(numwh)
# Para el bucle Do While, deberás crear la misma estructura que en el While,
# pero solo se debe ejecutar una vez.
def numdowh(k):
    """docstring for numdowh"""
    while True:
        k+=1
        print(k)
        if k<3:
            break

# Para el bucle For, crea una variable numeroFor, esta variable tendrá
# como valor 0 y su condición será que la variable sea igual o menor que 3,
# se irá incrementando en 1 su valor cada vez que se ejecute y deberá
# mostrarse por pantalla.

def numfo():
    """bucle for y comprobación"""
    # numerofor=0
    lim=3
    for k in list(len(lim)):
        print(k)
# Por último, para el Switch, deberás crear la variable estacion,
# y distintos case para las cuatro estaciones del año.
# Dependiendo del valor de la variable estacion se deberá
# mandar un mensaje por consola informando de la estación en la
# que está. También habrá que poner un default para cuando
# el valor de la variable no sea una estación.

def numsw(est):
    """Selector de estaciones"""
    switch={
            "Primavera":"Estamos en Primavera",
            "Verano":"Estamos en Verano",
            "Otoño":"Estamos en Otoño",
            "Invierno":"Estamos en Invierno",
            }
    return switch.get(est,"Invalid input")
