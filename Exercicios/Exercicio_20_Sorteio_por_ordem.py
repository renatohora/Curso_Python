''''O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''''

import random
n1 = str(input('Digite o nome do aluno: '))
n2 = str(input('Digite o nome do aluno: '))
n3 = str(input('Digite o nome do aluno: '))
n4 = str(input('Digite o nome do aluno: '))
lista = [n1, n2, n3, n4]
#utilizei o random.shuffle pra embaralhar os nomes da lista.
random.shuffle(lista)
print(lista)