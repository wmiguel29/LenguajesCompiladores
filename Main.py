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
import pandas as pd
import numpy as np
import sys 


#importar los modulos de las funciones requeridas
import identificarExpArit as expArit
import tablaSimbolos as tablaS
import tablaTokens as tablaT
import GLC as glc

ventana = Tk()

ventana.geometry('1024x1024')

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
    
entry_var=StringVar()
entry_var.set("Ingrese Numero Operacion")
label_var=StringVar()


def comprobar_expresion():
    numero=entry_var.get()
    
    if str.isdigit(numero):
        errores=glc.main(numero)
        texto=''
        for item in errores:
            texto+=item+'\n'
        label_var.set(texto)
    else:
        label_var.set("Debe ingresar un numero valido")
        
        
def comprobar_numero():
    numero=entry_var.get()
    
    if str.isdigit(numero):
        label_var.set("Numero valido")
    else:
        label_var.set("Debe ingresar un numero valido")
    
    
    

 

Button(text="Tabla Simbolos",bg="pale green",command=abrir_archivo).place(x=10,y=10)
Label(text="tabla_simbolos.csv",bg='pale green',fg='black').place(x=105,y=12)
Button(text="Tabla Tokens",bg="light blue",command=guardar_archivo).place(x=10,y=40)
Label(text="tabla_tokens.csv",bg='light blue',fg='black').place(x=95,y=42)
Button(text="Expresiones",bg="salmon",command=carpeta).place(x=10,y=70)
Label(text='tabla_operaciones.csv',bg='salmon',fg='black').place(x=90,y=72)
Entry(fg='black',bg='lavender',width=25, textvariable=entry_var).place(x=10,y=100)
Label(textvariable=label_var,bg='azure',fg='black',).place(x=10,y=160)
Button(text="Comprobar Expresion", bg="red", command= comprobar_expresion).place(x=10,y=130)
Button(text="Ingresar Numero", bg="lavender", command= comprobar_numero).place(x=167,y=95)
ventana.mainloop()