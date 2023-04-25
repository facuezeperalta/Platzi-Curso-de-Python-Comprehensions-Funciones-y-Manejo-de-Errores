# 
setCountries = {'Argentina','Colombia','Mexico'}

print(setCountries)
print(type(setCountries))

setNumbers = {1,2,3,4,5,443,5}
print(setNumbers) 

setString = set('Hola')

print(setString)

setFromTuple = set(('Sony',125,'Perro','Gato','abc','Sony'))

print(setFromTuple)

#se puede transformar en conjunto una lista de numeros para evitar los duplicados.
numbers = [1,2,3,1,3,4]

setNumbers = set(numbers)

print(setNumbers)
resultUniqueNumbers = list(setNumbers)
print(resultUniqueNumbers)
print(type(resultUniqueNumbers))