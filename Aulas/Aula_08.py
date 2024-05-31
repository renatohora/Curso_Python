#Importando modulos para Python no pycharm
#library
#Forma de importar
#importar toda a library e importar apenas uma parte da library
# 1 - import 'nome da library'
# 2 - from 'parte da library' 'Nome da library'
#funcionalidade de library math
#ceil      #arrendo para cima os valores
#floor     #arredonda para baixo os valores
#trunc     #vai eleminiar o numero depois da virgula se fazer arredondamento
#pow       #potencia que funciona semelhante aos **
#sqrt      #calcular rais quadrada
#factorial #calcula o valor fatorial
import math
import emoji
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a {}.'.format(num, raiz))
print('A simplificada é {:.2f}.'.format(raiz))
print('A Arredondando para cima é {}.'.format(math.ceil(raiz)))
print('A Arredondando para baixo é {}.'.format(math.floor(raiz)))
#navegar ate o site do python par consultar as library disponiveis para cada versão.
#https://docs.python.org/3.12/library/index.html

print(emoji.emojize('Ola, Mundo :beating_heart:'))
print(emoji.emojize('Python is :globe_showing_europe_africa:',))
