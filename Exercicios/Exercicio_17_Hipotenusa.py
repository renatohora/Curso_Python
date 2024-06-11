''''Faça um programa eu leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,  e calcule
#e mostre o comprimento da hipotenusa.'''''

import math
print('************** Calculando Triangulo Retangulo****************')
oposto = float(input('Digite o comprimento do Cateto Oposto: '))
print('*' * 50)
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print('*' * 50)
print('A hipotenusa do triangulo retangulo é {:.2f}'.format(hipotenusa))
print('*' * 50)

