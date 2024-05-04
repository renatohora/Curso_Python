#input solicita a informação
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

#variaveis
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

#show na tela
print('A soma de {} e {} é igual {}'.format(n1, n2, s))
print('A multiplicação de {} vezes {} é igual {}'.format(n1, n2, m))
print('A divisão de {} por {} é igual a {}'.format(n1,n2, d))
print('O resultado inteiro da divisao de {} por {} é {}'.format(n1, n2,di))
print('A potencia de {} e {} é igual {}'.format(n1, n2, e))
