# -*- coding: utf-8 -*-
"""Práctica 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qQj0Pz1WirakC8ha0zZu0j0cKusNWpOx
"""

import random  
import math  
import matplotlib.pyplot as plt  
random.seed()  
n=100 # número de pasos  
r=1 # longitud del paso  

#paseo unidimensional
x1d = 0
listax1d=[x1d]

for i in range (n):
  if random.random() < 0.5:
    r = -1*r
  x1d+= r
  listax1d.append(x1d)

print("El paseo aleatorio unidimensional es: ", listax1d)


#paseo bi-dimensional
x2d=y2d=0 # punto de partida (x,y)=(0,0)  
listax2d=[x2d]  
listay2d=[y2d]  

#la cantidad de radianes en un círculo es 2*pi
#por eso, para especificar el ángulo, cogemos un número aleatorio del 0 al 1 multiplicado por 2*pi
 
for i in range(n):  
  angulo=random.random()*math.pi*2
  x2d+=r*math.cos(angulo)  
  y2d+=r*math.sin(angulo)  
  
  listax2d.append(x2d)  
  listay2d.append(y2d)  
plt.plot(listax2d,listay2d)  
print("Representación gráfica del paseo aleatorio bidimensional:")
plt.show()