import utils
import readCSV
import charts


def run():
    data = readCSV.readCsv('./world_population.csv')
    
    country = input('ingrese el país ==> ')
    
    resultInput = utils.popByCountry(data,country)

    if len(resultInput) > 0:
        country = resultInput[0]
        labels, values = utils.getPopulation(country)
        charts.generateBarChart(labels, values)

    else: print('NO se ha encontrado el pais.')
    """ print(utils.name) #llamo a mod desde este archivo. """
    
    print('--------------------------------------------------------') 
""" result = utils.popByCountry(countriesToFilter,'Argentina')
print('---Filtado---')
print(result)

result = utils.popByCountry(countriesToFilter,'Chile')
print(result) """

if __name__ == '__main__':
    run()