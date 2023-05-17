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

print(list(zip(names,ages)))
 
new_dic = {name: age for (name,age) in zip(names,ages)}

print(new_dic)





