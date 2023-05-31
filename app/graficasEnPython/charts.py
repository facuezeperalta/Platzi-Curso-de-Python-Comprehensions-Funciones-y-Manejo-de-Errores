import matplotlib.pyplot as plt #lo usamos con ese sinónimo para usar la librería.

def generateBarChart():
    labels = ['a','b','c']
    values = [100,200,80]

    fig, ax = plt.subplot() #subplot es un método que vien de la librería
    ax.bar(labels, values)
    plt.show()

if __name__ == '__main__':
    generateBarChart()
