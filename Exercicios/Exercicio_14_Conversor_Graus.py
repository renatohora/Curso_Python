''''Crie um programa que leia a graus celsius e converta para fahrenheit'''

celsius = float(input('Digite a tempetura: '))
#Formula para calcular celsius em fahre..(31.5°C × 9/5) + 32 = 88.7°F
conversao = (celsius * 9 / 5) + 32
print('A temperatura {} celsius em fahrenheit correspondem {}F'.format(celsius, conversao))
