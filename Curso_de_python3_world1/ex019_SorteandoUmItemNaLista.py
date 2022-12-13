""" Desafio 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido."""

from random import choice

msg = ' Sorteio: um Dentre Quatro '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

# Entrada dos dados dos Alunos:
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

# Função "choice" contendo uma Lista com as variáveis dos dados dos alunos:
st = choice([a1, a2, a3, a4])

print('O aluno escolhido foi ', st)
