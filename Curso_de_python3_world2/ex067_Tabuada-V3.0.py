""" Desafio 067
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag).
"""


msg = '             TABUADA V3.0            '
m = len(msg)
print('\033[32m' + ('-' * m))
print(f'{msg}')
print(('-' * m) + '\033[m')

while True:
    contagem = 0
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    if tabuada < 0:
        break
    print('-'*20)
    for c in range(11):
        resultado = tabuada * c
        print(f'{tabuada} x {c} = {resultado}')
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
