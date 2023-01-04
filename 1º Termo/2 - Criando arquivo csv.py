import csv
with open ('dados_estacao.csv', 'w', newline='') as arquivo:

    final = csv.writer(arquivo, delimiter=';')

    final.writerow(['Pressão', 'Temperatura','Umidade'])
    final.writerow(['235,15','25,3','87'])
    final.writerow(['235,15','25,3','87'])
    final.writerow(['235,15','25,3','87'])
    final.writerow(['235,15','25,3','87'])
    final.writerow(['235,15','25,3','87'])