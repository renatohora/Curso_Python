''''Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e o ultimo nome separadamente.
Ex.: Ana maria de souza
First = Ana
last  = souza'''

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em conhecer voce {}'.format(nome))
print('Seu primeiro nome é {}'.format(nome[0]))        #utilizado 0 para mostrar o primeiro campo digitado.
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))#utilizado len -1 para mostrar o ultimo campo digitado.












#print('O nome digitado foi {}\nPrimeiro nome: {}\n Ultimo nome: {}'.format(nome))