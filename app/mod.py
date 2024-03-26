def getPopulation(data):
  years_population = {
    '2022': int(data[0]['2022 Population']),
    '2020': int(data[0]['2020 Population']),
    '2015': int(data[0]['2015 Population']),
    '2010': int(data[0]['2010 Population']),
    '2000': int(data[0]['2000 Population']),
    '1990': int(data[0]['1990 Population']),
    '1980': int(data[0]['1980 Population']),
    '1970': int(data[0]['1970 Population']),
  }
  labels = years_population.keys()
  values = years_population.values()
  return labels, values

def populatin_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  if result == []:
    return f'{country} no se encuentra en la base de datos'
  return result

def get_world_population_percentage(data):
  total= 0
  for item in data:
    print( item['World Population Percentage'])
  #world_population = list(sum(int(data['World Population Percentage'])))
  #print(data)