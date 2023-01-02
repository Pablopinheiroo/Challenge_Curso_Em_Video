""" Desafio 046
Faça um programa que mostre na tela uma contagem regressiva
para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""

from time import sleep

msg = '        Contagem Regressiva        '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

for c in range(10, -1, -1):
    print(c)
    sleep(0.6)
print('BUM! ', end='')
sleep(0.6)
print('BUM! ', end='')
sleep(0.4)
print('POOW!')
sleep(0.5)
