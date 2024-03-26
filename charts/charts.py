import matplotlib.pyplot as plt # importar librería para generar gráficas

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [100, 50, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('pie.png') # La gráfica se genera en una imagen
    plt.close()