""" Desafio 047
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."""

msg = '        Contagem de Números Pares        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

for pares in range(2, 51, 2):
    print(pares, end=' ')
print('Acabou')
