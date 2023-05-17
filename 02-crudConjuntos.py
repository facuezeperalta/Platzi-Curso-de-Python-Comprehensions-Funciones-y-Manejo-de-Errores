setCamaras = {'Nikon','Canon','Sony'}

size = len(setCamaras)
print(size)

print('Nikon' in setCamaras)
print('Fuji' in setCamaras)

#add
setCamaras.add('Fuji')
print(setCamaras)

#update

setCamaras.update({'Leica'})
print(setCamaras)

#remove

setCamaras.remove('Leica')
print(setCamaras)
setCamaras.discard('Sonya')
print(setCamaras)


#limpiar todo el conjunto 

setCamaras.clear()
print(setCamaras)