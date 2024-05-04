#Faça um programa que mostra que leia um numero inteiro e mostra seu sucessor e seu antecessor.
n1 = int(input('Digite um numero inteiro: '))
suc = n1 + 1
ant = n1 - 1
print('Voce digitou o numero {}.\nSeu suceesor é {}\ne antecessor é {}'.format(n1, suc, ant))