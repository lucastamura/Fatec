print('Liberação do emprestimo')

salario = float(input('Qual o valor do salário ---> R$'))
emprestimo = float(input('Qual o valor do emprestimo --> R$'))
salario20 = salario*(20/100)

if emprestimo <= salario20:
  print('Empréstimo concedido')

else:
  print('Empréstimo não concedido, valor máximo permitido de R$', salario20)