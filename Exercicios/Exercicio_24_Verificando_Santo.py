''''Crie uma programa que leia o nome de uma cidade e diga se ela
começa ou nao com o nome SANTO.'''

#Minha Solução
''''
nome = str(input('Digite o nome da Cidade: '))
dividir = nome.split()
first = dividir[0]
padrao = first.upper()
validacao = ('SANTO' in padrao)
print('A cidade {} começa com a palvra Santo?'.format(nome))
print('Verdadeiro ou falso: {}'.format(validacao))'''

#Solução do curso
cid = str(input('Digite o nome da Cidade: ')).strip() #utilizar o strip para eliminar espaços
#utilizar de 0 ou vazio antes do : ate o 5, converter para upper e utilizar o == para verificar se
#na opção anterior digitada é igual a SANTO.
print(cid[:5].upper() == 'SANTO')
