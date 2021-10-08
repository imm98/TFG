#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:15:35 2021

@author: inaki
"""
import copy #Para el constructor de copia que no hace falta

import turtle


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
        
        y_arriba=[] #Lista que nos indicará la altura de las aristas que pasen por encima del nudo
        x_arriba=[] #Lista de listas que nos indicará el valor mínimo y máximo de x para la altura y del vector de arriba    
        y_abajo=[]
        x_abajo=[]
        
        y_lista_fuera_raiz=[]
        lista_fuera_raiz=[]
        
        puntos_aux=[]   #Va a contener los diferentes vértices de las aristas del nudo resultante
        
        
        lista=[]    #Contiene los valores de los cruces que hemos recorrido 
        lista2=[]   #Contiene la coordenada x de los cruces que vamos obteniendo en la lista 1
        arriba=True #Creo que se puede eliminar
        acabarVolver=False
        
        
        
        if (self.numeros[0]>0):             #Esto es para el primer valor
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
        
        for x in range(len(self.numeros)):
            
            print ('x: ' + str(x))
            print ('len(self.numeros): ' + str(len(self.numeros)))

            
            
            #Valores pares
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
            
            
            
            
            if(volver==False):  #Si se llega antes al número par    #Habría que ver más adelante si se ha realizado previamente un cruce
                print('LLegaaa')
                if (acabarVolver==False):
                    cont_x+=1
                    print ('Contador: '+ str(cont_x) + ' cruce '+ str(2*x+2))
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
                    lista2.append(cont_x)    
                        
                else:   #En el caso de que el último cruce que hemos pasado fuera un cruce con los dos valores en la lista y en el que estemos analizando no esté ninguno
                    '''Queremos ver en que sentido tenemos que dibujar el siguiente cruce posteriormente a haber recorrido un cruce dos veces, que será nuevo ya que ninguno de sus valores está en la lista'''
                    print('Holaaaaaa')
                    aux=False
                    contador_aux=0
                    while(aux==False):
                        contador_aux+=1
                        if (contador_aux%2 ==1):
                            if abs(self.numeros[x+1]) in lista:
                                aux=True
                        else:
                            if 2*x+2+contador_aux in self.numeros:
                                vasoc=2*self.numeros.index(2*x+2+contador_aux)+1
                                if vasoc in lista:
                                    aux=True
                            else:
                                vasoc=2*self.numeros.index(-(2*x+2+contador_aux)+1)
                                if vasoc in lista:
                                    aux=True
                    print('contador_aux: '+ str(contador_aux))
                    
                    
                    if ((contador_aux)%2 ==0):  
                        posicion_relativa_x=lista2[lista.index(vasoc)]
                    else:
                        posicion_relativa_x=lista2[lista.index(self.numeros[x+1+contador_aux/2])]
                    
                    print('cont_x: '+ str(cont_x))
                    print('posicion_relativa_x: '+ str(posicion_relativa_x))
                    posicion_final_x=(cont_x+posicion_relativa_x)/2
                    print('posicion_final_x: '+ str(posicion_final_x))
                    if (self.numeros[x+1]>0): #cruce_inferior, llegamos hasta posicion_final_x-0.1 o +0.1
                        if (posicion_final_x>cont_x):
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            punto=[posicion_final_x-0.1, cont_y]
                            puntos_aux.append(punto)
                            punto=[posicion_final_x+0.1, cont_y]
                            cont_x=posicion_final_x+0.1
                            
                        else:
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            punto=[posicion_final_x+0.1, cont_y]
                            puntos_aux.append(punto)
                            punto=[posicion_final_x-0.1, cont_y]
                            cont_x=posicion_final_x-0.1
                    
                    lista_fuera_raiz.append(2*x+2)
                    y_lista_fuera_raiz.append(cont_y)

                    lista2.append(posicion_final_x)        
                  
                    values = ','.join(str(v) for v in puntos_aux)
                          
                    print ('Puntos nuevos: ' + values)       
            
                 
            else:               #Si es la segunda vez que lo vamos a recorrer
                print('Llegaa')
                acabarVolver=True   #Esta variable sirve para en caso de que volvamos y luego haya un cruce nuevo saber hacia donde nos debemos de mover en el eje x    
                print ('Cruce ' + str(2*x+2) + ' Valor asociado: '+str(valor_asociado))    
                posicion_x_final=lista2[lista.index(valor_asociado)]
                print('posicion_x_inicial: ' + str(cont_x))
                print('posicion_x_final: ' + str(posicion_x_final))
                print('lista_fuera_raiz')
                print (lista_fuera_raiz)

                if valor_asociado in lista_fuera_raiz:       #Es decir, si vamos a recorrer de nuevo un cruce que no está en la  'raiz principal'
                    print ('LLega par')
                    punto=[cont_x, cont_y] 
                    puntos_aux.append(punto)
                    
                    y_intermedia=( (cont_y+y_lista_fuera_raiz[lista_fuera_raiz.index(valor_asociado)])/2)
                    punto=[cont_x, y_intermedia]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    cont_x=posicion_x_final
                    punto=[cont_x, y_intermedia]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)

                    if 2*x+2 in self.numeros: #Si el cruce es superior
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

                    values = ','.join(str(v) for v in puntos_aux)
            
                    print ('Puntos nuevos: ' + values)
                                        

                else:
                    if arriba:                              #creo que se puede eliminar
                        arriba=False
                        if not y_arriba:                    #si es la primera vez que se va a pasar dos veces por el mismo cruce
                            y_arriba.append(1)
                            cont_x+=0.5
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
                                puntos_aux.append(punto)
                                punto=[x_arriba[len(x_arriba)-1], -0.1]
                                puntos_aux.append(punto)

                                
                            '''Dado que estamos en el caso de que y_arriba estuviera vacío, y_abajo también estará vacío, por tanto añadimos el valor -1'''
                            
                            
                            punto=[x_arriba[len(x_arriba)-1], -1]
                            puntos_aux.append(punto)
                            cont_x=posicion_x_final
                            cont_y=-1
                            #puntos_aux.append(punto)
                            values = ','.join(str(v) for v in puntos_aux)
            
                            print ('Puntos nuevos: ' + values)
                        
                        else: #si ya han sido varias veces las que se va a ir por encima del nudo (es decir, ahora la y no va a poder ser 1)
                            print('x_arriba_par: ')
                            print(x_arriba)
                            contador=0
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            cont_y=1
                            
                            for x_aux in x_arriba:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):
                                    if (x_aux>aux1):
                                        if (cont_x>aux1 and cont_x < x_aux ):
                                            cont_y-= y_arriba[int((contador-1)/2)]/2
                                        else:
                                            cont_y+= y_arriba[int((contador-1)/2)]/2
                                    else:
                                        if (cont_x>x_aux and cont_x < aux1 ):
                                            cont_y-= y_arriba[int((contador-1)/2)]/2
                                        else:
                                            cont_y+= y_arriba[int((contador-1)/2)]/2

                                    print ('const_y_intermedia_par: '+ str(cont_y))
                                contador+=1
                            
                            if (cont_y<=0): #Esto es para corregir la altura por si la altura es menor que 0, que no puede darse ya que es un 'arco superior' 
                                minimo=1
                                for i in y_arriba:
                                    if i<minimo:
                                        minimo=i
                                cont_y=minimo/2       
                                    
                                    
                            
                            print('cont_y_after_par: '+ str(cont_y))
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
                            if 2*x+2 not in self.numeros: #Es decir, si el cruce es inferior
                                punto=[cont_x, 0.1]
                                puntos_aux.append(punto)
                                cont_y=-0.1
                                '''punto=[cont_x, cont_y]
                                puntos_aux.append(punto)'''
                            else:
                                cont_y=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                
                            values = ','.join(str(v) for v in puntos_aux)
                            
                            print ('lista: ')
                            print(lista)
                            print('lista2: ')
                            print(lista2)
                            print ('Puntos nuevos: ' + values) 
                            print ('Arriba= '+ str(arriba))
                    
                    
                    
                    else:
                        
                        arriba=True
                        if not y_abajo:
                            y_abajo.append(-1)
                            punto=[cont_x, y_abajo[len(y_abajo)-1]]
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
                            print('x_abajo_pares: ')
                            print(x_abajo)
                            contador=0
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                            cont_y=-1
                            for x_aux in x_abajo:
                                if ((contador % 2)==0):
                                    aux1=x_aux
                                if ((contador % 2)==1):
                                    if (x_aux>aux1):
                                        if (cont_x>aux1 and cont_x < x_aux ):
                                            cont_y-= y_abajo[int((contador-1)/2)]/2
                                        else:
                                            cont_y+= y_abajo[int((contador-1)/2)]/2
                                            
                                    else:
                                        if (cont_x>x_aux and cont_x < aux1 ):
                                            cont_y-= y_abajo[int((contador-1)/2)]/2
                                        else:
                                            cont_y+= y_abajo[int((contador-1)/2)]/2
                                contador+=1
                                
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
                            if 2*x+2 not in self.numeros: #Es decir, si el cruce es inferior
                                punto=[cont_x, -0.1]
                                puntos_aux.append(punto)
                                cont_y=0.1
                                '''punto=[cont_x, cont_y]
                                puntos_aux.append(punto)'''
                            else:
                                cont_y=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                
                            values = ','.join(str(v) for v in puntos_aux)
                            
                            print ('Puntos nuevos: ' + values) 
                            print ('Arriba= '+ str(arriba))
                    
                    values = ','.join(str(v) for v in puntos_aux)
            
                    print ('Puntos: ' + values)
                
                lista2.append(cont_x)
            lista.append(2*x+2)
            





            if (x!=(len(self.numeros)-1)):  #Si no estamos en la última iteración del vector

                #Valores impares
                volver=False
                if abs(self.numeros[x+1]) in lista:
                    print(str(2*x+3)+' '+ str(abs(self.numeros[x+1])))
                    volver=True
                
                if (self.numeros[x+1]>0):   
                    signo='Neg'
                else:
                    signo='Pos'
                    
                    
                if (volver==False):             #Si es un punto nuevo
                    if (acabarVolver==False):
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
                            
                        lista2.append(cont_x)
                    
                    else:
                        print('Holaaaaaa2')
                        print(lista)
                        aux=False
                        contador_aux=0
                        while(aux==False):
                            contador_aux+=1
                            if ((contador_aux)%2 ==1):      #2*x+4
                                if 2*x+3+contador_aux in self.numeros:
                                    vasoc=2*self.numeros.index(2*x+3+contador_aux)+1    #Nos devuelve el número impar asociado al número par 2*x+3+contador_aux
                                    print('vasoc' + str(vasoc))
                                    if vasoc in lista:
                                        aux=True
                                else:
                                    vasoc=2*self.numeros.index(-(2*x+3+contador_aux))+1
                                    if vasoc in lista:
                                        aux=True  
                                
                            else:
                                if abs(self.numeros[x+1+contador_aux/2]) in lista:
                                    aux=True
                        print('contador_aux: '+ str(contador_aux))
                        
                        if ((contador_aux)%2 ==1):  
                            posicion_relativa_x=lista2[lista.index(vasoc)]
                        else:
                            posicion_relativa_x=lista2[lista.index(self.numeros[x+1+contador_aux/2])]
                        
                        print('cont_x: '+ str(cont_x))
                        print('posicion_relativa_x: '+ str(posicion_relativa_x))
                        posicion_final_x=(cont_x+posicion_relativa_x)/2
                        print('posicion_final_x: '+ str(posicion_final_x))
                        if (self.numeros[x+1]>0): #cruce_inferior, llegamos hasta posicion_final_x-0.1 o +0.1
                            if (posicion_final_x>cont_x):
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                punto=[posicion_final_x-0.1, cont_y]
                                puntos_aux.append(punto)
                                punto=[posicion_final_x+0.1, cont_y]
                                cont_x=posicion_final_x+0.1
                                
                            else:
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                punto=[posicion_final_x+0.1, cont_y]
                                puntos_aux.append(punto)
                                punto=[posicion_final_x-0.1, cont_y]
                                cont_x=posicion_final_x-0.1

                        lista_fuera_raiz.append(2*x+3)
                        y_lista_fuera_raiz.append(cont_y)      
                        lista2.append(posicion_final_x)
                        values = ','.join(str(v) for v in puntos_aux)
                            
                        print ('Puntos nuevos: ' + values)
            
            
                
                else:           #Si es la segunda vez que lo vamos a recorrer
                    acabarVolver=True   #Esta variable sirve para en caso de que volvamos y luego haya un cruce nuevo saber hacia donde nos debemos de mover en el eje x
                    posicion_x_final=lista2[lista.index(abs(self.numeros[x+1]))]
                    if abs(self.numeros[x+1]) in lista_fuera_raiz: #Es decir, si el número asociado a ese número impar no está en la raíz 
                        print ('LLega impar')
                        punto=[cont_x, cont_y] 
                        puntos_aux.append(punto)
                        
                        y_intermedia=( (cont_y+y_lista_fuera_raiz[lista_fuera_raiz.index(abs(self.numeros[x+1]))])/2)
                        punto=[cont_x, y_intermedia]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)
                        cont_x=posicion_x_final
                        punto=[cont_x, y_intermedia]
                        puntos_aux.append(punto)
                        puntos_aux.append(punto)

                        if abs(self.numeros[x+1]) not in self.numeros: #quiere decir que el cruce es superior
                            cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(abs(self.numeros[x+1]))]
                            punto=[cont_x, cont_y]
                            puntos_aux.append(punto)
                        
                        else:
                            if (y_intermedia < cont_y):
                                punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(abs(self.numeros[x+1]))]+0.1]
                                puntos_aux.append(punto)
                                cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(abs(self.numeros[x+1]))]-0.1
                            else:
                                punto=[cont_x, y_lista_fuera_raiz[lista_fuera_raiz.index(abs(self.numeros[x+1]))]-0.1]
                                puntos_aux.append(punto)
                                cont_y=y_lista_fuera_raiz[lista_fuera_raiz.index(abs(self.numeros[x+1]))]+0.1

                    else:
                        if arriba:
                            arriba=False
                            if not y_arriba:
                                y_arriba.append(1)
                                cont_x+=0.5
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
                                    puntos_aux.append(punto)
                                    punto=[x_arriba[len(x_arriba)-1], -0.1]
                                    puntos_aux.append(punto)
                                    
                                '''Dado que estamos en el caso de que y_arriba estuviera vacío, y_abajo también estará vacío, por tanto añadimos el valor -1'''
                                y_abajo.append(-1)
                                x_abajo.append(x_2)
                                punto=[x_arriba[len(x_arriba)-1], y_abajo[len(y_arriba)-1]]
                                puntos_aux.append(punto)
                                #puntos_aux.append(punto)
                                
                                cont_x=x_2
                                cont_y=y_abajo[len(y_abajo)-1]
                                print('cont_y= '+ str(cont_y))
                                values = ','.join(str(v) for v in puntos_aux)
                                
                                print ('Puntos nuevos: ' + values)
                            
                            else:
                                print('x_arriba_impar: ')
                                print(x_arriba)
                                contador=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                cont_y=1
                                for x_aux in x_arriba:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                cont_y-= y_arriba[int((contador-1)/2)]/2
                                            else:
                                                cont_y+= y_arriba[int((contador-1)/2)]/2
                                        else:
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                cont_y-= y_arriba[int((contador-1)/2)]/2
                                            else:
                                                cont_y+= y_arriba[int((contador-1)/2)]/2
                                        print ('const_y_intermedia_impar: '+ str(cont_y))
                                    contador+=1
                                
                                
                                if (cont_y<=0): #Esto es para corregir la altura por si la altura es mayo que 0, que no puede darse ya que es un 'arco inferior' 
                                    minimo=1
                                    for i in y_arriba:
                                        if i<minimo:
                                            minimo=i
                                    cont_y=minimo/2 

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
                                if (self.numeros[x+1]>0):   #Si el cruce es inferior...
                                    print ('selfnumeros: '+ str(self.numeros[x+1]))
                                    punto=[cont_x, 0.1]     #Lllega hasta 0.1
                                    puntos_aux.append(punto)
                                    cont_y=-0.1
                                    '''punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)'''
                                else:
                                    cont_y=0
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    
                                print ('lista: ')
                                print(lista)
                                print('lista2: ')
                                print(lista2)
                                
                                values = ','.join(str(v) for v in puntos_aux)
                                
                                print ('Puntos nuevos: ' + values)
                                print ('Arriba= '+ str(arriba))
                                
                        else:
                            arriba=True
                            if not y_abajo:
                            
                            
                                y_abajo.append(-1)
                                punto=[cont_x, y_abajo[len(y_abajo)-1]]
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
                                print('x_abajo_impares')
                                print(x_abajo)
                                contador=0
                                punto=[cont_x, cont_y]
                                puntos_aux.append(punto)
                                cont_y=-1
                                for x_aux in x_abajo:
                                    if ((contador % 2)==0):
                                        aux1=x_aux
                                    if ((contador % 2)==1):
                                        if (x_aux>aux1):
                                            if (cont_x>aux1 and cont_x < x_aux ):
                                                
                                                cont_y-= y_abajo[int((contador-1)/2)]/2
                                            else:
                                                
                                                cont_y+= y_abajo[int((contador-1)/2)]/2
                                                
                                        else:
                                            if (cont_x>x_aux and cont_x < aux1 ):
                                                
                                                cont_y-= y_abajo[int((contador-1)/2)]/2
                                            else:
                                                
                                                cont_y+= y_abajo[int((contador-1)/2)]/2
                                    contador+=1
                                    
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
                                
                                if (self.numeros[x+1]>0):   #Si el cruce es inferior...
                                    print ('selfnumeros: '+ str(self.numeros[x+1]))
                                    punto=[cont_x, -0.1]     #Lllega hasta 0.1
                                    puntos_aux.append(punto)
                                    cont_y=0.1
                                    '''punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)'''
                                else:
                                    cont_y=0
                                    punto=[cont_x, cont_y]
                                    puntos_aux.append(punto)
                                    
                                values = ','.join(str(v) for v in puntos_aux)
                                
                                print ('Puntos nuevos: ' + values)
                                print ('Arriba= '+ str(arriba))
                    
                
                    lista2.append(cont_x)
                lista.append(2*x+3)

            else: #Es decir, que haya que volver al 1 
                print('Ultimo punto')
                punto=[cont_x, cont_y]
                puntos_aux.append(punto)

                if arriba: #Me quiero volver por la el arco más arriba que se pueda construir 
                    maximo_y=0
                    for i in y_arriba:
                        if (i>maximo_y):
                            maximo_y=i
                    maximo_y+=0.5
                    cont_y=maximo_y
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
                    minimo_y=0
                    for i in y_abajo:
                        if (i<minimo_y):
                            minimo_y=i
                    minimo_y-=0.5
                    cont_y=minimo_y
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    cont_x=-0.5 #Es decir, donde empieza el segmento del cruce 1
                    punto=[cont_x, cont_y]
                    puntos_aux.append(punto)
                    puntos_aux.append(punto)
                    punto=[cont_x, 0]
                    puntos_aux.append(punto)

        return puntos_aux
       

n=Nudo(8, -10, 12, 2, 14, -6, 4) #Mis apuntes
#n.dibujar_nudo_dowker()

m=Nudo(-8,10,16,-12,14,-6,-2,4) #nudocap3a5.pdf
puntos=m.dibujar_nudo_dowker()


#m.numero_arcos_superiores() 
'''n.numero_arcos_superiores()
l=Nudo(10,14,16,12,6,2,8,4)
l.numero_arcos_superiores()




t.numero_arcos_superiores()
'''

print('Los puntos son: ')
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

