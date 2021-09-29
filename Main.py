# -*- coding: utf-8 -*-
"""
Created on Wed Sept 01 16:05:26 2021

Funcion principal donde se ubica la interfaz grafica, tiene los botones de 
guardar archivo y de las respectivas funciones. Tambien tiene una opcion de 
las diferentes tablas   

@author: Miguel Wagner
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import *
import os

#importar los modulos de las funciones requeridas
import identificarExpArit as expArit
import tablaSimbolos as tablaS
import tablaTokens as tablaT

ventana = Tk()

def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
    tablaS.main(archivo_abierto)


def guardar_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
    tablaT.main(archivo_abierto)

def carpeta():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
    expArit.main(archivo_abierto)

Button(text="Tabla Simbolos",bg="pale green",command=abrir_archivo).place(x=10,y=10)
Button(text="Tabla Tokens",bg="light blue",command=guardar_archivo).place(x=10,y=40)
Button(text="Expresiones",bg="salmon",command=carpeta).place(x=10,y=70)

ventana.mainloop()