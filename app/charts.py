import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig('bar.png')
  plt.close()

def geneart_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a','b','c']
  values = [40, 20, 60]
  geneart_pie_chart(labels, values)
#  generate_bar_chart(labels, values)