# import pickle

f=open('archivo.txt','w')
f.write('funciona\n')
lista=['e1','e2']
for elemento in lista:
    total=elemento+'\n'
    f.write(total)
f.close()
