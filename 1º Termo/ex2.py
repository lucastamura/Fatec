nome = str(input('Informe seu nome .....: ')) #aspas errada
nasc = int(input("infome ano de nascimento...: "))
hoje = int(input('Informe ano atual.....: '))
valor = int(input('Informe quanto tem no bolso:'))

idade = hoje - nasc

print('%s tem em torno de %d anos e possui R$ %.2f' %(nome,idade,valor))