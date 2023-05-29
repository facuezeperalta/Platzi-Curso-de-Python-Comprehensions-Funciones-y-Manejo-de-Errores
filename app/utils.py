#defino una función para llamarlo desde otro lugar

def getPopulation():
    keys  = ['Colombia','Argentina','Bolivia']
    values = ['150','500','200']
    return keys, values

""" name = 'Facundo' """

def popByCountry(data,country):
    result = list (filter(lambda item: item['Country'] == country, data))
    return result


