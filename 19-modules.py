import sys
print(sys.path)
import re 

text = 'mi numero es 313213321 soy facu y mi edad 28'
result = re.findall('[0-9]+',text) #las expresiones regulares tienen su propia sintaxis.
print(result)

import time  #modulo de tiempo

timestamp = time.time()
localhour = time.localtime()
resulthour = time.asctime(localhour)
print(resulthour) 

import collections #utilidad para manejar listas

numeros = [1,25,30,45,50,45,30,1,2,1,1,6,7,10,99,50,105,105,105]

counter = collections.Counter(numeros) #funcion counter sirve para allar la frencuencia de algo en especial en una lista, devuelve un diccionario con la frecuencide cada uno de los elementos de la lista.
print(counter)


