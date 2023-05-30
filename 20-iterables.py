for i in range(1,10):
    print(i)

myIterable = iter(range(1,11)) #iter es un objeto iterable especial de python.
print(myIterable)
print(next(myIterable)) #con next puedo iterar una vez, dentro de objeto iter.
print(next(myIterable)) #si repito next crece el valor.
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
#si repito el next y termina el rango produce una excepcion.

