# LenguajesCompiladores




OBJETIVO DEL TALLER:

Complementar los Talleres No. 1, 2 y 3 ya realizados, agregando nuevos componentes que permitan avanzar en los procesos de traducción dirigida por sintaxis mediante gramáticas libres de contexto.


QUÉ DEBO REALIZAR?

Agregar a su taller No. 1,2 y 3 (ya presentados) al menú básico una opción nueva que permita al usuario escoger entre las expresiones aritméticas reconocidas dentro del código (Taller No. 3) y suponiendo que la expresión aritmética seleccionada tenga una sintaxis válida, permita al usuario conocer su equivalente en notación prefijo y posfijo.

El análisis sintáctico de la expresión seleccionada por el usuario debe ser realizado mediante la implementación de la gramática libre de contexto correspondiente sobre el lenguaje por usted seleccionado y así mismo el proceso de traducción a la notación prefijo o posfijo deberá ser realizado mediante acciones semánticas sobre una gramática correspondiente.

Tenga en cuenta que el usuario después de realizar el análisis sintáctico y ver sus resultados deberá regresar al menu, donde podría seleccionar una nueva expresión o incluso cargar otros archivos utilizando las demás opciones ya implementadas en los talleres previos.   Así pues, el menú de su aplicación debería contener ahora las siguientes opciones:

    Cargar un archivo plano dado con código fuente a ser analizado.  Dando al usuario la posibilidad de escogerlo o indicar su ruta para ser cargado.
    Identificar e inventariar todos los elementos dentro del código definidos sobre la tabla de símbolos.  Símbolo, Clasificación, Ubicación (línea y columna).  Esto es lo ya desarrollado en el Taller 01.  Si le faltó corregir algo de una vez incluya sus correcciones.
    Identificar e inventariar todos los elementos dentro del código definidos sobre la tabla de Tokens entregando:  Token, #IdToken, Lexema generador.
    Identificar dentro del código fuente aquellas sentencias donde se encuentran expresiones aritméticas.   Analice: ¿Cómo identificaría usted dentro de un código o cadena que está analizando si éste es o no una expresión aritmética?   Su programa deberá indicar en dónde se encuentran este tipo de expresiones dentro del código analizado y además separarlas en alguna estructura independiente para futuro procesamiento.
    Seleccionar de la lista de expresiones detectadas alguna a la que desee verificar su sintaxis por medio de la implementación de la GLC correspondiente.
    Seleccionar una de las expresiones con sintaxis válida y visualizar su equivalencia en notaciones prefijo y posfijo.
    Opción de salir.


QUÉ DEBO ENTREGAR?

    Códigos fuente de su programa (comprimidos en formato zip).  Esto debe incluir además de los fuentes propios de la programación, los archivos que alimentan posibles tablas y archivo con el código fuente que será alimentado en el programa para su análisis.
    Pantallazos paso a paso del funcionamiento de su programa.  Estos pueden ser adjuntados sobre un archivo separado en el ZIP en formato documento de texto donde indique además lenguaje de programación utilizado y versión.
    Ejecutable (binario compilado) para ejecución directa de su programa.

RECOMENDACIONES:

    Recuerde documentar muy bien su código
    Asegúrese de ubicar correctamente los archivos que va a leer desde su programa.  Utilice de ser posible archivos sobre la misma ruta donde reside su aplicación para que al ser ejecutados no tengan problema en localizar el archivo que se desea analizar.
    Quienes por algún motivo deseen trabajar en equipos será máximo de dos integrantes y ambos estudiantes deberán cargar el mismo resultado por la plataforma de manera individual.  En el archivo de texto indicarán quiénes conformaban el equipo.
    Sea puntual en la fecha de entrega y el medio solicitado (esto se entrega a través del aula virtual, no otros medios)
    
