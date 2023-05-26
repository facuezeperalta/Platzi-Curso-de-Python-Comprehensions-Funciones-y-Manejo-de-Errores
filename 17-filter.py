numbers = [1,2,3,4,5]

newNumbers = list(filter(lambda nro : nro % 2 == 0, numbers))
oddNumbers = list(filter(lambda nro : nro % 2 != 0,numbers))

print('Numberos pares ==>',newNumbers)
print('Numberos impares ==>',oddNumbers)

