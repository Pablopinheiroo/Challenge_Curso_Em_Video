""" Desafio 028
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""

from random import randint
from time import sleep

msg = 'Vou pensar em um número entre 0 e 5. tente advinhar...'

print('-=' * 27)
print('{}'.format(msg))
print('-=' * 27)

# Sorteia um número entre 0 e 5
pc = randint(0, 5)

# Jogador tenta advinhar
pessoa = int(input('Em que número eu pensei? '))

sleep(0.5)
print('PROCESSANDO...')
sleep(1)

if pessoa == pc:
    print('PARABÉNS! Você conseguiu me vencer!'.format())
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(pc, pessoa))
