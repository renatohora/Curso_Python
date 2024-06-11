#pratica.
frase = 'Curso em video Python'
print(frase)
#fatiar
print(frase[3])
print(frase[3:13])
print(frase[:14])
print(frase[1:15:2])
'''#jeito facilitado para criar print de texto longo utilizando 3 aspas antes e depois.
print(In ancient Rome, there was the habit of celebrating the birthday of a person.
There weren’t parties like we know today, but cakes were prepared and offers
were made. Then, the habits of wishing happy birthday, giving gifts and lighting
candles became popular {} as a way to protect the birthday person from devils and
ensure good things to the next year in the person’s life. The celebrations only
became popular like we know today after fourteen centuries, in a collective
festival performed in Germany'''
#count
print(frase.count('o')) #python difere mauiscula de minuscula.
print(frase.count('O')) #no caso nao encontrou letra mauiscula O
#upper ou lower.
print(frase.upper())
print(frase.lower())
#len - conta quantas caracteres.
print(len(frase))         #conta todas as os caracteres incluindo espaços
print(len(frase.split())) #divide a string em palavras.
#replace - troca a string.
print(frase.replace('Python', 'Androide'))  #troca da placa por outra indicada.
                                                        #somente nessa instancia
#para salvar no codigo a mudança do replace precisamos realizar desta forma abaixo
#frase = frase.replace('Python', 'Androide') #nesse caso eu atribuia a frase
#print(frase)                                            #a mundança
##################################################################################
#utilizando a função in para verificar se uma palavra esta a string.
print('Curso' in frase) #retorna o comando com True
print(frase.find('video')) #o comando find mostra a posição que esta a string.
                           #quando nao encontra ele retorna -1
#utilizando o split
print(frase.split()) #retorna a frase com as palavras separadas utilizando aspas e vigula.
#podemos criar uma variavel.
dividido = frase.split()
print(dividido)     #a variavel retorma frase dividida conforme acima.
print(dividido[0])  #com a complemento 0 retorna a primeira palavra da string (Curso)
print(dividido[0][2]) #com a complemento 0 e 2 ele verifica a primeira palavra (Curso), e traz
                      #a letra r que esta na posição 2

print(len(frase.strip()))


