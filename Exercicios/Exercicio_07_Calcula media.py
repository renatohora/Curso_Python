#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

nota1 = float(input('Primeira nota: '))
note2 = float(input('Segunda nota: '))
media = (nota1 + note2) / 2
#foi adicionado ao print abaixo uma formataçao que mostra dois digitos apos o . utiliznado :.2f
print('O aluno obteve as seguintes notas {:.2f} e {:.2f}.\nSua media foi de {:.2f}'.format(nota1,note2,media))
