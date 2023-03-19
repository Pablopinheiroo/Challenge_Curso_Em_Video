""" Desafio 058
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep


msg = '             Jogo da Adivinhação v2.0            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

print('Sou seu computador...')
sleep(0.3)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(0.4)
print('Será que você consegue advinhar qual foi?')
sleep(0.4)

pc = randint(0, 10)  # Sorteia um número entre 0 e 5
tentativas = 1  # Declarando a variável

# Jogador tenta advinhar
pessoa = int(input('Qual é seu palpite? '))

sleep(0.5)
print('PROCESSANDO...')
sleep(1)

while pessoa != pc:
    tentativas += 1
    if pessoa > pc:
        print('Menos... Tente mais uma vez.')
    else:
        print('Mais... Tente mais uma vez.')
    pessoa = int(input('Qual é seu palpite? '))
print(f'PARABÉNS! Você conseguiu me vencer! Contudo precisou de {tentativas} tentativas...')
