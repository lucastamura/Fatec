import csv
with open('dados_estacao.csv') as csv_file:

    arquivo = csv.reader(csv_file, delimiter=';')

    for i in arquivo:
      print( i[0] + ', ' + i[1] + ', ' + i[2] )