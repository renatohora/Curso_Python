#Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo
#o nome deles e escrevendo o nome do escolhido na tela.
import random
nome1= input('Digite o nome do primeiro aluno: ')
nome2= input('Digite o nome do segundo aluno: ')
nome3= input('Digite o nome do terceiro aluno: ')
nome4= input('Digite o nome do Quarto aluno: ')
lista = list(nome1, nome2, nome3, nome4)
sorteado = random.Random(lista)
print('=' * 30)
print('Nomes digitados foram:')
print('{}\n{}\n{}\n{}\n'.format(nome1, nome2, nome3, nome4))
print('O nome sorteado foi {}'.format(sorteado))


