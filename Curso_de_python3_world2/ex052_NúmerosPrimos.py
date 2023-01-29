""" Desafio 052
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

msg = '             Identificador de Números Primos            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

n = int(input('Digite um número: '))

tot = 0

for c in range(1, n+1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso ele NÃO É PRIMO!')
