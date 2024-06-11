''''Crie um programa que leia um numero real qualquer pelo teclado, e mostre na tela a sua porção inteira.
Digite um numero: 6.127
O numero 6.127 tem a parte inteira 6.
versão importando toda library
adicionar 3 aspas para comentar um trecho inteiro.'''

import math
num = float(input('Digite um numero: '))
                                                    #Nesse caso colocar a referencia math.trunc
print('O numero digitado foi {} e a sua parte inteira é {}'.format(num, math.trunc(num)))
'''
#versã0 importando apenas o trunc.
from math import trunc
num = float(input('Digite um numero: '))
                                                    #nesse caso somente adicionar o trunc
print('O numero digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))
#podemos utilizar o int em frente a variável que tbm funciona segue exemplo abaixo.
#Ex. .format(num, int(num)))
