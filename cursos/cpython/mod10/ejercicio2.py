from tkinter import *

ventana = Tk()
ventana.geometry("300x200")

w = Label(ventana, text ='Lorem ipsum', font = "50")
w.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Boton1 = Checkbutton(ventana, text = "Texto 1",
					variable = Checkbutton1,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

Boton2 = Checkbutton(ventana, text = "Texto 2",
					variable = Checkbutton2,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

Boton3 = Checkbutton(ventana, text = "Texto 3",
					variable = Checkbutton3,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)
	
Boton1.pack()
Boton2.pack()
Boton3.pack()

mainloop()
