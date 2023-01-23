from tkinter import *

def sel():
   seleccion = "Seleccionaste la opción " + str(var.get())
   texto.config(text = seleccion)

def bor():
    var =0
    seleccion = " "
    R1.deselect()
    R2.deselect()
    R3.deselect()
    texto.config(text = seleccion)

ventana = Tk()
var = IntVar()
R1 = Radiobutton(ventana, text="Opción 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(ventana, text="Opción 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(ventana, text="Opción 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)

Rb = Button(ventana, text="Reinicio", command=bor)
Rb.pack( anchor = W)

texto = Label(ventana)
texto.pack()
ventana.mainloop()
