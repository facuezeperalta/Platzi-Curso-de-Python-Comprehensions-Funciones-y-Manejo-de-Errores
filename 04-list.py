numbers = []

for element in range(1,11):
    numbers.append(element *2)


print (numbers)

numbersv2 = [element * 2 for element in range(1,11)] #sintaxis mas corta que la anterior. y puedo operar el elemento, sea multiplicar o hacer cosas en una sola línea de código.
print (numbersv2)

numbereven= [element * 2 for element in range(1,101) if element % 2 == 0] #multiplico y si es par lo agrego a la lista.


print ('Pares ==> ',numbereven)
