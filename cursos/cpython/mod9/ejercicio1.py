# Crea un script que le pida al usuario una lista de países (separados por comas). 
# Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
# Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.

paises=input('Dame los países separados por comas: \n')
paises1=paises.split(',')
paises_sin_repetir=list(set(paises1))
paises_sin_repetir.sort()
paisesfinal=''
k=0
while k<len(paises_sin_repetir):
    if k+1==len(paises_sin_repetir):
        paisesfinal=paisesfinal+paises_sin_repetir[k]
    else:
        paisesfinal=paisesfinal+paises_sin_repetir[k]+', '
    k+=1
print(paisesfinal)
