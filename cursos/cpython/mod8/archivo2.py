
import pickle

class MiObjeto:
    def __init__(self, nombre):
        self.nombre = nombre

mi_objeto = MiObjeto("ejemplo")

with open('archivo.pickle', 'wb') as file:
    pickle.dump(mi_objeto, file)

file.close()
