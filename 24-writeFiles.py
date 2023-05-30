""" file = open("Platzi-Curso-de-Python-Comprehensions-Funciones-y-Manejo-de-Errores/text.txt") """
with open('Platzi-Curso-de-Python-Comprehensions-Funciones-y-Manejo-de-Errores/text.txt','r+') as file: #r+ es lectura + escritura.
    #w+ permite leer y escribir pero con sobreescritura que elimina lo que ya este guardado.
    for line in file:
        print(line)
    file.write('Nueva linea agregada en el archivo \n')
    file.write('Sony A7III \n')