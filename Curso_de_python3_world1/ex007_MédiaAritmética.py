""" Desafio 007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média."""

msg = 'Para saber a média da sua Nota'
m = len(msg)
print('-'*m)
print('{}'.format(msg))
print('-'*m)

nota1 = float(input('Informe sua Primeira Nota: '))
nota2 = float(input('Informe sua Segunda Nota: '))

print('Nota 1º = {:.1f} pts.\nNota 2º = {:.1f} pts.\nSua Média é igual a {:.1f} pontos.'.format(nota1, nota2, (nota1+nota2)/2))
