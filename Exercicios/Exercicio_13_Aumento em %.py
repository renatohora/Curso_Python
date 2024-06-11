''''Faça um algoritimo que leia o salario de um funcionario e mostra seu novo salario com 15% de aumento'''''

nome = input('Digite o nome do Funcionario: ')
salario = float(input('Digite o salario do funcionario: R$ '))
#minha Solução abaixo
#novo_salario = salario + ((salario / 100) * 15)
#solução do Curso em video
novo_salario = salario + (salario * 15 / 100)
print('=' * 70)
print('Segue dados do Funcionário com atualização de 15% no salario.')
print('Nome: {}'.format(nome))
print('Salario Atual: R$ {:.2f}\nNovo Salario: R$ {:.2f}'.format(salario, novo_salario))
print('=' * 70)