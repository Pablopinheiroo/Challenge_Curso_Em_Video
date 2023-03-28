""" Desafio 067
 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

msg = '             Vamos Jogar Par ou Ímpar            '
m = len(msg)
print('\033[32m' + ('-' * m))
print(f'{msg}')
print(('-' * m) + '\033[m')

n_vez = 0
while True:
    disputa = ' '
    pessoa = int(input('Digite um valor: '))
    while disputa not in 'PIÍ':
        disputa = str(input('Par ou Ímpar [P/I] ')).strip().upper()[0]
    pc = randint(0, 10)
    resultado = pessoa + pc
    valor = 'DEU PAR' if resultado % 2 == 0 else 'DEU ÍMPAR'

    print('--' * 20)
    print(f'Você jogou {pessoa} e o computador {pc}. Total de {resultado} {valor}')
    print('--' * 20)

    if (disputa in 'P' and valor == 'DEU PAR') or (disputa in 'IÍ' and valor == 'DEU ÍMPAR'):
        n_vez += 1
        print('\033[32mVocê VENCEU!\033[m')
        print('Vamos jogar novamente...')
        print('=-' * 20)
    else:
        print('\033[31mVocê PERDEU!\033[m')
        print('=-' * 20)
        break

print(f'\033[31mGAME OVER! Você venceu {n_vez} vezes.\033[m')
