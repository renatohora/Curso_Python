'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada
cada um dos digitos separados:
mostrando:
Unidade
dezena
Centena
Milhar'''

num = int(input('Digite um numero inteiro: '))
n1 = num // 1 % 10
n2 = num // 10 % 10
n3 = num // 100 % 10
n4 = num // 1000 % 10
print('Analizando o numero {}'.format(num))
print('Sua Unidade é {}'.format(n1))
print('Sua Dezena é {}'.format(n2))
print('Sua Centena é {}'.format(n3))
print('Seu Milhar é {}'.format(n4))
