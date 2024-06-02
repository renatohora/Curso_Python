#Crie um programa que leia um numero real qualquer pelo teclado, e mostre na tela a sua porção inteira.
#Digite um numero: 6.127
#O numero 6.127 tem a parte inteira 6.
import math
num = float(input('Digite um numero: '))
print('A parte inteira desse numero é {}'.format(math.floor(num)))