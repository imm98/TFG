#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:15:35 2021

@author: inaki
"""
import sys #Para hacer el sys.exit

import copy #Para el constructor de copia que no hace falta

from turtle import *

setup(2000, 600, 0,0)

speed(7)


class Nudo:
    def __init__(self, *numeros):
        '''
        El único atributo de la clase Nudo será una lista llamada numeros que será privada, que definirá el nudo.

        Argumentos:
            *numeros: Conjunto de números pares positivos y negativos consecutivos en valor absoluto y sin repetición (empezando por el 2)
        
        '''
        self.__numeros=[]
        for x in range(len(numeros)):
            self.__numeros.append(numeros[x])
        print(self.__numeros)

    def numero_arcos_superiores(self):
        '''
        Devuelve el número de arcos superiores que tendrá el nudo. 
        '''

        contador=0  #Esta variable almacenará la suma de arcos superiores e inferiores del nudo 
        if (self.__numeros[0]>0):
            superior_global=False       #Esta variable almacenará el estado del último cruce que hems recorrido
        else:
            superior_global=True
        
        for x in range(len(self.__numeros)-1):
            
            if 2*x+2 not in self.__numeros:   #Esto se hace para ver si los cruces de los números pares son superiores o inferiores. Si son inferiores...(es decir, si el número par no pertenece a la lista(dado que pertenece su opuesto))
                if (superior_global==True):
                    contador+=1
                    superior_global=False
            else:                           #Si son superiores
                if (superior_global==False):
                    contador+=1
                    superior_global=True
            
            if self.__numeros[x+1]>0:      #Esto se hace para ver si los cruces de los números impares son superiores o inferiores. Si son inferiores...
                   
                if (superior_global==True):  
                    contador+=1
                    superior_global=False
            else:                       #Si son superiores
                if (superior_global==False):
                    contador+=1
                    superior_global=True
        
        #Con esto comprobamos el último cruce 
        if 2*len(self.__numeros) not in self.__numeros:
            if (superior_global==True):
                contador+=1
                superior_global=False
        else:                           #Si son superiores
            if (superior_global==False):
                contador+=1
                superior_global=True
        
        #Con esto el primer cruce
        if (self.__numeros[0]>0):
            if (superior_global==True):
                contador+=1
                superior_global=False
        else:
            if (superior_global==False):
                contador+=1
                superior_global=True

        return(int(contador/2)) #Lo dividimos por dos ya que solo queremos el número de arcos superiores y dado que el número de arcos superiores e inferiores será el mismo 

    def __dividir_en_dos_subpermutaciones(self):
        '''
        Devuelve el índice de la secuencia a partir del cuál la secuencia dada por __numeros se puede separar en dos subpermutaciones
        En caso de que no se pueda separa en dos subpermutaciones se devuelve el valor -1

        Ejemplo:
            >>> x=Nudo(4,6,2, 10, 12, 8)
            >>> x.__dividir_en_dos_subpermutaciones()
            2       #Ya que se puede dividir en (4, 6, 2) y (10, 12, 8) y el 2 ocupa la posición 2 en la lista

            >>> x=Nudo (8,10,2,12,4, 6)
            >>> x.__dividir_en_dos_subpermutaciones()
            -1
        '''

        maximo=3        #Aquí almacenaremos el máximo valor par en valor absoluto de la lista __numeros conforma la vayamos recorriendo
        indice_maximo=-1    
        for x in range(len(self.__numeros)-1):
            if abs(self.__numeros[x]) > maximo: 
                maximo=abs(self.__numeros[x])
            
            if ((2*x+2)==maximo):       #Si coincide el número de cruces que hemos recorrido con el valor máximo significará que se puede dividir la permutación en dos subpermutaciones 
                indice_maximo=x
        return indice_maximo
    
    def dividir_nudo_en_arcos(self, puntos):

        '''
        El objetivo de esta función es poder dividir el conjunto de puntos obtenidos de la función obtener_puntos_nudo_dowker 
        en puntos pertenecientes a un arco superior o a un arco inferior.
        
        Para ello iremos recorriendo esa secuencia de puntos y determinando cuando se pasa de un arco inferior a uno superior y viceversa.
        
        Añadiremos puntos a la lista de puntos si es necesario, y esta función devolverá una lista de índices donde cada índice indicará una posición de
        la lista de puntos en la que se debe realizar el cambio de un arco superior a un arco inferior o viceversa
        
        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker 
        '''
        terminado=False
        contador_global=1
        
        contador_aux=1          
        punto_final=[-0.5,0]
        vector_cambio=[]

        if (self.__numeros[0]>0):
            superior=False
            superior_inicial=False
        else:
            superior=True
            superior_inicial=True
        
        
        while (terminado ==False):
            if (puntos[contador_global]==punto_final):
                terminado=True
            else:
                if superior:
                    if (contador_aux==1):
                        if (puntos[contador_global]!= puntos[contador_global+1]):   #Significa que hemos llegado a un cruce inferior por lo tanto hay que añadir un nuevo punto  
                            
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]  #Tomamos el punto medio que será el punto que añadiremos
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux) #Lo añadimos dos veces ya que dicho punto formará parte de dos aristas del nudo, perteneciendo una de ellas a un arco horizontal y la otra a un arco vertical
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)

                            superior=False
                            
                        else:
                            contador_aux=0
                    else:
                        contador_aux=1
                    
                else:
                    if (puntos[contador_global]== puntos [contador_global+1]):
                        if (puntos[contador_global-1][0] < puntos[contador_global][0] and puntos[contador_global][0] < puntos[contador_global+2][0]):
                            
                            #Hay que añadir el punto medio dos veces                             
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            

                        if (puntos[contador_global-1][1] < puntos[contador_global][1] and puntos[contador_global][1] < puntos[contador_global+2][1]):
                            
                            #Hay que añadir el punto medio dos veces 
                            
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            
                        
                        if (puntos[contador_global-1][0] > puntos[contador_global][0] and puntos[contador_global][0] > puntos[contador_global+2][0]):
                            
                            #Hay que añadir el punto medio dos veces  
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            
                        
                        if (puntos[contador_global-1][1] > puntos[contador_global][1] and puntos[contador_global][1] > puntos[contador_global+2][1]):

                            #Hay que añadir el punto medio dos veces   
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            
                
                contador_global+=1
        if ((superior==True and superior_inicial==False) or (superior==False and superior_inicial==True)):
            vector_cambio.insert(0, 0)
            vector_cambio.append(contador_global)

        
            
        return vector_cambio
    
    def dibujar_nudo(self, puntos):
        '''
        Se utiliza el módulo turtle de python para dibujar el nudo dado por los puntos obtenidos de la función obtener_puntos_nudo_dowker 
        en una ventana distinta a la ventana de IDLE. 
        Una flecha indicará la orientación del nudo.

        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
        '''

        
        title("Nudo obtenido a través de la notación Dowker")
        contador=0
        penup()
        for x in puntos:
            if (contador % 2==0):
                punto1=(100*x[0], 100*x[1])
            else:               #Solo dibujaremos la arista cuando tengamos los dos puntos de esta almacenados
                punto2=(100*x[0], 100*x[1])
                goto(punto1)
                pendown()
                goto(punto2)
                penup()
            contador+=1

        #Esto es para dibujar la flecha, que indicará la orientación del nudo
        penup()
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        begin_fill()
        pendown()
        punto_aux=[-0.38*100, -0.07*100]
        goto(punto_aux)
        punto_aux=[-0.22*100, 0.0]
        goto(punto_aux)
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        end_fill()

        hideturtle()
        exitonclick()
        Screen().bye()

    def dibujar_nudo_arcos(self, puntos, numeros_cambio):
        '''
        Se dibuja el nudo dado por los puntos obtenidos de la función obtener_puntos_nudo_dowker en una ventana emergente.
        En dicho dibujo, se representarán con color rojo los arcos superiores y con color azul los arcos inferiores.
        Una flecha indicará la orientación del nudo. 

        Args: 
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos) 
            numeros_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''
        if (self.__numeros[0]>0):
            superior_inicial=False  #Esta variable se utiliza para saber de que color debemos dibujar la flecha 
            superior=False
            pencolor("red")
        else:
            superior_inicial=True
            superior=True
            pencolor("blue")

        title("Nudo dividido en arcos superiores e inferiores")
        colormode(255)
        contador=0
        penup()
        pensize(3)
        for x in puntos:
            if (contador % 2==0):
                punto1=(100*x[0], 100*x[1])
            else:
                punto2=(100*x[0], 100*x[1])
                
                    
                    
                goto(punto1)
                pendown()
                goto(punto2)
                penup()
                if (contador in numeros_cambio):
                    if superior:
                        superior=False
                        pencolor("red")
                    else:
                        superior=True
                        pencolor("blue")
                    
            contador+=1

        #Dibujamos los puntos de Q
        for i in numeros_cambio:
            goto(100*puntos[i][0],100* puntos[i][1])
            dot(5, 0, 255,0)
        
        #Ahora dibujamos la flecha
        if (superior_inicial==False):
            fillcolor("red")
        else:
            fillcolor("blue")

        pensize(0.5)
        penup()
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        begin_fill()
        pendown()
        punto_aux=[-0.38*100, -0.07*100]
        goto(punto_aux)
        punto_aux=[-0.22*100, 0.0]
        goto(punto_aux)
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        end_fill()
        hideturtle()
        exitonclick()
        Screen().bye()

    def obtener_aristas(self, puntos):
        '''
        Dada la lista de puntos del nudo, obtiene las aristas horizontales y verticales de este y las devuelve,
        en una lista con dos elementos, siendo el primero de ellos una lista de las aristas horizontales y el segundo 
        una lista de las aristas verticales.

        Cada arista horizontal será una lista de 3 números [y, x_1, x_2] donde el primero de ellos será la coordenada 'y' de la arista horizontal, 
        el segundo elemento será la coordenada 'x' del vértice de la arista con menor valor y el tercero será la coordenada 'x' del vértice de la arista 
        con mayor valor.

        Cada arista vertical será una lista de 3 números [x, y_1, y_2] donde el primero de ellos será la coordenada 'x' de la arista vertical, 
        el segundo elemento será la coordenada 'y' del vértice de la arista con menor valor y el tercero será la coordenada 'y' del vértice de la arista 
        con mayor valor.

        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
        '''

        punto_inicial=puntos[0]
        horizontal=True
        aristas_horizontales=[]
        aristas_verticales=[]
        for x in range(len(puntos) - 1):
            if horizontal:
                if (puntos[x+1][1] != punto_inicial[1]):
                    horizontal=False
                    
                    if (punto_inicial[0] < puntos[x][0]): #Esto es para meter la arista con las coordenadas ordenadas 
                        arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                    else:
                        arista_h_aux=[punto_inicial[1],  puntos[x][0], punto_inicial[0]]

                    punto_inicial=puntos[x]
                    
                    aristas_horizontales.append(arista_h_aux)
            
            else:
                if (puntos[x+1][0] != punto_inicial[0]):
                    horizontal=True
                    
                    if (punto_inicial[1] < puntos[x][1]): #Esto es para meter la arista con las coordenadas ordenadas 
                        arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                    else:
                        arista_v_aux=[punto_inicial[0],  puntos[x][1], punto_inicial[1]]

                    punto_inicial=puntos[x]
                    aristas_verticales.append(arista_v_aux)

        if (punto_inicial[1]< 0):
            arista_v_aux=[-0.5, punto_inicial[1], 0]
        else:
            arista_v_aux=[-0.5, 0, punto_inicial[1]]

        aristas_verticales.append(arista_v_aux)

        aristas=[]
        aristas.append(aristas_horizontales)
        aristas.append(aristas_verticales)
        return aristas

    def __obtener_aristas_inferiores(self, puntos, vector_cambio):
        '''
        Dada la lista de puntos del nudo, obtiene las aristas horizontales y verticales de los arcos inferiores de este y las devuelve,
        en una lista con dos elementos, siendo el primero de ellos una lista de las aristas horizontales y el segundo 
        una lista de las aristas verticales, estando las aristas horizontales y verticales en el mismo formato que la función anterior.

        Estas aristas se utilizarán para, a la hora de determinar los caminos v_i, comprobar que dichos caminos no se intersecten con ninguna arista inferior o
        con ningún otro camino v_j j!=i


        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            vector_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        aristas_horizontales=[]
        aristas_verticales=[]
        if (self.__numeros[0]>0):
            superior=False
            punto_inicial=puntos[0]
            horizontal=True
        else:
            superior=True
        
        
        for x in range(len(puntos) - 1):
            if (superior==False):
                if horizontal:
                    if (puntos[x+1][1] != punto_inicial[1]):
                        horizontal=False
                        
                        if (punto_inicial[0] < puntos[x][0]): #Esto es para meter la arista con las coordenadas ordenadas 
                            arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                        else:
                            arista_h_aux=[punto_inicial[1],  puntos[x][0], punto_inicial[0]]

                        punto_inicial=puntos[x]
                        
                        aristas_horizontales.append(arista_h_aux)
                
                else:
                    if (puntos[x+1][0] != punto_inicial[0]):
                        horizontal=True
                        
                        if (punto_inicial[1] < puntos[x][1]): #Esto es para meter la arista con las coordenadas ordenadas 
                            arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                        else:
                            arista_v_aux=[punto_inicial[0],  puntos[x][1], punto_inicial[1]]

                        punto_inicial=puntos[x]
                        aristas_verticales.append(arista_v_aux)

            if (x in vector_cambio and x!=0):
                if (superior==False): #Si estabamos con los arcos inferiores hay que meter el último punto 
                    if horizontal:
                        if (punto_inicial[0] != puntos[x][0]): #Para ver que no es el mismo punto 

                            if (punto_inicial[0] < puntos[x][0]): #Esto es para meter la arista con las coordenadas ordenadas 
                                arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                            else:
                                arista_h_aux=[punto_inicial[1],  puntos[x][0], punto_inicial[0]]

                            aristas_horizontales.append(arista_h_aux)
                    else:
                        if(punto_inicial[1] != puntos[x][1]):
                            if (punto_inicial[1] < puntos[x][1]): #Esto es para meter la arista con las coordenadas ordenadas 
                                arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                            else:
                                arista_v_aux=[punto_inicial[0],  puntos[x][1], punto_inicial[1]]
                            
                            aristas_verticales.append(arista_v_aux)

                    superior=True
                else:
                    if (puntos[x+2][1] != puntos[x][1]):
                        horizontal=False
                    else:
                        horizontal=True
                    
                    punto_inicial=puntos[x]
                    superior=False
        
        if (superior==False):
            if (punto_inicial[1]< 0):
                arista_v_aux=[-0.5, punto_inicial[1], 0]
            else:
                arista_v_aux=[-0.5, 0, punto_inicial[1]]

            aristas_verticales.append(arista_v_aux)
        
        aristas=[]
        aristas.append(aristas_horizontales)
        aristas.append(aristas_verticales)
        return aristas

    def __obtener_aristas_superiores(self, puntos, vector_cambio):
        '''
        Dada la lista de puntos del nudo, obtiene las aristas horizontales y verticales de los arcos superiores de este y las devuelve,
        en una lista con dos elementos, siendo el primero de ellos una lista de las aristas horizontales y el segundo 
        una lista de las aristas verticales, estando las aristas horizontales y verticales en el mismo formato que la función obtener_aristas.

        Estas aristas se utilizarán para, a la hora de determinar los caminos u_i, comprobar que dichos caminos no se intersecten con ninguna arista superior ni 
        con otros caminos u_j j!=i.


        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            vector_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        aristas_horizontales=[]
        aristas_verticales=[]
        if (self.__numeros[0]>0):
            superior=False
            
        else:
            superior=True
            punto_inicial=puntos[0]
            horizontal=True
        
        for x in range(len(puntos) - 1):
            if (superior==True):
                if horizontal:
                    if (puntos[x+1][1] != punto_inicial[1]):
                        horizontal=False
                        
                        if (punto_inicial[0] < puntos[x][0]): #Esto es para meter la arista con las coordenadas ordenadas 
                            arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                        else:
                            arista_h_aux=[punto_inicial[1],  puntos[x][0], punto_inicial[0]]

                        punto_inicial=puntos[x]
                        
                        aristas_horizontales.append(arista_h_aux)
                
                else:
                    if (puntos[x+1][0] != punto_inicial[0]):
                        horizontal=True
                        
                        if (punto_inicial[1] < puntos[x][1]): #Esto es para meter la arista con las coordenadas ordenadas 
                            arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                        else:
                            arista_v_aux=[punto_inicial[0],  puntos[x][1], punto_inicial[1]]

                        punto_inicial=puntos[x]
                        aristas_verticales.append(arista_v_aux)

            if (x in vector_cambio and x!=0):
                if (superior==True): #Si estabamos con los arcos inferiores hay que meter el último punto 
                    if horizontal:
                        if (punto_inicial[0] != puntos[x][0]): #Para ver que no es el mismo punto 

                            if (punto_inicial[0] < puntos[x][0]): #Esto es para meter la arista con las coordenadas ordenadas 
                                arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                            else:
                                arista_h_aux=[punto_inicial[1],  puntos[x][0], punto_inicial[0]]

                            aristas_horizontales.append(arista_h_aux)
                    else:
                        if(punto_inicial[1] != puntos[x][1]):
                            if (punto_inicial[1] < puntos[x][1]): #Esto es para meter la arista con las coordenadas ordenadas 
                                arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                            else:
                                arista_v_aux=[punto_inicial[0],  puntos[x][1], punto_inicial[1]]
                            
                            aristas_verticales.append(arista_v_aux)

                    superior=False
                else:
                    if (puntos[x+2][1] != puntos[x][1]):
                        horizontal=False
                    else:
                        horizontal=True
                    
                    punto_inicial=puntos[x]
                    superior=True
        
        if (superior==True):
            if (punto_inicial[1]< 0):
                arista_v_aux=[-0.5, punto_inicial[1], 0]
            else:
                arista_v_aux=[-0.5, 0, punto_inicial[1]]

            aristas_verticales.append(arista_v_aux)
        
        aristas=[]
        aristas.append(aristas_horizontales)
        aristas.append(aristas_verticales)
        return aristas

    def __obtener_aristas_inferiores_ordenadas(self, puntos, vector_cambio):
        '''
        Dada la lista de puntos del nudo, obtiene las aristas horizontales y verticales de los arcos inferiores de este y las devuelve,
        en una lista con dos elementos, siendo el primero de ellos una lista de las aristas horizontales y el segundo 
        una lista de las aristas verticales.

        En este caso, el formato de las aristas horizontales y verticales devueltas es:

        Cada arista horizontal será una lista de 3 números [y, x_1, x_2] donde el primero de ellos será la coordenada 'y' de la arista horizontal, 
        el segundo elemento será la coordenada 'x' del primer vértice de la arista que ha sido recorrido (es decir, el que se encuentra antes en la lista de puntos)
        y el tercero será la coordenada 'x' del segundo vértice de la arista que ha sido recorrido.
        
        Cada arista vertical será una lista de 3 números [x, y_1, y_2] donde el primero de ellos será la coordenada 'x' de la arista vertical, 
        el segundo elemento será la coordenada 'y' del primer vértice de la arista que ha sido recorrido (es decir, el que se encuentra antes en la lista de puntos)
        y el tercero será la coordenada 'y' del segundo vértice de la arista que ha sido recorrido.

        Estas aristas se utilizarán para, a la hora de calcular la presentación inferior del nudo, tener en cuenta el sentido de los cruces de los caminos u_i con las
        aristas inferiores del nudo. 


        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            vector_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        aristas_i=[]
        aristas_horizontales_i=[]
        aristas_verticales_i=[]
        aristas=[]
        valor_salir=-1   #Este valor servirá para en caso de que tomemos las últimas aristas del nudo para meterlas como dentro del primer conjunto posterioremente no analizarlas
        
        if (self.__numeros[0]>0):
            superior=False     
        else:
            superior=True
        
        if (superior==False):
            if 0 not in vector_cambio:
                valor_salir=vector_cambio[len(vector_cambio)-1]
                indice_partida=vector_cambio[len(vector_cambio)-1]
                punto_inicial=puntos[indice_partida]
                if (puntos[indice_partida-1][0] != puntos[indice_partida][0]):
                    horizontal=True
                else:
                    horizontal=False

                for i in range(len(puntos) - indice_partida-1):
                    if horizontal:
                        if (puntos[indice_partida+i+1][1] != punto_inicial[1]):
                            horizontal=False
                            
                            
                            arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[indice_partida+i][0]]

                            punto_inicial=puntos[indice_partida+i]
                            
                            aristas_horizontales_i.append(arista_h_aux)
                    
                    else:
                        if (puntos[indice_partida+i+1][0] != punto_inicial[0]):
                            horizontal=True
                            
                            arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[indice_partida+i][1]]
        
                            punto_inicial=puntos[indice_partida+i]
                            aristas_verticales_i.append(arista_v_aux)

                arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[len(puntos)-1][1]]
                aristas_verticales_i.append(arista_v_aux)

            punto_inicial=puntos[0]
            horizontal=True

        condicion_salir=False
        for x in range(len(puntos) - 1):
            if (condicion_salir==False):
                if (superior==False):
                    if horizontal:
                        if (puntos[x+1][1] != punto_inicial[1]):
                            horizontal=False
                            
                            
                            arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                            

                            punto_inicial=puntos[x]
                            
                            aristas_horizontales_i.append(arista_h_aux)
                    
                    else:
                        if (puntos[x+1][0] != punto_inicial[0]):
                            horizontal=True
                            
                            
                            arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                            
                            punto_inicial=puntos[x]
                            aristas_verticales_i.append(arista_v_aux)

                if (x in vector_cambio and x!=0):
                    if (superior==False): #Si estabamos con los arcos inferiores hay que meter el último punto 
                        if horizontal:
                            if (punto_inicial[0] != puntos[x][0]): #Para ver que no es el mismo punto 

                                
                                arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]

                                aristas_horizontales_i.append(arista_h_aux)
                        else:
                            if(punto_inicial[1] != puntos[x][1]):
                                arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                                
                                aristas_verticales_i.append(arista_v_aux)

                        aristas_i.append(aristas_horizontales_i)
                        aristas_i.append(aristas_verticales_i)
                        aristas.append(aristas_i)

                        aristas_i=[]
                        aristas_horizontales_i=[]
                        aristas_verticales_i=[]
                        superior=True
                    else:
                        if (puntos[x+2][1] != puntos[x][1]):
                            horizontal=False
                        else:
                            horizontal=True
                        
                        punto_inicial=puntos[x]
                        superior=False

                    if (x==valor_salir):
                        condicion_salir=True
        
        if (condicion_salir==False):
            if (superior==False):
                
                arista_v_aux=[-0.5, punto_inicial[1], 0]
                

                aristas_verticales_i.append(arista_v_aux)
                aristas_i.append(aristas_horizontales_i)
                aristas_i.append(aristas_verticales_i)
                aristas.append(aristas_i)
        
        return aristas

    def __obtener_aristas_superiores_ordenadas(self, puntos, vector_cambio):
        '''
        Dada la lista de puntos del nudo, obtiene las aristas horizontales y verticales de los arcos superiores de este y las devuelve,
        en una lista con dos elementos, siendo el primero de ellos una lista de las aristas horizontales y el segundo 
        una lista de las aristas verticales.

        En este caso, el formato de las aristas horizontales y verticales devueltas es:

        Cada arista horizontal será una lista de 3 números [y, x_1, x_2] donde el primero de ellos será la coordenada 'y' de la arista horizontal, 
        el segundo elemento será la coordenada 'x' del primer vértice de la arista que ha sido recorrido (es decir, el que se encuentra antes en la lista de puntos)
        y el tercero será la coordenada 'x' del segundo vértice de la arista que ha sido recorrido.
        
        Cada arista vertical será una lista de 3 números [x, y_1, y_2] donde el primero de ellos será la coordenada 'x' de la arista vertical, 
        el segundo elemento será la coordenada 'y' del primer vértice de la arista que ha sido recorrido (es decir, el que se encuentra antes en la lista de puntos)
        y el tercero será la coordenada 'y' del segundo vértice de la arista que ha sido recorrido.

        Estas aristas se utilizarán para, a la hora de calcular la presentación superior del nudo, tener en cuenta el sentido de los cruces de los caminos v_i con las
        aristas superiores del nudo. 


        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            vector_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        aristas_i=[]
        aristas_horizontales_i=[]
        aristas_verticales_i=[]
        aristas=[]
        valor_salir=-1   #Este valor servirá para en caso de que tomemos las últimas aristas del nudo para meterlas como dentro del primer conjunto posterioremente no analizarlas
        if (self.__numeros[0]>0):
            superior=False
            
        else:
            superior=True
            
        if (superior==True):
            if 0 not in vector_cambio:
                valor_salir=vector_cambio[len(vector_cambio)-1]
                indice_partida=vector_cambio[len(vector_cambio)-1]
                punto_inicial=puntos[indice_partida]
                if (puntos[indice_partida-1][0] != puntos[indice_partida][0]):
                    horizontal=True
                else:
                    horizontal=False

                for i in range(len(puntos) - indice_partida-1):
                    if horizontal:
                        if (puntos[indice_partida+i+1][1] != punto_inicial[1]):
                            horizontal=False
                            
                            
                            arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[indice_partida+i][0]]

                            punto_inicial=puntos[indice_partida+i]
                            
                            aristas_horizontales_i.append(arista_h_aux)
                    
                    else:
                        if (puntos[indice_partida+i+1][0] != punto_inicial[0]):
                            horizontal=True
                            
                            arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[indice_partida+i][1]]
        
                            punto_inicial=puntos[indice_partida+i]
                            aristas_verticales_i.append(arista_v_aux)

                arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[len(puntos)-1][1]]
                aristas_verticales_i.append(arista_v_aux)

            punto_inicial=puntos[0]
            horizontal=True
        
        condicion_salir=False
        for x in range(len(puntos) - 1):
            if (condicion_salir==False):
                if (superior==True):
                    if horizontal:
                        if (puntos[x+1][1] != punto_inicial[1]):
                            horizontal=False
                            
                            
                            arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]
                            

                            punto_inicial=puntos[x]
                            
                            aristas_horizontales_i.append(arista_h_aux)
                    
                    else:
                        if (puntos[x+1][0] != punto_inicial[0]):
                            horizontal=True
                            
                            
                            arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                            
                            punto_inicial=puntos[x]
                            aristas_verticales_i.append(arista_v_aux)

                if (x in vector_cambio and x!=0):
                    if (superior==True): #Si estabamos con los arcos inferiores hay que meter el último punto 
                        if horizontal:
                            if (punto_inicial[0] != puntos[x][0]): #Para ver que no es el mismo punto 

                                
                                arista_h_aux=[punto_inicial[1], punto_inicial[0], puntos[x][0]]

                                aristas_horizontales_i.append(arista_h_aux)
                        else:
                            if(punto_inicial[1] != puntos[x][1]):
                                arista_v_aux=[punto_inicial[0], punto_inicial[1], puntos[x][1]]
                                
                                aristas_verticales_i.append(arista_v_aux)

                        aristas_i.append(aristas_horizontales_i)
                        aristas_i.append(aristas_verticales_i)
                        aristas.append(aristas_i)

                        aristas_i=[]
                        aristas_horizontales_i=[]
                        aristas_verticales_i=[]
                        superior=False
                    else:
                        if (puntos[x+2][1] != puntos[x][1]):
                            horizontal=False
                        else:
                            horizontal=True
                        
                        punto_inicial=puntos[x]
                        superior=True

                    if (x==valor_salir):
                        condicion_salir=True
        
        if (condicion_salir==False):
            if (superior==True):
                
                arista_v_aux=[-0.5, punto_inicial[1], 0]
                

                aristas_verticales_i.append(arista_v_aux)
                aristas_i.append(aristas_horizontales_i)
                aristas_i.append(aristas_verticales_i)
                aristas.append(aristas_i)
        
        return aristas

    def __coincidir_puntos_y_arista(self, coordenada_punto1, coordenada_punto2, arista):
        '''
        Esta función comprueba si una arista horizontal [vertical] almacenada en el parámetro 'arista' contiene un punto con coordenada 'x' ['y'] que esté contenido entre los valores coordenada_punto1 y coordenada_punto2.

        Args:
            coordenada_punto1: Coordenada 'x' ['y'] de valor menor de una arista horizontal [vertical] de un arco superior o inferior.
            coordenada_punto2: Coordenada 'x' ['y'] de valor mayor de una arista horizontal [vertical] de un arco superior o inferior.
            arista: Arista horizontal o vertical.
        '''

        if (arista[1] < (coordenada_punto2) and arista[2] > (coordenada_punto1)):
            return True
        else: 
            return False

    def __arista_y_puntos_no_coinciden(self, x, punto_1, punto_2):
        '''
        Comprueba si una arista vertical inferior (x), es consecutiva a la arista horizontal dada por los puntos punto_1 y punto_2. Para que sea consecutiva, 
        uno de los puntos tiene que tener la misma coordenada 'x' que dicha arista vertical y la coordenada 'y' de uno de los dos puntos de la arista vertical inferior 
        (x[1] o x[2]) debe coincidir con la coordenada 'y' de dicho punto.

        Este método únicamente es utilizado por el método __calcular_bordes_centrales.

        Args:
            x: Arista vertical inferior en formato: [x, y_1, y_2] donde el primero de ellos será la coordenada 'x' de la arista vertical inferior, 
        el segundo elemento será la coordenada 'y' del vértice de la arista con menor valor y el tercero será la coordenada 'y' del vértice de la arista 
        con mayor valor.
            punto_1: Primer punto de la arista horizontal que estamos analizando.
            punto_2: Segundo punto de la arista horizontal que estamos analizando. 
        '''

        no_coinciden=True
        if (x[0]==punto_1[0]):
            if (x[1]==punto_1[1] or x[2]==punto_1[1]):
                no_coinciden=False
        if (x[0]==punto_2[0]):
            if (x[1]==punto_2[1] or x[2]==punto_2[1]):
                no_coinciden=False
        return no_coinciden
    
    def __obtener_borde_izquierdo(self, punto, aristas_verticales):
        '''
        Devuelve el borde izquierdo (espacio por la izquierda) que se dejará entre el punto inicial puntos[0] y el camino u_1 o v_1

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            aristas_verticales: Segundo elemento de la lista que devuelve la función obtener_aristas.
        '''

        valor_mas_cercano=0.5
        for x in aristas_verticales:
            if ((x[0] < punto[0]) and ((punto[0]-x[0]) < valor_mas_cercano)):
                if ((x[2]> (punto[1]-0.2)) and (x[1] < (punto[1]+0.2))):
                    valor_mas_cercano=(punto[0]-x[0])

        return (valor_mas_cercano*0.4)

    def __calcular_bordes_centrales (self, punto_inicial, puntos, i, aristas_horizontales, aristas_verticales_inferiores_o_superiores):
        '''
        Dada una arista horizontal (determinada por los puntos "punto_inicial" y "puntos[i]") devuelve los espacios que se van a dejar por arriba y por abajo (borde_superior y borde inferior) entre 
        dicha arista horizontal y el camino v_i o u_i correspondiente. 

        Se devolverá el espacio mínimo entre el espacio superior y el inferior, por lo que el borde superior y el borde inferior serán el mismo en este caso. 

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            punto_inicial: Punto de origen de la arista horizontal de la cual queremos calcular los bordes centrales.
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
            i: índice de la lista de puntos, que indica la posición dentro de dicha lista del punto final de la arista.
            aristas_horizontales: Lista de las aristas horizontales del nudo, siendo el primer elemento de la lista obtenida de la función obtener_aristas
            aristas_verticales_inferiores: Lista de las aristas verticales inferiores o superiores del nudo en función de si estamos calculando los bordes y giros de un camino v_i o u_i, siendo el segundo elemento de la 
        lista obtenida de la función __obtener_aristas_inferiores

        '''
        
        valor_mas_cercano=0.5
        for x in aristas_horizontales:          #Se comprueba la distancia vertical con las otras aristas horizontales 
            if (punto_inicial[1]!= x[0] and abs(punto_inicial[1]-x[0])< valor_mas_cercano):
                if (punto_inicial[0] < puntos[i][0]): #Esta condición es para pasarle a la siguiente función los valores ordenados de menor a mayor
                    if (self.__coincidir_puntos_y_arista(punto_inicial[0], puntos[i][0], x)):
                        valor_mas_cercano=abs(punto_inicial[1]-x[0])
                else:
                    if (self.__coincidir_puntos_y_arista(puntos[i][0], punto_inicial[0], x)):
                        valor_mas_cercano=abs(punto_inicial[1]-x[0])
        

        
        for x in aristas_verticales_inferiores_o_superiores:             #Se comprueba la distancia vertical con el comienzo o fin de las aristas verticales inferiores ya que recordemos que los caminos v_i [u_i] no se pueden intersectar
            if self.__arista_y_puntos_no_coinciden(x, punto_inicial, puntos[i]):  #Esta función sirve para no contemplar las aristas verticales que estén unidas a la arista horizontal que estamos analizando 
                valorr=0.1
                
                if (punto_inicial[0] < puntos[i][0]):
                    if ((punto_inicial[0] - valorr) < x[0] and x[0] < (puntos[i][0] + valorr)):
                        
                        if (abs(x[1] - punto_inicial[1]) < valor_mas_cercano):
                            valor_mas_cercano=abs(x[1] - punto_inicial[1])
                        if ( abs(x[2] - punto_inicial[1]) < valor_mas_cercano ):
                            valor_mas_cercano= abs(x[2] - punto_inicial[1])
                else:
                    
                    if (((puntos[i][0]-valorr) < x[0]) and x[0] <(punto_inicial[0] + valorr)):
                        
                        if (abs(x[1] - punto_inicial[1]) < valor_mas_cercano):
                            valor_mas_cercano=abs(x[1] - punto_inicial[1])
                        if ( abs(x[2] - punto_inicial[1]) < valor_mas_cercano ):
                            valor_mas_cercano= abs(x[2] - punto_inicial[1])
                    
        return (valor_mas_cercano*0.4)

    def __calcular_bordes_laterales(self, punto_inicial, puntos, i, aristas_verticales, aristas_horizontales_inferiores_o_superiores):
        
        '''
        Dada una arista vertical (determinada por los puntos "punto_inicial" y "puntos[i]") devuelve los espacios que se van a dejar por la izquierda y por la derecha (borde_izquierda y borde_derecha) entre 
        dicha arista vertical y el correspondiente camino v_i o u_i correspondiente. 

        Se devolverá el espacio mínimo entre el espacio izquierdo y el derecho, por lo que el borde izquierdo y el borde derecho serán el mismo en este caso. 

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            punto_inicial: Punto de origen de la arista vertical de la cual queremos calcular los bordes centrales.
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
            i: índice de la lista de puntos, que indica la posición dentro de dicha lista del punto final de la arista.
            aristas_verticales: Lista de las aristas verticales del nudo, siendo el segundo elemento de la lista obtenida de la función obtener_aristas
            aristas_horizontales_inferiores: Lista de las aristas horizontales inferiores o superiores del nudo en función de si estamos calculando los bordes y giros de un camino v_i o u_i, siendo el primer elemento de la lista obtenida de la función __obtener_aristas_inferiores

        '''

        valor_mas_cercano=0.5
        for x in aristas_verticales:                #Se comprueba la distancia horizontal con otras aristas verticales 
            if ((punto_inicial[0]!= x[0]) and abs(punto_inicial[0]- x[0])< valor_mas_cercano):
                if (punto_inicial[1] < puntos[i][1]): #Esta condición es para pasarle a la siguiente función los valores ordenados de menor a mayor
                    if (self.__coincidir_puntos_y_arista(punto_inicial[1], puntos[i][1], x)):
                        valor_mas_cercano=abs(punto_inicial[0]- x[0])
                else:
                    if (self.__coincidir_puntos_y_arista(puntos[i][1], punto_inicial[1],  x)):
                        valor_mas_cercano=abs(punto_inicial[0]- x[0])
        
        for x in aristas_horizontales_inferiores_o_superiores:       #Se comprueba la distancia horizontal con el comienzo o fin de las aristas horizontales inferiores ya que recordemos que los caminos v_i [u_i] no se pueden intersectar
            if (punto_inicial[1] < puntos[i][1]):
                if (punto_inicial[1] < x[0] and x[0] < puntos[i][1]):
                    if (abs(x[1]- punto_inicial[0]) < valor_mas_cercano):
                        valor_mas_cercano=abs(x[1]- punto_inicial[0])
                    if (abs(x[2]- punto_inicial[0]) < valor_mas_cercano):
                        valor_mas_cercano=abs(x[2]- punto_inicial[0])
            else:
                if ( puntos[i][1] < x[0] and x[0] < punto_inicial[1]):
                    if (abs(x[1]- punto_inicial[0]) < valor_mas_cercano):
                        valor_mas_cercano=abs(x[1]- punto_inicial[0])
                    if (abs(x[2]- punto_inicial[0]) < valor_mas_cercano):
                        valor_mas_cercano=abs(x[2]- punto_inicial[0])

        return (valor_mas_cercano*0.4)

    def __limite_aristas_horizontales_borde_superior(self, punto, aristas_horizontales):
        '''
        Función que, dado el punto inicial de un arco superior o inferior y ser la primera arista de dicho arco una arista vertical que avanza de arriba a abajo, devuelve el borde superior.
        Igual pasaría si fuera el último punto de un arco superior o inferior y ser la ultima arista de dicho arco una arista vertical que avanza de abajo a arriba, devuelve el borde superior.

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            punto: Punto del que queremos calcular el borde_superior.
            aristas_horizontales: Primer elemento de la lista que devuelve la función obtener_aristas. 
        '''

        limite=0.5
        for x in aristas_horizontales:
            if (x[0] > punto[1] and (x[0]- punto[1])< limite):
                if ((x[1]-0.1) < punto[0] and (x[2]+0.1) > punto[0] ):
                    limite=(x[0]- punto[1])
        return (limite*0.4)
    
    def __limite_aristas_horizontales_borde_inferior(self,punto, aristas_horizontales):
        '''
        Función que, dado el punto inicial de un arco superior o inferior y ser la primera arista de dicho arco una arista vertical que avanza de abajo a arriba, devuelve el borde inferior.
        Igual pasaría si fuera el último punto de un arco superior o inferior y ser la ultima arista de dicho arco una arista vertical que avanza de arriba a abajo, devuelve el borde inferior.

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            punto: Punto del que queremos calcular el borde inferior.
            aristas_horizontales: Primer elemento de la lista que devuelve la función obtener_aristas. 
        '''

        limite=0.5
        for x in aristas_horizontales:
            if (x[0] < punto[1] and (punto[1]- x[0] < limite)):
                if ((x[1]-0.1) < punto[0] and (x[2]+0.1) > punto[0] ):
                    limite=(punto[1]-x[0])
        return (limite*0.4)

    def __limite_aristas_verticales_borde_derecha(self, punto, aristas_verticales):
        '''
        Función que, dado el punto inicial de un arco superior o inferior y ser la primera arista de dicho arco una arista horizontal que avanza de derecha a izquierda, devuelve el borde derecho.
        Igual pasaría si fuera el último punto de un arco superior o inferior y ser la ultima arista de dicho arco una arista horizontal que avanza de izquierda a derecha, devuelve el borde derecho.

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            punto: Punto del que queremos calcular el borde derecho.
            aristas_verticales: Segundo elemento de la lista que devuelve la función obtener_aristas. 
        '''
        
        limite=0.5
        for x in aristas_verticales:
            if (x[0] > punto[0] and (x[0] - punto[0])<limite):
                if ((x[1] - 0.1) < punto[1] and (x[2] + 0.1) < punto[1]):
                    limite=(x[0]- punto[0])
        
        return (limite*0.4)
    
    def __limite_aristas_verticales_borde_izquierda(self, punto, aristas_verticales):
        '''
        Función que, dado el punto inicial de un arco superior o inferior y ser la primera arista de dicho arco una arista horizontal que avanza de izquierda a derecha, devuelve el borde izquierdo.
        Igual pasaría si fuera el último punto de un arco superior o inferior y ser la última arista de dicho arco una arista horizontal que avanza de derecha a izquierda, devuelve el borde izquierdo.

        Este método únicamente es utilizado por el método __obtener_bordes_y_giros_vi_ui.

        Args:
            punto: Punto del que queremos calcular el borde izquierdo.
            aristas_verticales: Segundo elemento de la lista que devuelve la función obtener_aristas. 
        '''
        
        limite=0.5
        for x in aristas_verticales:
            if(x[0] < punto[0] and (punto[0]- x[0])< limite):
                if ((x[1] - 0.1) < punto[1] and  punto[1]<(x[2] + 0.1) ):
                    limite=(punto[0] - x[0])
        
        return (limite*0.4)
    
    def __obtener_bordes_y_giros_vi_ui(self, puntos, aristas, valor_inicial, valor_final, aristas_inferiores_o_superiores):
        '''
        Método que, dados los índices de la lista 'puntos', valor_inicial y valor final, que denotan el punto inicial (puntos[valor_inicial]) y el punto_final (puntos[valor_final]) de un arco inferior o superior, 
        calcula los bordes que tendrá que tener el camino v_i (asociado a un arco inferior) o el camino u_i (asociado a un arco superior), con respecto a dicho arco superior en todas las aristas de dicho arco superior o inferior. 
        Si dicho arco superior o inferior tiene n aristas, la lista de bordes tendrá n elementos, siendo cada uno de ellos una lista del tipo [borde_izquierda, borde_derecha, borde_superior, borde_inferior].
        
        También se calculará una lista de giros que indicará los giros que se realizan para pasar de una arista de dicho arco a la siguiente. Por ejemplo si estamos en una arista horizontal yendo de izquierda a derecha, solo tendremos las 
        opciones :
            "ab_d", que significa 'abajo derecha' que indicará que la siguiente arista será una arista vertical que irá desde arriba hacia abajo, 
            "ar_d": que significa 'arriba derecha' que indicará que la siguiente arista será una arista vertical que irá desde abajo hacia arriba.
        Si en la arista horizontal fuéramos de izquierda a derecha las opciones serían "ab_i" y "ar_i".
        Si un determinado arco tiene n aristas, tendremos en la lista de giros n-1 elementos.

        Se devuelve una lista de dos elementos, siendo el primero de ellos la lista de bordes, y el segundo de ellos la lista de giros. 

        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
            aristas: Lista de aristas obtenida de la función calcular_aristas. Se utilizan para calcular los bordes que tendrán los caminos v_i y u_i con respcto al correspondiente arco inferior y superior respectivamente.
            valor_inicial: Índice de la lista puntos del punto inicial del arco superior o inferior que estamos analizando. 
            valor_final: Índice de la lista puntos del punto final del arco superior o inferior que estamos analizando.
            aristas_inferiores_o_superiores: Lista de aristas obtenida de la función __obtener_aristas_inferiores u __obtener_aristas_superiores en función de si estamos calculando los bordes y giros de un camino v_i o u_i, que servirá para calcular los bordes
        que tendrán los caminos v_i y u_i con respcto al correspondiente arco inferior y superior respectivamente.
        '''

        borde_arriba=0
        borde_abajo=0
        borde_izquierda=0
        borde_derecha=0

        bordes=[]
        if (valor_inicial==0):
            borde_izquierda=self.__obtener_borde_izquierdo(puntos[0], aristas[1])
            horizontal=True
        
        else:   #En otro caso tenemos que ver si partimos de una zona horizontal o vertical 
            punto_anterior=puntos[valor_inicial-1]
            if (punto_anterior[0] != puntos[valor_inicial][0]):
                horizontal=True
                if  (punto_anterior[0] > puntos[valor_inicial][0]):  #Vamos hacia la izquierda, por lo tanto calculamos el borde derecho
            
                    limite=self.__limite_aristas_verticales_borde_derecha(puntos[valor_inicial], aristas_inferiores_o_superiores[1])

                    if ((punto_anterior[0] - puntos[valor_inicial][0])/2 < limite):
                        limite=(punto_anterior[0] - puntos[valor_inicial][0])/2
                    
                    borde_derecha=limite
                
                else:                                                #Vamos hacia la derecha, por lo tanto calculamos el borde izquierdo
                    
                    limite=self.__limite_aristas_verticales_borde_izquierda(puntos[valor_inicial], aristas_inferiores_o_superiores[1])

                    if (( puntos[valor_inicial][0] - punto_anterior[0])/2 < limite):
                        limite=(puntos[valor_inicial][0] - punto_anterior[0])/2
                    
                    borde_izquierda=limite
                
            else:
                horizontal=False
                if (punto_anterior[1] > puntos[valor_inicial][1]):      #Vamos hacia abajo por lo que hay que calcular el borde superior
                    
                    limite=self.__limite_aristas_horizontales_borde_superior(puntos[valor_inicial], aristas_inferiores_o_superiores[0])

                    if ((punto_anterior[1] - puntos[valor_inicial][1])/2 < limite):
                        limite=(punto_anterior[1] - puntos[valor_inicial][1])/2
                    
                    borde_arriba=limite
                
                else:                                                   #Vamos hacia arriba por lo que hay que calcular el borde inferior 
                    
                    limite= self.__limite_aristas_horizontales_borde_inferior(puntos[valor_inicial], aristas_inferiores_o_superiores[0])

                    if (( puntos[valor_inicial][1] - punto_anterior[1])/2 < limite):
                        limite=(puntos[valor_inicial][1] - punto_anterior[1])/2
                    
                    borde_abajo=limite
    
        punto_inicial=puntos[valor_inicial]
        contador=0          #Este contador servirá para el contador de bordes 
        giros=[]
        for i in range(valor_final - valor_inicial):
            if horizontal:
                if (punto_inicial[1] != puntos[valor_inicial + i +1][1]):
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_d") or (giros[len(giros)-1]== "ar_d") ):
                            borde_izquierda=bordes[len(bordes)-1][0]
                        else:
                            borde_derecha=bordes[len(bordes)-1][1]
                    
                    bordes_centrales=self.__calcular_bordes_centrales(punto_inicial, puntos, valor_inicial+i, aristas[0], aristas_inferiores_o_superiores[1])
                    bordes_aux=[borde_izquierda, borde_derecha, bordes_centrales, bordes_centrales]
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ab_d") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                            bordes[len(bordes)-1][3]=bordes_centrales
                        else:
                            bordes[len(bordes)-1][2]=bordes_centrales

                    bordes.append(bordes_aux)
                    if (punto_inicial[1] > puntos[valor_inicial + i +1][1]):
                        if (borde_derecha==0):
                            giros.append("ab_d") #Abajo derecha
                        else:
                            giros.append("ab_i") #Abajo izquierda
                    else:
                        if (borde_derecha==0):
                            giros.append("ar_d") #Arriba derecha
                        else:
                            giros.append("ar_i") #Arriba izquierda

                    punto_inicial=puntos[valor_inicial+i]
                    borde_izquierda=0
                    borde_derecha=0
                    borde_arriba=0
                    borde_abajo=0
                    contador+=1
                    horizontal=False
            else:
                if (punto_inicial[0]!= puntos[valor_inicial +i +1][0]):
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ab_d") ):    #Si el giro anterior es para abajo
                            borde_arriba=bordes[len(bordes)-1][2]   #Es decir el borde de arriba del nuevo será el borde de arriba del anterior
                        else:                                       #Si el giro es hacia arriba
                            borde_abajo=bordes[len(bordes)-1][3]    #El borde de abajo del nuevo será el borde de abajo del anterior

                    bordes_laterales=self.__calcular_bordes_laterales(punto_inicial, puntos, valor_inicial+i, aristas[1], aristas_inferiores_o_superiores[0])
                    bordes_aux=[bordes_laterales, bordes_laterales, borde_arriba, borde_abajo]
                    #Ahora modificamos el valor que estaba a 0 en la lista de bordes anterior
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ar_i") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                            bordes[len(bordes)-1][0]=bordes_laterales
                        else:
                            bordes[len(bordes)-1][1]=bordes_laterales

                    bordes.append(bordes_aux)

                    if (punto_inicial[0] > puntos[valor_inicial + i +1][0] ): #Esto quiere decir que giramos para la izquierda
                        if (borde_arriba==0): #Esto quiere decir que estamos yendo hacia arriba
                            giros.append("ar_i")
                        else:
                            giros.append("ab_i")
                    else:   #Giramos para la derecha
                        if (borde_arriba==0):
                            giros.append("ar_d")
                        else:
                            giros.append("ab_d")

                    punto_inicial=puntos[valor_inicial+i]
                    borde_izquierda=0
                    borde_derecha=0
                    borde_arriba=0
                    borde_abajo=0
                    contador+=1
                    horizontal=True

        if (valor_final!= (len(puntos)-1)):
            punto_siguiente=puntos[valor_final+2]
        else:
            if (puntos[valor_final-1][1] < 0): #Es decir si venimos en dirección vertical ascendente
                punto_siguiente=[puntos[0][0], puntos[0][1]+0.5]
            else:
                punto_siguiente=[puntos[0][0], puntos[0][1]-0.5]

        if horizontal: 
            
            if (contador!=0):
                if ( (giros[len(giros)-1]== "ab_d") or (giros[len(giros)-1]== "ar_d") ):
                    borde_izquierda=bordes[len(bordes)-1][0]
                else:
                    borde_derecha=bordes[len(bordes)-1][1]

            if  (punto_siguiente[0] > puntos[valor_final][0]):  #Vamos hacia la derecha, por lo tanto calculamos el borde derecho porque el izquierdo ya lo teníamos calculado  y el borde derecho de la siguiente forma 
                #borde_derecha=puntos[valor_final][0]
                limite=self.__limite_aristas_verticales_borde_derecha(puntos[valor_final], aristas_inferiores_o_superiores[1])

                if ((punto_siguiente[0] - puntos[valor_final][0])/2 < limite):
                    limite=(punto_siguiente[0] - puntos[valor_final][0])/2
                
                borde_derecha=limite
                
                
            
            else:                                                #Vamos hacia la izquierda, por lo tanto calculamos el borde derecho
                #borde_izquierda=puntos[valor_final][0]
                limite=self.__limite_aristas_verticales_borde_izquierda(puntos[valor_final], aristas_inferiores_o_superiores[1])

                if (( puntos[valor_final][0] - punto_siguiente[0])/2 < limite):
                    limite=(puntos[valor_final][0] - punto_siguiente[0])/2
                
                borde_izquierda=limite

            bordes_centrales=self.__calcular_bordes_centrales(punto_inicial, puntos, valor_final, aristas[0], aristas_inferiores_o_superiores[1])
            bordes_aux=[borde_izquierda, borde_derecha, bordes_centrales, bordes_centrales]
            if (contador!=0):
                if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ab_d") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                    bordes[len(bordes)-1][3]=bordes_centrales
                else:
                    bordes[len(bordes)-1][2]=bordes_centrales
            bordes.append(bordes_aux)      
            

        else:
            if (contador!=0):
                if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ab_d") ):    
                    borde_arriba=bordes[len(bordes)-1][2]   
                else:                                       
                    borde_abajo=bordes[len(bordes)-1][3] 

            if (punto_siguiente[1] > puntos[valor_final][1]):      #Vamos hacia abajo por lo que hay que calcular el borde superior
                
                limite=self.__limite_aristas_horizontales_borde_superior(puntos[valor_final], aristas_inferiores_o_superiores[0])

                if ((punto_siguiente[1] - puntos[valor_final][1])/2 < limite):
                    limite=(punto_siguiente[1] - puntos[valor_final][1])/2
                
                borde_arriba=limite
            
            else:
                
                limite= self.__limite_aristas_horizontales_borde_inferior(puntos[valor_final], aristas_inferiores_o_superiores[0])
                
                if (( puntos[valor_final][1] - punto_siguiente[1])/2 < limite):
                    limite=((puntos[valor_final][1] - punto_siguiente[1])/2)
                
                borde_abajo=limite

            bordes_laterales=self.__calcular_bordes_laterales(punto_inicial, puntos, valor_inicial+i, aristas[1], aristas_inferiores_o_superiores[0])
            bordes_aux=[bordes_laterales, bordes_laterales, borde_arriba, borde_abajo]
            if (contador!=0):
                if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ar_i") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                    bordes[len(bordes)-1][0]=bordes_laterales
                else:
                    bordes[len(bordes)-1][1]=bordes_laterales
            bordes.append(bordes_aux)

        bordes_y_giros=[bordes, giros]
        return bordes_y_giros    

    def __obtener_puntos_vi_ui(self, bordes_y_giros, puntos, valor_inicial, valor_final):
        '''
        Función que calcula para cada arco superior o inferior, determinado por los puntos comprendidos entre puntos[valor_inicial] y puntos[valor_final], los caminos v_i y u_i que rodean a dichos arcos inferiores y superiores respectivamente.
        Para ello se requiere de los bordes y los giros calculados mediante la función __obtener_bordes_y_giros. 

        Esta función devuelve una secuencia de puntos que serán los vértices de las aristas del camino poligonal v_i o u_i.

        Args:
            bordes_y_giros: Lista de dos elementos, siendo el primero de ellos los bordes y el segundo los giros, obtenida de la función __obtener_bordes_y_giros.
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
            valor_inicial: Índice de la lista puntos del punto inicial del arco superior o inferior que estamos analizando. 
            valor_final: Índice de la lista puntos del punto final del arco superior o inferior que estamos analizando.

        '''

        
        if (valor_inicial==0):
            horizontal=True
        
        else:   #En otro caso tenemos que ver si partimos de una zona horizontal o vertical 
            punto_anterior=puntos[valor_inicial-1]
            if (punto_anterior[0] != puntos[valor_inicial][0]):
                horizontal=True
            else:
                horizontal=False
        
        bordes=bordes_y_giros[0]
        giros=bordes_y_giros[1]
        puntos_vi=[]
        if not giros:       #Esto ocurre en el caso que el arco superior o inferior, este comprendido únicamente por una aristas vertical u horizontal.

            if (puntos[valor_inicial][0] < puntos[valor_final][0]):
                punto_mayor=puntos[valor_final]
                punto_menor=puntos[valor_inicial]
            else:
                punto_mayor=puntos[valor_inicial]
                punto_menor=puntos[valor_final]
            
            punto_aux=[punto_menor[0]-bordes[0][0], punto_menor[1]+bordes[0][2]]  #Esquina superior izquierda
            puntos_vi.append(punto_aux)
            punto_aux=[punto_menor[0]-bordes[0][0], punto_menor[1]-bordes[0][3]]  #Esquina inferior izquierda
            puntos_vi.append(punto_aux)
            punto_aux=[punto_mayor[0]+bordes[0][1], punto_mayor[1]-bordes[0][3]]  #Esquina inferior derecha
            puntos_vi.append(punto_aux)
            punto_aux=[punto_mayor[0]+bordes[0][1], punto_mayor[1]+bordes[0][2]]  #Esquina inferior derecha
            puntos_vi.append(punto_aux)
        else:
            contador=0
            punto_inicial=puntos[valor_inicial]
            
            for i in range(valor_final - valor_inicial):
                if (contador==0):       #Caso en el que estemos calculando los puntos de la primera arista del arco superior o inferior
                    if horizontal:              #Si la arista que etsamos recorriendo es horizontal
                        if (punto_inicial[1] != puntos[valor_inicial + i +1][1]):           #Si llegamos al vértice de dicha arista horizontal con una vertical 
                            punto_final=puntos[valor_inicial+i]

                            if ( giros[contador]=="ar_d" or giros[contador]=="ab_d"):
                                if (giros[contador]=="ar_d"):
                                    signo=1
                                else:
                                    signo=-1
                                punto_aux=[punto_final[0]- signo*bordes[contador][1], punto_final[1]+bordes[contador][2]] #Punto superior derecho
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0]-bordes[contador][0], punto_inicial[1]+bordes[contador][2]]    #Punto superior izquierdo 
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0]-bordes[contador][0], punto_inicial[1]-bordes[contador][3]]      #Punto inferior izquierdo 
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_final[0]+ signo*bordes[contador][1], punto_final[1]-bordes[contador][3]]          #Punto inferior derecho
                                puntos_vi.append(punto_aux)

                            else:
                                if (giros[contador]=="ab_i"):
                                    signo=1
                                else: 
                                    signo=-1
                                punto_aux=[punto_final[0] + signo*bordes[contador][0], punto_final[1]- bordes[contador][3]]   #Punto inferior izquierdo 
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0] + bordes[contador][1], punto_inicial[1]- bordes[contador][3]] #Punto inferior derecho
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0] + bordes[contador][1], punto_inicial[1]+ bordes[contador][2]] #Punto superior derecho
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_final[0] - signo*bordes[contador][0], punto_final[1]+ bordes[contador][2]]  #Punto superior izquierdo 
                                puntos_vi.append(punto_aux)
                            horizontal=False
                            contador+=1
                            punto_inicial=puntos[valor_inicial+i]
                    else:                       #Si la arista que estamos recorriendo es vertical 
                        if (punto_inicial[0] != puntos[valor_inicial + i +1][0]):       #Si llegamos al vértice de dicha arista vertical con una horizontal
                            punto_final=puntos[valor_inicial+i]
                            
                            if (giros[contador]=="ab_d" or giros[contador]=="ab_i"):
                                if (giros[contador]=="ab_d"):
                                    signo= 1
                                else:
                                    signo= -1

                                punto_aux=[punto_final[0]+ bordes[contador][1], punto_final[1]+ signo*bordes[contador][3]] #Punto inferior derecho
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0]+bordes[contador][1], punto_inicial[1]+ bordes[contador][2]] #Punto superior derecho
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0] - bordes[contador][0], punto_inicial[1] + bordes [contador][2]] #Punto superior izquierdo
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_final[0] - bordes[contador][0], punto_final[1] - signo*bordes[contador][3]]    #Punto inferior izquierdo
                                puntos_vi.append(punto_aux)
                            else:
                                if (giros[contador]=="ar_d"):
                                    signo=1
                                else:
                                    signo=-1

                                punto_aux=[punto_final[0] - bordes[contador][0], punto_final[1] + signo*bordes[contador][2]] #Punto superior izquierdo
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0] -bordes[contador][0], punto_inicial[1] - bordes[contador][3] ] #Punto inferior izquierdo
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_inicial[0] + bordes[contador][1], punto_inicial[1] - bordes[contador][3]] #Punto inferior derecho
                                puntos_vi.append(punto_aux)
                                punto_aux=[punto_final[0] + bordes[contador][1], punto_final[1] - signo*bordes[contador][2]] #Punto superior derecho 
                                puntos_vi.append(punto_aux)
                            contador+=1
                            horizontal=True
                            punto_inicial=puntos[valor_inicial+i]
                                
                else:                   #Caso en el que no estemos calculando los puntos asociados a la primera arista del arco superior o inferior
                    if horizontal:
                        if (punto_inicial[1] != puntos[valor_inicial + i +1][1]):
                            punto_final=puntos[valor_inicial+i]
                            if ( giros[contador]=="ar_d" or giros[contador]=="ab_d"):
                                if (giros[contador]=="ar_d"):
                                    signo=1
                                else:
                                    signo=-1
                                
                                punto_aux=[punto_final[0]+ signo*bordes[contador][1], punto_final[1] - bordes[contador][3]]
                                if (punto_aux[1]==puntos_vi[0][1]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)
                                
                                punto_aux=[punto_final[0] - signo*bordes[contador][1], punto_final[1]+ bordes[contador][2]]
                                if (punto_aux[1]==puntos_vi[0][1]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)

                            else:
                                if (giros[contador]=="ar_i"):
                                    signo=1
                                else:
                                    signo=-1

                                punto_aux=[punto_final[0] + signo*bordes[contador][0], punto_final[1]+ bordes[contador][2]]
                                if (punto_aux[1]==puntos_vi[0][1]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)
                                
                                punto_aux=[punto_final[0] - signo*bordes[contador][0], punto_final[1]- bordes[contador][3]]
                                if (punto_aux[1]==puntos_vi[0][1]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)
                            contador+=1
                            horizontal=False
                            punto_inicial=puntos[valor_inicial+i]

                    else:
                        if (punto_inicial[0] != puntos[valor_inicial + i +1][0]):
                            punto_final=puntos[valor_inicial+i]
                            if ( giros[contador]=="ar_d" or giros[contador]=="ar_i"):
                                if (giros[contador]=="ar_d"):
                                    signo=1
                                else:
                                    signo=-1
                            
                                punto_aux=[punto_final[0]-bordes[contador][0], punto_final[1] + signo*bordes[contador][2]]

                                if (punto_aux[0]==puntos_vi[0][0]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)
                                
                                punto_aux=[punto_final[0]+ bordes[contador][1], punto_final[1] - signo*bordes[contador][2]]
                                if (punto_aux[0]==puntos_vi[0][0]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)

                            else: 
                                if (giros[contador]=="ab_d"):
                                    signo=1
                                else:
                                    signo=-1
                                
                                punto_aux=[punto_final[0]-bordes[contador][0], punto_final[1]- signo*bordes[contador][3]]
                                if (punto_aux[0]==puntos_vi[0][0]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)
                                
                                punto_aux=[punto_final[0] + bordes[contador][1], punto_final[1]+signo*bordes[contador][3]]
                                if (punto_aux[0]==puntos_vi[0][0]):
                                    puntos_vi.insert(0, punto_aux)
                                else:
                                    puntos_vi.append(punto_aux)
                            contador+=1
                            horizontal=True
                            punto_inicial=puntos[valor_inicial+i]
            
            #Aquí vamos a analizar el caso en el que estemos hallando los puntos de la última arista 
            punto_final=puntos[valor_final]
            if horizontal:
                
                if (puntos[valor_final-1][0] > punto_final[0]): #Si estamos yendo para la izquierda (de derecha a izquierda)
                    punto_aux=[punto_final[0] - bordes[contador][0], punto_final[1]+ bordes[contador][2]]

                    if (punto_aux[1]==puntos_vi[0][1]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)

                    punto_aux=[punto_final[0] - bordes[contador][0], punto_final[1]- bordes[contador][3]]

                    if (punto_aux[1]==puntos_vi[0][1]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)

                else:                                           #Si estamos yendo para la derecha (de izquierda a derecha) 
                    
                    punto_aux=[punto_final[0] + bordes[contador][1], punto_final[1]+ bordes[contador][2]]

                    if (punto_aux[1]==puntos_vi[0][1]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)

                    punto_aux=[punto_final[0] + bordes[contador][1], punto_final[1]- bordes[contador][2]]
                    if (punto_aux[1]==puntos_vi[0][1]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)

            else:
                
                if (puntos[valor_final-1][1] > punto_final[1]): #Si estamos yendo para abajo (de arriba a abajo)
                    punto_aux=[punto_final[0]- bordes[contador][0], punto_final[1] - bordes[contador][3]]
                    if (punto_aux[0]==puntos_vi[0][0]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)
                    punto_aux=[punto_final[0] + bordes[contador][1], punto_final[1] - bordes[contador][3]]
                    if (punto_aux[0]==puntos_vi[0][0]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)
                
                else:       #Si estamos yendo hacia arriba (de abajo a arriba)
                    punto_aux=[punto_final[0] - bordes[contador][0], punto_final[1]+ bordes[contador][2]]
                    if (punto_aux[0]==puntos_vi[0][0]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)
                    
                    punto_aux=[punto_final[0]+ bordes[contador][1], punto_final[1]+ bordes[contador][2]]
                    if (punto_aux[0]==puntos_vi[0][0]):
                        puntos_vi.insert(0, punto_aux)
                    else:
                        puntos_vi.append(punto_aux)

        return puntos_vi               

    def obtener_caminos_vi (self, puntos, aristas, vector_cambio):
        '''
        Dados los puntos del nudo, y el vector de índices de la lista de puntos en los cuales se produce el cambio de un arco superior a uno inferior o viceversa, tras obtener los bordes y giros de cada camino v_i, llamamos a la función __obtener_puntos_vi_ui 
        para obtener los puntos de cada camino v_i y almacenamos dichos puntos en una lista.

        Dicha lista, será una lista con tantos elementos como arcos inferiores tenga el nudo donde en la posición j se almacenarán los puntos del camino v_j.

        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
            aristas: Lista de aristas obtenida de la función calcular_aristas. Se utilizan para calcular los bordes que tendrán los caminos v_i y u_i con respcto al correspondiente arco inferior y superior respectivamente.
            vector_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        aristas_inferiores=self.__obtener_aristas_inferiores(puntos, vector_cambio)
        contador=0
        puntos_vi=[]
        if 0 not in vector_cambio: #Si el 0 no pertenece al vector que nos indica cuando hay que cambiar de arcos superiores a inferiores, nos creamos una lista auxiliar para que nos sea más fácil su manejo.
            lista_puntos_auxiliares=[]
            indice_partida=vector_cambio[len(vector_cambio)-1]
            for i in range(len(puntos) - indice_partida+1):
                lista_puntos_auxiliares.append(puntos[indice_partida+i-1])
            
            for i in range(vector_cambio[0]+3):    #Le añado dos puntos más (por ello pongo +3) para poder comparar el punto final con el punto siguiente al final 
                lista_puntos_auxiliares.append(puntos[i])
            
            if (self.__numeros[0]>0):         #Es decir el caso en el que el arco que pase por encima del primer cruce sea un cruce inferior
                
                bordes_y_giros=self.__obtener_bordes_y_giros_vi_ui(lista_puntos_auxiliares, aristas, 1, len(lista_puntos_auxiliares)-3, aristas_inferiores)
                puntos_vi_aux=self.__obtener_puntos_vi_ui(bordes_y_giros, lista_puntos_auxiliares, 1,len(lista_puntos_auxiliares)-3)
                puntos_vi.append(puntos_vi_aux)
                modulo2=1
                contador+=1
            else:
                modulo2=0

        else:
            if (self.__numeros[0]>0):
                modulo2=0
            else:
                modulo2=1

        
        for i in range(len(vector_cambio)-1):
            if (i%2==modulo2):
                bordes_y_giros=self.__obtener_bordes_y_giros_vi_ui(puntos, aristas, vector_cambio[i], vector_cambio[i+1], aristas_inferiores)
                puntos_vi_aux=self.__obtener_puntos_vi_ui(bordes_y_giros, puntos, vector_cambio[i], vector_cambio[i+1])
                puntos_vi.append(puntos_vi_aux)
                contador+=1

        return puntos_vi

    def obtener_caminos_ui (self, puntos, aristas, vector_cambio):
        '''
        Dados los puntos del nudo, y el vector de índices de la lista de puntos en los cuales se produce el cambio de un arco superior a uno inferior o viceversa, tras obtener los bordes y giros de cada camino u_i, llamamos a la función __obtener_puntos_vi_ui 
        para obtener los puntos de cada camino u_i y almacenamos dichos puntos en una lista.

        Dicha lista, será una lista con tantos elementos como arcos superiores tenga el nudo donde en la posición j se almacenarán los puntos del camino u_j.

        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
            aristas: Lista de aristas obtenida de la función calcular_aristas. Se utilizan para calcular los bordes que tendrán los caminos v_i y u_i con respcto al correspondiente arco inferior y superior respectivamente.
            vector_cambio: Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        aristas_superiores=self.__obtener_aristas_superiores(puntos, vector_cambio)
        contador=0
        puntos_ui=[]
        if 0 not in vector_cambio:
            lista_puntos_auxiliares=[]
            indice_partida=vector_cambio[len(vector_cambio)-1]
            for i in range(len(puntos) - indice_partida+1):
                lista_puntos_auxiliares.append(puntos[indice_partida+i-1])
            
            for i in range(vector_cambio[0]+3):    #Le añado dos puntos más (por ello pongo +3) para poder comparar el punto final con el punto siguiente al final 
                lista_puntos_auxiliares.append(puntos[i])
            
            if (self.__numeros[0] < 0): #Es decir el caso en el que el arco que pase por encima del primer cruce sea un cruce superior
                bordes_y_giros=self.__obtener_bordes_y_giros_vi_ui(lista_puntos_auxiliares, aristas, 1, len(lista_puntos_auxiliares)-3, aristas_superiores)
                puntos_ui_aux=self.__obtener_puntos_vi_ui(bordes_y_giros, lista_puntos_auxiliares, 1,len(lista_puntos_auxiliares)-3)
                puntos_ui.append(puntos_ui_aux)
                superior=False
                modulo2=1
                contador+=1
            else:
                superior=True
                modulo2=0
        
        else:
            if (self.__numeros[0] < 0):
                superior=True
                modulo2=0
            else:
                superior=False
                modulo2=1
        
        
        for i in range(len(vector_cambio)-1):
            if (i%2==modulo2):
                
                bordes_y_giros=self.__obtener_bordes_y_giros_vi_ui(puntos, aristas, vector_cambio[i], vector_cambio[i+1], aristas_superiores)
                puntos_ui_aux=self.__obtener_puntos_vi_ui(bordes_y_giros, puntos, vector_cambio[i], vector_cambio[i+1])
                puntos_ui.append(puntos_ui_aux)
                contador+=1

        return puntos_ui    

    def __coincidir_arista_vertical_y_flecha(self, punto_1, punto_2, puntos):
        '''
        Esta función se utiliza a la hora de dibujar los caminos v_i y u_i en las funciones dibujar_caminos_vi y dibujar_caminos_ui respectivamente. Esta función determina, si en una arista horizontal, de un camino v_i o u_i "hay espacio" para dibujar una 
        flecha que indique el sentido del camino v_i o u_i. 
        
        En caso de que exista dicho espacio, se devolverá el valor de la coordenada x sobre la que se tiene que dibujar dicha flecha horizontal, siendo la variable que se devuelve la coordenada 'x' central de 
        dicha flecha. En caso contrario, se devolverá el valor -100. 

        Lo que se comprueba es que no haya ninguna arista vertical entre dichos puntos punto_1 y punto_2 que haga que la distancia entre dichos puntos y la arista vertical sea tan pequeña que no "quepa" la flecha.

        Args:
            punto_1: Punto inicial de la arista perteneciente a un camino v_i o u_i.
            punto_2: Punto final de la arista perteneciente a un camino v_i o u_i.
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
        '''
        aristas=self.obtener_aristas(puntos)
        aristas_verticales=aristas[1]
        punto_medio_x=(punto_1[0]+ punto_2[0])/2
        volverAIterar=True

        while(volverAIterar==True):
            parar=False
            for x in aristas_verticales:
                if (parar==False):
                    if (x[0] > (punto_medio_x - 0.07) and x[0] < (punto_medio_x + 0.07)): #Es decir si coinciden las coordenadas x de la arista vertical y la de la flecha
                        if (x[1] < punto_1[1] and punto_1[1] < x[2]): #Si coinciden también las cooredenadas y
                            if (abs (punto_1[0]- punto_medio_x) > 0.25): #Cambiamos de punto medio 
                                punto_medio_x=(punto_1[0]+ punto_medio_x)/2
                                parar=True
                                volverAIterar=True
                            else:
                                punto_medio_x=-100
                                parar=True
                                volverAIterar=False
            if (parar==False):
                volverAIterar=False
        
        return punto_medio_x
    
    def __coincidir_arista_horizontal_y_flecha (self, punto_1, punto_2, puntos):
        '''
        Esta función se utiliza a la hora de dibujar los caminos v_i y u_i en las funciones dibujar_caminos_vi y dibujar_caminos_ui respectivamente. Esta función determina, si en una arista vertical, de un camino v_i o u_i "hay espacio" para dibujar una 
        flecha que indique el sentido del camino v_i o u_i. 
        
        En caso de que exista dicho espacio, se devolverá el valor de la coordenada y sobre la que se tiene que dibujar dicha flecha vertical, siendo la variable que se devuelve la coordenada 'y' central de 
        dicha flecha. En caso contrario, se devolverá el valor -100. 

        Lo que se comprueba es que no haya ninguna arista horizontal entre dichos puntos punto_1 y punto_2 que haga que la distancia entre dichos puntos y la arista horizontal sea tan pequeña que no "quepa" la flecha.

        Args:
            punto_1: Punto inicial de la arista perteneciente a un camino v_i o u_i.
            punto_2: Punto final de la arista perteneciente a un camino v_i o u_i.
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos).
        '''

        aristas=self.obtener_aristas(puntos)
        aristas_horizontales=aristas[0]
        punto_medio_y=(punto_1[1] + punto_2[1] )/2
        volverAIterar=True
        while(volverAIterar==True):
            parar=False
            for x in aristas_horizontales:
                if (parar==False):
                    if (x[0] > (punto_medio_y - 0.07) and x[0] < (punto_medio_y + 0.07)): #Es decir si coinciden las coordenadas y de la arista vertical y la de la flecha
                        if (x[1] < punto_1[0] and x[2] > punto_1[0]): #Si coinciden también las coordenadas x
                            if (abs (punto_1[1]- punto_medio_y) > 0.25): #Cambiamos de punto medio 
                                punto_medio_y=(punto_1[1]+ punto_medio_y)/2
                                parar=True
                                volverAIterar=True
                            else:
                                punto_medio_y=-100
                                parar=True
                                volverAIterar=False
            if(parar==False):
                volverAIterar=False
        
        return punto_medio_y

    def dibujar_caminos_vi (self, puntos, puntos_vi, numeros_cambio):
        '''
        Se utiliza el módulo turtle de python para dibujar lo siguiente:
            El nudo dado por los puntos obtenidos de la función obtener_puntos_nudo_dowker dividido en arcos superiores (color azul) y arcos inferiores (color rojo).
            Una flecha indicará la orientación del nudo. 
            Los caminos v_i que rodeen a todos los arcos inferiores del nudo dado, representados con color verde. 
            Una flecha que indique el sentido de cada uno de los caminos v_i (que debido a ser caminos v_i tenrán sentido antihorario), representadas con color verde y borde gris.
            Espacios V_i que se encuentran en el interior de los caminos v_i, representados con color rojo claro.
        
        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            puntos_vi: Lista de puntos de los caminos v_i, que se obtiene de la función obtener_caminos_vi.
            numeros_cambio:  Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        colormode(255)
        pencolor(121,221,0)

        title("Nudo dividido en arcos superiores e inferiores junto con caminos v_i y espacios V_i")

        for x in puntos_vi:
            penup()
            primer_punto=(100*x[0][0], 100*x[0][1])
            goto(primer_punto)
            contador=0
            fillcolor(241,183,194)
            
            begin_fill()
            pendown()
            for i in x:
                if (contador!=0):
                    punto_aux=[100*i[0], 100*i[1]]
                    goto(punto_aux)
                contador+=1
            
            goto(primer_punto)
            end_fill()

        if (self.__numeros[0]>0):
            superior=False
            superior_inicial=False
            pencolor("red")
        else:
            superior=True
            superior_inicial=True
            pencolor("blue")

        contador=0
        penup()
        pensize(2)
        for x in puntos:
            if (contador % 2==0):
                punto1=(100*x[0], 100*x[1])
            else:
                punto2=(100*x[0], 100*x[1])
              
                goto(punto1)
                pendown()
                goto(punto2)
                penup()
                if (contador in numeros_cambio):
                    if superior:
                        superior=False
                        pencolor("red")
                    else:
                        superior=True
                        pencolor("blue")
                    
            contador+=1

        #Esto es para dibujar la flecha del nudo 
        if (superior_inicial==False):       
            fillcolor("red")
        else:
            fillcolor("blue")

        pensize(1)
        penup()
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        begin_fill()
        pendown()
        punto_aux=[-0.38*100, -0.07*100]
        goto(punto_aux)
        punto_aux=[-0.22*100, 0.0]
        goto(punto_aux)
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        end_fill()

        #A continuación vamos a dibujar la flecha de cada camino v_i que tendrá sentido antihorario 

        
    
        for x in puntos_vi:
            penup()
            pensize(1)
            fillcolor(121,221,0)
            pencolor("grey")
            flecha_dibujada=False  #Voy a necesitar que entre dos puntos cualquiera del camino haya una distancia mínima de 0.25 para que haya espacio para dibujar la flecha 
            for i in range(len(x)-1):
                if (flecha_dibujada==False):
                    if ( (x[i][0] != x[i+1][0]) and abs(x[i][0]- x[i+1][0] ) > 0.25  ): #Es decir, si las coordenadas x no son iguales y su distancia es mayor de 0.25
                        x_medio=self.__coincidir_arista_vertical_y_flecha(x[i], x[i+1], puntos)
                        if (x_medio != -100):

                        #x_medio=(x[i][0] + x[i+1][0])/2
                            if (x[i][0] > x[i+1][0]):
                                
                                punto1=[(x_medio-0.05)*100, x[i][1]*100]
                                punto2=[(x_medio+0.05)*100, (x[i][1]+0.04)*100]
                                punto3=[(x_medio+0.05)*100, (x[i][1]-0.04)*100]
                            else:
                                punto1=[(x_medio+0.05)*100, x[i][1]*100]
                                punto2=[(x_medio-0.05)*100, (x[i][1]+0.04)*100]
                                punto3=[(x_medio-0.05)*100, (x[i][1]-0.04)*100]
                            flecha_dibujada=True
                        
                    
                    if ( (x[i][1] != x[i+1][1]) and abs(x[i][1]- x[i+1][1] ) > 0.25  ):
                        y_medio=self.__coincidir_arista_horizontal_y_flecha(x[i], x[i+1], puntos)
                        if (y_medio!=-100):
                            if (x[i][1] > x[i+1][1]):
                                punto1=[x[i][0]*100, (y_medio-0.05)*100]
                                punto2=[(x[i][0] - 0.04)*100, (y_medio+0.05)*100]
                                punto3=[(x[i][0] + 0.04)*100, (y_medio+0.05)*100]
                            else:
                                punto1=[x[i][0]*100, (y_medio+0.05)*100]
                                punto2=[(x[i][0] - 0.04)*100, (y_medio-0.05)*100]
                                punto3=[(x[i][0] + 0.04)*100, (y_medio-0.05)*100]  

                            flecha_dibujada=True
            
            if (flecha_dibujada==True):
                
                
                
                goto(punto1)
                begin_fill()
                pendown()
                goto(punto2)
                goto(punto3)
                goto(punto1)
                end_fill()
                

        
        hideturtle()
        exitonclick()
        Screen().bye()

    def dibujar_caminos_ui (self, puntos, puntos_ui, numeros_cambio):
        '''
        Se utiliza el módulo turtle de python para dibujar lo siguiente:
            El nudo dado por los puntos obtenidos de la función obtener_puntos_nudo_dowker dividido en arcos superiores (color azul) y arcos inferiores (color rojo).
            Una flecha indicará la orientación del nudo. 
            Los caminos u_i que rodeen a todos los arcos superiores del nudo dado, representados con color morado. 
            Una flecha que indique el sentido de cada uno de los caminos u_i (que debido a ser caminos u_i tenrán sentido horario), representadas con color morado.
            Espacios U_i que se encuentran en el interior de los caminos u_i, representados con color azul claro.
        
        Args:
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            puntos_ui: Lista de puntos de los caminos u_i, que se obtiene de la función obtener_caminos_ui.
            numeros_cambio:  Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        colormode(255)
        
        pencolor(152,0,255)
        title("Nudo dividido en arcos superiores e inferiores junto con caminos u_i y espacios U_i")
        for x in puntos_ui:
            penup()
            primer_punto=(100*x[0][0], 100*x[0][1])
            goto(primer_punto)
            contador=0
            fillcolor(213,227,248)
            
            begin_fill()
            pendown()
            for i in x:
                if (contador!=0):
                    punto_aux=[100*i[0], 100*i[1]]
                    goto(punto_aux)
                contador+=1
            
            goto(primer_punto)
            end_fill()

        if (self.__numeros[0]>0):
            superior=False
            superior_inicial=False
            pencolor("red")
        else:
            superior=True
            superior_inicial=True
            pencolor("blue")

        contador=0
        penup()
        pensize(2)
        for x in puntos:
            if (contador % 2==0):
                punto1=(100*x[0], 100*x[1])
            else:
                punto2=(100*x[0], 100*x[1])
              
                goto(punto1)
                pendown()
                goto(punto2)
                penup()
                if (contador in numeros_cambio):
                    if superior:
                        superior=False
                        pencolor("red")
                    else:
                        superior=True
                        pencolor("blue")
                        '''if (puntos[contador-1][0] != puntos[contador][0]): #Si lo que ha variado es la coordenada 
                            setpos(puntos[contador][0]*100,(puntos[contador][1]+0.02)*100)
                            write('A_1')  
                        else:
                            setpos((puntos[contador][0]+0.03)*100,puntos[contador][1]*100)
                            write('A')'''

                    
            contador+=1

        #Ahora dibujamos la flecha
        if (superior_inicial==False):
            fillcolor("red")
        else:
            fillcolor("blue")

        pensize(1)
        penup()
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        begin_fill()
        pendown()
        punto_aux=[-0.38*100, -0.07*100]
        goto(punto_aux)
        punto_aux=[-0.22*100, 0.0]
        goto(punto_aux)
        punto_aux=[-0.38*100, 0.07*100]
        goto(punto_aux)
        end_fill()

        #A continuación vamos a dibujar la flecha de cada camino u_i que tendrá sentido horario

        for x in puntos_ui:
            penup()
            pensize(1)
            fillcolor(152,0,255)
            pencolor("grey")
            flecha_dibujada=False  #Voy a necesitar que entre dos puntos cualquiera del camino haya una distancia mínima de 0.25 para que haya espacio para dibujar la flecha 
            for i in range(len(x)-1):
                if (flecha_dibujada==False):
                    if ( (x[i][0] != x[i+1][0]) and abs(x[i][0]- x[i+1][0] ) > 0.25  ): #Es decir, si las coordenadas x no son iguales y su distancia es mayor de 0.25
                        x_medio=self.__coincidir_arista_vertical_y_flecha(x[i], x[i+1], puntos)
                        if (x_medio != -100):

                        #x_medio=(x[i][0] + x[i+1][0])/2
                            if (x[i][0] > x[i+1][0]):
                                punto1=[(x_medio+0.05)*100, x[i][1]*100]
                                punto2=[(x_medio-0.05)*100, (x[i][1]+0.04)*100]
                                punto3=[(x_medio-0.05)*100, (x[i][1]-0.04)*100]
                                
                            else:
                                punto1=[(x_medio-0.05)*100, x[i][1]*100]
                                punto2=[(x_medio+0.05)*100, (x[i][1]+0.04)*100]
                                punto3=[(x_medio+0.05)*100, (x[i][1]-0.04)*100]
                            flecha_dibujada=True
                        
                    
                    if ( (x[i][1] != x[i+1][1]) and abs(x[i][1]- x[i+1][1] ) > 0.25  ):
                        y_medio=self.__coincidir_arista_horizontal_y_flecha(x[i], x[i+1], puntos)
                        if (y_medio!=-100):
                            if (x[i][1] > x[i+1][1]):
                                punto1=[x[i][0]*100, (y_medio+0.05)*100]
                                punto2=[(x[i][0] - 0.04)*100, (y_medio-0.05)*100]
                                punto3=[(x[i][0] + 0.04)*100, (y_medio-0.05)*100] 
                            else:
                                punto1=[x[i][0]*100, (y_medio-0.05)*100]
                                punto2=[(x[i][0] - 0.04)*100, (y_medio+0.05)*100]
                                punto3=[(x[i][0] + 0.04)*100, (y_medio+0.05)*100]
                            flecha_dibujada=True
            
            if (flecha_dibujada==True):
                
                
                
                goto(punto1)
                begin_fill()
                pendown()
                goto(punto2)
                goto(punto3)
                goto(punto1)
                end_fill()

            
        hideturtle()
        exitonclick()
        Screen().bye()

    def __calcular_signo_cruce_arista_vertical(self, segmento, arista_vertical):
        '''
        Esta función es utilizada para calcular el signo de los componentes de los relatores de las presentaciones superior e inferior del nudo K. Comprueba para una arista vertical del nudo K dada por 'arista_vertical' y una arista horizontal del camino v_i o u_i 
        dada por 'segmento' que se intersectan el signo de dicho cruce. 

        Devuelve :
            1 en caso de que la arista vertical del nudo y la arista horizontal del camino u_i o v_i formen un tornillo de la mano derecha.
            -1 en caso de que la arista vertical del nudo y la arista horizontal del camino u_i o v_i formen un tornillo de la mano izquierda.

        Args:
            segmento: Lista de dos puntos, siendo los dos puntos de la arista_horizontal de u_i o v_i que estamos analizando.
            arista_vertical: Arista vertical ordenada, es decir, un elemento de la lista obtenida de la función __obtener_aristas_inferiores_ordenadas u __obtener_aristas_superiores_ordenadas
        '''

        if (arista_vertical[1] > arista_vertical[2]):
            if (segmento[0][0] > segmento[1][0]):
                signo=1
            else:
                signo=-1
        else:
            if (segmento[0][0] < segmento[1][0]):
                signo=1
            else:
                signo=-1
        return signo

    def __calcular_signo_cruce_arista_horizontal(self, segmento, arista_horizontal):
        '''
        Esta función es utilizada para calcular el signo de los componentes de los relatores de las presentaciones superior e inferior del nudo K. Comprueba para una arista horizontal  del nudo K dada por 'arista_horizontal' y una arista vertical del camino v_i o u_i 
        dada por 'segmento' que se intersectan el signo de dicho cruce. 

        Devuelve :
            1 en caso de que la arista horizontal del nudo y la arista vertical del camino u_i o v_i formen un tornillo de la mano derecha.
            -1 en caso de que la arista horizontal del nudo y la arista vertical del camino u_i o v_i formen un tornillo de la mano izquierda.

        Args:
            segmento: Lista de dos puntos, siendo los dos puntos de la arista_vertical de u_i o v_i que estamos analizando.
            arista_horizontal: Arista horizontal ordenada, es decir, un elemento de la lista obtenida de la función __obtener_aristas_inferiores_ordenadas u __obtener_aristas_superiores_ordenadas
        '''
        if (arista_horizontal[1] < arista_horizontal[2]):
            if (segmento[0][1] > segmento[1][1]):
                signo=1
            else:
                signo=-1
        
        else:
            if (segmento[0][1] < segmento[1][1]):
                signo=1
            else:
                signo=-1
                
        return signo

    def __interseccion_aristas_verticales(self, segmento, aristas_inferiores_o_superiores):
        '''
        Esta función se utiliza para hallar los relatores de las presentaciones superior e inferior del nudo. Si estamos calculando la presentación superior [inferior], se le pasa por parámetro las aristas superiores [inferiores] y obtendremos las aristas verticales 
        superiores [inferiores], que se intersectan con el segmento horizontal del camino v_i [u_i] dado por 'segmento', que contendrá los dos puntos de una arista horizontal del camino v_i [u_i]. Posteriormente, calcularemos el signo de dicho cruce e introduciremos en una lista 
        el valor obtenido de multiplicar el signo del cruce por el número de arco superior [inferior] en el que se encuentra la arista vertical que se intersecta con el segmento.

        En caso de que más de una arista vertical intersecte al segmento horizontal, habría que ordenar los valores resultantes según el orden en el que han sido intersectados. 

        Ejemplo:
            La arista vertical [0, -1, 1] (recordemos que 0 es la coordenada 'x' y -1 es la coordenada 'y' del primer punto y 1 la coordenada 'y' del segundo punto) contenida en la 4ª posición de la lista de aristas_inferiores_o_superiores 
            se intersecta con el segmento horizontal [[-1,0], [1,0]]. Por tanto, el signo del cruce sería -1 y se introduciría en la lista resultante el valor -1*5=-5 (es 5 porque la posición i de la lista la tiene asociada el arco superior [inferior] i+1)

        Args:
            segmento: Lista de dos puntos, siendo los dos puntos de la arista horizontal de u_i o v_i que estamos analizando.
            aristas_inferiores_o_superiores: Lista de aristas obtenida de la función __obtener_aristas_inferiores u __obtener_aristas_superiores en función de si estamos calculando la presentación inferior o superior, de la que solo nos interesan las aristas verticales.
        '''


        contador=1
        lista_x=[]
        lista_indices=[]
        for x in aristas_inferiores_o_superiores:
            for i in x[1]:              #es decir, miramos solo las aristas superiores verticales (en caso de estar calculando la presentación superior) y las aristas inferiores verticales (en caso de estar calculando la presentación inferior)
                if (i[1] < segmento[0][1] and  segmento[0][1] < i[2]):          #Comprobamos si se intersecta dicha arista vertical con el segmento horizontal que se pasa por parámetro
                    if (segmento[0][0] < i[0] and i[0] < segmento[1][0]):
                        lista_x.append(i[0])                                    #En caso de que se intersecten, introducimos en una lista la coordenada x del punto de intersección del segmento horizontal y la arsita vertical 
                        signo_cruce=self.__calcular_signo_cruce_arista_vertical(segmento, i)
                        lista_indices.append(signo_cruce*contador)              #En caso de que se intersecten introducimos en una lista la posición de la lista aristas_inferiores_o_superiores donde se encuentra la arista que se intersecta (que nos servirá para construir el relator) y el signo del cruce
                    if (segmento[1][0] < i[0] and i[0] < segmento[0][0]):
                        lista_x.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_vertical(segmento, i)
                        lista_indices.append(signo_cruce*contador)
                
                if (i[2] < segmento[0][1] and  segmento[0][1] < i[1]):
                    if (segmento[0][0] < i[0] and i[0] < segmento[1][0]):
                        lista_x.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_vertical(segmento, i)
                        lista_indices.append(signo_cruce*contador)
                    if ( segmento[1][0] < i[0] and i[0] < segmento[0][0]):
                        lista_x.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_vertical(segmento, i)
                        lista_indices.append(signo_cruce*contador)
            contador+=1
        
        if (len(lista_indices)>1):      #En caso de que haya más de una arista vertical que se intersecte con el semgmento dado por 'segmento' hay que ordenarlos según el orden de los cruces. 
            if (segmento[0][0] < segmento[1][0]): #Hay que ordenarlos de menor a mayor.
                lista_aux=[]
                while(len(lista_indices)>1):
                    valor_menor=100
                    indice_menor=-1
                    for i in range(len(lista_x)):
                        if (lista_x[i] < valor_menor):
                            valor_menor=lista_x[i]
                            indice_menor=i
                            
                    lista_aux.append(lista_indices[indice_menor])
                    lista_x.pop(indice_menor)
                    lista_indices.pop(indice_menor)
                lista_aux.append(lista_indices[0])
                lista_indices=lista_aux
            else: #Hay que ordenarlos de mayor a menor. 
                lista_aux=[]
                while(len(lista_indices)>1):
                    valor_mayor=-100
                    indice_mayor=-1
                    for i in range(len(lista_x)):
                        if (lista_x[i] > valor_mayor):
                            valor_mayor=lista_x[i]
                            indice_mayor=i
                    lista_aux.append(lista_indices[indice_mayor])
                    lista_x.pop(indice_mayor)
                    lista_indices.pop(indice_mayor)
                lista_aux.append(lista_indices[0])
                lista_indices=lista_aux

        return lista_indices

    def __interseccion_aristas_horizontales(self, segmento, aristas_inferiores_o_superiores):
        '''
        Esta función se utiliza para hallar los relatores de las presentaciones superior e inferior del nudo. Si estamos calculando la presentación superior [inferior], se le pasa por parámetro las aristas superiores [inferiores] y obtendremos las aristas horizontales 
        superiores [inferiores], que se intersectan con el segmento vertical del camino v_i [u_i] dado por 'segmento', que contendrá los dos puntos de una arista vertical del camino v_i [u_i] que estamos analizando. Posteriormente, calcularemos el signo de dicho cruce 
        e introduciremos en una lista el valor obtenido de multiplicar el signo del cruce por el número de arco superior [inferior] en el que se encuentra la arista horizontal del nudo que se intersecta con el segmento.

        En caso de que más de una arista horizontal intersecte al segmento vertical, habría que ordenar los valores resultantes según el orden en el que han sido intersectados. 

        Ejemplo:
            La arista horizontal [1, -2, 0] (recordemos que 1 es la coordenada 'y', -2 es la coordenada 'x' del primer punto y 0 la coordenada 'x' del segundo punto) contenida en la 1ª posición de la lista de aristas_inferiores_o_superiores 
            se intersecta con el segmento vertical [[-1,5,0], [-1,5,2]]. Por tanto, el signo del cruce sería -1 y se introduciría en la lista resultante el valor -1*2=-2 (es 2 porque la posición i de la lista la tiene asociada el arco superior [inferior] i+1)

        Args:
            segmento: Lista de dos puntos, siendo los dos puntos de la arista vertical de u_i o v_i que estamos analizando.
            aristas_inferiores_o_superiores: Lista de aristas obtenida de la función __obtener_aristas_inferiores u __obtener_aristas_superiores en función de si estamos calculando la presentación inferior o superior, de la que solo nos interesan las aristas horizontales.
        '''

        contador=1
        lista_y=[]
        lista_indices=[]
        for x in aristas_inferiores_o_superiores:
            for i in x[0]: #es decir, solo miramos las aristas horizontales superiores o inferiores
                if (i[1] < segmento[0][0] and segmento[0][0] < i[2]):
                    if (segmento[0][1] < i[0] and i[0] < segmento[1][1]):
                        lista_y.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_horizontal(segmento, i)
                        lista_indices.append(signo_cruce*contador)
                    
                    if (segmento[1][1] < i[0] and i[0] < segmento[0][1]):
                        lista_y.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_horizontal(segmento, i)
                        lista_indices.append(signo_cruce*contador)
                
                if (i[2] < segmento[0][0] and segmento[0][0] < i[1]):
                    if (segmento[0][1] < i[0] and i[0] < segmento[1][1]):
                        lista_y.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_horizontal(segmento, i)
                        lista_indices.append(signo_cruce*contador)
                    
                    if (segmento[1][1] < i[0] and i[0] < segmento[0][1]):
                        lista_y.append(i[0])
                        signo_cruce=self.__calcular_signo_cruce_arista_horizontal(segmento, i)
                        lista_indices.append(signo_cruce*contador)
            contador+=1

        if (len(lista_indices) > 1): #Hay que ordenarlos 
            if (segmento[0][1] < segmento[1][1]): #De menor a mayor
                lista_aux=[]
                while(len(lista_indices) > 1):
                    valor_menor=100
                    indice_menor=-1
                    for i in range(len(lista_y)):
                        if (lista_y[i] < valor_menor):
                            valor_menor=lista_y[i]
                            indice_menor=i
                            
                    lista_aux.append(lista_indices[indice_menor])
                    lista_y.pop(indice_menor)
                    lista_indices.pop(indice_menor)
                lista_aux.append(lista_indices[0])
                lista_indices=lista_aux

            else: #De mayor a menor 
                lista_aux=[]
                while(len(lista_indices)>1):
                    valor_mayor=-100
                    indice_mayor=-1
                    for i in range(len(lista_y)):
                        if (lista_y[i] > valor_mayor):
                            valor_mayor=lista_y[i]
                            indice_mayor=i
                    lista_aux.append(lista_indices[indice_mayor])
                    lista_y.pop(indice_mayor)
                    lista_indices.pop(indice_mayor)
                lista_aux.append(lista_indices[0])
                lista_indices=lista_aux

        return lista_indices

    def __representar_relator_presentacion_superior(self, lista_indices): 
        '''
        Esta función toma una lista de enteros, cuyo valor absoluto indicará el arco superior del nudo con el que se intersecará el camino v_i y el signo que acompaña a dicho número en valor absoluto indicará el signo del cruce de dicho arco superior con el camino v_i.
        Pasaremos esa lista de enteros al formato que tiene un relator.

        Esta función es llamada por la función representar_presentacion_superior.

        Ejemplo:
            >>> __representar_relator_presentacion_superior([1,4,-2,-4]) 
            "x₁x₄x₂⁻¹x₄⁻¹"
        
        Args: 
            lista_indices: Lista de números enteros, que queremos transformar en una cadena con el formato de relator de la presentación superior.
        '''
        
        SUPER=str.maketrans("-1", "⁻¹")
        SUB=str.maketrans("123456789", "₁₂₃₄₅₆₇₈₉")

        relator=""
        for j in range(len(lista_indices)):
            aux="x"
            aux+=str(abs(lista_indices[j]))
            aux2=aux.translate(SUB)
            if (lista_indices[j] < 0):
                aux2+="-"
                aux2+=str(1)
                aux3=aux2.translate(SUPER)
                relator+=aux3
            else:
                relator+=aux2
                
        return relator

    def __representar_relator_presentacion_inferior(self, lista_indices):
        '''
        Esta función toma una lista de enteros, cuyo valor absoluto indicará el arco inferior del nudo con el que se intersecará el camino u_i y el signo que acompaña a dicho número en valor absoluto indicará el signo del cruce de dicho arco inferior con el camino u_i.
        Pasaremos esa lista de enteros al formato que tiene un relator.

        Esta función es llamada por la función representar_presentacion_inferior.

        Ejemplo:
            >>> __representar_relator_presentacion_inferior([1,4,-2,-4]) 
            "y₁y₄y₂⁻¹y₄⁻¹"
        
        Args: 
            lista_indices: Lista de números enteros, que queremos transformar en una cadena con el formato de relator de la presentación inferior.
        '''

        SUPER=str.maketrans("-1", "⁻¹")
        SUB=str.maketrans("123456789", "₁₂₃₄₅₆₇₈₉")

        relator=""
        for j in range(len(lista_indices)):
            aux="y"
            aux+=str(abs(lista_indices[j]))
            aux2=aux.translate(SUB)
            if (lista_indices[j] < 0):
                aux2+="-"
                aux2+=str(1)
                aux3=aux2.translate(SUPER)
                relator+=aux3
            else:
                relator+=aux2
                
        return relator
    
    def __representar_generadores_presentacion_superior (self):
        '''
        Este método calcula el número de arcos superiores del nudo que denotaremos por 'n' y develve una cadena con los 'n' generadores de la presentación superior del grupo de un nudo, siendo estos x₁, x₂...

        Ejemplo:
            >>> __representar_generadores_presentacion_superior()       Imaginemos que el número de arcos superiores es 5
            "x₁, x₂, x₃, x₄, x₅"
        
        '''
        num_arcos_super=self.numero_arcos_superiores()
        generadores=""
        SUB=str.maketrans("123456789", "₁₂₃₄₅₆₇₈₉")
        contador=0
        for i in range(num_arcos_super):
            aux="x"
            aux+=str(i+1)
            aux2=aux.translate(SUB)
            generadores+=aux2
            if (contador!=((num_arcos_super)-1)):
                generadores+=", "
            contador+=1

        return generadores

    def __representar_generadores_presentacion_inferior(self):
        '''
        Este método calcula el número de arcos inferiores del nudo (que es el mismo que el número de arcos superiores) que denotaremos por 'n' y develve una cadena con los 'n' generadores de la presentación inferior del grupo de un nudo, siendo estos y₁, y₂...

        Ejemplo:
            >>> __representar_generadores_presentacion_inferior()               Imaginemos que el número de arcos superiores es 5
            "y₁, y₂, y₃, y₄, y₅"
        
        '''
        num_arc_infer=self.numero_arcos_superiores()
        generadores=""
        SUB=str.maketrans("123456789", "₁₂₃₄₅₆₇₈₉")
        contador=0

        for i in range(num_arc_infer):
            aux="y"
            aux+=str(i+1)
            aux2=aux.translate(SUB)
            generadores+=aux2
            if (contador!=(num_arc_infer-1)):
                generadores+=", "
            contador+=1

        return generadores

    def obtener_presentacion_superior(self, puntos_vi, puntos, vector_cambio):
        '''
        Esta función calcula los n relatores de la presentación superior del nudo dado por los puntos 'puntos' pasados por parámetro, siendo n el numero de arcos superiores. Gracias a los caminos v_i obtenidos mediante la función 'obtener_caminos_vi',
        en esta función calcularemos las aristas de los arcos superiores que intersectan con dichos caminos v_i, y el signo del cruce de estas con los caminos v_i y así seremos capaces de calcular los relatores de la presentación superior del grupo del nudo. 

        El formato de los relatores será [+/- A₁, ... ,+/- Aₙ] indicando Aᵢ la que la i-ésima arista que intersecta al camino v_j pertenece al arco superior Aᵢ.

        Args: 
            puntos_vi: Lista de los puntos de los caminos vi obtenidos de la función obtener_caminos_vi
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            vector_cambio:  Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        presentacion_superior=[]

        aristas_superiores=self.__obtener_aristas_superiores_ordenadas(puntos, vector_cambio)

        for x in puntos_vi:
            lista_indices_i=[]
            for i in range(len(x) -1):
                segmento_a_estudiar=[]
                segmento_a_estudiar.append(x[i])
                segmento_a_estudiar.append(x[i+1])
                if (x[i][0] != x[i+1][0]): #Es decir, si el segmento es horizontal tendremos que comprobar con que aristas verticales intersecta
                    lista_indices_aux=self.__interseccion_aristas_verticales(segmento_a_estudiar, aristas_superiores)
                    
                    
                else: #El segmento es vertical y tenemos que comprobar con que aristas horizntales intersecta 
                    lista_indices_aux=self.__interseccion_aristas_horizontales(segmento_a_estudiar, aristas_superiores)
                    
                if lista_indices_aux:
                    for j in lista_indices_aux:
                        lista_indices_i.append(j)

            segmento_a_estudiar=[]
            segmento_a_estudiar.append(x[(len(x)-1)])
            segmento_a_estudiar.append(x[0])

            if (x[(len(x)-1)][0] != x[0][0] ):
                lista_indices_aux=self.__interseccion_aristas_verticales(segmento_a_estudiar, aristas_superiores)
                   
            else:
                lista_indices_aux=self.__interseccion_aristas_horizontales(segmento_a_estudiar, aristas_superiores)
                
                
            if lista_indices_aux:
                for j in lista_indices_aux:
                    lista_indices_i.append(j)

            
            presentacion_superior.append(lista_indices_i)
        
        return presentacion_superior

    def obtener_presentacion_inferior (self, puntos_ui, puntos, vector_cambio):
        '''
        Esta función calcula los n relatores de la presentación inferior del nudo dado por los puntos 'puntos' pasados por parámetro, siendo n el numero de arcos inferiores. Gracias a los caminos u_i obtenidos mediante la función 'obtener_caminos_ui',
        en esta función calcularemos las aristas de los arcos inferiores que intersectan con dichos caminos u_i, y el signo del cruce de estas con los caminos u_i y así seremos capaces de calcular los relatores de la presentación inferior del grupo del nudo. 

        El formato de los relatores será [+/- B₁, ... ,+/- Bₙ] indicando Bᵢ la que la i-ésima arista que intersecta al camino u_j pertenece al arco inferior Bᵢ.

        Args: 
            puntos_ui: Lista de los puntos de los caminos ui obtenidos de la función obtener_caminos_ui
            puntos: Lista obtenida de la función obtener_puntos_nudo_dowker (y modificada posterioremente por la función dividir_nudo_en_arcos)
            vector_cambio:  Lista de índices obtenida de la función dividir_nudo_en_arcos.
        '''

        presentacion_inferior=[]
        
        aristas_inferiores=self.__obtener_aristas_inferiores_ordenadas(puntos, vector_cambio)

        for x in puntos_ui:
            lista_indices_i_so=[]
            for i in range(len(x) -1):
                segmento_a_estudiar=[]
                segmento_a_estudiar.append(x[i])
                segmento_a_estudiar.append(x[i+1])
                if (x[i][0] != x[i+1][0]): #Es decir, si el segmento es horizontal tendremos que comprobar con que aristas verticales intersecta
                    lista_indices_aux=self.__interseccion_aristas_verticales(segmento_a_estudiar, aristas_inferiores)
                         
                else: #El segmento es vertical y tenemos que comprobar con que aristas horizntales intersecta 
                    lista_indices_aux=self.__interseccion_aristas_horizontales(segmento_a_estudiar, aristas_inferiores)
                    
                if lista_indices_aux:
                    
                    for j in lista_indices_aux:
                        
                        lista_indices_i_so.append((-1)*j) #Lo multiplicamos por -1 porque los caminos u_j tienen sentido contrario al que indica el recorrido de los puntos del camino que hacemos 

            segmento_a_estudiar=[]
            segmento_a_estudiar.append(x[(len(x)-1)])
            segmento_a_estudiar.append(x[0])

            if (x[(len(x)-1)][0] != x[0][0] ):
                lista_indices_aux=self.__interseccion_aristas_verticales(segmento_a_estudiar, aristas_inferiores)
                
            else:
                lista_indices_aux=self.__interseccion_aristas_horizontales(segmento_a_estudiar, aristas_inferiores)
                
                

            
            if lista_indices_aux:
                for j in lista_indices_aux:
                    lista_indices_i_so.append((-1)*j) #Lo multiplicamos por -1 porque los caminos u_j tienen sentido contrario al que indica el recorrido de los puntos del camino que hacemos 

            #Como el sentido es horario invertimos los valores de la lista
            lista_indices_i=[]
            lista_indices_i.append(lista_indices_i_so[0])
            for i in range(len(lista_indices_i_so)-1):
                lista_indices_i.append(lista_indices_i_so[len(lista_indices_i_so)-i-1])

            presentacion_inferior.append(lista_indices_i)

        return presentacion_inferior

    def representar_presentacion_superior(self, presentacion_superior):
        '''
        Método que, dados los relatores de la presentación superior del grupo de un nudo, en el parámetro 'presentacion_superior', muestra por pantalla la presentación de dicho grupo en el formato propio de la presentacion superior del grupo de un nudo. 
        Es decir, llama a las funciones __representar_generadores_presentacion_superior y __representar_relator_presentacion_superior para construir una cadena que sea la presentación superior del grupo del nudo analizado.

        Ejemplo: 
            >>> __representar_presentacion_superior([[6, -2, -1, 2], [3, 1, -3, -2], [1, 2, -1, -3], [3, -5, -4, 5], [6, 4, -6, -5], [4, 5, -4, -6]])
            <x₁, x₂, x₃, x₄, x₅, x₆ : x₆x₂⁻¹x₁⁻¹x₂, x₃x₁x₃⁻¹x₂⁻¹, x₁x₂x₁⁻¹x₃⁻¹, x₃x₅⁻¹x₄⁻¹x₅, x₆x₄x₆⁻¹x₅⁻¹, x₄x₅x₄⁻¹x₆⁻¹>
        
        Args:
            presentacion_superior: lista de los relatores de la presentación superior del grupo del nudo analizado, obtenida de la funcion obtener_presentacion_superior.
        '''

        pre_superior="<"
        pre_superior+=self.__representar_generadores_presentacion_superior()
        pre_superior+=" : "

        contador=0 #este contador es para no introducir la última coma ","
        for x in presentacion_superior:
            pre_superior+=self.__representar_relator_presentacion_superior(x)
            if (contador!=(len(presentacion_superior)-1)):
                pre_superior+=", "
            contador+=1

        pre_superior+=">"
        print(pre_superior)

    def representar_presentacion_inferior(self, presentacion_inferior):
        '''
        Método que, dados los relatores de la presentación inferior del grupo de un nudo, en el parámetro 'presentacion_inferior', muestra por pantalla la presentación de dicho grupo en el formato propio de la presentacion inferior del grupo de un nudo. 
        Es decir, llama a las funciones __representar_generadores_presentacion_inferior y __representar_relator_presentacion_inferior para construir una cadena que sea la presentación inferior del grupo del nudo analizado.

        Ejemplo: 
            >>> __representar_presentacion_superior([[-1, 3, 2, -3], [1, 3, -1, -2], [2, 4, -2, -3], [-4, 6, 5, -6], [4, 6, -4, -5], [5, 1, -5, -6]])
            <y₁, y₂, y₃, y₄, y₅, y₆ : y₁⁻¹y₃y₂y₃⁻¹, y₁y₃y₁⁻¹y₂⁻¹, y₂y₄y₂⁻¹y₃⁻¹, y₄⁻¹y₆y₅y₆⁻¹, y₄y₆y₄⁻¹y₅⁻¹, y₅y₁y₅⁻¹y₆⁻¹>
        
        Args:
            presentacion_inferior: lista de los relatores de la presentación inferior del grupo  del nudo analizado, obtenida de la funcion obtener_presentacion_inferior.
        '''

        pre_inferior="<"
        pre_inferior+=self.__representar_generadores_presentacion_inferior()
        pre_inferior+=" : "
        
        contador=0 #este contador es para no introducir la última coma ","
        for x in presentacion_inferior:
            pre_inferior+=self.__representar_relator_presentacion_inferior(x)
            if (contador!=(len(presentacion_inferior)-1)):
                pre_inferior+=", "
            contador+=1
        pre_inferior+=">"
        print(pre_inferior)

    def obtener_puntos_nudo_dowker(self):
        '''
        Método que, dada la secuencia de enteros pares consecutivos en valor absoluto almacenada en la lista que es atributo de la clase nudo, calcula la secuencia de puntos de la aristas del nudo poligonal resultante. A dicha secuencia de enteros pares se le 
        llamará notación Dowker de un nudo, y a través de esa información construiremos el nudo. 

        Este método devolverá una lista de puntos, con una cantidad par de puntos donde un punto en una posición par de la lista significa que es el vértice de inicio de una arista (a la hora de dibujarlo) y en las posiciones impares de dicha lista se almacenarán
        los vértices de fin de una arista. Por tanto, si el nudo resultante tiene dos aristas consecutivas, el punto en posición impar de la primera arista será el mismo que el punto en la siguiente posición de la lista de puntos.

        Los puntos de la lista resultante serán de la forma [x, y] donde x e y son las coordenadas 'x' e 'y' de dicho punto.
        '''

        cont_x=0    #Nos indicará la coordenada x de la posición por la que vamos añadiendo aristas
        cont_y=0    #Nos indicará la coordenada y de la posición por la que vamos añadiendo aristas
        
        y_arriba=[] #Lista que nos indicará la altura de las aristas que pasen por encima del nudo
        x_arriba=[] #Lista de listas que nos indicará el valor mínimo y máximo de x para la altura y del vector de arriba    
        y_abajo=[]
        x_abajo=[]
        
        y_lista_fuera_raiz=[]
        lista_fuera_raiz=[]
        x_lista_fuera_raiz=[]


        y_lista_intermedia=[]
        x_arriba_lista_intermedia=[]
        x_abajo_lista_intermedia=[]
        puntos_aux=[]   #Va a contener los diferentes vértices de las aristas del nudo resultante
        
        
        lista=[]    #Contiene los valores de los cruces que hemos recorrido 
        lista2=[]   #Contiene la coordenada x de los cruces que vamos obteniendo en la lista 1
        arriba=True #Creo que se puede eliminar
        raiz_principal=True
        acabar_aniadir_nuevo_cruce=False
        
        indice_permutacion=self.__dividir_en_dos_subpermutaciones()
        if (indice_permutacion!=-1):        #Es decir, cuando se puede dividir en dos subpermutaciones
            minimo_raiz_antigua=0
            maximo_raiz_antigua=0
        print ('indice_permutacion: '+ str(indice_permutacion))

        if (self.__numeros[0]>0):             #Esto es para el primer valor
            print('Contador='+ str(cont_x))
            punto=[cont_x-0.5,cont_y]
            puntos_aux.append(punto)
            punto=[cont_x-0.1,cont_y]
            puntos_aux.append(punto)
            
            cont_x=0.1

            
        else:
            punto=[cont_x-0.5,cont_y]
            puntos_aux.append(punto)
            '''punto=[cont_x+0.5,cont_y]
            puntos_aux.append(punto)'''
            punto=[cont_x,cont_y]
            puntos_aux.append(punto)
          
        lista.append(1)
        lista2.append(0)       #Mas adelante se podrían juntar en un map o algo así 
        
        
        
        values2 = ','.join(str(v) for v in puntos_aux)
        
        print ('Puntos_aux: ' + values2)
        
        for x in range(len(self.__numeros)):
            
            print ('x: ' + str(x))
            print ('len(self.__numeros): ' + str(len(self.__numeros)))

            
            
            #Valores pares
            '''Este if es para asignarle SIGNO al cruce y para decir si es la SEGUNDA vez que se recorre un cruce'''
            volver=False
            if 2*x+2 in self.__numeros:       #Si es un cruce superior
                signo='Pos' #Indica si se pasa por encima (Pos) o por debajo (Neg)
                valor_asociado=2*self.__numeros.index(2*x+2)+1
                if valor_asociado in lista:     #Si el valor asociado ya ha sido analizado
                    print('Llega ' +str(2*x+2) + ' '+str(valor_asociado))
                    volver=True
            else:   #Si es un cruce inferior
                signo='Neg'
                valor_asociado=2*self.__numeros.index(-(2*x+2))+1
                if valor_asociado in lista:
                    print('Llega2 '+ str(-(2*x+2)) + ' '+str(valor_asociado))
                    volver=True
            
            
            
            
            if(volver==False):  #Si es la PRIMERA VEZ que se llega a un cruce, caso PAR
                if (raiz_principal==True): #Esto nos dice que TODAVIA NO hemos tenido que pasar por ningún cruce DOS VECES
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    
                    posicion_x_final=cont_x+1
                    print ('Contador: '+ str(cont_x) + ' cruce '+ str(2*x+2))
                    if (signo=='Neg'):
                        punto=[posicion_x_final-0.1,cont_y]
                        puntos_aux.append(punto)
                        cont_x=posicion_x_final+0.1
                        '''punto=[cont_x-0.1,cont_y]
                        puntos_aux.append(punto)
                        punto=[cont_x+0.1,cont_y]
                        puntos_aux.append(punto)
                        punto=[cont_x+0.5,cont_y]
                        puntos_aux.append(punto)'''
                    else:
                        cont_x=posicion_x_final
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        '''punto=[cont_x-0.5,cont_y]
                        puntos_aux.append(punto)
                        punto=[cont_x+0.5,cont_y]
                        puntos_aux.append(punto)  '''
                    lista2.append(posicion_x_final)    
                        
                else:   #Caso en el que NO estamos en la RAIZ PRINCIPAL pero queremos ANIADIR un NUEVO CRUCE
                    '''Queremos ver en que sentido tenemos que dibujar el siguiente cruce nuevo posteriormente a haber recorrido un cruce dos veces, que será nuevo ya que ninguno de sus valores está en la lista'''
                    print('Holaaaaaa par '+ str(cont_y))
                    print ('x: ' + str(x))
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    aux=False
                    contador_aux=0
                    contador_ya_lista=0 #Este contador solo sirve para colocar el nuevo punto en el caso de que podamos dividirlo en dos subpermutaciones 

                    while(aux==False):  #Esto se hace para ver cual es el siguiente cruce que está ya en la lista
                        contador_aux+=1
                        print('contador_aux: ' + str(contador_aux) + ' suma: '+ str(contador_aux/2+x) + ' len: '+ str (len(self.__numeros)))
                        
                        if (int(2*x+2+ contador_aux)==(2*len(self.__numeros)+1)): #Caso en el que podamos dividir en dos subpermutaciones, SOBRA
                            aux=True

                        else:
                            if (contador_aux%2 ==1):
                                if (abs(self.__numeros[x+1]) in lista):
                                    contador_ya_lista+=1                          
                                    aux=True
                            else:
                                if 2*x+2+contador_aux in self.__numeros:
                                    vasoc=2*self.__numeros.index(2*x+2+contador_aux)+1
                                    if (vasoc in lista) :
                                        contador_ya_lista+=1
                                        aux=True
                                else:
                                    vasoc=2*self.__numeros.index(-(2*x+2+contador_aux))+1
                                    if (vasoc in lista):
                                        contador_ya_lista+=1
                                        
                                        aux=True
                    print('contador_aux: '+ str(contador_aux))
                    print ('contador_ya_lista: '+ str(contador_ya_lista))

                    if (int(2*x+2+ contador_aux)==(2*len(self.__numeros)+1)): #Caso en el que podamos dividir en dos subpermutaciones
                        posicion_relativa_x=-0.5
                        fragmentos=(contador_aux-contador_ya_lista) #Esto es para ver en el número de fragmentos que se va a dividir el fragmento 
                        posicion_final_x= (cont_x*fragmentos/2 + posicion_relativa_x) / (fragmentos/2 +1)
                    
                    else:
                       
                        if ((contador_aux)%2 ==0):  
                            posicion_relativa_x=lista2[lista.index(vasoc)]
                        else:
                            posicion_relativa_x=lista2[lista.index(abs(self.__numeros[int(x+1+contador_aux/2)]))]
                        
                        posicion_final_x=(cont_x*contador_aux+posicion_relativa_x)/(contador_aux+1)
                    
                    print('cont_x: '+ str(cont_x))
                    print('posicion_relativa_x: '+ str(posicion_relativa_x))

                    
                    
                    print('posicion_final_x: '+ str(posicion_final_x))

                    darVuelta=False
                    if (acabar_aniadir_nuevo_cruce==False):
                        if arriba:
                            contador=0
                            for x_aux in x_arriba:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):
                                    if (x_aux > aux1):
                                        if (cont_x > x_aux or cont_x < aux1): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                            if (aux1 < posicion_relativa_x and posicion_relativa_x < x_aux):
                                                darVuelta=True
                                    else:
                                        if (cont_x > aux1 or cont_x < x_aux): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                            if (x_aux < posicion_relativa_x and posicion_relativa_x < aux1):
                                                darVuelta=True
                                contador+=1
                            
                            
                        else:
                            contador=0
                            for x_aux in x_abajo:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):
                                    if (x_aux > aux1):
                                        if (cont_x > x_aux or cont_x < aux1): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                            if (aux1 < posicion_relativa_x and posicion_relativa_x < x_aux):
                                                darVuelta=True
                                    else:
                                        if (cont_x > aux1 or cont_x < x_aux): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                            if (x_aux < posicion_relativa_x and posicion_relativa_x < aux1):
                                                darVuelta=True
                                contador+=1

                        if (darVuelta==True):
                            print('HEMOS DADO LA VUELTA PAR')
                        else:
                            print('NO HEMOS DADO LA VUELTA PAR')
                            x_lista_fuera_raiz.append(cont_x)
                            x_lista_fuera_raiz.append(posicion_relativa_x)
            


                                                
                        if (darVuelta==True):
                            print ('DAR VUELTA: posicion_final_x: '+ str(posicion_final_x))
                            if arriba:                                  #Queda todavía por hacer el de abajo !!!
                                maximo=0
                                
                                for y_ar in y_arriba:
                                    if (y_ar > maximo):
                                        maximo=y_ar
                                
                                maximo+=0.5
                                y_arriba.append(maximo) #Esto lo hacemos porque va a haber un arco que pase por encima del nudo 
                                x_arriba.append(cont_x)
                                x_arriba.append(-1)     #Vamos a hacer el giro en sentido antihorario
                                cont_y=maximo
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                cont_x=-1
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                minimo=0
                                for y_ab in y_abajo:
                                    if (y_ab < minimo):
                                        minimo=y_ab
                                
                                for y_ab in y_lista_fuera_raiz:
                                    if (y_ab < minimo):
                                        minimo=y_ab
                                minimo-=0.5
                                cont_y=minimo
                                x_lista_fuera_raiz.append(cont_x)
                                x_lista_fuera_raiz.append(posicion_relativa_x)
                                y_lista_fuera_raiz.append(minimo)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                arriba=False
                                

                                
                            
                            else:
                                minimo=0
                                for y_ab in y_abajo:
                                    if (y_ab < minimo):
                                        minimo=y_ab
                                
                                minimo-=0.5
                                y_abajo.append(minimo)
                                x_abajo.append(cont_x)
                                x_abajo.append(-1)
                                cont_y=minimo
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                cont_x=-1
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                maximo=0

                                for y_ar in y_arriba:
                                    if (y_ar > maximo):
                                        maximo=y_ar
                                
                                for y_ar in y_lista_fuera_raiz:
                                    if (y_ar > maximo):
                                        maximo=y_ar

                                maximo+=0.5
                                cont_y=maximo
                                x_lista_fuera_raiz.append(cont_x)
                                x_lista_fuera_raiz.append(posicion_relativa_x)
                                y_lista_fuera_raiz.append(maximo)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                arriba=True

                            if (signo=='Neg'):           
                                punto=[posicion_final_x-0.1, cont_y]
                                puntos_aux.append(punto)
                                cont_x=posicion_final_x+0.1
                            else:
                                cont_x=posicion_final_x
                                punto=[posicion_final_x, cont_y]
                                puntos_aux.append(punto)

                    
                        else:
                            if (posicion_final_x>cont_x):   #Esto simplemente es para el caso en el que sea un cruce inferior y haya que tener cuidado con el signo de 0.1
                                sig=1
                            else:
                                sig=-1

                            if not arriba:      #Si nos encontramos en la parte de abajo del nudo 
                                #Aquí hay que hacer lo de si hay que dar la vuelta
                                if not y_abajo: #Es decir, si estamos abajo
                                    y_aux_abajo=-100
                                    y_aux_arriba=0
                                    contador=0
                                    for y_aux in y_lista_fuera_raiz:
                                        if (y_aux < 0):

                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                valor_mayor=x_lista_fuera_raiz[2*contador + 1]
                                                valor_menor=x_lista_fuera_raiz[2*contador]
                                            else:
                                                valor_mayor=x_lista_fuera_raiz[2*contador]
                                                valor_menor=x_lista_fuera_raiz[2*contador+1]
                                            
                                            print ('valor_menor: ' + str(valor_menor)+ ' valor_mayor: '+ str(valor_mayor)+ ' cont_x: '+ str(cont_x)+ ' posicion_x_final: '+ str(posicion_x_final)+ ' cont_y: '+  str(cont_y)+ ' y_aux: '+ str(y_aux))
                                            if (cont_y <= y_aux):
                                                print('LLEGAAA')
                                                if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux
                                                
                                                
                                            else:
                                                if (cont_x > posicion_x_final):
                                                    if (cont_x > valor_mayor and posicion_x_final < valor_menor):
                                                        print('ahsjdhajsd')
                                                        if (y_aux < y_aux_arriba):
                                                            y_aux_arriba=y_aux
                                                
                                                else:
                                                    if (posicion_x_final > valor_mayor and cont_x < valor_menor):
                                                        if (y_aux < y_aux_arriba):
                                                            y_aux_arriba=y_aux


                                                if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                    if (y_aux > y_aux_abajo):
                                                        y_aux_abajo=y_aux
                                            
                                        contador+=1
                                    print ('y_aux_arriba: '+ str (y_aux_arriba) + ' y_aux_abajo: '+ str(y_aux_abajo))
                                    if (y_aux_arriba==0):
                                        if (y_aux_abajo==-100):
                                            cont_y=-1
                                        else:
                                            cont_y=y_aux_abajo/2

                                    else:
                                        if (y_aux_abajo==-100):
                                            cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                        else:
                                            cont_y= (y_aux_arriba + y_aux_abajo)/2
                                else:
                                    contador=0
                                        
                                    y_aux_abajo=-100
                                    y_aux_arriba=0

                                    for x_aux in x_abajo:
                                        if ((contador % 2)==0):
                                            aux1=x_aux
                                        if ((contador % 2)==1):
                                            if (x_aux>aux1):
                                                print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                                if (cont_x>aux1 and cont_x < x_aux ):
                                                    if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                        y_aux_abajo=y_abajo[int((contador-1)/2)]
                                            else:
                                                print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                                if (cont_x>x_aux and cont_x < aux1 ):
                                                    if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                        y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                    
                                            if (cont_x > posicion_x_final):
                                                if (aux1 > posicion_x_final and aux1 < cont_x):
                                                    if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                        y_aux_arriba=y_abajo[int((contador-1)/2)]
                                            else:
                                                if (aux1 > cont_x and aux1 < posicion_x_final):
                                                    if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                        y_aux_arriba=y_abajo[int((contador-1)/2)]

                                            
                                        contador+=1
                                    

                                    print ('y_aux_arriba: ' + str (y_aux_arriba))
                                    print ('y_aux_abajo: '+ str(y_aux_abajo))



                                    if (y_aux_arriba==0):
                                        if (y_aux_abajo==-100):
                                            cont_y=-1
                                        else:
                                            cont_y=y_aux_abajo/2

                                    else:
                                        if (y_aux_abajo==-100):
                                            cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                        else:
                                            cont_y= (y_aux_arriba + y_aux_abajo)/2  

                                        
                            
                            else: #Aquí no se puede dar el caso de que no exista y_arriba
                                contador=0
                                cont_y=1

                                y_aux_arriba=100
                                y_aux_abajo=0

                                for x_aux in x_arriba:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                        else:
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                
                                        if (cont_x > posicion_x_final):
                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                        else:
                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
        
                                    contador+=1
                                
                                if (y_aux_arriba==100):
                                    if (y_aux_abajo==0):
                                        cont_y=1
                                    else:
                                        cont_y=y_aux_abajo+0.5

                                else:
                                    if (y_aux_abajo==0):
                                        cont_y=y_aux_arriba/2 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                    else:
                                        cont_y= (y_aux_arriba + y_aux_abajo)/2
                            
                            if (signo=='Neg'): #cruce_inferior, llegamos hasta posicion_final_x-0.1 o +0.1
                                print('Hola impar inferior')
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                punto=[posicion_final_x-sig*0.1, cont_y]
                                puntos_aux.append(punto)
                                punto=[posicion_final_x+sig*0.1, cont_y]
                                cont_x=posicion_final_x+sig*0.1
                            else:
                                print('Hola impar superior')
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                punto=[posicion_final_x, cont_y]
                                puntos_aux.append(punto)
                                cont_x=posicion_final_x

                            y_lista_fuera_raiz.append(cont_y)

                    else:
                        x_lista_fuera_raiz.append(cont_x)
                        x_lista_fuera_raiz.append(posicion_relativa_x)
                        y_lista_fuera_raiz.append(cont_y)
                        if (posicion_final_x>cont_x):   #Esto simplemente es para el caso en el que sea un cruce inferior y haya que tener cuidado con el signo de 0.1
                            sig=1
                        else:
                            sig=-1

                        if (signo=='Pos'):
                            cont_x=posicion_final_x
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                        else:
                            punto=[posicion_final_x - sig*0.1, cont_y]
                            puntos_aux.append(punto)
                            cont_x= posicion_final_x + sig*0.1
                    acabar_aniadir_nuevo_cruce=True
                    lista_fuera_raiz.append(2*x+2)
                            
                    lista2.append(posicion_final_x)
                    
                 
            else:               #Si es la segunda vez que lo vamos a recorrer
                
                if (raiz_principal==True):
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    punto=[lista2[len(lista2)-1]+0.5, cont_y]
                    puntos_aux.append(punto)
                    raiz_principal=False   #Esta variable sirve para en caso de que volvamos y luego haya un cruce nuevo saber hacia donde nos debemos de mover en el eje x    
                print ('Cruce ' + str(2*x+2) + ' Valor asociado: '+str(valor_asociado))    
                posicion_x_final=lista2[lista.index(valor_asociado)]
                print('posicion_x_inicial: ' + str(cont_x))
                print('posicion_x_final: ' + str(posicion_x_final))



                if (acabar_aniadir_nuevo_cruce==True):
                    
                    acabar_aniadir_nuevo_cruce=False
                    if(arriba==True):
                        print('acabar_aniadir_cruce_par_arriba')
                        
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        cont_x=posicion_x_final
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        if valor_asociado in lista_fuera_raiz:
                            if (signo=='Neg'):
                                if (puntos_aux[len(puntos_aux)-2][1] < y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]): 
                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                    puntos_aux.append(punto)
                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] + 0.1
                                
                                else:
                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                    puntos_aux.append(punto)
                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] - 0.1

                            else:
                                cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                        
                        else:                               
                            if (signo=='Pos'):
                                cont_y=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                            else:
                                punto=[cont_x, 0.1]
                                puntos_aux.append(punto)
                                cont_y=-0.1
                            arriba=False

                    else:
                        print('acabar_aniadir_cruce_par_abajo')
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        cont_x=posicion_x_final
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        if valor_asociado in lista_fuera_raiz:
                            if (signo=='Neg'):
                                if (puntos_aux[len(puntos_aux)-2][1] < y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]): 
                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                    puntos_aux.append(punto)
                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] + 0.1
                                
                                else:
                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                    puntos_aux.append(punto)
                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] - 0.1

                            else:
                                cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                        
                        else:       #Esto es lo normal 
                        
                            if (signo=='Pos'):
                                cont_y=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                            else:
                                punto=[cont_x, -0.1]
                                puntos_aux.append(punto)
                                cont_y=0.1
                            arriba=True
                
                else:
                    if valor_asociado in lista_fuera_raiz:       #Es decir, si vamos a recorrer de nuevo un cruce que no está en la  'raiz principal'
                        print ('valor_asociado in lista_fuera_raiz_par')
                        punto=[cont_x, cont_y] 
                        puntos_aux.append(punto)
                        
                        indice=lista_fuera_raiz.index(valor_asociado)
                        estar_dentro=False
                        if (x_lista_fuera_raiz[2*indice]<x_lista_fuera_raiz[2*indice + 1]):
                            print ('x_lista_fuera_raiz[2*indice]: '+ str(x_lista_fuera_raiz[2*indice]) + ' x_lista_fuera_raiz[2*indice+1]: '+ str(x_lista_fuera_raiz[2*indice + 1]))
                            if (cont_x >= (x_lista_fuera_raiz[2*indice] -0.1) and cont_x <= (x_lista_fuera_raiz[2*indice + 1]+0.1)):
                                estar_dentro=True
                        else:
                            print ('x_lista_fuera_raiz[2*indice]: '+ str(x_lista_fuera_raiz[2*indice]) + ' x_lista_fuera_raiz[2*indice+1]: '+ str(x_lista_fuera_raiz[2*indice + 1]))
                            if (cont_x <= (x_lista_fuera_raiz[2*indice]+0.1) and cont_x >= (x_lista_fuera_raiz[2*indice + 1]-0.1)):
                                estar_dentro=True
                        
                        if (arriba):
                            print('arriba')
                        else:
                            print('abajo')
                        if (estar_dentro==True):
                            print('estar_dentro')

                            if (cont_y-0.1 <= y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] and cont_y+0.1 >= y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] ):
                                misma_rama=True
                                print('misma_rama')
                            else:
                                misma_rama=False
                                print('no_misma_rama')
                            
                            if (misma_rama==True):
                                print('Llega1')
                                if (not arriba):
                                    print('Llega2')
                                    if (puntos_aux[len(puntos_aux)-2][1] > cont_y):     #Falta la otra condicion pero es rara
                                        y_intermedia= y_lista_fuera_raiz[indice]-0.5
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        
                                        x_abajo.append(cont_x)
                                        x_abajo.append(posicion_x_final)
                                        y_abajo.append(y_intermedia)

                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        if (signo=='Pos'):
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1
                                    
                                    else:
                                        contador=0
                                
                                        y_aux_abajo=-100
                                        y_aux_arriba=0

                                        for x_aux in x_abajo:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                else:
                                                    print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_x_final):
                                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_abajo[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_abajo[int((contador-1)/2)]

                                                
                                            contador+=1

                                        contador=0
                                        for y_aux in y_lista_fuera_raiz:
                                            if (y_aux < 0 and y_aux > cont_y):
                                                if (contador!=indice):
                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                        
                                                        if ( x_lista_fuera_raiz[2*contador] < posicion_x_final and posicion_x_final < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                    else:
                                                        if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                        if ( x_lista_fuera_raiz[2*contador] > posicion_x_final and posicion_x_final > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux

                                            contador+=1
                                        
                                        contador=0
                                        for y_aux in y_lista_intermedia:
                                            if (y_aux < 0 and y_aux > cont_y):
                                                if (cont_x>posicion_x_final):
                                                    if (posicion_x_final <= x_arriba_lista_intermedia[contador] and x_arriba_lista_intermedia[contador] <= cont_x):
                                                        if (y_aux < y_aux_arriba):
                                                            y_aux_arriba=y_aux
                                                else:
                                                    if (cont_x <= x_arriba_lista_intermedia[contador] and x_arriba_lista_intermedia[contador] <= posicion_x_final):
                                                        if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                            contador+=1
                                        y_intermedia=(cont_y+y_aux_arriba)/2
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        
                                        x_abajo.append(cont_x)
                                        x_abajo.append(posicion_x_final)
                                        y_abajo.append(y_intermedia)

                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        if (signo=='Pos'):
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1

                                
                                else:
                                    print('Llega3')
                                    if (puntos_aux[len(puntos_aux)-2][1] < cont_y):
                                        y_intermedia= y_lista_fuera_raiz[indice]+0.5
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)

                                        x_arriba.append(cont_x)
                                        x_arriba.append(posicion_x_final)
                                        y_arriba.append(y_intermedia)

                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        if (signo=='Pos'):
                                            y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1
                                    
                                    else: 
                                        contador=0
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        

                                        y_aux_arriba=100
                                        y_aux_abajo=0

                                        for x_aux in x_arriba:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_x_final):
                                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]

                                            contador+=1


                                        contador=0
                                        for y_aux in y_lista_fuera_raiz:
                                            if (y_aux > 0 and y_aux < cont_y):
                                                if (contador!=indice):
                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                        
                                                        if ( x_lista_fuera_raiz[2*contador] < posicion_x_final and posicion_x_final < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                    else:
                                                        if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                        if ( x_lista_fuera_raiz[2*contador] > posicion_x_final and posicion_x_final > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                            contador+=1
                                        
                                        contador=0
                                        for y_aux in y_lista_intermedia:
                                            if (y_aux > 0 and y_aux < cont_y):
                                                if (cont_x>posicion_x_final):
                                                    if (posicion_x_final <= x_abajo_lista_intermedia[contador] and x_abajo_lista_intermedia[contador] <= cont_x):
                                                        if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                else:
                                                    if (cont_x <= x_abajo_lista_intermedia[contador] and x_abajo_lista_intermedia[contador] <= posicion_x_final):
                                                        if (y_aux > y_aux_abajo):
                                                            y_aux_abajo=y_aux
                                            contador+=1




                                        y_intermedia=(cont_y+y_aux_abajo)/2
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        
                                        x_abajo.append(cont_x)
                                        x_abajo.append(posicion_x_final)
                                        y_abajo.append(y_intermedia)

                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        if (signo=='Pos'):
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1

                            else:
                                

                                y_intermedia=( (cont_y+y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)])/2)
                                punto=[cont_x, y_intermedia]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)

                                
                                y_lista_intermedia.append(y_intermedia)
                                if (y_intermedia < cont_y):
                                    x_arriba_lista_intermedia.append(cont_x)
                                    x_abajo_lista_intermedia.append(posicion_x_final)
                                    
                                else:
                                    x_abajo_lista_intermedia.append(cont_x)
                                    x_arriba_lista_intermedia.append(posicion_x_final)  
                                   

                                cont_x=posicion_x_final
                                punto=[cont_x, y_intermedia]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)

                                if (signo=='Pos'): #Si el cruce es superior
                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                else:
                                    if (y_intermedia < cont_y):
                                        punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                        puntos_aux.append(punto)
                                        cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1
                                    else:
                                        punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                        puntos_aux.append(punto)
                                        cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1
                        
                        else:
                            if (arriba==True):
                                contador=0

                                y_aux_arriba=100
                                y_aux_abajo=0

                                for x_aux in x_arriba:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                        else:
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                
                                        if (cont_x > posicion_x_final):
                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                        else:
                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
    
                                    contador+=1
                                
                                if (-0.1 <= cont_y and cont_y <=0.1):
                                    for y_aux in y_lista_fuera_raiz:
                                        if (y_aux > 0):
                                            if (contador!=indice):
                                                if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                    if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                        if (y_aux < y_aux_arriba):
                                                            y_aux_arriba=y_aux
                                                else:
                                                    if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                        if (y_aux < y_aux_arriba):
                                                            y_aux_arriba=y_aux

                                        contador+=1

                                if (y_aux_arriba==100):
                                    y_aux_arriba=y_lista_fuera_raiz[indice]+1 #Para que al dividir por 2 me quede +0.5

                                y_intermedia= (y_lista_fuera_raiz[indice]+y_aux_arriba)/2
                                punto=[cont_x, y_intermedia]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                cont_x=posicion_x_final
                                punto=[cont_x, y_intermedia]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                if (signo=='Pos'):
                                    cont_y=y_lista_fuera_raiz[indice]
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                else:
                                    punto=[cont_x, y_lista_fuera_raiz[indice]+0.1]
                                    puntos_aux.append(punto)
                                    cont_y=y_lista_fuera_raiz[indice] - 0.1
                            
                            else:
                                contador=0
                                        

                                y_aux_abajo=-100
                                y_aux_arriba=0

                                for x_aux in x_abajo:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                        else:
                                            print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                
                                        if (cont_x > posicion_x_final):
                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]
                                        else:
                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]

                                        
                                    contador+=1
                                
                                contador=0
                                if (-0.1 <= cont_y and cont_y <=0.1):
                                    for y_aux in y_lista_fuera_raiz:
                                        if (y_aux < 0):
                                            if (contador!=indice):
                                                if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                    if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                        if (y_aux > y_aux_abajo):
                                                            y_aux_abajo=y_aux
                                                else:
                                                    if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                        if (y_aux > y_aux_abajo):
                                                            y_aux_abajo=y_aux

                                        contador+=1
                                        
                                if (y_aux_abajo==-100):
                                    y_aux_abajo=y_lista_fuera_raiz[indice]-1 #Para que al dividir entre 2 se le reste 0.5 a la original

                                y_intermedia= (y_lista_fuera_raiz[indice]+y_aux_abajo)/2
                                punto=[cont_x, y_intermedia]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                cont_x=posicion_x_final
                                punto=[cont_x, y_intermedia]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                if (signo=='Pos'):
                                    cont_y=y_lista_fuera_raiz[indice]
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                else:
                                    punto=[cont_x, y_lista_fuera_raiz[indice]-0.1]
                                    puntos_aux.append(punto)
                                    cont_y=y_lista_fuera_raiz[indice] + 0.1

                        
                                            

                    else:
                        if arriba:     
                            arriba=False
                            if not y_arriba:                    #si es la primera vez que se va a pasar dos veces por el mismo cruce
                                y_arriba.append(1)
                                cont_x=lista2[len(lista2)-1]+0.5
                                x_1=cont_x
                                x_2=posicion_x_final
                                x_arriba.append(x_1)
                                x_arriba.append(x_2)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                punto=[cont_x, y_arriba[len(y_arriba)-1]]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                print (x_arriba[len(x_arriba)-1])
                                punto=[x_arriba[len(x_arriba)-1], y_arriba[len(y_arriba)-1]]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                
                                if 2*x+2 not in self.__numeros: #Es decir, si el cruce es inferior
                                    punto=[x_arriba[len(x_arriba)-1], 0.1]
                                    cont_y=-0.1
                                else:
                                    punto=[x_arriba[len(x_arriba)-1], 0]
                                    cont_y=0

                                puntos_aux.append(punto)

                                    
                                '''Dado que estamos en el caso de que y_arriba estuviera vacío, y_abajo también estará vacío, por tanto añadimos el valor -1'''
                                
                                

                                cont_x=posicion_x_final
                                #puntos_aux.append(punto)
                                
                            
                            else: #si ya han sido varias veces las que se va a ir por encima del nudo (es decir, ahora la y no va a poder ser 1)
                                print('y_arriba_par: ')
                                


                                darVuelta=False
                                contador=0
                                for x_aux in x_arriba:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (aux1 > x_aux):
                                            x_mayor=aux1
                                            x_menor=x_aux

                                        else:
                                            x_mayor=x_aux
                                            x_menor=aux1

                                        if (cont_x < x_menor or cont_x > x_mayor):
                                            if (x_menor < posicion_x_final and posicion_x_final < x_mayor):
                                                darVuelta=True
                                        

                                        
                                    contador+=1
                                
                                if (darVuelta==True):   #Esto es para reutilizar código
                                    posicion_relativa_x=posicion_x_final
                                    posicion_x_final=-1 #Dado que vamos a dar la vuelta 

                                
                                contador=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                

                                y_aux_arriba=100
                                y_aux_abajo=0

                                for x_aux in x_arriba:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                        else:
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                
                                        if (cont_x > posicion_x_final):
                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                        else:
                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]

                                    contador+=1
                                
                                contador=0
                                for y_aux in y_lista_fuera_raiz:
                                    if (y_aux > 0):
                                        if (cont_y >= y_aux):
                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux > y_aux_abajo):
                                                        y_aux_abajo=y_aux
                                            else:
                                                if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux > y_aux_abajo):
                                                        y_aux_abajo=y_aux
                                        else:
                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux
                                            else:
                                                if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux

                                    contador+=1
                                
                                if (y_aux_arriba==100):
                                    if (y_aux_abajo==0):
                                        cont_y=1
                                    else:
                                        cont_y=y_aux_abajo+0.5

                                else:
                                    if (y_aux_abajo==0):
                                        cont_y=y_aux_arriba/2 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                    else:
                                        cont_y= (y_aux_arriba + y_aux_abajo)/2  

                                print('cont_y_after_impar: '+ str(cont_y))
                                y_arriba.append(cont_y)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                x_arriba.append(cont_x)
                                x_arriba.append(posicion_x_final)
                                cont_x=posicion_x_final
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)

                                if (darVuelta==True):
                                    minimo=0
                                    for y_ab in y_abajo:
                                        if (y_ab < minimo):
                                            minimo=y_ab
                                    
                                    for y_ab in y_lista_fuera_raiz:
                                        if (y_ab < minimo):
                                            minimo=y_ab
                                    
                                    minimo-=0.5
                                    cont_y=minimo
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    puntos_aux.append(punto)

                                    y_abajo.append(minimo)
                                    x_abajo.append(cont_x)
                                    x_abajo.append(posicion_relativa_x)

                                    cont_x=posicion_relativa_x
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    puntos_aux.append(punto)
                                    print('DA VUELTA impar arriba')
                                    arriba=True #Porque vamos a seguir estando arriba
                                    

                                
                                if (signo=='Neg'): #Es decir, si el cruce es inferior
                                    if (darVuelta==True):
                                        punto=[cont_x, -0.1]
                                        cont_y=0.1
                                    else:
                                        punto=[cont_x, 0.1]
                                        cont_y=-0.1
                                    puntos_aux.append(punto)
                                    
                                else:
                                    cont_y=0
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    
                                values = ','.join(str(v) for v in puntos_aux)
                                
                                print ('lista: ')
                                print(lista)
                                print('lista2: ')
                                print(lista2)
                                
                                
                        
                        
                        
                        else:
                            arriba=True
                            if not y_abajo:
                                print ('not_y_abajo_par')
                                print (y_lista_fuera_raiz)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)

                                y_aux_abajo=-100
                                y_aux_arriba=0
                                contador=0
                                for y_aux in y_lista_fuera_raiz:
                                    if (y_aux < 0):

                                        if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                            valor_mayor=x_lista_fuera_raiz[2*contador + 1]
                                            valor_menor=x_lista_fuera_raiz[2*contador]
                                        else:
                                            valor_mayor=x_lista_fuera_raiz[2*contador]
                                            valor_menor=x_lista_fuera_raiz[2*contador+1]
                                        
                                        print ('valor_menor: ' + str(valor_menor)+ ' valor_mayor: '+ str(valor_mayor)+ ' cont_x: '+ str(cont_x)+ ' posicion_x_final: '+ str(posicion_x_final)+ ' cont_y: '+  str(cont_y)+ ' y_aux: '+ str(y_aux))
                                        if (cont_y <= y_aux):
                                            print('LLEGAAA')
                                            if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                if (y_aux < y_aux_arriba):
                                                    y_aux_arriba=y_aux
                                            
                                            
                                        else:
                                            if (cont_x > posicion_x_final):
                                                if (cont_x > valor_mayor and posicion_x_final < valor_menor):
                                                    print('ahsjdhajsd')
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux
                                            
                                            else:
                                                if (posicion_x_final > valor_mayor and cont_x < valor_menor):
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux


                                            if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                if (y_aux > y_aux_abajo):
                                                    y_aux_abajo=y_aux
                                        
                                    contador+=1
                                print ('y_aux_arriba: '+ str (y_aux_arriba) + ' y_aux_abajo: '+ str(y_aux_abajo))
                                if (y_aux_arriba==0):
                                    if (y_aux_abajo==-100):
                                        cont_y=-1
                                    else:
                                        cont_y=y_aux_abajo/2

                                else:
                                    if (y_aux_abajo==-100):
                                        cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                    else:
                                        cont_y= (y_aux_arriba + y_aux_abajo)/2  

                                y_abajo.append(cont_y)

                                punto=[cont_x, y_abajo[len(y_abajo)-1]]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                x_abajo.append(cont_x)
                                x_abajo.append(posicion_x_final)
                                punto=[x_abajo[len(x_abajo)-1], y_abajo[len(y_abajo)-1]]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                cont_x=posicion_x_final
                                if 2*x+2 in self.__numeros: #Es decir, si el cruce es superior llegará hasta el cero 
                                    cont_y=0
                                    punto=[cont_x,cont_y]
                                else:
                                    cont_y=0.1  #Es decir ponemos que se continúe a partir del 0.1 pero metemos en los puntos el -0.1
                                    punto=[cont_x, -0.1]
                                    
                                puntos_aux.append(punto)  
                            else:
                                print('y_abajo_par')

                                darVuelta=False
                                contador=0
                                for x_aux in x_abajo:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (aux1 > x_aux):
                                            x_mayor=aux1
                                            x_menor=x_aux

                                        else:
                                            x_mayor=x_aux
                                            x_menor=aux1

                                        if (cont_x < x_menor or cont_x > x_mayor):
                                            if (x_menor < posicion_x_final and posicion_x_final < x_mayor):
                                                darVuelta=True
                                        

                                        
                                    contador+=1
                                
                                if (darVuelta==True):   #Esto es para reutilizar código
                                    posicion_relativa_x=posicion_x_final
                                    posicion_x_final=-1 #Dado que vamos a dar la vuelta 

                                



                                contador=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                

                                y_aux_abajo=-100
                                y_aux_arriba=0

                                for x_aux in x_abajo:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                        else:
                                            print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                
                                        if (cont_x > posicion_x_final):
                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]
                                        else:
                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]

                                        
                                    contador+=1
                                

                                contador=0
                                for y_aux in y_lista_fuera_raiz:
                                    if (y_aux < 0):
                                        if (cont_y <= y_aux):
                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux
                                            else:
                                                if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux < y_aux_arriba):
                                                        y_aux_arriba=y_aux
                                        else:
                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux > y_aux_abajo):
                                                        y_aux_abajo=y_aux
                                            else:
                                                if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                    if (y_aux > y_aux_abajo):
                                                        y_aux_abajo=y_aux

                                    contador+=1

                                print ('y_aux_arriba: ' + str (y_aux_arriba))
                                print ('y_aux_abajo: '+ str(y_aux_abajo))


                                if (y_aux_arriba==0):
                                    if (y_aux_abajo==-100):
                                        cont_y=-1
                                    else:
                                        cont_y=y_aux_abajo/2

                                else:
                                    if (y_aux_abajo==-100):
                                        cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                    else:
                                        cont_y= (y_aux_arriba + y_aux_abajo)/2  


                                    
                                y_abajo.append(cont_y)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                x_abajo.append(cont_x)
                                x_abajo.append(posicion_x_final)
                                cont_x=posicion_x_final
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)

                                if (darVuelta==True):
                                    maximo=0
                                    for y_ar in y_arriba:
                                        if (y_ar > maximo):
                                            maximo=y_ar
                                    
                                    for y_ar in y_lista_fuera_raiz:
                                        if (y_ar > maximo):
                                            maximo=y_ar
                                    
                                    maximo+=0.5
                                    cont_y=maximo
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    puntos_aux.append(punto)

                                    y_arriba.append(maximo)
                                    x_arriba.append(cont_x)
                                    x_arriba.append(posicion_relativa_x)

                                    cont_x=posicion_relativa_x
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    puntos_aux.append(punto)
                                    print('DA VUELTA par')
                                    abajo=True
                                
                                if (signo=='Neg'): #Es decir, si el cruce es inferior
                                    if (darVuelta==False):
                                        punto=[cont_x, -0.1]
                                        cont_y=0.1
                                    else:
                                        punto=[cont_x, 0.1]
                                        cont_y=-0.1
                                    puntos_aux.append(punto)
                                    
                                else:
                                    cont_y=0
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    
                                
                                
                        
                        
                    
                lista2.append(cont_x)
            
            values = ','.join(str(v) for v in puntos_aux)
                                
            print ('Puntos nuevos: ' + values)
            lista.append(2*x+2)
            




            #Valores impares

            if (x!=(len(self.__numeros)-1)):  #Si no estamos en la última iteración del vector
                
                if (indice_permutacion != x):
                    volver=False
                    if abs(self.__numeros[x+1]) in lista:
                        print(str(2*x+3)+' '+ str(abs(self.__numeros[x+1])))
                        volver=True
                    
                    if (self.__numeros[x+1]>0):   
                        signo='Neg'
                    else:
                        signo='Pos'
                        
                        
                    if (volver==False):             #Si es un punto nuevo
                        if (raiz_principal==True):
                           
                        
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            
                            posicion_x_final=cont_x+1
                            print ('Contador: '+ str(cont_x) + ' cruce '+ str(2*x+2))
                            if (signo=='Neg'):
                                punto=[posicion_x_final-0.1,cont_y]
                                puntos_aux.append(punto)
                                cont_x=posicion_x_final+0.1
                                
                            else:
                                cont_x=posicion_x_final
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                
                            lista2.append(posicion_x_final)  

                        else:
                            print('Holaaaaaa impar '+ str(cont_y))
                            print ('x: '+ str(x))
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            print(lista)
                            aux=False
                            contador_aux=0
                            contador_ya_lista=0
                            while(aux==False):
                                contador_aux+=1
                                print('contador_aux: ' + str(contador_aux) + ' suma: '+ str(contador_aux+ 2*x+3) + ' len: '+ str (len(self.__numeros)))
                                if (int(contador_aux+ 2*x+3)==(2*len(self.__numeros)+1)): #Caso en el que podamos dividir en dos subpermutaciones
                                    aux=True
                                
                                else:

                                    if ((contador_aux)%2 ==1):      #2*x+4
                                        if 2*x+3+contador_aux in self.__numeros:
                                            vasoc=2*self.__numeros.index(2*x+3+contador_aux)+1    #Nos devuelve el número impar asociado al número par 2*x+3+contador_aux
                                            print('vasoc' + str(vasoc))
                                            if (vasoc in lista):
                                                contador_ya_lista+=1
                                                aux=True
                                        else:
                                            vasoc=2*self.__numeros.index(-(2*x+3+contador_aux))+1
                                            if (vasoc in lista):
                                                contador_ya_lista+=1
                                                aux=True 
                                        
                                    else:
                                        if (abs(self.__numeros[int(x+1+contador_aux/2)]) in lista ):
                                            contador_ya_lista+=1
                                            if (abs(self.__numeros[int(x+1+contador_aux/2)]) not in lista_fuera_raiz):
                                                aux=True

                            print ('contador_ya_lista: ' + str(contador_ya_lista))     
                            print('contador_aux: '+ str(contador_aux))
                            
                            if (int(contador_aux/2+x+1)==len(self.__numeros)):
                                posicion_relativa_x=-0.5
                                fragmentos=(contador_aux-contador_ya_lista) #Esto es para ver en el número de fragmentos que se va a dividir el fragmento 
                                posicion_final_x= (cont_x*fragmentos/2 + posicion_relativa_x) / (fragmentos/2 +1)

                            else:    
                                 
                                if ((contador_aux)%2 ==1):  
                                    posicion_relativa_x=lista2[lista.index(vasoc)]
                                else:
                                    posicion_relativa_x=lista2[lista.index(abs(self.__numeros[int (x+1+contador_aux/2)]))]
                                posicion_final_x=(cont_x*contador_aux + posicion_relativa_x)/(contador_aux+1) 
                            
                            print('cont_x: '+ str(cont_x))
                            print('posicion_relativa_x: '+ str(posicion_relativa_x))
                                
                            print('posicion_final_x: '+ str(posicion_final_x))


                            
                            '''Hay que ver si hay que dar la vuelta por uno de los extremos'''
                            
                            
                            if (acabar_aniadir_nuevo_cruce==False):
                                darVuelta=False
                                if arriba:
                                    print ('x_arriba')
                                    print(x_arriba)
                                    contador=0
                                    for x_aux in x_arriba:
                                        if ((contador % 2)==0):
                                            aux1=x_aux
                                        if ((contador % 2)==1):
                                            
                                            if (x_aux > aux1):
                                                if (cont_x > x_aux or cont_x < aux1): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                                    if (aux1 < posicion_relativa_x and posicion_relativa_x < x_aux):
                                                        darVuelta=True
                                            else:
                                                if (cont_x > aux1 or cont_x < x_aux): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                                    if (x_aux < posicion_relativa_x and posicion_relativa_x < aux1):
                                                        darVuelta=True
                                        contador+=1
                                    
                                    
                                else:
                                    contador=0
                                    for x_aux in x_abajo:
                                        if ((contador % 2)==0):
                                            aux1=x_aux
                                        if ((contador % 2)==1):
                                            if (x_aux > aux1):
                                                if (cont_x > x_aux or cont_x < aux1): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                                    if (aux1 < posicion_relativa_x and posicion_relativa_x < x_aux):
                                                        darVuelta=True
                                            else:
                                                if (cont_x > aux1 or cont_x < x_aux): #Es decir, solo daremos la vuelta si no estamos encerrados actualmente
                                                    if (x_aux < posicion_relativa_x and posicion_relativa_x < aux1):
                                                        darVuelta=True
                                        contador+=1

                                

                                if (darVuelta==True):
                                    print('HEMOS DADO LA VUELTA IMPAR')
                                else:
                                    print('NO HEMOS DADO LA VUELTA IMPAR')
                                    x_lista_fuera_raiz.append(cont_x)
                                    x_lista_fuera_raiz.append(posicion_relativa_x)


                                
                                if (darVuelta==True):
                                    print ('DAR VUELTA: posicion_final_x: '+ str(posicion_final_x))
                                    if arriba:                                  #Queda todavía por hacer el de abajo !!!
                                        maximo=0
                                        
                                        for y_ar in y_arriba:
                                            if (y_ar > maximo):
                                                maximo=y_ar
                                        
                                        maximo+=0.5
                                        y_arriba.append(maximo) #Esto lo hacemos porque va a haber un arco que pase por encima del nudo 
                                        x_arriba.append(cont_x)
                                        x_arriba.append(-1)     #Vamos a hacer el giro en sentido antihorario
                                        cont_y=maximo
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        cont_x=-1
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        minimo=0
                                        for y_ab in y_abajo:
                                            if (y_ab < minimo):
                                                minimo=y_ab
                                        
                                        for y_ab in y_lista_fuera_raiz:
                                            if (y_ab < minimo):
                                                minimo=y_ab
                                        minimo-=0.5
                                        cont_y=minimo
                                        x_lista_fuera_raiz.append(cont_x)
                                        x_lista_fuera_raiz.append(posicion_relativa_x)
                                        y_lista_fuera_raiz.append(minimo)
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        arriba=False
                                        

                                        
                                    
                                    else:
                                        minimo=0
                                        for y_ab in y_abajo:
                                            if (y_ab < minimo):
                                                minimo=y_ab
                                        
                                        minimo-=0.5
                                        y_abajo.append(minimo)
                                        x_abajo.append(cont_x)
                                        x_abajo.append(-1)
                                        cont_y=minimo
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        cont_x=-1
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        minimo=0

                                        for y_ar in y_arriba:
                                            if (y_ar > maximo):
                                                maximo=y_ar
                                        
                                        for y_ar in y_lista_fuera_raiz:
                                            if (y_ar > maximo):
                                                maximo=y_ar
                                        maximo+=0.5
                                        cont_y=maximo
                                        x_lista_fuera_raiz.append(cont_x)
                                        x_lista_fuera_raiz.append(posicion_relativa_x)
                                        y_lista_fuera_raiz.append(maximo)
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        arriba=True

                                    if (signo=='Neg'):           
                                        punto=[posicion_final_x-0.1, cont_y]
                                        puntos_aux.append(punto)
                                        cont_x=posicion_final_x+0.1
                                    else:
                                        cont_x=posicion_final_x
                                        punto=[posicion_final_x, cont_y]
                                        puntos_aux.append(punto)

                                else:
                                    print('posicion_final_x: '+ str(posicion_final_x)+ ' cont_x: '+ str (cont_x))
                                    if (posicion_final_x>cont_x):   #Esto simplemente es para el caso en el que sea un cruce inferior y haya que tener cuidado con el signo de 0.1
                                        sig=1
                                    else:
                                        sig=-1

                                    if not arriba:      #Si nos encontramos en la parte de abajo del nudo 
                                        print ('Llegamos ')
                                        #Aquí hay que hacer lo de si hay que dar la vuelta
                                        if not y_abajo: #Es decir, si estamos abajo

                                           

                                            y_aux_abajo=-100
                                            y_aux_arriba=0
                                            contador=0
                                            for y_aux in y_lista_fuera_raiz:
                                                if (y_aux < 0):

                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        valor_mayor=x_lista_fuera_raiz[2*contador + 1]
                                                        valor_menor=x_lista_fuera_raiz[2*contador]
                                                    else:
                                                        valor_mayor=x_lista_fuera_raiz[2*contador]
                                                        valor_menor=x_lista_fuera_raiz[2*contador+1]
                                                    
                                                    print ('valor_menor: ' + str(valor_menor)+ ' valor_mayor: '+ str(valor_mayor)+ ' cont_x: '+ str(cont_x)+ ' posicion_x_final: '+ str(posicion_x_final)+ ' cont_y: '+  str(cont_y)+ ' y_aux: '+ str(y_aux))
                                                    if (cont_y <= y_aux):
                                                        print('LLEGAAA')
                                                        if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                        
                                                        
                                                    else:
                                                        if (cont_x > posicion_x_final):
                                                            if (cont_x > valor_mayor and posicion_x_final < valor_menor):
                                                                print('ahsjdhajsd')
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux
                                                        
                                                        else:
                                                            if (posicion_x_final > valor_mayor and cont_x < valor_menor):
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux


                                                        if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                    
                                                contador+=1
                                            print ('y_aux_arriba: '+ str (y_aux_arriba) + ' y_aux_abajo: '+ str(y_aux_abajo))
                                            if (y_aux_arriba==0):
                                                if (y_aux_abajo==-100):
                                                    cont_y=-1
                                                else:
                                                    cont_y=y_aux_abajo/2

                                            else:
                                                if (y_aux_abajo==-100):
                                                    cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                                else:
                                                    cont_y= (y_aux_arriba + y_aux_abajo)/2


                                            
                                        else:
                                            contador=0
                                            
                                            y_aux_abajo=-100
                                            y_aux_arriba=0

                                            for x_aux in x_abajo:
                                                if ((contador % 2)==0):
                                                    aux1=x_aux
                                                if ((contador % 2)==1):
                                                    if (x_aux>aux1):
                                                        print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                                        if (cont_x>aux1 and cont_x < x_aux ):
                                                            if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                                y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                    else:
                                                        print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                                        if (cont_x>x_aux and cont_x < aux1 ):
                                                            if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                                y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                            
                                                    if (cont_x > posicion_relativa_x):
                                                        if (aux1 > posicion_relativa_x and aux1 < cont_x):
                                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                                y_aux_arriba=y_abajo[int((contador-1)/2)]
                                                    else:
                                                        if (aux1 > cont_x and aux1 < posicion_relativa_x):
                                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                                y_aux_arriba=y_abajo[int((contador-1)/2)]

                                                    
                                                contador+=1
                                            
                                            contador=0
                                            for y_aux in y_lista_fuera_raiz:
                                                if (y_aux < 0):
                                                    if (cont_y <= y_aux):
                                                        if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                            if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux
                                                        else:
                                                            if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux
                                                    else:
                                                        if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                            if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux > y_aux_abajo):
                                                                    y_aux_abajo=y_aux
                                                        else:
                                                            if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux > y_aux_abajo):
                                                                    y_aux_abajo=y_aux

                                                contador+=1
                                            print ('y_aux_arriba: ' + str (y_aux_arriba))
                                            print ('y_aux_abajo: '+ str(y_aux_abajo))



                                            if (y_aux_arriba==0):
                                                if (y_aux_abajo==-100):
                                                    cont_y=-1
                                                else:
                                                    cont_y=y_aux_abajo/2

                                            else:
                                                if (y_aux_abajo==-100):
                                                    cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                                else:
                                                    cont_y= (y_aux_arriba + y_aux_abajo)/2  
        
                                                
                                    
                                    else: #Aquí no se puede dar el caso de que no exista y_arriba
                                        contador=0
                                        cont_y=1

                                        y_aux_arriba=100
                                        y_aux_abajo=0

                                        for x_aux in x_arriba:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_relativa_x):
                                                    if (aux1 > posicion_relativa_x and aux1 < cont_x):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_relativa_x):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
                
                                            contador+=1
                                        
                                        if (y_aux_arriba==100):
                                            if (y_aux_abajo==0):
                                                cont_y=1
                                            else:
                                                cont_y=y_aux_abajo+0.5

                                        else:
                                            if (y_aux_abajo==0):
                                                cont_y=y_aux_arriba/2 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                            else:
                                                cont_y= (y_aux_arriba + y_aux_abajo)/2


                                    if (signo=='Neg'): #cruce_inferior, llegamos hasta posicion_final_x-0.1 o +0.1
                                        print('Hola impar inferior')
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        punto=[posicion_final_x-sig*0.1, cont_y]
                                        puntos_aux.append(punto)
                                        punto=[posicion_final_x+sig*0.1, cont_y]
                                        cont_x=posicion_final_x+sig*0.1
                                    else:
                                        print('Hola impar superior')
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        punto=[posicion_final_x, cont_y]
                                        puntos_aux.append(punto)
                                        cont_x=posicion_final_x

                                    y_lista_fuera_raiz.append(cont_y)

                            else:
                                x_lista_fuera_raiz.append(cont_x)
                                x_lista_fuera_raiz.append(posicion_final_x)
                                y_lista_fuera_raiz.append(cont_y)
                                print('Acabar aniadir cruce impar ' + signo)
                                if (posicion_final_x>cont_x):   #Esto simplemente es para el caso en el que sea un cruce inferior y haya que tener cuidado con el signo de 0.1
                                    sig=1
                                else:
                                    sig=-1

                                if (signo=='Pos'):
                                    cont_x=posicion_final_x
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                else:
                                    punto=[posicion_final_x - sig*0.1, cont_y]
                                    puntos_aux.append(punto)
                                    cont_x= posicion_final_x + sig*0.1
                            acabar_aniadir_nuevo_cruce=True
                            lista_fuera_raiz.append(2*x+3)
                                
                            lista2.append(posicion_final_x)
                            
                
                
                                    
                    else:           #Si es la segunda vez que lo vamos a recorrer
                        

                        if (raiz_principal==True):
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            punto=[lista2[len(lista2)-1]+0.5, cont_y]
                            puntos_aux.append(punto)
                            raiz_principal=False   #Esta variable sirve para en caso de que volvamos y luego haya un cruce nuevo saber hacia donde nos debemos de mover en el eje x    
                        
                        posicion_x_final=lista2[lista.index(abs(self.__numeros[x+1]))]
                        
                        if (acabar_aniadir_nuevo_cruce==True):
                            acabar_aniadir_nuevo_cruce=False
                            if(arriba==True):
                                print('acabar_aniadir_cruce_impar_arriba')
                                #y_arriba.append(cont_y)
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                cont_x=posicion_x_final
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)

                                if valor_asociado in lista_fuera_raiz:
                                    if (signo=='Neg'):
                                        if (puntos_aux[len(puntos_aux)-2][1] < y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]): 
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] + 0.1
                                        
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] - 0.1

                                    else:
                                        cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                
                                else:

                                    if (signo=='Pos'):
                                        cont_y=0
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                    else:
                                        punto=[cont_x, 0.1]
                                        puntos_aux.append(punto)
                                        cont_y=-0.1
                                    arriba=False

                            else:
                                print('acabar_aniadir_cruce_impar_abajo')
                                #y_abajo.append(cont_y)

                                

                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                cont_x=posicion_x_final
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                puntos_aux.append(punto)
                                if valor_asociado in lista_fuera_raiz:
                                    if (signo=='Neg'):
                                        if (puntos_aux[len(puntos_aux)-2][1] < y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]): 
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] + 0.1
                                        
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] - 0.1

                                    else:
                                        cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                
                                else:
                                    if (signo=='Pos'):
                                        cont_y=0
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                    else:
                                        punto=[cont_x, -0.1]
                                        puntos_aux.append(punto)
                                        cont_y=0.1
                                    arriba=True
                        else:

                            if abs(self.__numeros[x+1]) in lista_fuera_raiz: #Es decir, si el número asociado a ese número impar no está en la raíz 
                                print ('valor_asociado in lista_fuera_raiz_impar')
                                valor_asociado=abs(self.__numeros[x+1])
                                punto=[cont_x, cont_y] 
                                puntos_aux.append(punto)
                                
                                indice=lista_fuera_raiz.index(valor_asociado)
                                estar_dentro=False
                                if (x_lista_fuera_raiz[2*indice]<x_lista_fuera_raiz[2*indice + 1]):
                                    if (cont_x >= (x_lista_fuera_raiz[2*indice]-0.1) and cont_x <= (x_lista_fuera_raiz[2*indice + 1]+0.1)):
                                        estar_dentro=True
                                else:
                                    if (cont_x <= (x_lista_fuera_raiz[2*indice]+0.1) and cont_x >= (x_lista_fuera_raiz[2*indice + 1]-0.1)):
                                        estar_dentro=True
                                

                                if (estar_dentro==True):
                                    print ('estar_dentro')
                                    if (cont_y-0.1 <= y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] and cont_y+0.1 >= y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)] ):
                                        misma_rama=True
                                        print('misma_rama')
                                    else:
                                        misma_rama=False
                                        print('no_misma_rama')

                                    if (misma_rama==True):
                                        if (not arriba):
                                            print('Llega2')
                                            if (puntos_aux[len(puntos_aux)-2][1] > cont_y):     #Falta la otra condicion pero es rara
                                                y_intermedia= y_lista_fuera_raiz[indice]-0.5
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                
                                                x_abajo.append(cont_x)
                                                x_abajo.append(posicion_x_final)
                                                y_abajo.append(y_intermedia)

                                                cont_x=posicion_x_final
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                if (signo=='Pos'):
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                                    punto=[cont_x, cont_y]
                                                    puntos_aux.append(punto)
                                                else:
                                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                                    puntos_aux.append(punto)
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1
                                            
                                            else:
                                                contador=0
                                        
                                                y_aux_abajo=-100
                                                y_aux_arriba=0

                                                for x_aux in x_abajo:
                                                    if ((contador % 2)==0):
                                                        aux1=x_aux
                                                    if ((contador % 2)==1):
                                                        if (x_aux>aux1):
                                                            print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                        else:
                                                            print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                                
                                                        if (cont_x > posicion_x_final):
                                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                                if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]
                                                        else:
                                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                                if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]

                                                        
                                                    contador+=1

                                                contador=0
                                                for y_aux in y_lista_fuera_raiz:
                                                    if (y_aux < 0 and y_aux > cont_y):
                                                        if (contador!=indice):
                                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                                if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux < y_aux_arriba):
                                                                        y_aux_arriba=y_aux
                                                                
                                                                if ( x_lista_fuera_raiz[2*contador] < posicion_x_final and posicion_x_final < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux < y_aux_arriba):
                                                                        y_aux_arriba=y_aux
                                                            else:
                                                                if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux < y_aux_arriba):
                                                                        y_aux_arriba=y_aux
                                                                if ( x_lista_fuera_raiz[2*contador] > posicion_x_final and posicion_x_final > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux < y_aux_arriba):
                                                                        y_aux_arriba=y_aux

                                                    contador+=1
                                                
                                                contador=0
                                                for y_aux in y_lista_intermedia:
                                                    if (y_aux < 0 and y_aux > cont_y):
                                                        if (cont_x>posicion_x_final):
                                                            if (posicion_x_final <= x_arriba_lista_intermedia[contador] and x_arriba_lista_intermedia[contador] <= cont_x):
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux
                                                        else:
                                                            if (cont_x <= x_arriba_lista_intermedia[contador] and x_arriba_lista_intermedia[contador] <= posicion_x_final):
                                                                if (y_aux < y_aux_arriba):
                                                                        y_aux_arriba=y_aux
                                                    contador+=1

                                                y_intermedia=(cont_y+y_aux_arriba)/2
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                
                                                x_abajo.append(cont_x)
                                                x_abajo.append(posicion_x_final)
                                                y_abajo.append(y_intermedia)

                                                cont_x=posicion_x_final
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                if (signo=='Pos'):
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                                    punto=[cont_x, cont_y]
                                                    puntos_aux.append(punto)
                                                else:
                                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                                    puntos_aux.append(punto)
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1

                                        
                                        else:
                                            print('Llega3')
                                            if (puntos_aux[len(puntos_aux)-2][1] < cont_y):
                                                y_intermedia= y_lista_fuera_raiz[indice]+0.5
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)

                                                x_arriba.append(cont_x)
                                                x_arriba.append(posicion_x_final)
                                                y_arriba.append(y_intermedia)

                                                cont_x=posicion_x_final
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                if (signo=='Pos'):
                                                    y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                                    punto=[cont_x, cont_y]
                                                    puntos_aux.append(punto)
                                                else:
                                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                                    puntos_aux.append(punto)
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1
                                            
                                            else: 
                                                contador=0
                                                punto=[cont_x, cont_y]
                                                puntos_aux.append(punto)
                                                

                                                y_aux_arriba=100
                                                y_aux_abajo=0

                                                for x_aux in x_arriba:
                                                    if ((contador % 2)==0):
                                                        aux1=x_aux
                                                    if ((contador % 2)==1):
                                                        if (x_aux>aux1):
                                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                        else:
                                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                                
                                                        if (cont_x > posicion_x_final):
                                                            if (aux1 > posicion_x_final and aux1 < cont_x):
                                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                                        else:
                                                            if (aux1 > cont_x and aux1 < posicion_x_final):
                                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]

                                                    contador+=1
                                                contador=0
                                                for y_aux in y_lista_fuera_raiz:
                                                    if (y_aux > 0 and y_aux < cont_y):
                                                        if (contador!=indice):
                                                            if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                                if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux > y_aux_abajo):
                                                                        y_aux_abajo=y_aux
                                                                
                                                                if ( x_lista_fuera_raiz[2*contador] < posicion_x_final and posicion_x_final < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux > y_aux_abajo):
                                                                        y_aux_abajo=y_aux
                                                            else:
                                                                if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux > y_aux_abajo):
                                                                        y_aux_abajo=y_aux
                                                                if ( x_lista_fuera_raiz[2*contador] > posicion_x_final and posicion_x_final > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                    if (y_aux > y_aux_abajo):
                                                                        y_aux_abajo=y_aux
                                                    contador+=1
                                                
                                                contador=0
                                                for y_aux in y_lista_intermedia:
                                                    if (y_aux > 0 and y_aux < cont_y):
                                                        if (cont_x>posicion_x_final):
                                                            if (posicion_x_final <= x_abajo_lista_intermedia[contador] and x_abajo_lista_intermedia[contador] <= cont_x):
                                                                if (y_aux > y_aux_abajo):
                                                                        y_aux_abajo=y_aux
                                                        else:
                                                            if (cont_x <= x_abajo_lista_intermedia[contador] and x_abajo_lista_intermedia[contador] <= posicion_x_final):
                                                                if (y_aux > y_aux_abajo):
                                                                    y_aux_abajo=y_aux
                                                    contador+=1

                                                y_intermedia=(cont_y+y_aux_abajo)/2
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                
                                                x_abajo.append(cont_x)
                                                x_abajo.append(posicion_x_final)
                                                y_abajo.append(y_intermedia)

                                                cont_x=posicion_x_final
                                                punto=[cont_x, y_intermedia]
                                                puntos_aux.append(punto)
                                                puntos_aux.append(punto)
                                                if (signo=='Pos'):
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                                    punto=[cont_x, cont_y]
                                                    puntos_aux.append(punto)
                                                else:
                                                    punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                                    puntos_aux.append(punto)
                                                    cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1
                                    else:
                                        y_intermedia=( (cont_y+y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)])/2)
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)

                                        if (signo=='Pos'): #Si el cruce es superior
                                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            if (y_intermedia < cont_y):
                                                punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1]
                                                puntos_aux.append(punto)
                                                cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1
                                            else:
                                                punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]-0.1]
                                                puntos_aux.append(punto)
                                                cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)]+0.1
                                
                                else:
                                    print('no estar_dentro')
                                    if (arriba==True):

                                        contador=0

                                        y_aux_arriba=100
                                        y_aux_abajo=0

                                        for x_aux in x_arriba:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_x_final):
                                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
            
                                            contador+=1
                                        
                                        contador=0
                                        
                                        if (-0.1 <= cont_y and cont_y <=0.1):
                                            for y_aux in y_lista_fuera_raiz:
                                                if (y_aux > 0):
                                                    if (contador!=indice):
                                                        if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                            if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux
                                                        else:
                                                            if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux < y_aux_arriba):
                                                                    y_aux_arriba=y_aux

                                                contador+=1

                                        if (y_aux_arriba==100):
                                            y_aux_arriba=y_lista_fuera_raiz[indice]+1 #Para que al dividir por 2 me quede +0.5

                                        y_intermedia= (y_lista_fuera_raiz[indice]+y_aux_arriba)/2
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        if (signo=='Pos'):
                                            cont_y=y_lista_fuera_raiz[indice]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[indice]+0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[indice] - 0.1
                                    
                                    else:

                                        contador=0
                                        

                                        y_aux_abajo=-100
                                        y_aux_arriba=0

                                        for x_aux in x_abajo:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                else:
                                                    print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_x_final):
                                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_abajo[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_abajo[int((contador-1)/2)]

                                                
                                            contador+=1
                                        
                                        contador=0

                                        if (-0.1 <= cont_y and cont_y <=0.1):
                                            for y_aux in y_lista_fuera_raiz:
                                                if (y_aux < 0):
                                                    if (contador!=indice):
                                                        if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                            if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux > y_aux_abajo):
                                                                    y_aux_abajo=y_aux
                                                        else:
                                                            if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                                if (y_aux > y_aux_abajo):
                                                                    y_aux_abajo=y_aux

                                                contador+=1
                                  
                                        if (y_aux_abajo==-100):
                                            y_aux_abajo=y_lista_fuera_raiz[indice]-1 #Para que al dividir entre 2 se le reste 0.5 a la original

                                        y_intermedia= (y_lista_fuera_raiz[indice]+y_aux_abajo)/2

                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        cont_x=posicion_x_final
                                        punto=[cont_x, y_intermedia]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        if (signo=='Pos'):
                                            cont_y=y_lista_fuera_raiz[indice]
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                        else:
                                            punto=[cont_x, y_lista_fuera_raiz[indice]-0.1]
                                            puntos_aux.append(punto)
                                            cont_y=y_lista_fuera_raiz[indice] + 0.1

                                
                            else:
                                if arriba:
                                    arriba=False
                                    if not y_arriba:
                                        y_arriba.append(1)
                                        cont_x=lista2[len(lista2)-1]+0.5
                                        x_1= cont_x
                                        x_2=posicion_x_final
                                        x_arriba.append(x_1)
                                        x_arriba.append(x_2)
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        punto=[cont_x, y_arriba[len(y_arriba)-1]]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        print (x_arriba[len(x_arriba)-1])
                                        punto=[x_arriba[len(x_arriba)-1], y_arriba[len(y_arriba)-1]]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        
                                        if self.__numeros[x+1]>0: #Es decir, si el cruce es inferior
                                            punto=[x_arriba[len(x_arriba)-1], 0.1]
                                            cont_y=-0.1
                                        else:
                                            punto=[x_arriba[len(x_arriba)-1], 0]
                                            cont_y=0
                                        puntos_aux.append(punto)
                                            
                                            
                                        '''Dado que estamos en el caso de que y_arriba estuviera vacío, y_abajo también estará vacío, por tanto añadimos el valor -1'''
                                        #puntos_aux.append(punto)
                                        
                                        cont_x=x_2
                                        
                                        print('cont_y= '+ str(cont_y))
                                        
                                    
                                    else:
                                        print('y_arriba_impar: ')

                                        darVuelta=False
                                        contador=0
                                        for x_aux in x_arriba:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (aux1 > x_aux):
                                                    x_mayor=aux1
                                                    x_menor=x_aux

                                                else:
                                                    x_mayor=x_aux
                                                    x_menor=aux1

                                                if (cont_x < x_menor or cont_x > x_mayor):
                                                    if (x_menor < posicion_x_final and posicion_x_final < x_mayor):
                                                        darVuelta=True
                                                

                                               
                                            contador+=1
                                        
                                        if (darVuelta==True):   #Esto es para reutilizar código
                                            posicion_relativa_x=posicion_x_final
                                            posicion_x_final=-1 #Dado que vamos a dar la vuelta 

                                        
                                        contador=0
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        cont_y=1

                                        y_aux_arriba=100
                                        y_aux_abajo=0

                                        for x_aux in x_arriba:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_x_final):
                                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
            
                                            contador+=1
                                        
                                        contador=0
                                        for y_aux in y_lista_fuera_raiz:
                                            if (y_aux > 0):
                                                if (cont_y >= y_aux):
                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                    else:
                                                        if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                else:
                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                    else:
                                                        if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux

                                            contador+=1
                                        
                                        if (y_aux_arriba==100):
                                            if (y_aux_abajo==0):
                                                cont_y=1
                                            else:
                                                cont_y=y_aux_abajo+0.5

                                        else:
                                            if (y_aux_abajo==0):
                                                cont_y=y_aux_arriba/2 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                            else:
                                                cont_y= (y_aux_arriba + y_aux_abajo)/2  

                                        print('cont_y_after_impar: '+ str(cont_y))
                                        y_arriba.append(cont_y)
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        x_arriba.append(cont_x)
                                        x_arriba.append(posicion_x_final)
                                        cont_x=posicion_x_final
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)

                                        if (darVuelta==True):
                                            minimo=0
                                            for y_ab in y_abajo:
                                                if (y_ab < minimo):
                                                    minimo=y_ab
                                            
                                            for y_ab in y_lista_fuera_raiz:
                                                if (y_ab < minimo):
                                                    minimo=y_ab
                                            
                                            minimo-=0.5
                                            cont_y=minimo
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                            puntos_aux.append(punto)

                                            y_abajo.append(minimo)
                                            x_abajo.append(cont_x)
                                            x_abajo.append(posicion_relativa_x)

                                            cont_x=posicion_relativa_x
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                            puntos_aux.append(punto)
                                            print('DA VUELTA impar arriba')
                                            arriba=True #Porque vamos a seguir estando arriba
                                            

                                        
                                        if (signo=='Neg'):   #Si el cruce es inferior...
                                            if (darVuelta==False):
                                                punto=[cont_x, 0.1]     #Lllega hasta 0.1
                                                cont_y=-0.1
                                            else:
                                                punto=[cont_x, -0.1]     #Lllega hasta 0.1
                                                cont_y=0.1
                                            puntos_aux.append(punto)
                                            

                                        else:
                                            cont_y=0
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                            
                                        print ('lista: ')
                                        print(lista)
                                        print('lista2: ')
                                        print(lista2)
                                        
                                        
                                        

                                        
                                else:
                                    arriba=True
                                    if not y_abajo:
                                        print ('not_y_abajo_impar')
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)

                                        y_aux_abajo=-100
                                        y_aux_arriba=0
                                        contador=0
                                        for y_aux in y_lista_fuera_raiz:
                                            if (y_aux < 0):

                                                if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                    valor_mayor=x_lista_fuera_raiz[2*contador + 1]
                                                    valor_menor=x_lista_fuera_raiz[2*contador]
                                                else:
                                                    valor_mayor=x_lista_fuera_raiz[2*contador]
                                                    valor_menor=x_lista_fuera_raiz[2*contador+1]
                                                
                                                print ('valor_menor: ' + str(valor_menor)+ ' valor_mayor: '+ str(valor_mayor)+ ' cont_x: '+ str(cont_x)+ ' posicion_x_final: '+ str(posicion_x_final)+ ' cont_y: '+  str(cont_y)+ ' y_aux: '+ str(y_aux))
                                                if (cont_y <= y_aux):
                                                    print('LLEGAAA')
                                                    if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                        if (y_aux < y_aux_arriba):
                                                            y_aux_arriba=y_aux
                                                    
                                                    
                                                else:
                                                    if (cont_x > posicion_x_final):
                                                        if (cont_x > valor_mayor and posicion_x_final < valor_menor):
                                                            print('ahsjdhajsd')
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                    
                                                    else:
                                                        if (posicion_x_final > valor_mayor and cont_x < valor_menor):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux


                                                    if ( valor_menor < cont_x and cont_x < valor_mayor  ):
                                                        if (y_aux > y_aux_abajo):
                                                            y_aux_abajo=y_aux
                                                
                                            contador+=1
                                        print ('y_aux_arriba: '+ str (y_aux_arriba) + ' y_aux_abajo: '+ str(y_aux_abajo))
                                        if (y_aux_arriba==0):
                                            if (y_aux_abajo==-100):
                                                cont_y=-1
                                            else:
                                                cont_y=y_aux_abajo/2

                                        else:
                                            if (y_aux_abajo==-100):
                                                cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                            else:
                                                cont_y= (y_aux_arriba + y_aux_abajo)/2  

                                        y_abajo.append(cont_y)

                                        punto=[cont_x, y_abajo[len(y_abajo)-1]]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        x_abajo.append(cont_x)
                                        x_abajo.append(posicion_x_final)
                                        punto=[x_abajo[len(x_abajo)-1], y_abajo[len(y_abajo)-1]]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        cont_x=posicion_x_final
                                        if self.__numeros[x+1]<0: #Es decir, si el cruce es superior llegará hasta el cero 
                                            cont_y=0
                                            punto=[cont_x,cont_y]
                                        else:
                                            cont_y=0.1  #Es decir ponemos que se continúe a partir del 0.1 pero metemos en los puntos el -0.1
                                            punto=[cont_x, -0.1]
                                        puntos_aux.append(punto)  
                                    
                                    else:   
                                        print('y_abajo_impar')
                                        
                                        darVuelta=False
                                        contador=0
                                        for x_aux in x_abajo:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (aux1 > x_aux):
                                                    x_mayor=aux1
                                                    x_menor=x_aux

                                                else:
                                                    x_mayor=x_aux
                                                    x_menor=aux1

                                                if (cont_x < x_menor or cont_x > x_mayor):
                                                    if (x_menor < posicion_x_final and posicion_x_final < x_mayor):
                                                        darVuelta=True
                                                

                                                
                                            contador+=1
                                        
                                        if (darVuelta==True):   #Esto es para reutilizar código
                                            posicion_relativa_x=posicion_x_final
                                            posicion_x_final=-1 #Dado que vamos a dar la vuelta 

                                        



                                        contador=0
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        

                                        y_aux_abajo=-100
                                        y_aux_arriba=0

                                        for x_aux in x_abajo:
                                            if ((contador % 2)==0):
                                                aux1=x_aux
                                            if ((contador % 2)==1):
                                                if (x_aux>aux1):
                                                    print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                                    if (cont_x>aux1 and cont_x < x_aux ):
                                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                else:
                                                    print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                                    if (cont_x>x_aux and cont_x < aux1 ):
                                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                                        
                                                if (cont_x > posicion_x_final):
                                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_abajo[int((contador-1)/2)]
                                                else:
                                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                            y_aux_arriba=y_abajo[int((contador-1)/2)]

                                                
                                            contador+=1
                                        

                                        contador=0
                                        for y_aux in y_lista_fuera_raiz:
                                            if (y_aux < 0):
                                                if (cont_y <= y_aux):
                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                    else:
                                                        if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux < y_aux_arriba):
                                                                y_aux_arriba=y_aux
                                                else:
                                                    if (x_lista_fuera_raiz[2*contador] < x_lista_fuera_raiz[2*contador + 1]):
                                                        if ( x_lista_fuera_raiz[2*contador] < cont_x and cont_x < x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux
                                                    else:
                                                        if ( x_lista_fuera_raiz[2*contador] > cont_x and cont_x > x_lista_fuera_raiz[2*contador + 1]  ):
                                                            if (y_aux > y_aux_abajo):
                                                                y_aux_abajo=y_aux

                                            contador+=1

                                        print ('y_aux_arriba: ' + str (y_aux_arriba))
                                        print ('y_aux_abajo: '+ str(y_aux_abajo))


                                        if (y_aux_arriba==0):
                                            if (y_aux_abajo==-100):
                                                cont_y=-1
                                            else:
                                                cont_y=y_aux_abajo/2

                                        else:
                                            if (y_aux_abajo==-100):
                                                cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                                            else:
                                                cont_y= (y_aux_arriba + y_aux_abajo)/2  


                                            
                                        y_abajo.append(cont_y)
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)
                                        x_abajo.append(cont_x)
                                        x_abajo.append(posicion_x_final)
                                        cont_x=posicion_x_final
                                        punto=[cont_x, cont_y]
                                        puntos_aux.append(punto)
                                        puntos_aux.append(punto)

                                        if (darVuelta==True):
                                            maximo=0
                                            for y_ar in y_arriba:
                                                if (y_ar > maximo):
                                                    maximo=y_ar
                                            
                                            for y_ar in y_lista_fuera_raiz:
                                                if (y_ar > maximo):
                                                    maximo=y_ar
                                            
                                            maximo+=0.5
                                            cont_y=maximo
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                            puntos_aux.append(punto)

                                            y_arriba.append(maximo)
                                            x_arriba.append(cont_x)
                                            x_arriba.append(posicion_relativa_x)

                                            cont_x=posicion_relativa_x
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                            puntos_aux.append(punto)
                                            print('DA VUELTA abajo impar')
                                            abajo=True
                                        
                                        if (signo=='Neg'):   #Si el cruce es inferior...
                                            if (darVuelta==False):
                                                punto=[cont_x, -0.1]     #Lllega hasta 0.1
                                                cont_y=0.1
                                            else:
                                                punto=[cont_x, 0.1]     #Lllega hasta 0.1
                                                cont_y=-0.1
                                            puntos_aux.append(punto)

                                        else:
                                            cont_y=0
                                            punto=[cont_x, cont_y]
                                            puntos_aux.append(punto)
                                            
                                        
                                        
                        
                    
                        lista2.append(cont_x)
                    lista.append(2*x+3)


                else:
                    print('indice_permutacion==x')
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)

                    for y_aux in y_arriba:              #Esto es para almacenar el valor máximo y minimo de la coordenada y de la raiz anterior, ya que vamos a borrar toda la informacion anterior
                        if (y_aux>maximo_raiz_antigua):
                            maximo_raiz_antigua=y_aux

                    
                    for y_aux in y_abajo:
                        if (y_aux < minimo_raiz_antigua):
                            minimo_raiz_antigua=y_aux

                    maximo_x=0
                    for x_cruces in lista2:
                        if (x_cruces>maximo_x):
                            maximo_x=x_cruces

                    if arriba: #revisar por si se pudiera hacer más formal 
                        maximo_raiz_antigua+=0.5
                        cont_y=maximo_raiz_antigua
                    
                    else:
                        minimo_raiz_antigua-=0.5
                        cont_y=minimo_raiz_antigua
                    
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    cont_x=maximo_x+1

                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)

                    cont_y=0
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    cont_x+=0.5
                    posicion_x_final=cont_x
                    if (self.__numeros[x+1]>0):   #signo negativo
                        punto=[cont_x-0.1, cont_y]
                        puntos_aux.append(punto)
                        cont_x+=0.1
                        
                        
                    else:
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)

                    y_arriba.clear() #Lista que nos indicará la altura de las aristas que pasen por encima del nudo
                    x_arriba.clear() #Lista de listas que nos indicará el valor mínimo y máximo de x para la altura y del vector de arriba    
                    y_abajo.clear()
                    x_abajo.clear()
                    
                    y_lista_fuera_raiz.clear()
                    lista_fuera_raiz.clear()
                    x_lista_fuera_raiz.clear()
                    raiz_principal=True
                    arriba=True
                    '''Eliminamos todas los datos de las listas utilizadas hasta ahora'''
                    lista.append(2*x+3)
                    lista2.append(posicion_x_final)



            
            else:       #Es decir, que haya que volver al 1 
                print('Ultimo punto')
                punto=[cont_x, cont_y]
                puntos_aux.append(punto)
                posicion_x_final=-0.5 #Dado que es el ultimo punto
                contador=0

                if (lista[len(lista)-1] in self.__numeros):   #Tomamos su valor asociado
                    vasoc=2*self.__numeros.index(lista[len(lista)-1])+1
                else:
                    vasoc=2*self.__numeros.index(- lista[len(lista)-1])+1

                if (vasoc in lista_fuera_raiz):
                    y_fuera_raiz=y_lista_fuera_raiz[lista_fuera_raiz.index(vasoc)]
                    x1_fuera_raiz=x_lista_fuera_raiz[2*lista_fuera_raiz.index(vasoc)]
                    x2_fuera_raiz=x_lista_fuera_raiz[2*lista_fuera_raiz.index(vasoc) + 1]


                    print('ULTIMAA')
                    
                    print ('x_abajo: ')
                    print(x_abajo)
                    print('y_abajo: ')
                    print(y_abajo)
                    print('x_arriba')
                    print(x_arriba)
                    print('y_arriba')
                    print(y_arriba)
                    print('lista')
                    print(lista)
                    print('lista2')
                    print(lista2)
                    print('x_lista_fuera_raiz')
                    print(x_lista_fuera_raiz)
                    print('y_lista_fuera_raiz')
                    print(y_lista_fuera_raiz)
                    print('lista_fuera_raiz')
                    print(lista_fuera_raiz)
                    print (lista[len(lista)-1])
                    
                    if (y_fuera_raiz<0):
                        
                        if (puntos_aux[len(puntos_aux)-3][1] <= cont_y): #Es decir si venimos de un camino en vertical hacia arriba
                            y_aux_abajo=-100
                            y_aux_arriba=0
                            for x_aux in x_abajo:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):
                                    print ('x1_fuera_raiz: '+ str(x1_fuera_raiz) + ' x2_fuera_raiz: '+ str(x2_fuera_raiz) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                    if (x_aux>aux1):
                                        if (x1_fuera_raiz>aux1 and x1_fuera_raiz < x_aux ):
                                            if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                y_aux_abajo=y_abajo[int((contador-1)/2)]
                                    else:
                                        if (x1_fuera_raiz>x_aux and x1_fuera_raiz < aux1 ):
                                            if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                y_aux_abajo=y_abajo[int((contador-1)/2)]
                                            
                                    if (x1_fuera_raiz > x2_fuera_raiz):
                                        print ('contador: '+ str (contador))
                                        if (aux1 > x2_fuera_raiz and aux1 < x1_fuera_raiz):
                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                if (y_abajo[int((contador-1)/2)]>y_fuera_raiz):
                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]
                                    else:
                                        if (aux1 > x1_fuera_raiz and aux1 < x2_fuera_raiz):
                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                if (y_abajo[int((contador-1)/2)]> y_fuera_raiz):
                                                    y_aux_arriba=y_abajo[int((contador-1)/2)]
                                                
                                contador+=1
                                print ('y_aux_arriba: '+ str(y_aux_arriba)) 
                                print ('y_aux_abajo: '+ str(y_aux_abajo))       
                                if (puntos_aux[len(puntos_aux)-3][1] > cont_y): #Es decir si venimos de un camino en vertical hacia abajo
                                    print('ENTRAAA')
                                    if (y_aux_abajo==-100):
                                        cont_y=y_fuera_raiz-0.5
                                    else:
                                        cont_y=(y_fuera_raiz+y_aux_abajo)/2

                                else:        
                                    cont_y=(y_fuera_raiz+y_aux_arriba)/2
                    
                        else:
                            contador=0
                            y_aux_abajo=-100
                            y_aux_arriba=0
                            for x_aux in x_abajo:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):

                                    print ('x1_fuera_raiz: '+ str(x1_fuera_raiz) + ' x2_fuera_raiz: '+ str(x2_fuera_raiz) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                    if (x_aux>aux1):
                                        if (x1_fuera_raiz>aux1 and x1_fuera_raiz < x_aux ):
                                            if (y_abajo[int((contador-1)/2)] < cont_y):
                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]
                                    else:
                                        if (x1_fuera_raiz>x_aux and x1_fuera_raiz < aux1 ):
                                            if (y_abajo[int((contador-1)/2)] < cont_y):
                                                if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_abajo[int((contador-1)/2)]

                                    if (x_aux>aux1):
                                        if (cont_x>x_aux and posicion_x_final < aux1 ):
                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                y_aux_arriba=y_abajo[int((contador-1)/2)]
                                        
                                        if (cont_x < aux1 and posicion_x_final > x_aux):
                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                y_aux_arriba=y_abajo[int((contador-1)/2)]
                                    
                                    else:
                                        if (cont_x>aux1 and posicion_x_final < x_aux ):
                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                y_aux_arriba=y_abajo[int((contador-1)/2)]
                                        
                                        if (cont_x < x_aux and posicion_x_final > aux1):
                                            if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                                y_aux_arriba=y_abajo[int((contador-1)/2)]

                                contador+=1


                            if (y_aux_arriba< cont_y):
                                if (y_aux_abajo==-100):
                                    cont_y = y_aux_arriba -0.5
                                else:
                                    cont_y=(y_aux_arriba+y_aux_abajo)/2
                            else:
                                if (y_aux_abajo==-100):
                                    cont_y-=0.5
                                else:
                                    cont_y=(cont_y+y_aux_abajo)/2



                                


                    
                    else:
                        if (puntos_aux[len(puntos_aux)-3][1] >= cont_y):
                            contador=0
                            y_aux_arriba=100
                            y_aux_abajo=0
                            for x_aux in x_arriba:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):
                                    if (x_aux>aux1):
                                        if (x1_fuera_raiz>aux1 and x1_fuera_raiz < x_aux ):
                                            if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                y_aux_arriba=y_arriba[int((contador-1)/2)]
                                    else:
                                        if (x1_fuera_raiz>x_aux and x1_fuera_raiz < aux1 ):
                                            if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                y_aux_arriba=y_arriba[int((contador-1)/2)]
                                            
                                    if (x1_fuera_raiz > x2_fuera_raiz):
                                        if (aux1 > x2_fuera_raiz and aux1 < x1_fuera_raiz):
                                            if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                if (y_arriba[int((contador-1)/2)] < y_fuera_raiz):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                    else:
                                        if (aux1 > x1_fuera_raiz and aux1 < x2_fuera_raiz):
                                            if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                if (y_arriba[int((contador-1)/2)] < y_fuera_raiz):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]

                                contador+=1
                            
                            if (puntos_aux[len(puntos_aux)-3][1] < cont_y): #Es decir si venimos de un camino en vertical hacia arriba
                                if (y_aux_arriba==100):
                                    cont_y=y_fuera_raiz+0.5
                                else:
                                    cont_y=(y_fuera_raiz+y_aux_arriba)/2
                            else:
                                cont_y=(y_fuera_raiz+y_aux_abajo)/2
                        else:
                            contador=0
                            y_aux_arriba=100
                            y_aux_abajo=0
                            for x_aux in x_arriba:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):

                                    if (x_aux>aux1):
                                        if (x1_fuera_raiz>aux1 and x1_fuera_raiz < x_aux ):
                                            if ( y_arriba[int((contador-1)/2)] > cont_y):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]
                                    else:
                                        if (x1_fuera_raiz>x_aux and x1_fuera_raiz < aux1 ):
                                            if ( y_arriba[int((contador-1)/2)] > cont_y):
                                                if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                                    y_aux_arriba=y_arriba[int((contador-1)/2)]

                                    if (x_aux>aux1):
                                        if (cont_x>x_aux and posicion_x_final < aux1 ):
                                            if (y_arriba[int((contador-1)/2)] > cont_y):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                        
                                        if (cont_x < aux1 and posicion_x_final > x_aux):
                                            if (y_arriba[int((contador-1)/2)] > cont_y):
                                                if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                    y_aux_abajo=y_arriba[int((contador-1)/2)]
                                    
                                    else:
                                        if (cont_x>aux1 and posicion_x_final < x_aux ):
                                            if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                y_aux_abajo=y_arriba[int((contador-1)/2)]
                                        
                                        if (cont_x < x_aux and posicion_x_final > aux1):
                                            if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                                y_aux_abajo=y_arriba[int((contador-1)/2)]
                                contador+=1

                            if (y_aux_abajo > cont_y):
                                if (y_aux_arriba==100):
                                    cont_y=y_aux_abajo+0.5
                                else:
                                    cont_y=(y_aux_arriba+y_aux_abajo)/2
                            else:
                                if (y_aux_arriba==100):
                                    cont_y+=0.5
                                else:
                                    cont_y=(cont_y+y_aux_arriba)/2
                            

                        
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    cont_x=-0.5 #Es decir, donde empieza el segmento del cruce 1
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    punto=[cont_x, 0]
                    puntos_aux.append(punto)
                
                else:
                    if arriba: #Me quiero volver por la el arco más arriba que se pueda construir 
                        y_aux_arriba=100
                        y_aux_abajo=0

                        for x_aux in x_arriba:
                            if ((contador % 2)==0):
                                aux1=x_aux
                            if ((contador % 2)==1):
                                if (x_aux>aux1):
                                    if (cont_x>aux1 and cont_x < x_aux ):
                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                else:
                                    if (cont_x>x_aux and cont_x < aux1 ):
                                        if ( y_arriba[int((contador-1)/2)] < y_aux_arriba):
                                            y_aux_arriba=y_arriba[int((contador-1)/2)]
                                        
                                if (cont_x > posicion_x_final):
                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                            y_aux_abajo=y_arriba[int((contador-1)/2)]
                                else:
                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                        if ( y_arriba[int((contador-1)/2)] > y_aux_abajo):
                                            y_aux_abajo=y_arriba[int((contador-1)/2)]

                            contador+=1
                        
                        if (indice_permutacion!=-1):
                            if (maximo_raiz_antigua>y_aux_abajo):
                                y_aux_abajo=maximo_raiz_antigua

                        if (y_aux_arriba==100):
                            if (y_aux_abajo==0):
                                cont_y=1
                            else:
                                cont_y=y_aux_abajo+0.5

                        else:
                            if (y_aux_abajo==0):
                                cont_y=y_aux_arriba/2 #Dividimos entre dos para asegurarnos de que no sea negativo 
                            else:
                                cont_y= (y_aux_arriba + y_aux_abajo)/2  
                        

                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        cont_x=-0.5 #Es decir, donde empieza el segmento del cruce 1
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        punto=[cont_x, 0]
                        puntos_aux.append(punto)
                
                    else:
                        y_aux_abajo=-100
                        y_aux_arriba=0

                        for x_aux in x_abajo:
                            if ((contador % 2)==0):
                                aux1=x_aux
                            if ((contador % 2)==1):
                                if (x_aux>aux1):
                                    print ('cont_x: '+ str(cont_x) + ' aux1: '+ str(aux1) + ' x_aux: '+ str(x_aux))
                                    if (cont_x>aux1 and cont_x < x_aux ):
                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                else:
                                    print ('cont_x: '+ str(cont_x)  + ' x_aux: '+ str(x_aux)+ ' aux1: '+ str(aux1))
                                    if (cont_x>x_aux and cont_x < aux1 ):
                                        if ( y_abajo[int((contador-1)/2)] > y_aux_abajo):
                                            y_aux_abajo=y_abajo[int((contador-1)/2)]
                                        
                                if (cont_x > posicion_x_final):
                                    if (aux1 > posicion_x_final and aux1 < cont_x):
                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                            y_aux_arriba=y_abajo[int((contador-1)/2)]
                                else:
                                    if (aux1 > cont_x and aux1 < posicion_x_final):
                                        if ( y_abajo[int((contador-1)/2)] < y_aux_arriba):
                                            y_aux_arriba=y_abajo[int((contador-1)/2)]

                                
                            contador+=1
                        
                        if (indice_permutacion!=-1):
                            if (minimo_raiz_antigua< y_aux_arriba):
                                y_aux_arriba=minimo_raiz_antigua

                        print ('y_aux_arriba: ' + str (y_aux_arriba))
                        print ('y_aux_abajo: '+ str(y_aux_abajo))


                        if (y_aux_arriba==0):
                            if (y_aux_abajo==-100):
                                cont_y=-1
                            else:
                                cont_y=y_aux_abajo/2

                        else:
                            if (y_aux_abajo==-100):
                                cont_y=y_aux_arriba - 0.5 #Dividimos entre dos para asegurarnos de que no sea negativo 
                            else:
                                cont_y= (y_aux_arriba + y_aux_abajo)/2  
                        

                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        cont_x=-0.5 #Es decir, donde empieza el segmento del cruce 1
                        punto=[cont_x, cont_y]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        punto=[cont_x, 0]
                        puntos_aux.append(punto)

            values = ','.join(str(v) for v in puntos_aux)
                                
            print ('Puntos nuevos: ' + values)
        
        return puntos_aux
       
    

#x=Nudo(8, -10, 12, 2, 14, -6, 4) #Mis apuntes

#x=Nudo(-8,10,16,-12,14,-6,-2,4) #nudocap3a5.pdf  

x=Nudo(4,6,2, 10, 12, 8)

#x=Nudo (6, 10, 2, 12, 4, 8)

#x=Nudo(8, 10, 12, 2, 6, 4)         #https://www.youtube.com/watch?v=3o5CMWZ9qvo&ab_channel=MatthewSalomone

#x=Nudo (8,14,12,10,2,6,4)               #video de arriba

#x=Nudo (8,10,2,12,4, 6)                 #http://katlas.org/wiki/DT_(Dowker-Thistlethwaite)_Codes

#x=Nudo(6,10,14,12,16,2,18,4,8)                  #http://katlas.org/wiki/DT_(Dowker-Thistlethwaite)_Codes

#x=Nudo(4, 8, 10, -14, 2, -16, -18, -6, -12)         #http://katlas.org/wiki/DT_(Dowker-Thistlethwaite)_Codes

puntos=x.obtener_puntos_nudo_dowker()

vector_cambio=x.dividir_nudo_en_arcos(puntos)

aristas=x.obtener_aristas(puntos)

print("Numero arcos superiores: "+ str(x.numero_arcos_superiores()))

puntos_ui=x.obtener_caminos_ui(puntos, aristas, vector_cambio)

puntos_vi=x.obtener_caminos_vi (puntos, aristas, vector_cambio)

presentacion_superior=x.obtener_presentacion_superior(puntos_vi, puntos, vector_cambio)

print("Presentación superior del grupo del nudo: ")

x.representar_presentacion_superior(presentacion_superior)

presentacion_inferior=x.obtener_presentacion_inferior(puntos_ui, puntos, vector_cambio)

print("Presentación inferior del grupo del nudo: ")

x.representar_presentacion_inferior(presentacion_inferior)

x.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)

x.dibujar_nudo_arcos(puntos, vector_cambio)

x.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)

x.dibujar_nudo(puntos)

sys.exit()