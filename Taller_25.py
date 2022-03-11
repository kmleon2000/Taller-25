import pandas as pd

data = pd.read_csv('tabla.csv',encoding='iso-8859-1')

def Valor_promedio_mun(mun:str):
  """a. Calcule el valor promedio por metro cuadrado de un municipio dado, es decir,
    el nombre del municipio es un parámetro de la función"""

  filtered_data = data[data.Municipio == mun]

  return sum(filtered_data.Precio) / sum(filtered_data.Área)

#def lista_de_predios(mun:str, tipo:str):

def lista_de_predios(mun:str, tipo:str, ret:int = 1):
  """b. Retorne una lista ordenada de precios para un municipio y tipo dado, es
    decir, el municipio y el tipo son parámetros de la función."""

  params = [('Municipio',mun),('Tipo',tipo)]
  selected = data

  for key, val in params:
    selected = selected[selected[key] == val]

  if ret == 1:
    return list(selected.Precio)
  elif ret == 2:
    return selected

def lista_de_predios_umbral(mun:str, tipo:str, precio:int):
  """c. Retorne una lista ordenada de los precios que sean iguales o mayores a un
    valor dado para un municipio y tipo específico. Tanto el valor, como el nombre
    de municipio y tipo son parámetros de la función."""
  
  selected = lista_de_predios(mun, tipo, 2)

  selected = selected[selected['Precio'] >= precio]

  return list(selected.Precio)

def promedio_area():
  """d. Retorne el promedio del área de todos los predios de la tabla."""
  
  return sum(list(data.Área))/len(list(data.Área))

def lista_municipios():
  """e. Retorne una lista ordenada de los municipios que tienen predios registrados
    en la tabla. Los nombres no pueden ir repetidos"""

  return list(data.Municipio.unique())
  

def lista_areas(tipo:str):
  """f. Retorne una tupla con las áreas de los predios de un tipo dado. El tipo es un
    parámetro de la función."""
  
  return list(data[data.Tipo == tipo].Área.unique())

def ver_predio(cod:int):
  """g. Retorne un diccionario con los datos completos de un predio dado. El código
    del predio es un parámetro de la función."""
  
  selected = data[data.Código_predio == cod]
  dictionary = dict()
  for i in range(0,len(data.columns)):
    dictionary.setdefault(selected.columns[i],selected.values.tolist()[0][i])
    
  return dictionary


print("""a. Calcule el valor promedio por metro cuadrado de un municipio dado, es decir,
  el nombre del municipio es un parámetro de la función""")
print(Valor_promedio_mun(input('digite el municipio: ')))

print("""\nb. Retorne una lista ordenada de precios para un municipio y tipo dado, es
  decir, el municipio y el tipo son parámetros de la función.""")
print(lista_de_predios(
  input('digite el municipio: '),
  input('digite el tipo: ')
))

print("""\nc. Retorne una lista ordenada de los precios que sean iguales o mayores a un
  valor dado para un municipio y tipo específico. Tanto el valor, como el nombre
  de municipio y tipo son parámetros de la función.""")
print(lista_de_predios_umbral(
  input('digite el municipio: '),
  input('digite el tipo: '),
  int(input('digite el valor: '))
))

print("""\nd. Retorne el promedio del área de todos los predios de la tabla.""")
print(promedio_area())

print("""\ne. Retorne una lista ordenada de los municipios que tienen predios registrados
  en la tabla. Los nombres no pueden ir repetidos""")
print(lista_municipios())

print("""\nf. Retorne una tupla con las áreas de los predios de un tipo dado. El tipo es un
  parámetro de la función.""")
print(lista_areas(input('digite el tipo: ')))

print("""\ng. Retorne un diccionario con los datos completos de un predio dado. El código
  del predio es un parámetro de la función.""")
print(ver_predio(int(input('digite el código: '))))