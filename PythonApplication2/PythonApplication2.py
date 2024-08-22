import tkinter as tk
from tkinter import ttk

def C_to_F():
    cadena = entrada.get()  # obtener el valor de entrada
    numero = float(cadena)  # pasar el valor de entrada a un tipo float- numerico
    resultado =(numero * 9/5) + 32
    lbRespuesta.config(text=str(resultado) + " F")
    
def F_to_C():
    cadena = entrada.get() 
    numero = float(cadena)  
    resultado =  (5 * (numero - 32))/9
    lbRespuesta.config(text=str(resultado) + " C")

    
def clear_full():
    lbRespuesta.config(text="Ingresa una cantidad a convertir")
   
    entrada.delete(0, tk.END) #.END para limpiar los datos contenidos en entrada
    


ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("400x200")


lb1 =tk.Label(ventana, text="Tipos de conversion")  
lb1.pack()
lb1.place(x=30, y=0)

boton = ttk.Button(ventana, text="C to F", command=C_to_F) # se usa para que una función que se debe ejecutar se ejecute en la instruccion
boton.place(x=50, y=30)


btnC_F =ttk.Button(ventana, text="F to C", command=F_to_C)  
btnC_F.place(x=50, y=75)


lb1 =tk.Label(ventana, text="Ingresa un dato a convertir")  
lb1.pack()
lb1.place(x=190, y=40)


entrada =ttk.Entry()
entrada.place(x=200, y=65, width=120)

lb2=tk.Label(ventana, text="Resultado de conversion:")
lb2.pack()
lb2.place(x=190, y=90)


lbRespuesta=tk.Label(ventana, text="Ingresa la cantidad a convertir")
lbRespuesta.pack()
lbRespuesta.place(x=145, y=115, width=250)



btnClear = ttk.Button(ventana, text="Clear", command=clear_full)
btnClear.place(x=220, y=150)


ventana.mainloop()
