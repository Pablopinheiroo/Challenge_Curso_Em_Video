""" Desafio 061
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""


msg = '             Gerador de PA            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

p1 = int(input('Primeiro Termo: '))
rz = int(input('Razão da PA: '))

contador = 0
somap1 = p1

print(f'{p1} -> ', end='')

while contador < 9:
    contador += 1
    somap1 += rz
    print(f'{somap1} -> ', end='')
print('FIM')
