#Escreva um programa que leia um valor em metros e exiba em centimetros e milimetros
metros = float(input('Digite o valor em metros: '))
cm = int(metros * 100)
mil = int(metros * 1000)
print('Voce digitou o valor de {}\nMetragem em CM {}\nMetragem em milimetro {}'.format(metros,cm,mil))



