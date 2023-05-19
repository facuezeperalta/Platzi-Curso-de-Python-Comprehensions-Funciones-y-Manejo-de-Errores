#Escrito en varias líneas
import random
diccionario = {}

for i in range(1,11):
    diccionario[i] = i * 2

print (diccionario)

diccionarioV2 = {i: i * 2 for i in range(1,11)} #permite resolver todo en una sola línea de código.
print (diccionarioV2)

countries = ['Argentina','Mexico','Colombia']
population = {}

for country in countries: 
    population[country] = random.randint(1,500)
print(population)

populationV2 = {country: random.randint(1,500) for country in countries} #version corta.
print (populationV2)


print('----------------------------------------------------------------')

names = ['Facundo','Nicolas','Roberto','Jorge']
ages = [28,27,25,18]


 
new_dic = {name: age for (name,age) in zip(names,ages)}

print(new_dic)


print('----------------------------------------------------------------')

cameras =['D7200','D5300']
lenses =['17-50 2.8','70-200 2.8']

""" print(list(zip(cameras,lenses))) """ #uno las listas con zip creando una lista con tuplas dentro de ella.

equiment = {camera : lenses for (camera,lenses) in zip(cameras,lenses)} #clave seria camera y el valor viene dado por lenses, luego recorro con for y las dos variables en el zip de las dos listas.
print(equiment) 

print('---------')

services = ['Wedding Photo','Wedding Video','15 Photo','15 video']
print(type(services))
prices = [250,350,200,250]
print(type(services))

pricesList = {services : prices for (services,prices) in zip(services,prices)}

print(pricesList)
print(type(pricesList))








