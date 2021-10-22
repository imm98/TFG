#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:15:35 2021

@author: inaki
"""
import sys #Para hacer el sys.exit

import copy #Para el constructor de copia que no hace falta

from turtle import *



class Nudo:
    def __init__(self, *numeros):
       
        self.numeros=[]
        for x in range(len(numeros)):
            self.numeros.append(numeros[x])
        print(self.numeros)
        
    def copy(self):
        '''Devuelve un nudo con exactamente
        los mismos puntos que el que se le 
        pasa por argumento'''
        return copy.deepcopy(self)
        '''return Nudo(self.numeros.copy())'''

    def numero_arcos_superiores(self):
        contador=0
        if (self.numeros[0]>0):
            superior_global=False
        else:
            superior_global=True
        
        for x in range(len(self.numeros)-1):
            
            if 2*x+2 not in self.numeros:   #Esto se hace para ver si los cruces de los números pares son superiores o inferiores. Si son inferiores...(es decir, si el número par no pertenece a la lista(dado que pertenece su opuesto))
                if (superior_global==True):
                    print (2*x+2)
                    print ("False")
                    contador+=1
                    superior_global=False
            else:                           #Si son superiores
                if (superior_global==False):
                    print (2*x+2)
                    print ("True")
                    contador+=1
                    superior_global=True
            
            if self.numeros[x+1]>0:      #Esto se hace para ver si los cruces de los números impares son superiores o inferiores. Si son inferiores...
                   
                if (superior_global==True):  
                    
                    print (2*x+3)
                    print("False")
                    contador+=1
                    superior_global=False
            else:                       #Si son superiores
                if (superior_global==False):
                    
                    print(2*x+3)
                    print("True")
                    contador+=1
                    superior_global=True
        
        if 2*len(self.numeros) not in self.numeros:
            if (superior_global==True):
                print(2*len(self.numeros))
                contador+=1
                superior_global=False
        else:                           #Si son superiores
            if (superior_global==False):
                print(2*len(self.numeros))
                contador+=1
                superior_global=True
        
        if (self.numeros[0]>0):
            if (superior_global==True):
                print (1)
                contador+=1
                superior_global=False
        else:
            if (superior_global==False):
                print(1)
                contador+=1
                superior_global=True
        return(contador/2)


    def divide_dos_permutaciones(self):
        maximo=3
        indice_maximo=-1   #Es -2 para que luego no haya problemas en la otra función 
        for x in range(len(self.numeros)-1):
            if abs(self.numeros[x]) > maximo:
                maximo=abs(self.numeros[x])
            
            if ((2*x+2)==maximo):
                indice_maximo=x
        return indice_maximo


    def dividir_nudo_en_arcos(self, puntos):
        
        
        
        terminado=False
        contador_global=1
        
        contador_aux=1
        punto_final=[-0.5,0]
        vector_cambio=[]

        if (self.numeros[0]>0):
            superior=False
            superior_inicial=False
        else:
            superior=True
            superior_inicial=True
            
        
        print ('superior: '+ str(superior))
        while (terminado ==False):
            if (puntos[contador_global]==punto_final):
                terminado=True
            else:
                if superior:
                    if (contador_aux==1):
                        if (puntos[contador_global]!= puntos[contador_global+1]):   #Significa que hemos llegado a un cruce inferior por lo tanto hay que dibujar 
                            print ('puntos[contador_global] i: '+ str (puntos[contador_global]) + ' puntos[contador_global + 1] i: '+ str (puntos[contador_global+1]))
                            
                        

                            #Hay que añadir los puntos y dibujar 
                            print ('Hay que aniadir los puntos i')
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
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
                            print ('puntos[contador_global] j: '+ str (puntos[contador_global]))
                            #Hay que añadir los puntos y dibujar 
                            print ('Hay que aniadir los puntos i')
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            

                        if (puntos[contador_global-1][1] < puntos[contador_global][1] and puntos[contador_global][1] < puntos[contador_global+2][1]):
                            print ('puntos[contador_global] j: '+ str (puntos[contador_global]))
                            #Hay que añadir los puntos y dibujar 
                            print ('Hay que aniadir los puntos i')
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            
                        
                        if (puntos[contador_global-1][0] > puntos[contador_global][0] and puntos[contador_global][0] > puntos[contador_global+2][0]):
                            print ('puntos[contador_global] j: '+ str (puntos[contador_global]))
                            #Hay que añadir los puntos y dibujar 
                            print ('Hay que aniadir los puntos i')
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            
                        
                        if (puntos[contador_global-1][1] > puntos[contador_global][1] and puntos[contador_global][1] > puntos[contador_global+2][1]):
                            print ('puntos[contador_global] j: '+ str (puntos[contador_global]))
                            #Hay que añadir los puntos y dibujar 
                            print ('Hay que aniadir los puntos i')
                            punto_aux=[(puntos[contador_global][0]+puntos[contador_global-1][0])/2, (puntos[contador_global][1]+puntos[contador_global-1][1])/2]
                            puntos.insert(contador_global, punto_aux)
                            puntos.insert(contador_global, punto_aux)
                            contador_global+=2
                            
                            vector_cambio.append(contador_global-2)
                            
                            superior=True
                            contador_aux=0
                            
                
                contador_global+=1
        #print('Contador_global: '+ str (contador_global)+ ' len(puntos): '+ str(len(puntos)) + ' Superior_inicial: '+ str(superior_inicial)+ ' superior: '+ str(superior))
        if ((superior==True and superior_inicial==False) or (superior==False and superior_inicial==True)):
            vector_cambio.insert(0, 0)
            vector_cambio.append(contador_global)

        print(puntos)
            
        return vector_cambio
                


    def dibujar_nudo_arcos(self, puntos, numeros_cambio):
        print('Los puntos son: ')
        print (puntos)
        if (self.numeros[0]>0):
            superior_inicial=False  #Esta variable se utiliza para saber de que color debemos dibujar la flecha 
            superior=False
            pencolor("red")
        else:
            superior_inicial=True
            superior=True
            pencolor("blue")

        setup(1000, 480, 500, 240)
        title("Nudo dividido en arcos superiores e inferiores")
        colormode(255)
        speed(7)
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

    def obtener_aristas_inferiores(self, puntos, vector_cambio):
        aristas_horizontales=[]
        aristas_verticales=[]
        if (self.numeros[0]>0):
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

    def obtener_aristas_superiores(self, puntos, vector_cambio):
        aristas_horizontales=[]
        aristas_verticales=[]
        if (self.numeros[0]>0):
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

    def coincidir_punto_y_arista(coordenada_punto, arista):
        if ((arista[2] > (coordenada_punto - 0.2)) and (arista[1] < (coordenada_punto+0.2))):
            return True
        else: 
            return False

    def coincidir_puntos_y_arista(self, coordenada_punto1, coordenada_punto2, arista):
        if (arista[1] < (coordenada_punto2) and arista[2] > (coordenada_punto1)):
            return True
        else: 
            return False

    def arista_y_puntos_no_coinciden(self, x, punto_1, punto_2):
        no_coinciden=True
        if (x[0]==punto_1[0]):
            if (x[1]==punto_1[1] or x[2]==punto_1[1]):
                no_coinciden=False
        if (x[0]==punto_2[0]):
            if (x[1]==punto_2[1] or x[2]==punto_2[1]):
                no_coinciden=False
        return no_coinciden
    
    def obtener_borde_izquierdo(self, punto, aristas_verticales):
        valor_mas_cercano=0.5
        for x in aristas_verticales:
            if ((x[0] < punto[0]) and ((punto[0]-x[0]) < valor_mas_cercano)):
                if (coincidir_punto_y_arista (punto[1], x)):
                    valor_mas_cercano=(punto[0]-x[0])
        print('Valor_mas_cercano ' + str(valor_mas_cercano))
        return (valor_mas_cercano*0.4)

    def calcular_bordes_centrales (self, punto_inicial, puntos, i, aristas_horizontales, aristas_verticales_inferiores):
        
        
        valor_mas_cercano=0.5
        for x in aristas_horizontales:
            if (punto_inicial[1]!= x[0] and abs(punto_inicial[1]-x[0])< valor_mas_cercano):
                if (punto_inicial[0] < puntos[i][0]): #Esta condición es para pasarle a la siguiente función los valores ordenados de menor a mayor
                    if (self.coincidir_puntos_y_arista(punto_inicial[0], puntos[i][0], x)):
                        valor_mas_cercano=abs(punto_inicial[1]-x[0])
                else:
                    if (self.coincidir_puntos_y_arista(puntos[i][0], punto_inicial[0], x)):
                        valor_mas_cercano=abs(punto_inicial[1]-x[0])
        

        print ('calcular_bordes_centrales: punnto_inicial: ')
        print (punto_inicial)
        print (puntos[i])
        for x in aristas_verticales_inferiores:
            if self.arista_y_puntos_no_coinciden(x, punto_inicial, puntos[i]):  #Esta función sirve para no contemplar las aristas verticales que estén unidas a la arista horizontal que estamos analizando 
                valorr=0.1
                print ('First x[0]: '+ str(x[0]))
                if (punto_inicial[0] < puntos[i][0]):
                    if ((punto_inicial[0] - valorr) < x[0] and x[0] < (puntos[i][0] + valorr)):
                        print ('x[0]: '+ str(x[0]))
                        if (abs(x[1] - punto_inicial[1]) < valor_mas_cercano):
                            valor_mas_cercano=abs(x[1] - punto_inicial[1])
                        if ( abs(x[2] - punto_inicial[1]) < valor_mas_cercano ):
                            valor_mas_cercano= abs(x[2] - punto_inicial[1])
                else:
                    
                    if (((puntos[i][0]-valorr) < x[0]) and x[0] <(punto_inicial[0] + valorr)):
                        print ('x[0]: '+ str(x[0]))
                        if (abs(x[1] - punto_inicial[1]) < valor_mas_cercano):
                            valor_mas_cercano=abs(x[1] - punto_inicial[1])
                        if ( abs(x[2] - punto_inicial[1]) < valor_mas_cercano ):
                            valor_mas_cercano= abs(x[2] - punto_inicial[1])
                    
        return (valor_mas_cercano*0.4)

    def calcular_bordes_laterales(self, punto_inicial, puntos, i, aristas_verticales, aristas_horizontales_inferiores):
        
        
        valor_mas_cercano=0.5
        for x in aristas_verticales:
            if ((punto_inicial[0]!= x[0]) and abs(punto_inicial[0]- x[0])< valor_mas_cercano):
                if (punto_inicial[1] < puntos[i][1]): #Esta condición es para pasarle a la siguiente función los valores ordenados de menor a mayor
                    if (self.coincidir_puntos_y_arista(punto_inicial[1], puntos[i][1], x)):
                        valor_mas_cercano=abs(punto_inicial[0]- x[0])
                else:
                    if (self.coincidir_puntos_y_arista(puntos[i][1], punto_inicial[1],  x)):
                        valor_mas_cercano=abs(punto_inicial[0]- x[0])
        
        for x in aristas_horizontales_inferiores:
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

    def limite_aristas_horizontales_borde_arriba(self, punto, aristas_horizontales):
        limite=0.5
        for x in aristas_horizontales:
            if (x[0] > punto[1] and (x[0]- punto[1])< limite):
                if ((x[1]-0.1) < punto[0] and (x[2]+0.1) > punto[0] ):
                    limite=(x[0]- punto[1])
        return (limite*0.4)
    
    def limite_aristas_horizontales_borde_abajo(self,punto, aristas_horizontales):
        limite=0.5
        for x in aristas_horizontales:
            if (x[0] < punto[1] and (punto[1]- x[0] < limite)):
                if ((x[1]-0.1) < punto[0] and (x[2]+0.1) > punto[0] ):
                    limite=(punto[1]-x[0])
        return (limite*0.4)

    def limite_aristas_verticales_borde_derecha(self, punto, aristas_verticales):
        limite=0.5
        for x in aristas_verticales:
            if (x[0] > punto[0] and (x[0] - punto[0])<limite):
                if ((x[1] - 0.1) < punto[1] and (x[2] + 0.1) < punto[1]):
                    limite=(x[0]- punto[0])
        
        return (limite*0.4)
    
    def limite_aristas_verticales_borde_izquierda(self, punto, aristas_verticales):
        limite=0.5
        for x in aristas_verticales:
            if(x[0] < punto[0] and (punto[0]- x[0])< limite):
                if ((x[1] - 0.1) < punto[1] and (x[2] + 0.1) < punto[1]):
                    limite=(punto[0] - x[0])
        
        return (limite*0.4)
    
    def obtener_v_i(self, puntos, aristas_horizontales, aristas_verticales, valor_inicial, valor_final, aristas_inferiores):
        
        borde_arriba=0
        borde_abajo=0
        borde_izquierda=0
        borde_derecha=0

        bordes=[]
        if (valor_inicial==0):
            borde_izquierda=self.obtener_borde_izquierdo(puntos[0], aristas_verticales)
            horizontal=True
        
        else:   #En otro caso tenemos que ver si partimos de una zona horizontal o vertical 
            punto_anterior=puntos[valor_inicial-1]
            if (punto_anterior[0] != puntos[valor_inicial][0]):
                horizontal=True
                if  (punto_anterior[0] > puntos[valor_inicial][0]):  #Vamos hacia la izquierda, por lo tanto calculamos el borde derecho
                    #borde_derecha=puntos[valor_inicial][0]
                    limite=self.limite_aristas_verticales_borde_derecha(puntos[valor_inicial], aristas_inferiores[1])

                    if ((punto_anterior[0] - puntos[valor_inicial][0])/2 < limite):
                        limite=(punto_anterior[0] - puntos[valor_inicial][0])/2
                    
                    borde_derecha=limite
                
                else:                                                #Vamos hacia la izquierda, por lo tanto calculamos el borde derecho
                    #borde_izquierda=puntos[valor_inicial][0]
                    limite=self.limite_aristas_verticales_borde_izquierda(puntos[valor_inicial], aristas_inferiores[1])

                    if (( puntos[valor_inicial][0] - punto_anterior[0])/2 < limite):
                        limite=(puntos[valor_inicial][0] - punto_anterior[0])/2
                    
                    borde_izquierda=limite
                
            else:
                horizontal=False
                if (punto_anterior[1] > puntos[valor_inicial][1]):      #Vamos hacia abajo por lo que hay que calcular el borde superior
                    #borde_arriba=puntos[valor_inicial][1]
                    limite=self.limite_aristas_horizontales_borde_arriba(puntos[valor_inicial], aristas_inferiores[0])

                    if ((punto_anterior[1] - puntos[valor_inicial][1])/2 < limite):
                        limite=(punto_anterior[1] - puntos[valor_inicial][1])/2
                    
                    borde_arriba=limite
                
                else:
                    #borde_abajo=puntos[valor_inicial][1]
                    limite= self.limite_aristas_horizontales_borde_abajo(puntos[valor_inicial], aristas_inferiores[0])

                    if (( puntos[valor_inicial][1] - punto_anterior[1])/2 < limite):
                        limite=(puntos[valor_inicial][1] - punto_anterior[1])/2
                    
                    borde_abajo=limite
    
        punto_inicial=puntos[valor_inicial]
        contador=0 #Este contador servirá para el contador de bordes 
        giros=[]
        print('borde_izda: ' +str(borde_izquierda))
        for i in range(valor_final - valor_inicial):
            if horizontal:
                if (punto_inicial[1] != puntos[valor_inicial + i +1][1]):
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_d") or (giros[len(giros)-1]== "ar_d") ):
                            borde_izquierda=bordes[len(bordes)-1][0]
                        else:
                            borde_derecha=bordes[len(bordes)-1][1]
                    
                    bordes_centrales=self.calcular_bordes_centrales(punto_inicial, puntos, valor_inicial+i, aristas_horizontales, aristas_inferiores[1])
                    bordes_aux=[borde_izquierda, borde_derecha, bordes_centrales, bordes_centrales]
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ab_d") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                            bordes[len(bordes)-1][3]=bordes_centrales
                        else:
                            bordes[len(bordes)-1][2]=bordes_centrales

                    bordes.append(bordes_aux)
                    if (punto_inicial[1] > puntos[valor_inicial + i +1][1]):
                        if (borde_derecha==0):
                            giros.append("ab_d") #abajo derecha
                        else:
                            giros.append("ab_i")
                    else:
                        if (borde_derecha==0):
                            giros.append("ar_d") #abajo derecha
                        else:
                            giros.append("ar_i")
                    punto_inicial=puntos[valor_inicial+i]
                    print('Horizontal, contador= '+ str(contador)+ ' i= '+ str(i)+ ' bordes= ')
                    print(bordes)
                    print('giros: ')
                    print(giros)
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

                    bordes_laterales=self.calcular_bordes_laterales(punto_inicial, puntos, valor_inicial+i, aristas_verticales, aristas_inferiores[0])
                    bordes_aux=[bordes_laterales, bordes_laterales, borde_arriba, borde_abajo]
                    #Ahora modificamos el valor que estaba a 0 en la lista de bordes anterior
                    if (contador!=0):
                        if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ar_i") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                            bordes[len(bordes)-1][0]=bordes_laterales
                        else:
                            bordes[len(bordes)-1][1]=bordes_laterales

                    bordes.append(bordes_aux)

                    if (punto_inicial[0] > puntos[valor_inicial + i +1][0] ): #Esto quiere decir que giramos para la izquierda
                        if (borde_arriba==0): #Esto quiere decir que estamos yendo hacia abajo 
                            giros.append("ar_i")
                        else:
                            giros.append("ab_i")
                    else:   #Giramos para la derecha
                        if (borde_arriba==0):
                            giros.append("ar_d")
                        else:
                            giros.append("ab_d")

                    punto_inicial=puntos[valor_inicial+i]
                    print('Vertical, contador= '+ str(contador)+ ' i= '+ str(i)+ ' bordes= ')
                    print(bordes)
                    print('giros: ')
                    print(giros)
                    borde_izquierda=0
                    borde_derecha=0
                    borde_arriba=0
                    borde_abajo=0
                    contador+=1
                    horizontal=True
        
        print(puntos)
        print('valor_final: '+ str(valor_final))
        print('len(puntos): '+ str(len(puntos)))
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
                limite=self.limite_aristas_verticales_borde_derecha(puntos[valor_final], aristas_inferiores[1])

                if ((punto_siguiente[0] - puntos[valor_final][0])/2 < limite):
                    limite=(punto_siguiente[0] - puntos[valor_final][0])/2
                
                borde_derecha=limite
                
                
            
            else:                                                #Vamos hacia la izquierda, por lo tanto calculamos el borde derecho
                #borde_izquierda=puntos[valor_final][0]
                limite=self.limite_aristas_verticales_borde_izquierda(puntos[valor_final], aristas_inferiores[1])

                if (( puntos[valor_final][0] - punto_siguiente[0])/2 < limite):
                    limite=(puntos[valor_final][0] - punto_siguiente[0])/2
                
                borde_izquierda=limite

            bordes_centrales=self.calcular_bordes_centrales(punto_inicial, puntos, valor_final, aristas_horizontales, aristas_inferiores[1])
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
                #borde_arriba=puntos[valor_final][1]
                limite=self.limite_aristas_horizontales_borde_arriba(puntos[valor_final], aristas_inferiores[0])

                if ((punto_siguiente[1] - puntos[valor_final][1])/2 < limite):
                    limite=(punto_siguiente[1] - puntos[valor_final][1])/2
                
                borde_arriba=limite
            
            else:
                #borde_abajo=puntos[valor_final][1]
                limite= self.limite_aristas_horizontales_borde_abajo(puntos[valor_final], aristas_inferiores[0])
                
                if (( puntos[valor_final][1] - punto_siguiente[1])/2 < limite):
                    limite=((puntos[valor_final][1] - punto_siguiente[1])/2)
                
                borde_abajo=limite

            bordes_laterales=self.calcular_bordes_laterales(punto_inicial, puntos, valor_inicial+i, aristas_verticales, aristas_inferiores[0])
            bordes_aux=[bordes_laterales, bordes_laterales, borde_arriba, borde_abajo]
            if (contador!=0):
                if ( (giros[len(giros)-1]== "ab_i") or (giros[len(giros)-1]== "ar_i") ):    #Si el giro es en el lado izquierdo, en la lista de bordes anterior teníamos el borde de la izda a 0 por lo que lo modificamos
                    bordes[len(bordes)-1][0]=bordes_laterales
                else:
                    bordes[len(bordes)-1][1]=bordes_laterales
            bordes.append(bordes_aux)

        print('Ultimo de la tanda: contador= '+ str(contador)+ ' i= '+ str(i)+ ' bordes= ')
        print(bordes)
        print('giros: ')
        print(giros)
        bordes_y_giros=[bordes, giros]
        return bordes_y_giros
        

    def obtener_puntos_v_i(self, bordes_y_giros, puntos, valor_inicial, valor_final):
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
        if not giros:

            print('Comprobacion: '+ str (bordes[0][0]))
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
            
            for i in range(valor_final - valor_inicial ):
                if (contador==0):
                    if horizontal:
                        if (punto_inicial[1] != puntos[valor_inicial + i +1][1]):
                            punto_final=puntos[valor_inicial+i]
                            
                            print ('IGUALDAD 0: ')
                            print(punto_inicial)
                            print(punto_final)

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
                    else:
                        if (punto_inicial[0] != puntos[valor_inicial + i +1][0]):
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
                                
                else:
                    if horizontal:
                        if (punto_inicial[1] != puntos[valor_inicial + i +1][1]):
                            punto_final=puntos[valor_inicial+i]
                            print ('IGUALDAD ' + str(contador)+ ': ')
                            print(punto_inicial)
                            print(punto_final)
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
                            print ('IGUALDAD ' + str(contador)+ ': ')
                            print(punto_inicial)
                            print(punto_final)
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
            
            punto_final=puntos[valor_final]
            if horizontal:
                
                if (puntos[valor_final-1][0] > punto_final[0]): #Si estamos yendo para la izquierda
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

                else:
                    
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
                
                if (puntos[valor_final-1][1] > punto_final[1]): #Estamos yendo para abajo 
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
                
                else:       #Estamos yendo para arriba
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


    def obtener_caminos_v_i (self, puntos, aristas_horizontales, aristas_verticales, vector_cambio):
        
        aristas_inferiores=self.obtener_aristas_inferiores(puntos, vector_cambio)
        contador=0
        puntos_vi=[]
        if 0 not in vector_cambio: #Si el 0 no pertenece al vector que nos indica cuando hay que cambiar de arcos superiores a inferiores, nos creamos una lista auxiliar para que nos sea más fácil su manejo 
            lista_puntos_auxiliares=[]
            indice_partida=vector_cambio[len(vector_cambio)-1]
            for i in range(len(puntos) - indice_partida+1):
                lista_puntos_auxiliares.append(puntos[indice_partida+i-1])
            
            for i in range(vector_cambio[0]+3):    #Le añado dos puntos más (por ello pongo +3) para poder comparar el punto final con el punto siguiente al final 
                lista_puntos_auxiliares.append(puntos[i])
            
            print('lista_puntos_auxiliares: ')
            print(lista_puntos_auxiliares)
            if (self.numeros[0]>0):         #Es decir el caso en el que el arco que pase por encima del primer cruce sea un cruce inferior
                
                bordes_y_giros=self.obtener_v_i(lista_puntos_auxiliares, aristas_horizontales, aristas_verticales, 1, len(lista_puntos_auxiliares)-3, aristas_inferiores)
                puntos_vi_aux=self.obtener_puntos_v_i(bordes_y_giros, lista_puntos_auxiliares, 1,len(lista_puntos_auxiliares)-3)
                puntos_vi.append(puntos_vi_aux)
                print ('Puntos_vi['+str(contador)+']')
                print(puntos_vi[contador])
                superior=True
                modulo2=1
                contador+=1
            else:
                superior=False
                modulo2=0

        else:
            if (self.numeros[0]>0):
                superior=False
                modulo2=0
            else:
                superior=True
                modulo2=1

        
        for i in range(len(vector_cambio)-1):
            if (i%2==modulo2):
                print('obtener_caminos_v_'+ str(contador))
                bordes_y_giros=self.obtener_v_i(puntos, aristas_horizontales, aristas_verticales, vector_cambio[i], vector_cambio[i+1], aristas_inferiores)
                puntos_vi_aux=self.obtener_puntos_v_i(bordes_y_giros, puntos, vector_cambio[i], vector_cambio[i+1])
                puntos_vi.append(puntos_vi_aux)
                print ('Puntos_vi['+str(contador)+']')
                print(puntos_vi[contador])
                contador+=1

        return puntos_vi

    def obtener_caminos_u_i (self, puntos, aristas_horizontales, aristas_verticales, vector_cambio):
        aristas_superiores=self.obtener_aristas_superiores(puntos, vector_cambio)
        contador=0
        puntos_ui=[]
        if 0 not in vector_cambio:
            lista_puntos_auxiliares=[]
            indice_partida=vector_cambio[len(vector_cambio)-1]
            for i in range(len(puntos) - indice_partida+1):
                lista_puntos_auxiliares.append(puntos[indice_partida+i-1])
            
            for i in range(vector_cambio[0]+3):    #Le añado dos puntos más (por ello pongo +3) para poder comparar el punto final con el punto siguiente al final 
                lista_puntos_auxiliares.append(puntos[i])
            
            if (self.numeros[0] < 0): #Es decir el caso en el que el arco que pase por encima del primer cruce sea un cruce superior
                bordes_y_giros=self.obtener_v_i(lista_puntos_auxiliares, aristas_horizontales, aristas_verticales, 1, len(lista_puntos_auxiliares)-3, aristas_superiores)
                puntos_ui_aux=self.obtener_puntos_v_i(bordes_y_giros, lista_puntos_auxiliares, 1,len(lista_puntos_auxiliares)-3)
                puntos_ui.append(puntos_ui_aux)
                superior=False
                modulo2=1
                contador+=1
            else:
                superior=True
                modulo2=0
        
        else:
            if (self.numeros[0] < 0):
                superior=True
                modulo2=0
            else:
                superior=False
                modulo2=1
        
        
        for i in range(len(vector_cambio)-1):
            if (i%2==modulo2):
                print('obtener_caminos_u_'+ str(contador))
                bordes_y_giros=self.obtener_v_i(puntos, aristas_horizontales, aristas_verticales, vector_cambio[i], vector_cambio[i+1], aristas_superiores)
                puntos_ui_aux=self.obtener_puntos_v_i(bordes_y_giros, puntos, vector_cambio[i], vector_cambio[i+1])
                puntos_ui.append(puntos_ui_aux)
                print ('Puntos_ui['+str(contador)+']')
                print(puntos_ui[contador])
                contador+=1

        return puntos_ui    

    def coindidir_arista_vertical_y_flecha(self, punto_1, punto_2, puntos):
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
    
    def coincidir_arista_horizontal_y_flecha (self, punto_1, punto_2, puntos):
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
        speed(7)
        colormode(255)
        pencolor(121,221,0)
        setup(1000, 480, 500, 240)
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

        if (self.numeros[0]>0):
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
                        x_medio=self.coindidir_arista_vertical_y_flecha(x[i], x[i+1], puntos)
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
                        y_medio=self.coincidir_arista_horizontal_y_flecha(x[i], x[i+1], puntos)
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
        speed(7)
        colormode(255)
        
        pencolor(152,0,255)
        setup(1000, 480, 500, 240)
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

        if (self.numeros[0]>0):
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
                        x_medio=self.coindidir_arista_vertical_y_flecha(x[i], x[i+1], puntos)
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
                        y_medio=self.coincidir_arista_horizontal_y_flecha(x[i], x[i+1], puntos)
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

    def obtener_puntos_nudo_dowker(self):
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
        
        indice_permutacion=self.divide_dos_permutaciones()
        if (indice_permutacion!=-1):        #Es decir, cuando se puede dividir en dos subpermutaciones
            minimo_raiz_antigua=0
            maximo_raiz_antigua=0
        print ('indice_permutacion: '+ str(indice_permutacion))

        if (self.numeros[0]>0):             #Esto es para el primer valor
            print('Contador='+ str(cont_x))
            punto=[cont_x-0.5,cont_y]
            puntos_aux.append(punto)
            punto=[cont_x-0.1,cont_y]
            puntos_aux.append(punto)
            
            '''punto=[cont_x+0.1,cont_y]
            puntos_aux.append(punto)
            punto=[cont_x+0.5,cont_y]
            puntos_aux.append(punto)'''
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
        
        for x in range(len(self.numeros)):
            
            print ('x: ' + str(x))
            print ('len(self.numeros): ' + str(len(self.numeros)))

            
            
            #Valores pares
            '''Este if es para asignarle SIGNO al cruce y para decir si es la SEGUNDA vez que se recorre un cruce'''
            volver=False
            if 2*x+2 in self.numeros:       #Si es un cruce superior
                signo='Pos' #Indica si se pasa por encima (Pos) o por debajo (Neg)
                valor_asociado=2*self.numeros.index(2*x+2)+1
                if valor_asociado in lista:     #Si el valor asociado ya ha sido analizado
                    print('Llega ' +str(2*x+2) + ' '+str(valor_asociado))
                    volver=True
            else:   #Si es un cruce inferior
                signo='Neg'
                valor_asociado=2*self.numeros.index(-(2*x+2))+1
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
                        print('contador_aux: ' + str(contador_aux) + ' suma: '+ str(contador_aux/2+x) + ' len: '+ str (len(self.numeros)))
                        
                        if (int(2*x+2+ contador_aux)==(2*len(self.numeros)+1)): #Caso en el que podamos dividir en dos subpermutaciones, SOBRA
                            aux=True

                        else:
                            if (contador_aux%2 ==1):
                                if (abs(self.numeros[x+1]) in lista):
                                    contador_ya_lista+=1                          
                                    aux=True
                            else:
                                if 2*x+2+contador_aux in self.numeros:
                                    vasoc=2*self.numeros.index(2*x+2+contador_aux)+1
                                    if (vasoc in lista) :
                                        contador_ya_lista+=1
                                        aux=True
                                else:
                                    vasoc=2*self.numeros.index(-(2*x+2+contador_aux))+1
                                    if (vasoc in lista):
                                        contador_ya_lista+=1
                                        
                                        aux=True
                    print('contador_aux: '+ str(contador_aux))
                    print ('contador_ya_lista: '+ str(contador_ya_lista))

                    if (int(2*x+2+ contador_aux)==(2*len(self.numeros)+1)): #Caso en el que podamos dividir en dos subpermutaciones
                        posicion_relativa_x=-0.5
                        fragmentos=(contador_aux-contador_ya_lista) #Esto es para ver en el número de fragmentos que se va a dividir el fragmento 
                        posicion_final_x= (cont_x*fragmentos/2 + posicion_relativa_x) / (fragmentos/2 +1)
                    
                    else:
                       
                        if ((contador_aux)%2 ==0):  
                            posicion_relativa_x=lista2[lista.index(vasoc)]
                        else:
                            posicion_relativa_x=lista2[lista.index(abs(self.numeros[int(x+1+contador_aux/2)]))]
                        
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
                                
                                if 2*x+2 not in self.numeros: #Es decir, si el cruce es inferior
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
                                if 2*x+2 in self.numeros: #Es decir, si el cruce es superior llegará hasta el cero 
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

            if (x!=(len(self.numeros)-1)):  #Si no estamos en la última iteración del vector
                
                if (indice_permutacion != x):
                    volver=False
                    if abs(self.numeros[x+1]) in lista:
                        print(str(2*x+3)+' '+ str(abs(self.numeros[x+1])))
                        volver=True
                    
                    if (self.numeros[x+1]>0):   
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
                                print('contador_aux: ' + str(contador_aux) + ' suma: '+ str(contador_aux+ 2*x+3) + ' len: '+ str (len(self.numeros)))
                                if (int(contador_aux+ 2*x+3)==(2*len(self.numeros)+1)): #Caso en el que podamos dividir en dos subpermutaciones
                                    aux=True
                                
                                else:

                                    if ((contador_aux)%2 ==1):      #2*x+4
                                        if 2*x+3+contador_aux in self.numeros:
                                            vasoc=2*self.numeros.index(2*x+3+contador_aux)+1    #Nos devuelve el número impar asociado al número par 2*x+3+contador_aux
                                            print('vasoc' + str(vasoc))
                                            if (vasoc in lista):
                                                contador_ya_lista+=1
                                                aux=True
                                        else:
                                            vasoc=2*self.numeros.index(-(2*x+3+contador_aux))+1
                                            if (vasoc in lista):
                                                contador_ya_lista+=1
                                                aux=True 
                                        
                                    else:
                                        if (abs(self.numeros[int(x+1+contador_aux/2)]) in lista ):
                                            contador_ya_lista+=1
                                            if (abs(self.numeros[int(x+1+contador_aux/2)]) not in lista_fuera_raiz):
                                                aux=True

                            print ('contador_ya_lista: ' + str(contador_ya_lista))     
                            print('contador_aux: '+ str(contador_aux))
                            
                            if (int(contador_aux/2+x+1)==len(self.numeros)):
                                posicion_relativa_x=-0.5
                                fragmentos=(contador_aux-contador_ya_lista) #Esto es para ver en el número de fragmentos que se va a dividir el fragmento 
                                posicion_final_x= (cont_x*fragmentos/2 + posicion_relativa_x) / (fragmentos/2 +1)

                            else:    
                                 
                                if ((contador_aux)%2 ==1):  
                                    posicion_relativa_x=lista2[lista.index(vasoc)]
                                else:
                                    posicion_relativa_x=lista2[lista.index(abs(self.numeros[int (x+1+contador_aux/2)]))]
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
                        
                        posicion_x_final=lista2[lista.index(abs(self.numeros[x+1]))]
                        
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

                            if abs(self.numeros[x+1]) in lista_fuera_raiz: #Es decir, si el número asociado a ese número impar no está en la raíz 
                                print ('valor_asociado in lista_fuera_raiz_impar')
                                valor_asociado=abs(self.numeros[x+1])
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
                                        
                                        if self.numeros[x+1]>0: #Es decir, si el cruce es inferior
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
                                        if self.numeros[x+1]<0: #Es decir, si el cruce es superior llegará hasta el cero 
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
                    if (self.numeros[x+1]>0):   #signo negativo
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

                if (lista[len(lista)-1] in self.numeros):   #Tomamos su valor asociado
                    vasoc=2*self.numeros.index(lista[len(lista)-1])+1
                else:
                    vasoc=2*self.numeros.index(- lista[len(lista)-1])+1

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
       
    



n=Nudo(8, -10, 12, 2, 14, -6, 4) #Mis apuntes

'''
puntos=n.obtener_puntos_nudo_dowker()
vector_cambio=n.dividir_nudo_en_arcos(puntos)

aristas=n.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])

print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=n.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')

puntos_vi=n.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
n.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
puntos_ui=n.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
n.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
'''

m=Nudo(-8,10,16,-12,14,-6,-2,4) #nudocap3a5.pdf

'''
puntos=m.obtener_puntos_nudo_dowker()
vector_cambio=m.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas=m.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])



aristas_inferiores=m.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')

puntos_vi=m.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
m.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
puntos_ui=m.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
m.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
'''

p=Nudo(4,6,2, 10, 12, 8)

'''
puntos=p.obtener_puntos_nudo_dowker()
aristas=p.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=p.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=p.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')


puntos_vi=p.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
p.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
p.dibujar_nudo_arcos(puntos, vector_cambio)
puntos_ui=p.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
p.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
'''
#p.dibujar_nudo_arcos(puntos, vector_cambio)


r=Nudo (6, 10, 2, 12, 4, 8)
'''
puntos=r.obtener_puntos_nudo_dowker()
aristas=r.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=r.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=r.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')


puntos_vi=r.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
r.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
r.dibujar_nudo_arcos(puntos, vector_cambio)
puntos_ui=r.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
r.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
'''

t=Nudo(8, 10, 12, 2, 6, 4)
#puntos=t.obtener_puntos_nudo_dowker()         #https://www.youtube.com/watch?v=3o5CMWZ9qvo&ab_channel=MatthewSalomone
'''
puntos=t.obtener_puntos_nudo_dowker()
aristas=t.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=t.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=t.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')


puntos_vi=t.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
t.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
t.dibujar_nudo_arcos(puntos, vector_cambio)
puntos_ui=t.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
t.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
'''
u=Nudo (8,14,12,10,2,6,4)               #video de arriba
#puntos=u.obtener_puntos_nudo_dowker()
'''
puntos=u.obtener_puntos_nudo_dowker()
aristas=u.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=u.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=u.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')


puntos_vi=u.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
u.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
u.dibujar_nudo_arcos(puntos, vector_cambio)
puntos_ui=u.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
u.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
'''
v=Nudo (8,10,2,12,4, 6)                 #http://katlas.org/wiki/DT_(Dowker-Thistlethwaite)_Codes
#puntos=v.obtener_puntos_nudo_dowker()
'''
puntos=v.obtener_puntos_nudo_dowker()
aristas=v.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=v.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=v.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')

puntos_vi=v.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
v.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)
puntos_ui=v.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
v.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)
v.dibujar_nudo_arcos(puntos, vector_cambio)
'''

w=Nudo(6,10,14,12,16,2,18,4,8)                  #http://katlas.org/wiki/DT_(Dowker-Thistlethwaite)_Codes

'''
puntos=w.obtener_puntos_nudo_dowker()
aristas=w.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=w.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)

aristas_inferiores=w.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')
puntos_ui=w.obtener_caminos_u_i (puntos, aristas[0], aristas[1], vector_cambio)
w.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)

puntos_vi=w.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)
w.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)


'''


x=Nudo(4, 8, 10, -14, 2, -16, -18, -6, -12)         #http://katlas.org/wiki/DT_(Dowker-Thistlethwaite)_Codes


puntos=x.obtener_puntos_nudo_dowker()
aristas=x.obtener_aristas(puntos)

print('Las aristas horizontales del nudo son: ')
print (aristas[0])
print('Las aristas verticales del nudo son: ')
print (aristas[1])
vector_cambio=x.dividir_nudo_en_arcos(puntos)
print('Vector_cambio')
print(vector_cambio)
aristas_superiores=x.obtener_aristas_superiores(puntos, vector_cambio)
print('Aristas superiores horizontales: ')
print(aristas_superiores[0])
print('Aristas superiores verticales: ')
print(aristas_superiores[1])


aristas_inferiores=x.obtener_aristas_inferiores(puntos, vector_cambio)
print('Las aristas horizontales inferiores del nudo son: ')
print(aristas_inferiores[0])
print('Las aristas verticales inferiores del nudo son: ')
print(aristas_inferiores[1])

print('OBTENER V_I')

puntos_ui=x.obtener_caminos_u_i(puntos, aristas[0], aristas[1], vector_cambio)

x.dibujar_caminos_ui(puntos, puntos_ui, vector_cambio)

puntos_vi=x.obtener_caminos_v_i (puntos, aristas[0], aristas[1], vector_cambio)

x.dibujar_caminos_vi(puntos, puntos_vi, vector_cambio)



x.dibujar_nudo_arcos(puntos, vector_cambio)

'''

turtle.speed(1)
contador=0
turtle.penup()
for x in puntos:
    if (contador % 2==0):
        punto1=(100*x[0], 100*x[1])
    else:
        punto2=(100*x[0], 100*x[1])
        turtle.goto(punto1)
        turtle.pendown()
        turtle.goto(punto2)
        turtle.penup()
    contador+=1





turtle.hideturtle()
turtle.exitonclick()
turtle.Screen().bye()
'''

sys.exit()