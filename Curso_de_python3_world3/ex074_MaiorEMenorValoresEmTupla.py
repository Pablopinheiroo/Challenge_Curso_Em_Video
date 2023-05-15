""" Desafio 074
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
msg = '           TUPLA COM NÚMEROS ALEATÓRIOS           '
m = len(msg)
print('\033[32m' + ('=' * m))
print(f'{msg}')
print(('=' * m) + '\033[m')

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
