'''Criando um programa de radar'''

carro = float(input('Digite a velocidade do carro: '))
if carro > 80:
    print("Velocidade acima do limite. Voce foi multado em R$ {}")

else:
    print('Velocidade de {} OK. Boa viagem!'.format(carro))
print('Tenha um bom dia! Dirija com segurança')
