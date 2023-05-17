setCameras = {'Nikon','Canon','Sony'}
setFlashes = {'Godox','ProFoto','BrownColor','Nikon','Canon'}


#union de conjuntos

set_CamsAndFlashes = setCameras.union(setFlashes)
print(set_CamsAndFlashes)

#también se pueden usar operadores matematicos en vez de llamar al método
print(setCameras | setFlashes ) # | es para unión.

#Intersección: elementos en común que tiene en común.
set_CamsAndFlashes = setCameras.intersection(setFlashes)
print(set_CamsAndFlashes)
#con operador &
print(setCameras & setFlashes)


#diferencia operador: -
set_CamsAndFlashes = setCameras.difference(setFlashes)
print(set_CamsAndFlashes)

#difrencia simétrica. operador: ^

set_CamsAndFlashes = setCameras.symmetric_difference(setFlashes)
print('Difrencia simetrica: ')
print(set_CamsAndFlashes)