import mod
import read_csv
import charts


def run(data):
  country = input('Ingresa el país: ')
  result = mod.populatin_country(data, country)
  labels, values = mod.getPopulation(result)
  charts.generate_bar_chart(labels, values)
#  print(result)  

def world_population_percentage(data):
  mod.get_world_population_percentage(data)



if __name__ == '__main__':
  data = read_csv.read_csv('data.csv')
  #run(data)
  world_population_percentage(data)
  