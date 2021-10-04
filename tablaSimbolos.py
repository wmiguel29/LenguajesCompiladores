# -*- coding: utf-8 -*-
"""
Created on Wed Sept 01  08:41:02 2021

Codigo base en Python 3.8.5 que trata de resolver el problema de la
identificacion de simbolos propuesto del taller 2 sobre el 
analizador lexico-grafico.
La tabla de Simbolos se llama Tabla.xlsx que se encuentra en la carpeta
temporal, esta tabla posteriormente se convierte en un Dataframe con Pandas 
para su posterior utilizacion.
Despues se recorre el archivo caracter por caracter donde posteriormente 
se almacena si es un simbolo y sus tipos o si es un identificador en un
diccionario de listas, el cual al final se convierte en un Dataframe para 
despues volverse un archivo Excel llamado tablaSimbolos.xlsx y un archivo 
.csv llamado tabla_simbolos, en  algunos casos en el archivo de excel el
igual(=) se puede ver como un 0, por lo tanto esta el archivo csv de 
respaldo

Hay dos codigos fuentes en formato .txt, se llaman texto1.txt y texto2.txt

El formato de la ubicacion es y,x

@author: Miguel Wagner
"""

#importar las librerias a usar
import pandas as pd
import numpy as np


def analizar_cadena(cadena,diccionario,x,y,lista_simbolos,df_simbolos):
    """
    Funcion que analiza la cadena e identifica si es un simbolo o un identificador
    y lo agrega al diccionario
    Recibe como parametros la cadena,el diccionario, las listas con los 
    nombres y la posicion x y y

    Parameters
    ----------
    cadena : string
        cadena de caracteres a analizar.
    diccionario : dict
        Diccionario donde se guarda la informacion obtenida.
    x : int
        posicion x del caracter en el texto
    y : int
        posicion y del caracter en el texto
    lista_simbolos : list
        lista de todos los nombres del simbolo
    df_simbolos : dataframe
        Dataframe donde se almacena la informacion de los simbolos

    Returns
    -------
    None.

    """
    
    #comprobar que el string no este vacio 
    if not cadena.strip():
        pass    
    #comprobar que la cadena si este en la lista de simbolos
    elif cadena in lista_simbolos:
        index=lista_simbolos.index(cadena)
        #agregar el simbolo al diccionario con los datos del Dataframe
        diccionario['Simbolo'].append(df_simbolos.iloc[index,2])
        diccionario['Ubicacion'].append(str(y)+','+str(x-len(cadena)))
        diccionario['Tipo1'].append(df_simbolos.iloc[index,3])
        diccionario['Tipo2'].append(df_simbolos.iloc[index,4])
        diccionario['Tipo3'].append(df_simbolos.iloc[index,5])
    else:
        #agregar el identificador al diccionario 
        diccionario['Simbolo'].append(cadena)
        diccionario['Ubicacion'].append(str(y)+','+str(x-len(cadena)))
        diccionario['Tipo1'].append('Identificador')
        diccionario['Tipo2'].append('')
        diccionario['Tipo3'].append('')
        
        
        

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
        DESCRIPTION.

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
                    if aux=='':
                        aux+=linea[i]
                    
                    analizar_cadena(aux,diccionario,i,y,lista_simbolos,
                                    df_simbolos)
                    analizar_cadena('Enter',diccionario,i+5,y,lista_simbolos,
                                    df_simbolos)
                    #reiniciar el acumulador para la nueva linea
                    aux=''
                #comprobar si el caracter es un simbolo o espacio
                elif linea[i] in lista_simbolos or linea[i]==' ':
                    #clasificar y agregar el acumulador como identificador
                    #o simbolo
                    analizar_cadena(aux,diccionario,i,y,lista_simbolos,
                                    df_simbolos)
                    #si es un espacio agregar a la tabla como 'Espacio'
                    if linea[i] == ' ':
                        analizar_cadena('Espacio',diccionario,i+7,y,
                                        lista_simbolos,df_simbolos)
                    else:
                        #agregar a la tabla el simbolo 
                        analizar_cadena(linea[i],diccionario,i+1,y,
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
    dict_analizador={"Simbolo":[],"Ubicacion":[],"Tipo1":[],"Tipo2":[],"Tipo3":[]}
    
    
    #llamar a la funcion para rellenar el diccionario con simbolos e identificador
    dict_analizador=recorrer_archivo(archivoTexto,dict_analizador,df_simbolos,
                                 simbolos)




    #convertir el diccionario a un Dataframe
    df=pd.DataFrame(dict_analizador, 
                    columns = ['Simbolo','Tipo1','Tipo2','Tipo3','Ubicacion'])
    
    
    
    
    #convertir el Dataframe en un archivo en excel
    #df.to_excel('tablaSimbolos.xlsx','final',index=False)
    
    
    
    #convertir el Dataframe en un archivo .csv
    df.to_csv('tabla_simbolos.csv',index=False)
    

    
