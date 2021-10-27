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
import prefijo as prefijo
import posfijo as posfijo

ventana = Tk()

ventana.geometry('1024x1024')

ventana.title("Compilador")


def abrir_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
    tablaS.main(archivo_abierto)
    os.system("tabla_simbolos.csv")


def guardar_archivo():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
    tablaT.main(archivo_abierto)
    os.system("tabla_tokens.csv")

def carpeta():
    archivo_abierto=filedialog.askopenfilename(initialdir = "/",
                title = "Seleccione archivo",filetypes = (("txt files","*.txt"),
                ("all files","*.*")))
    expArit.main(archivo_abierto)
    os.system('tabla_operaciones.csv')


    
entry_var=StringVar()
entry_var.set("Ingrese Numero Operacion")
label_var=StringVar()

expr_var=StringVar()
expr_var.set("Ingrese Operacion Corregida")




def comprobar_expresion():
    numeroE=entry_var.get()
    expresion = expr_var.get()
    
    label_var.set('')
    
    if expresion != "Ingrese Operacion Corregida" and expresion:
        errores=glc.main(expresionA = expresion)

        texto=''
        for item in errores:
            texto+=item+'\n'
        label_var.set(texto)
    else:
        if str.isdigit(numeroE):
            errores=glc.main(numero = numeroE)
            texto=''
            for item in errores:
                texto+=item+'\n'
            label_var.set(texto)
        else:
            label_var.set("Debe ingresar un numero valido")
            
        #entry_var.set('')
        
        
def prefija():
    numero = entry_var.get()
    expresion = expr_var.get()
    
    label_var.set('')
    
    if expresion != "Ingrese Operacion Corregida" and expresion:
        texto = prefijo.main(numero = None, expresionA = expresion)
        label_var.set(texto)
    else:
        if str.isdigit(numero):
            texto=prefijo.main(numero= numero)
            label_var.set(texto)
        else:
            label_var.set("Debe ingresar un numero valido")
            
  
    
    del expresion
            
            
        
def posfija():
    numero = entry_var.get()
    expresion = expr_var.get()
    
    label_var.set('')
    
    if expresion != "Ingrese Operacion Corregida" and expresion:
        texto = posfijo.main(numero = None, expresionA = expresion)
        label_var.set(texto)
           
    else:
        if str.isdigit(numero):
            texto=prefijo.main(numero= numero)
            label_var.set(texto)
        else:
            label_var.set("Debe ingresar un numero valido")
    expresion=''
    
    
    
    
    del expresion
            
    
    
        
        
def comprobar_numero():
    numero=entry_var.get()
    
    if str.isdigit(numero):
        label_var.set("Numero valido")
    else:
        label_var.set("Debe ingresar un numero valido")
        
"""       
def clear():
    entry_var.set('')
    expr_var.set('')
    expr_var.set("Ingrese Operacion Corregida")
    entry_var.set("Ingrese Numero Operacion")
 """
    
    
    
        
        
        
    
    
    

 

Button(text="Tabla Simbolos",bg="pale green",command=abrir_archivo).place(x=10,y=10)
Label(text="tabla_simbolos.csv",bg='pale green',fg='black').place(x=105,y=12)
Button(text="Tabla Tokens",bg="light blue",command=guardar_archivo).place(x=10,y=40)
Label(text="tabla_tokens.csv",bg='light blue',fg='black').place(x=95,y=42)
Button(text="Expresiones",bg="salmon",command=carpeta).place(x=10,y=70)
Label(text='tabla_operaciones.csv',bg='salmon',fg='black').place(x=90,y=72)
Entry(fg='black',bg='lavender',width=25, textvariable=entry_var).place(x=10,y=100)

Button(text="Ingresar Numero", bg="lavender", command= comprobar_numero).place(x=167,y=95)
Button(text="Comprobar Expresion", bg="red", command= comprobar_expresion).place(x=10,y=125)

Entry(fg='black',bg='lavender',width= 30, textvariable=expr_var).place(x=10,y=155)
Button(text="Prefija", bg="sky blue", command= prefija).place(x=10,y=180)
Button(text="Posfija", bg="sea green", command= posfija).place(x=60,y=180)
Label(textvariable=label_var,bg='azure',fg='black',).place(x=10,y=225)
#Button(text = 'Clear', bg = 'alice blue', command = clear).place(x = 110, y = 180)


ventana.mainloop()