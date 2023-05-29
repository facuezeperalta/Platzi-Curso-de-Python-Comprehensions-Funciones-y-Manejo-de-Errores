import utils

keys, values = utils.getPopulation()
print(keys, values)

""" print(utils.name) #llamo a mod desde este archivo. """


countriesToFilter = [
    {
        'Country' : 'Colombia',
        'population' : 500,
    },
    {
        'Country' : 'Argentina',
        'population' : 1500
    },
    {
        'Country' : 'Chile',
        'population' : 350
    }
]


pais = input('ingrese el país ==> ')

resultInput = utils.popByCountry(countriesToFilter,pais)

print(resultInput)
print('--------------------------------------------------------') 
""" result = utils.popByCountry(countriesToFilter,'Argentina')
print('---Filtado---')
print(result)

result = utils.popByCountry(countriesToFilter,'Chile')
print(result) """