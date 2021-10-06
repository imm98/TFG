#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:15:35 2021

@author: inaki
"""
import copy

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
        print(contador/2)






    def dibujar_nudo_dowker(self):
        cont_x=0    #Nos indicará la coordenada x de la posición por la que vamos añadiendo aristas
        cont_y=0    #Nos indicará la coordenada y de la posición por la que vamos añadiendo aristas
        
        y_arriba=[] #Lista que nos indicará la altura y de las aristas que pasen por encima del nudo
        x_arriba=[] #Lista de listas que nos indicará el valor mínimo y máximo de x para la altura y del vector de arriba    
        y_abajo=[]
        x_abajo=[]
        puntos_aux=[]
        lista=[]    #Contiene los valores de los cruces que hemos recorrido 
        lista2=[]   #Contiene la coordenada x de los cruces que vamos obteniendo en la lista 1
        arriba=True #Creo que se puede eliminar
        if (self.numeros[0]>0):
            print('Contador='+ str(cont_x))
            punto=[cont_x-0.5,cont_y]
            puntos_aux.append(punto)
            punto=[cont_x-0.1,cont_y]
            puntos_aux.append(punto)
            
            punto=[cont_x+0.1,cont_y]
            puntos_aux.append(punto)
            punto=[cont_x+0.5,cont_y]
            puntos_aux.append(punto)

            
        else:
            punto=[cont_x-0.5,cont_y]
            puntos_aux.append(punto)
            punto=[cont_x+0.5,cont_y]
            puntos_aux.append(punto)
          
        lista.append(1)
        lista2.append(cont_x)       #Mas adelante se podrían juntar en un map o algo así 
        
        
        
        values2 = ','.join(str(v) for v in puntos_aux)
        
        print ('Puntos_aux: ' + values2)
        
        for x in range(len(self.numeros)-1):
            
            
            
            #Valores pares
            volver=False
            if 2*x+2 in self.numeros:       #Si es un cruce superior
                signo='Pos' #Indica si se pasa por encima (Pos) o por debajo (Neg)
                valor_asociado=2*self.numeros.index(2*x+2)+1
                if valor_asociado in lista:     #Si el valor asociado ya ha sido analizado
                    print(str(2*x+2) + ' '+str(valor_asociado))
                    volver=True
            else:   #Si es un cruce inferior
                signo='Neg'
                valor_asociado=2*self.numeros.index(-(2*x+2))+1
                if valor_asociado in lista:
                    print(str(-(2*x+2)) + ' '+str(valor_asociado))
                    volver=True
            
            
            
            
            if(volver==False):  #Si se llega antes al número par    #Habría que ver más adelante si se ha realizado previamente un cruce
                cont_x+=1
                print ('Contador: '+ str(cont_x))
                if (signo=='Neg'):
                    punto=[cont_x-0.5,cont_y]
                    puntos_aux.append(punto)
                    punto=[cont_x-0.1,cont_y]
                    puntos_aux.append(punto)
                    punto=[cont_x+0.1,cont_y]
                    puntos_aux.append(punto)
                    punto=[cont_x+0.5,cont_y]
                    puntos_aux.append(punto)
                else:
                    punto=[cont_x-0.5,cont_y]
                    puntos_aux.append(punto)
                    punto=[cont_x+0.5,cont_y]
                    puntos_aux.append(punto)   
                    
            else:               #Si se llega en segundo lugar al valor par hay que hacer lo de dar la vuelta
                print ('Cruce' + str(2*x+2) + ' Valor asociado: '+str(valor_asociado))    
                posicion_x_final=lista2[lista.index(valor_asociado)]
                print('posicion_x_inicial: ' + str(cont_x))
                print('posicion_x_final: ' + str(posicion_x_final))
                if arriba:
                    arriba=False
                    if not y_arriba:
                        y_arriba.append(1)
                        x_1=cont_x
                        x_2=posicion_x_final
                        x_arriba.append(x_1)
                        x_arriba.append(x_2)
                        punto=[cont_x+0.5, cont_y]
                        puntos_aux.append(punto)
                        punto=[cont_x+0.5, y_arriba[len(y_arriba)-1]]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        print (x_arriba[len(x_arriba)-1])
                        punto=[x_arriba[len(x_arriba)-1], y_arriba[len(y_arriba)-1]]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        
                        if 2*x+2 not in self.numeros: #Es decir, si el cruce es inferior
                            punto=[x_arriba[len(x_arriba)-1], 0.1]
                            puntos_aux.append(punto)
                            puntos_aux.append(punto)
                            punto=[x_arriba[len(x_arriba)-1], -0.1]
                            puntos_aux.append(punto)
                            puntos_aux.append(punto)
                            
                        '''Dado que estamos en el caso de que y_arriba estuviera vacío, y_abajo también estará vacío, por tanto añadimos el valor -1'''
                        y_abajo.append(-1)
                        x_abajo.append(x_2)
                        punto=[x_arriba[len(x_arriba)-1], y_abajo[len(y_arriba)-1]]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        values = ','.join(str(v) for v in puntos_aux)
        
                        print ('Puntos nuevos: ' + values)
                
                
                values = ','.join(str(v) for v in puntos_aux)
        
                print ('Puntos: ' + values)
              
                
            lista.append(2*x+2)
            lista2.append(cont_x)






            #Valores impares
            volver=False
            if abs(self.numeros[x+1]) in lista:
                print(str(2*x+3)+' '+ str(abs(self.numeros[x+1])))
                volver=True
            
            if (self.numeros[x+1]>0):
                signo='Neg'
            else:
                signo='Pos'
            if (volver==False):
                cont_x+=1
                print ('Contador: '+ str(cont_x) + ' cruce '+ str(2*x+3))
                if (signo=='Neg'):
                    punto=[cont_x-0.5,0]
                    puntos_aux.append(punto)
                    punto=[cont_x-0.1,0]
                    puntos_aux.append(punto)
                    punto=[cont_x+0.1,0]
                    puntos_aux.append(punto)
                    punto=[cont_x+0.5,0]
                    puntos_aux.append(punto)
                else:
                    punto=[cont_x-0.5,0]
                    puntos_aux.append(punto)
                    punto=[cont_x+0.5,0]
                    puntos_aux.append(punto)   
            
            
            else:
                posicion_x_final=lista2[lista.index(abs(self.numeros[x+1]))]
                if arriba:
                    arriba=False
                    if not y_arriba:
                        y_arriba.append(1)
                        x_1=cont_x
                        x_2=posicion_x_final
                        x_arriba.append(x_1)
                        x_arriba.append(x_2)
                        punto=[cont_x+0.5, cont_y]
                        puntos_aux.append(punto)
                        punto=[cont_x+0.5, y_arriba[len(y_arriba)-1]]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        print (x_arriba[len(x_arriba)-1])
                        punto=[x_arriba[len(x_arriba)-1], y_arriba[len(y_arriba)-1]]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        
                        if self.numeros[x+1]>0: #Es decir, si el cruce es inferior
                            punto=[x_arriba[len(x_arriba)-1], 0.1]
                            puntos_aux.append(punto)
                            puntos_aux.append(punto)
                            punto=[x_arriba[len(x_arriba)-1], -0.1]
                            puntos_aux.append(punto)
                            puntos_aux.append(punto)
                            
                        '''Dado que estamos en el caso de que y_arriba estuviera vacío, y_abajo también estará vacío, por tanto añadimos el valor -1'''
                        y_abajo.append(-1)
                        x_abajo.append(x_2)
                        punto=[x_arriba[len(x_arriba)-1], y_abajo[len(y_arriba)-1]]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        values = ','.join(str(v) for v in puntos_aux)
        
                        print ('Puntos nuevos: ' + values)
            
            lista.append(2*x+3)
            lista2.append(cont_x)
            
        if 2*len(self.numeros) in self.numeros:     #Esto no hace mucha falta porque siempre este número va a estar ya en la lista
            valor_asociado=2*self.numeros.index(2*len(self.numeros))+1
            if valor_asociado in lista:
                print (str(2*len(self.numeros))+ ' ' + str(valor_asociado))
                volver=True
            else:
                if 2*self.numeros.index(-2*len(self.numeros))+1 in lista:
                    print (str(-2*len(self.numeros))+ ' ' + str(2*self.numeros.index(-2*len(self.numeros))+1))
                    volver=True
                
        print(puntos_aux)
        print(lista)

n=Nudo(8, -10, 12, 2, 14, -6, 4) #Mis apuntes
n.dibujar_nudo_dowker()

m=Nudo(-8,10,16,-12,14,-6,-2,4) #nudocap3a5.pdf
#m.dibujar_nudo_dowker()


#m.numero_arcos_superiores() 
'''n.numero_arcos_superiores()
l=Nudo(10,14,16,12,6,2,8,4)
l.numero_arcos_superiores()




t.numero_arcos_superiores()
'''

'''
import turtle

point1 = (50, 100)
point2 = (150, 200)

turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.goto(point2)

turtle.hideturtle()
turtle.exitonclick()
'''
