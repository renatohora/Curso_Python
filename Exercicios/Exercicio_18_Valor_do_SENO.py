''''Faça um programa que leia ou angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.'''''

import math
angulo = float(input('Digite o angulo que vc deseja: '))
#para calcular angulo, precisa converter para radiano.
sin = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O angulo digitado foi {:.2f}\nSeno é {:.2f}\nCosseno é {:.2f}\nTangente é {:.2f}'.format(angulo, sin, cos, tan))
#Obs. ao importar apenas os SIN, COS, TAN e RADIOANS precisa tirar a referencia math da frente dos
#comandos acima.