# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:29:10 2021

Codigo base en Python 3.8.5 que contiene la codificacion de la Gramatica Libre 
de Contexto(GLC) basica utilizada en clase para la mayoria de los ejercicios
de clase 

GLC ORIGINAL:
    <EXP>  := <EXP> + <TERMIN>
            | <EXP> - <TERMIN>
            | <TERM>
    <TERM> := <TERM>*<FACT>
            | <TERM>/<FACT>
            | <FACT>
    <FACT> := (<EXPR>)
            | <NUMS>
            | <IDENT>
    <NUMS> := <NUMS> <DIGT>
            |<DIGT>
    <DIGT> := 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
    <IDENT> := <IDENT> <LETRA>
             | <LETRA>
    <LETRA> := A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P 
             | Q | R | S | T | U | V | W | Y | X | Z | a | b | c | d | e | f 
             | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v 
             | w | y | x | z
            
GLC SIN RESURSIVIDAD: 
    <EXPR> := <TERM><EXPR`>
    <EXPR`> := + <TERM> <EXPR`>
             | - <TERM> <EXPR`>
             | ε 
    <TERM> := <FACT> <TERM`>
    <TERM`> := *<FACT> <TERM`>
             | /<FACT> <TERM`>
             | ε
    <FACT> := (<EXPR>)
            | <NUMS>
            | <IDENT>
    <NUMS> := <DIGT> <NUMS`>
    <NUMS`> := <DIGT> <NUMS`>
             | ε
    <DIGT> := 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
    <IDENT> := <LETRA> <IDENT`>
    <IDENT`> := <LETRA> <IDENT`>
             | ε
    <LETRA> := A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P 
             | Q | R | S | T | U | V | W | Y | X | Z | a | b | c | d | e | f 
             | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v 
             | w | y | x | z

@author: Miguel Wagner
"""

#Importar los modulos y librerias necesarias
import pandas as pd

#Definir las variables iniciales  a utilizar
#Posicion Inicial de la cadena
posicion=0

#Definir la variable del token de entrada
token_entrada=''

#Lista con la expresion Posfija
posfija = []


#Definir la cadena a recorrer
cadena=''


#Definir lista donde se van a guardar los errores
errores=[]


#No Terminales
def expresion():
    termino()
    expresion_prima()
    
    
def expresion_prima():
    if token_entrada=='+':
        #print('+')
        match('+')
        termino()
        expresion_prima() 
    elif token_entrada=='-':
       # print('-')
        match('-')
        termino()
        expresion_prima()
    else:
        pass
   
    
def termino():
    factor()
    termino_prima()
   
    
def termino_prima():
    if token_entrada =='*':
        #print('*')
        match('*')
        factor()
        termino_prima()
    elif token_entrada =='/':
        #print('/')
        match('/')
        factor()
        termino_prima()
    else:
        pass
    
        
    
def factor():
    global token_entrada
    if token_entrada=='(':
        #print ("(")
        match('(')
        expresion()
        print (")")
        match(')')
    elif  isdigit(token_entrada):
        numero()
    elif  isalpha(token_entrada):
        identificador()
    else:
        error="Se esperaba un factor en la posicion : "+str(posicion-1)
        error+=", se obtuvo " + token_entrada
        errores.append(error)
        token_entrada=siguienteToken()
    
    
 
#Terminales o que contienen Terminales
def identificador():
    letra()
    identificador_prima()
    
    
def identificador_prima():
    global token_entrada
    if isalpha(token_entrada):
        letra()
        identificador_prima()
    elif  isdigit(token_entrada):
        error="Se esperaba una letra y se obtuvo " + token_entrada
        error+= ", en la posicion " + str(posicion-1)
        errores.append(error)
        token_entrada=siguienteToken()
        identificador_prima()
    elif token_entrada is None:
        pass
    

def letra():
    global token_entrada
    if isalpha(token_entrada):
        print(token_entrada)
        match(token_entrada)
    else:
        error="Se esperaba un digito se obtuvo: " + token_entrada
        error+= ", en la posicion " + str(posicion-1)
        errores.append(error)
        token_entrada=siguienteToken()
            

def numero():
    digito()
    numero_prima()
    
    
def numero_prima():
    global token_entrada
    if isdigit(token_entrada):
        digito()
        numero_prima()
    elif  isalpha(token_entrada):
        error="Se esperaba un numero y se obtuvo " + token_entrada
        error+= ", en la posicion " + str(posicion-1)
        errores.append(error)
        token_entrada=siguienteToken()
        numero_prima()
    elif token_entrada is None:
        pass
  

def digito():
    global token_entrada
    if isdigit(token_entrada):
        print(token_entrada)
        match(token_entrada)
    else:
        error="Se esperaba un digito se obtuvo: " + token_entrada
        error+= ", en la posicion " + str(posicion-1)
        errores.append()
        token_entrada=siguienteToken()
        
#Funciones Complementarias
def siguienteToken():
    global posicion
    if posicion==len(cadena):
        return 
    else: 
        posicion= posicion +1
        return cadena[posicion-1]


def match(caracter):
    global token_entrada
    if caracter == token_entrada:
        token_entrada=siguienteToken()
    else:
        error="Se esperaba " + caracter + " se obtuvo " + token_entrada
        error+=", en la posicion : " + str(posicion-1)
        errores.append
        token_entrada=siguienteToken()
        
        
def isdigit(caracter):
    if caracter is None:
        return False
    elif str.isdigit(caracter):
        return True
    else:
        return False
   
    
def isalpha(caracter):
    if caracter is None:
        return False
    elif str.isalpha(caracter):
        return True
    else:
        return False

        

def main(numero= None, expresionA = ''):
    
    
    if numero:
        #Si entra como string trasnformarlo a un int
        numero=int(numero)
        
        #leer y almacenar la tabla con las operaciones en un dataframe
        df_operaciones=pd.read_csv('tabla_operaciones.csv')
        
        
        #Referenciar la cadena global
        global cadena
        
        
        #Buscar la expresion especifica
        texto=df_operaciones.iloc[numero,1]
        texto=str(texto)
    else:
        texto = expresionA
    
    
    #texto="a + b * c *(votos/electores) * 1000*x*x + b*x + c *(alto - bajo)/2 *3600 + minutos*60 + segundos numero%2 "
    #Quitar los espacios en blanco de la cadena
    cadena=texto.replace(' ','')
    cadena.lstrip()
    
    
    #Referenciar el token de Entrada a nivel global
    global token_entrada
    
    #Asignar un valor al token
    token_entrada=siguienteToken()
    
    
    #Llamar a la primera regla de derivacion
    expresion()
    
    
    #Si hay errores insertar en la primera posicion la cadena original
    if errores:
        errores.insert(0,cadena+'\n')
        return errores
    
    #Si no hay errores retornar una lista con la cadena y un String que
    #diga expresion correcta
    else:
        return [cadena,"Expresion Correcta"]
    
    
    



    

    



