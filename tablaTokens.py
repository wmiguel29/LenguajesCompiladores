# -*- coding: utf-8 -*-
"""
Created on Wed Sept 01 08:41:02 2021

Codigo base en Python 3.8.5 que trata de resolver el problema de la
identificacion de Tokens propuesto del taller 2 sobre el 
analizador lexico-grafico.
La tabla de Simbolos se llama Tabla.xlsx que se encuentra en la carpeta
temporal, la cual tiene el id de cada token y su respectivo token
esta tabla posteriormente se convierte en un Dataframe con Pandas 
para su posterior utilizacion.
Despues se recorre el archivo caracter por caracter donde posteriormente 
se almacena si es un token,su ID y su lexema generador en un
diccionario de listas, el cual al final se convierte en un Dataframe para 
despues volverse un archivo Excel llamado tablaTokens.xlsx y un archivo 
.csv llamado tabla_tokens, en  algunos casos en el archivo de excel el
igual(=) se puede ver como un 0, por lo tanto esta el archivo csv de 
respaldo

Hay dos codigos fuentes en formato .txt, se llaman texto1.txt y texto2.txt



@author: Miguel Wagner
"""

#importar las librerias a usar
import pandas as pd
import numpy as np


def analizar_cadena(cadena,diccionario,lista_simbolos,df_simbolos):
    """
    Funcion que analiza la cadena e identifica si es un Token 
    y lo agrega al diccionario, con su ID
    Recibe como parametros la cadena,el diccionario, las listas con los 
    nombres

    Parameters
    ----------
    cadena : string
        cadena para ser analizada
    diccionario : dict
        Diccionario donde se almacena la informacion recolectada
    lista_simbolos : list
        Lista con el nombre de los simbolos
    df_simbolos : dataframe
        Dataframe donde se almacena la informacion de los simbolos

    Returns
    -------
    None.

    """

    
    #comprobar que el string no este vacio 
    if not cadena.strip():
        pass    
    
    #Agregar el espacio y enter
    elif cadena=='Enter'or cadena=='Espacio':
    
        index=lista_simbolos.index(cadena)
        #agregar el token al diccionario con los datos del Dataframe
        diccionario['Token'].append(df_simbolos.iloc[index,1])
        diccionario['TokenID'].append(df_simbolos.iloc[index,0])
        diccionario['Lexema'].append('')
        
        
    #comprobar que la cadena si este en la lista de tokens
    elif cadena in lista_simbolos:
        index=lista_simbolos.index(cadena)
        #agregar el token al diccionario con los datos del Dataframe
        diccionario['Token'].append(df_simbolos.iloc[index,1])
        diccionario['TokenID'].append(df_simbolos.iloc[index,0])
        diccionario['Lexema'].append(cadena)
    
    
    else:
        #agregar el identificador al diccionario 
        diccionario['Lexema'].append(cadena)
        diccionario['TokenID'].append(1)
        diccionario['Token'].append('Identificador')
        
        
        

def recorrer_archivo(nombre_codigo,diccionario,df_simbolos,lista_simbolos):
    """
    Funcion para recorrer el archivo, que recibe como parametro el archivo y
    Se recorre linea por linea y caracter por caracter el archivo como una 
    cadena de texto

    Parameters
    ----------
    nombre_codigo : string
        Nombre del archivo .txt con el codigo a analizar
    diccionario : dict
        DESCRIPTION.
    df_simbolos : dataframe
        Dataframe donde se almacena los datos recogidos.
    lista_simbolos : list
        Lista con el nombre de los diferentes simbolos.

    Returns
    -------
    diccionario : dict
        Dictionario con la informacion recolectada

    """
    
    texto=open(nombre_codigo,'r')
    #variable contadora de la cantidad de renglones tiene el texto
    y=0
    
    #variable acumuladora de caracteres que se va recorriendo
    aux=''
    
    #recorrer el archivo linea por linea
    for linea in texto:
        
        #recorrer byte por byte cada linea o cadena de texto del archivo
            for i in range(len(linea)):
                
                #comprobar la ultima posicion de la cadena, buscando si hay 
                #simbolo y agregar el salto de linea
                if i == len(linea)-1:
                    
                    analizar_cadena(aux,diccionario,lista_simbolos,
                                    df_simbolos)
                    analizar_cadena('Enter',diccionario,lista_simbolos,
                                    df_simbolos)
                    #reiniciar el acumulador para la nueva linea
                    aux=''
                    
                    
                #comprobar si el caracter es un simbolo o espacio
                elif linea[i] in lista_simbolos or linea[i]==' ':
                    
                    #clasificar y agregar el acumulador como identificador
                    #o simbolo
                    analizar_cadena(aux,diccionario,lista_simbolos,
                                    df_simbolos)
                    
                    #si es un espacio agregar a la tabla como 'Espacio'
                    if linea[i] == ' ':
                        analizar_cadena('Espacio',diccionario,
                                        lista_simbolos,df_simbolos)
                        
                    else:
                        #agregar a la tabla el simbolo 
                        analizar_cadena(linea[i],diccionario,
                                        lista_simbolos,df_simbolos)
                        
                    #vaciar el acumulador para una nueva combinacion de
                    #caracteres
                    aux=''
                    
                    
                else:
                    #si no es un simbolo, agregar el caracter al acumulador
                    aux+=linea[i]
                    
                    
            #aumentarle 1 al contador de filas
            y+=1
            
            
    #devolver el diccionario
    return diccionario




def main(archivoTexto):
    '''
    Funcion Principal que se encarga de toda la logistica para que funcione 
    el metodo

    Parameters
    ----------
    archivoTexto : String
        El archivo de texto ingresado por la interfaz

    Returns
    -------
    None.

    '''
    #alamacenar tanto la tabla de operadores como la de simbolos en variables
    #distintas
    df_simbolos=pd.read_excel('Tabla.xlsx', sheet_name='tabla de simbolos')
    
    
    
    
    #reemplazar todos los espacios vacios del dataframe como una cadena vacia
    df_simbolos=df_simbolos.replace(np.nan,'',regex=True)
    
    
    
    
    #convertir toda la columna de Nombre en los dos DataFrame como str
    df_simbolos['Simbolo']=df_simbolos['Simbolo'].astype(str)
    
    
    
    
    #almacenar en una lista el nombre de los simbolos y operadores
    simbolos=df_simbolos['Simbolo'].tolist()
    
    
    
    #Crear el diccionario donde se va almacenar la informacion
    dict_analizador={"Token":[],"TokenID":[],"Lexema":[]}
    
    
    #llamar a la funcion para rellenar el diccionario con simbolos e identificador
    dict_analizador=recorrer_archivo(archivoTexto,dict_analizador,df_simbolos,
                                 simbolos)




    #convertir el diccionario a un Dataframe
    df=pd.DataFrame(dict_analizador, 
                    columns = ['Token','TokenID','Lexema'])
    
    
    
    
    #convertir el Dataframe en un archivo en excel
    #df.to_excel('tablatokens.xlsx','final',index=False)
    
    
    
    #convertir el Dataframe en un archivo .csv
    df.to_csv('tabla_tokens.csv',index=False)
    

    

