""" Desafio 025
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome."""

msg = '   Identificador Da Palavra Silva   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

nome = str(input('Qual é seu nome completo? ').upper().strip())
print('Seu nome tem Silva? {}'.format('SILVA' in nome))

