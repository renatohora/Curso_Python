#Faça um algoritimo que leia o salario de um funcionario e mostra seu novo salario com 15% de aumento
nome = input('Digite o nome do Funcionario: ')
salario = float(input('Digite o salario do funcionario: R$ '))
novo_salario = salario + ((salario / 100) * 15)
print('=====================================================================')
print('Segue dados do Funcionário {} com atualização de 15% no salario.'.format(nome))
print('Nome: {}'.format(nome))
print('Salario Atual: R$ {:.2f}\nNovo Salario: R$ {:.2f}'.format(salario, novo_salario))


