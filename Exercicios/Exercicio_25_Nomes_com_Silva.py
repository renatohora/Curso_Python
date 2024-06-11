''''Crie um programa que leia o nome de uma pessoa e diga se ela
tem SILVA no nome.'''

nome = str(input('Digite o nome completo: '))
padrao = nome.upper()
print('O nome {} contem Silva?'.format(nome))
print('Verdadeio ou falso?')
print('SILVA' in padrao)