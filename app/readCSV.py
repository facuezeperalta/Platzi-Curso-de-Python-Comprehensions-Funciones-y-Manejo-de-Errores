import csv
def readCsv(path):
    with open(path,'r') as csvfile:
        data = []
        reader = csv.reader(csvfile,delimiter=',')
        header = next(reader) #obtengo los titulos de la primera fila.
        for row in reader:
            iterable = zip(header,row)
            countryDic = {key:value for key,value in iterable}
            data.append(countryDic)
        return data
            

if __name__ == '__main__': #corre como script
    data = readCsv('../app/world_population.csv')
    print(data[0])



    