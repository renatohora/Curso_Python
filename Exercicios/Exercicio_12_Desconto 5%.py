#Faca um algoritimo que leia o preço de um produto e mostra seu novo valor com 5% de desconto
produto = float(input('Valor do produto: R$ '))
#exemplo abaixo podemoc calcular porcentagem
novo_valor = produto - (produto * 5 / 100)
#print adicionei o \n para quebrar a linha
print('Valor do produto digitado R$ {:.2f}\nDesconto de 5% fica R$ {:.2f}'.format(produto, novo_valor))

