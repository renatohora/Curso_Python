''''Escreva um programa que leia um valor em metros e exiba em centimetros e milimetros'''''
metros = float(input('Digite o valor em metros: '))
cm = metros * 100
mil = metros * 1000
print('Voce digitou o valor em metros de: {:.2f} MTs\nEm Centimetros são: {:.0f} cm\nEm Milimetros são: {:.0f} mm'.format(metros,cm,mil))



