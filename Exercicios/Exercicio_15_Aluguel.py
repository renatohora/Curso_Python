#Escreve um programa que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelos
#quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 dia e R$ 0,15 o Km rodado.
print('*' * 55)
dias = int (input('Digite quantos dias foram de aluguel do Veiculo: '))
KM = float(input('Quantos KM foram rodados: '))
total = (dias * 60) + (KM * 0.15)
print('*' * 55)
print('Segue informações da Locação')
print('*' * 55)
print('Dias alugagos: {}'.format(dias))
print('KM rodado no periodo {:.0f}'.format(KM))
print('O valor a ser pago na locação é R$ {:.2f}'.format(total))
print('*' * 55)


