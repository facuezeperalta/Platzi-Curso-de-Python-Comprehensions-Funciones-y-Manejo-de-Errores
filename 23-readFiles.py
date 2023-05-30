file = open('Platzi-Curso-de-Python-Comprehensions-Funciones-y-Manejo-de-Errores/text.txt')
""" print(file.read()) #lee todo el archivo, puede ser un método pesado.
print(file.readline()) #lee solo una linea del archivo, este método es mas liviano ya que va línea por linea.
print(file.readline())
print(file.readline())
print(file.readline())  """

for line in file: #corre como ciclo y lo abre y ocupa menos memoria
    print(line)


file.close() #cerramos el archivo y liberamos memoria.
print('----------------------------------------------------------------')
with open('Platzi-Curso-de-Python-Comprehensions-Funciones-y-Manejo-de-Errores/text.txt') as file: #abre y hace lo que tiene que hacer y luego cierra el archivo.
    for line in file:
        print(line)
