''''teste  Jogo da Adivinhação v.1.0'''

from random import randint #importei uma função do random
from time import sleep

computador = randint(1, 5) #um random de 1 a 5
print('-=-' * 20)
print('Vou pensar em um numero entre 1 e 5 tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Ok eu acho oque vc pensou no: ')) #vc tenta adivinha qual o numero
print('processando.....')
sleep(2)
if jogador == computador:
    print(f'PARABENS! voce acertou! Eu havia pensado {computador} o mesmo oque vc!')
else:
    print(f'EROOOOOU! O mumero correto foi {computador}!')








