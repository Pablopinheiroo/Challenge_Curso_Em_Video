""" Desafio 024
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"."""

msg = '   Identificando se a Cidade Começa com Santo   '
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

cidade = (input('Em que cidade você nasceu?: ').upper().split())
print('SANTO' in cidade[0])
