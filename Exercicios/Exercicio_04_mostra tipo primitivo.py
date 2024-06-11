''''faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo'''''
#n no codigo abaixo é objeto
n = input('Digite algo: ')
#os metodos estao entre parenteres no caso abaixo .is alguma coisa
print('So tem espaços? ', n.isspace())
print('O tipo primitivo desse valor é: ', type(n))
print('É um número?', n.isnumeric())
print('É uma letra?', n.isalpha())
print('Ele tem letras ou números? ', n.isalnum())
print('Esta em letras maisculas? ', n.isupper())
print('Esta em letras minusculas? ', n.islower())
print('O que foi escrito esta capitalizado? ', n.istitle())







