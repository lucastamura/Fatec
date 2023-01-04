nome = 'Luis'
idade = 10
valor = 50

print('Luis tem', idade,'anos')
print('Luis tem',idade,'anos e R$ %d no bolso'%valor)
print('Luis tem %d anos' %idade)
print('Luis tem {} anos'.format(idade))
print(nome,'tem',idade,'anos e apenas R$',valor,'no bolso')
print('%s tem %d anos e apenas R$ %.f no bolso' %(nome, idade, valor))
print('{} tem {} anos e apenas R$ {} no bolso'.format(nome, idade, valor))