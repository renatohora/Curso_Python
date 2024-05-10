#Faca um algoritimo que leia o preço de um produto e mostra seu novo valor com 5% de desconto

produto = float(input('Valor do produto: '))
novo_valor = produto - ((produto / 100) * 5)
print('Produto digitado custa R${:.2f}\nDesconto de 5% fica R${:.2f}'.format(produto, novo_valor))

