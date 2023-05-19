import random

countries = ['Argentina','Chile','Mexico','Brasil']

population = {country: random.randint(100,2500) for country in countries}
print (population)
