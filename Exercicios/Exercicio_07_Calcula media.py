#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua media

nota1 = float(input('Primeira nota: '))
note2 = float(input('Segunda nota: '))
soma = nota1 + note2
media = soma / 2
print('O aluno obteve as seguintes notas {} e {}.\nSua media foi de {}'.format(nota1,note2,media))
