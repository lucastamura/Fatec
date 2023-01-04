import csv
with open ('dados_empresa.csv', 'w', newline='') as arquivo:

    final = csv.writer(arquivo, delimiter=';')

    final.writerow(['Nome Completo', 'Data de nascimento', 'Número do cartão do princesa', 'CPF', 'Celular', 'Endereço','Número'])
    final.writerow(['Gabriel Henrique de Oliveira Garcia', '05/04/2004', '3303000039404', '51660959870', '14999078712', 'Rua Roberto Zapoula', '145'])
    final.writerow(['Cristhian Cesar Gabriel','20/02/2004','3303000039897','48836725813','14998345411','Jucidene Braga Sales Barreto','146'])
    final.writerow(['Lucas Izumi Tamura Santos','29/10/2003','3303000040143','48939518829','14996058356','Rua Ribeirão Preto', '460'])
    final.writerow(['Vinicius chociai', '10/11/2003', '3303000040275','05910956965','14998511900','rua Pedro Martins', '69'])
    final.writerow(['João Pedro Bertonha Betini','20/02/2003','3303700639497', '537.690.938-79' , '14998222003', 'R. Olavo Bilac', '461'])
