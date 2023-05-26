def find_volume(length =1,width=1,depth=1): #puedo mandar valores por defecto como argumentos a una función.
    return length * width * depth,width, 'Hola'

firstResult = find_volume(width=10)

print (firstResult)
print (type(firstResult))