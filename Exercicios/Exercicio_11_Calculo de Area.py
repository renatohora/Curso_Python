''''Faça um programa que leia a largura e altura de uma parede em metros,
calcula a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que a cada litro de tinta pinta uma
area de 2 metros quadrados.'''''

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da Parade: '))
metragem = altura * largura
tinta = metragem / 2
print('A parede descrita tem {:.2f} metros quadrados'.format(metragem))
print('Para realizar a pintura dessa parede é necessario {:.2f} litros de tinta.'.format(tinta))

