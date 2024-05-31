#Crie um programa que leia quanto dinheiro uma pessoa tem na
#carteira e mostre quantos dolares ela pode comprar.
n = float(input('Digite o valor que deseja converter em em Dolar: R$ '))
dolar = 5.07
conversao = n / dolar
print('Com o valor R${:.2f} e com a cotação atual de {:.2f} é possivel comprar $ {:.2f} dolar(s)'.format(n, dolar, conversao))