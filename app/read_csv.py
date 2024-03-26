import csv

def read_csv(path):
  with open(path, 'r') as file:
    reader = csv.reader(file, delimiter=',') # csv.reader convierte los datos en un objeto
    
    header = next(reader) # Trae la primera linea del archivo donde está el encabezado 
    data = []
    #print(header)
    for row in reader:
      iterable = zip(header, row) # Guarda en tuplas el encabezado y el valor de cada fila
#      print(list(iterable))
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
