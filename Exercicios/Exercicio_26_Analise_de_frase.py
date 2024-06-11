''''Faça um programa que leia uma frase pelo teclado e mostre
1 - Quantas vezes aparece a palavra A
2 - Em que posição ela aparece a primeira vez
3 - Em que posição ela aparece a ultima vez'''

frase = str(input('Digite a frase a ser analizada: ')).strip().upper() #utilizando dois parametos para facilitar o print
print('A letra A aparece {} vezes na frase digitada.'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra apareceu pela ultima vez na posição {}'.format(frase.rfind('A')))




