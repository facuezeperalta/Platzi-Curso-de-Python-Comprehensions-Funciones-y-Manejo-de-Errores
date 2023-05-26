import random

countries = ['Argentina','Chile','Mexico','Brasil']

populationV2 = {country: random.randint(100,2500) for country in countries}
print (populationV2)

result = {country:population for (country,population) in populationV2.items() if country == 'Argentina' and population > 500  }

print (result)

text = 'Sooy Faacu'

vocals = { c : c.upper()  for c in text if c in 'aeiou'}
print(vocals)
