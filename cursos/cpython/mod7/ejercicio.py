import time
tiem=time.localtime()
horsal=19
if tiem[3]<horsal:
    resto=horsal-tiem[3]
    print('Horas por laburar: '+str(resto))
else:
    print('Ya vámonos, Sofía')
