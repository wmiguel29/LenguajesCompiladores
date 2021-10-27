# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:29:10 2021

Codigo base en Python 3.8.5 que contiene la codificacion de la Gramatica Libre 
de Contexto(GLC) basica utilizada en clase para la mayoria de los ejercicios
de clase, con la adicion de acciones para convertir una 
expresion infija a prefija, el funcionamiento general es el mismo que 
el de la posfija, sino que la unica diferencia es que la cadena al principio
se invierte incluidos los parentesis y se utiliza para recorrer la gramatica
para posteriormente volverse a invertir

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
            
GLC SIN RESURSIVIDAD CON  ACCIONES SEMANTICAS : 
    <EXPR> := <TERM><EXPR`>
    <EXPR`> := + <TERM> {Save '+'} <EXPR`> 
             | - <TERM> {Save '-'} <EXPR`> 
             | ε 
    <TERM> := <FACT> <TERM`>
    <TERM`> := *<FACT> {Save '*'} <TERM`> 
             | /<FACT> {Save '/'} <TERM`> 
             | ε
    <FACT> := (<EXPR>)  
            | <NUMS>
            | <IDENT>
    <NUMS> := <DIGT> <NUMS`> {Save ' '}
    <NUMS`> := <DIGT> <NUMS`>
             | ε
    <DIGT> := 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 {Save 'Digito'}
    <IDENT> := <LETRA> <IDENT`> {Save ' '}
    <IDENT`> := <LETRA> <IDENT`>
             | ε
    <LETRA> := A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P 
             | Q | R | S | T | U | V | W | Y | X | Z | a | b | c | d | e | f 
             | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v 
             | w | y | x | z  {Save 'Letra'}

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
cadena=[]




#No Terminales

def expresion():
    termino()
    expresion_prima()
    
    
def expresion_prima():
    if token_entrada=='+':
        #print('+')
        match('+')
        termino()
        posfija.append('+')
        posfija.append(' ')
        expresion_prima()
    elif token_entrada=='-':
       # print('-')
        match('-')
        termino()
        posfija.append('-')
        posfija.append(' ')
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
        posfija.append('*')
        posfija.append(' ')
        termino_prima()
    elif token_entrada =='/':
        #print('/')
        match('/')
        factor()
        posfija.append('/')
        posfija.append(' ')
        termino_prima()
    else:
        pass
    
        
    
def factor():
    global token_entrada
    if token_entrada=='(':
        #print ("(")
        match('(')
        expresion()
        #print (")")
        match(')')
    elif  isdigit(token_entrada):
        numero()
    elif  isalpha(token_entrada):
        identificador()
    else:
        token_entrada=siguienteToken()
    
    
 # Terminales o que Contienen Terminales   
def identificador():
    letra()
    identificador_prima()
    posfija.append(' ')
    
    
    
def identificador_prima():
    global token_entrada
    if isalpha(token_entrada):
        letra()
        identificador_prima()
    elif  isdigit(token_entrada):
        token_entrada=siguienteToken()
        identificador_prima()
    elif token_entrada is None:
        pass
    else :
        pass
    

def letra():
    global token_entrada
    if isalpha(token_entrada):
        #print(token_entrada)
        token=token_entrada
        match(token_entrada)
        posfija.append(token)
    else:
        token_entrada=siguienteToken()
            

def numero():
    digito()
    numero_prima()
    posfija.append(' ')
    
    
def numero_prima():
    global token_entrada
    if isdigit(token_entrada):
        digito()
        numero_prima()
    elif  isalpha(token_entrada):
        token_entrada=siguienteToken()
        numero_prima()
    elif token_entrada is None:
        pass
  

def digito():
    global token_entrada
    if isdigit(token_entrada):
        #print(token_entrada)
        token=token_entrada
        match(token_entrada)
        posfija.append(token)
    else:
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
    
    
    
 
def listToString(s):
    """
    Function para convertir una lista en un String

    Parameters
    ----------
    s : Lista
        Lista donde se almacenaron todos los tokens

    Returns
    -------
    str1 : String
        Expresion 

    """
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        



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
        
    else:
        
        texto = expresionA
        
        
        
    #texto ='u*u-(a+a*a)'
    #texto="a + b * c *(votos/electores) * 1000*x*x + b*x + c *(alto - bajo)/2 *3600 + minutos*60 + segundos numero%2 "
   
    #Quitar los espacios en blanco de la cadena
    cadena = texto.replace(' ','')
    
    
    #Invertir la cadena
    cadena = cadena[::-1]
    
    
    #Invertir de sentido los parentesis
    cadena=cadena.replace('(','$')
    cadena=cadena.replace(')','(')
    cadena=cadena.replace('$',')')
    
    
    
    #Referenciar el token de Entrada a nivel global
    global token_entrada
    
    #Asignar un valor al token
    token_entrada=siguienteToken()
    
    
    #Llamar a la primera regla de derivacion
    expresion()
    
    
    #print(listToString(posfija)[::-1])
    #retornar la cadena invertida otra vez
    return listToString(posfija)[::-1]
    
    

   
#main(expresionA=" (5+(26-87*5)*2)-(32*(4-16*13))")




    
    
    



