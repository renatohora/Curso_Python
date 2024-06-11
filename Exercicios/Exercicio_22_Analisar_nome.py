''''Crie um programa que leia o nome completo de uma pessoa mostre:
1 - O nome com todas as letras maiusculas
2 - O nome com todas as letras minusculas
3 - Quantas letras ao todo (sem consideirar espaços)
4 - Quantas letras tem o primeiro nome.'''''

#Minha Solução
''''n1 = str(input('Digite o nome completo: '))
maius = n1.upper()      #varivael para deixar todas as letras maiusculas
minus = n1.lower()      #variavel para deixar todas letras minusculas
total = len(n1.strip()) # variavel para contar o nome sem os espaços
primeira = n1.split()   #variavel para dividir o nome

print('O nome digitado foi {}\nLetras maiusculas: {}\nLetras minusculas {}\n'
      'Total de letras: {}\n'                                                #0 entre [] para mostrar a primeira palavra
      'Primeiro nome {} tem {} letras'.format(n1, maius, minus, total, primeira[0], len(primeira[0])))
                                                                                          #utilizei o mesmo principio
                                                                                          #anterior em () e o len para
                                                                                          #contar as letras.'''''

#solução do Curso.
n1 = str(input('Digite o nome completo: ')).strip()
print('Analizando seu nome...')
print('Seu nome em Maiusculas é {}'.format(n1.upper()))
print('Seu nome em Minuscula é {}'.format(n1.lower()))
print('Seu nome tem ao todo {} letras'.format(len(n1) - n1.count(' ')))#logica foi contar o toda string menos os espaços
print('Seu primeiro nome tem {} letras'.format(n1.find(' ')))
separado = n1.split()
print('Seu primeiro nome {} tem {} letras'.format(separado[0], len(separado[0])))





