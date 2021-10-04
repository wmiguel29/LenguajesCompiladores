# -*- coding: utf-8 -*-
"""
Created on Wed Sept 01 16:05:26 2021

Modulo de la tercera parte del taller el cual identifica la presencia de
expresiones aritmeticas, lo que hace este metodo es recorrer la tabla de 
simbolos generada en el primer taller y verifica en los simbolos con 
operaciones aritmeticas y concatena el identificador anterior y en los 
siguientes se asegura que no halla nos identificadores seguidos o dos 
operadores seguidos, el numero menos de elementos de una operacion es tres

@author: Miguel Wagner
"""

#Importar el modulo de la tabla de simbolos
import tablaSimbolos as fl
#Importar librerias requeridas
import pandas as pd


    


def recorrer_df(df,diccionario):
    '''
    Recorre el dataframe de arriba hacia abajo, fila por fila y identifica
    donde hay operaciones

    Parameters
    ----------
    df : Datafrane
        Dataframe de la tabla de simbolos
    diccionario : Diccionario
        Diccionario creado para almacenar la informacion

    Returns
    -------
    diccionario : Diccionario
        Diccionario final

    '''
    
    #Operadores para tener en cuenta en una operacion aritmetica
    x="Operacion Aritmetica"
    #y="Delimitar"
    
    
    #Lista para almacenar los componentes de la operacion
    aux=[]
    
    
    #contador del numero de filas de el dataframe
    i=0
    
    
    #bandera para salir del while interno
    flag=True
    
    
    #recorrer todo el dataframe completo
    while i in range(len(df)):
        
        #No tener en cuenta ni la primera ni la ultima posicion
        if i==0 or i==len(df)-1:
            i+=1
            pass
        
        
        #comprobar donde halla un simbolo operador o separador
        elif x in df.iloc[i].tolist()  :
            #agregar el simbolo y token pasado a la variable auxiliar y ubicacion
            aux.append(df.iloc[i-1,0])
            aux.append(df.iloc[i,0])
            diccionario['Ubicacion'].append(df.iloc[i-1,4])
            
            
            #Flag de si es un separador
            sep=True
            i+=1
            
            
            flag=True
            #recorrer mientras este correcta la operacion y este dentro
            #del rango del dataframe
            while flag and i in range(len(df)):
                
                
                #Si es un operador hay que comprobar que no sigue otro operador
                #Si es un identificador se agrega al auxiliar
                #Si no es ninguno no es una expresion
                if sep:
                    if x in df.iloc[i].tolist():
                        flag=False
                    elif df.iloc[i,1]=='Identificador':
                        aux.append(df.iloc[i,0])
                        sep=False
                        i+=1
                    else:
                        flag=False
                        
                #Si no es un operador hay que comprobar que el siguiente 
                #no sea un identificador ni otra cosa
                #Si es un operador se agrega al aux
                else:
                    if df.iloc[i,1]=='Identificador':
                        flag=False
                    elif x in df.iloc[i].tolist() :
                        aux.append(df.iloc[i,0])
                        sep=True
                        i+=1
                    else:
                        flag=False
                        
                        
            v=''
            #Comprobar que la operacion tenga la suficiente longitud
            #Convertirla en un String para posteriormente almacenarla en el
            #diccionario
            if len(aux)>2:
                for w in aux:
                  v+=w
                diccionario['Expresion'].append(v)
                aux.clear()
                
                
            #si no cumple con la longitud se limpia el aux y se borra la 
            #ubicacion
            else:
                aux.clear()
                diccionario['Ubicacion'].pop()
                
            i+=1
        else:
            i+=1
                
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
    
    
    #llama al modulo de tabla de simbolos para generar la tabla
    fl.main(archivoTexto)
    
    
    #leer el archivo.csv como Dataframe
    df=pd.read_csv('tabla_simbolos.csv')
    
    
    #convertir todas las celulas del dataframe a String
    df=df.applymap(str)
    
    
    #Eliminar los simbolos de espacio del dataframe
    df_final=df[df['Simbolo']!='Espacio']
    
    
    #Crear el diccionario para almacenar la info
    diccionario={'Expresion':[],'Ubicacion':[]}
    
    #recorrer el dataframe para completar el diccionario
    diccionario=recorrer_df(df_final,diccionario)
    
    
    #convertir el diccionario a un Dataframe
    df=pd.DataFrame(diccionario, 
                    columns = ['Expresion','Ubicacion'])
    
    
    #convertir el Dataframe en un archivo en excel
    #df.to_excel('tabla_operadores.xlsx','final',index=False)
    
    
    
    #convertir el Dataframe en un archivo .csv
    df.to_csv('tabla_operaciones.csv',index=True)
    
    

        
        
                
            


