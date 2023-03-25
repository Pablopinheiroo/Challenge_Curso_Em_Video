""" Desafio 063
Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""

msg = '             Sequência de Fibonacci            '
m = len(msg)
print('\033[32m' + ('-' * m))
print('{}'.format(msg))
print(('-' * m) + '\033[m')

termos = 0

while termos == 0:
    termos = int(input('Quantos termos você quer mostrar? '))
    print('~~' * 22)
    if termos == 0:
        print('\033[31mErro: INFORME UM NÚMERO VÁLIDO\033[m')
        print('~~' * 22)
    if termos == 1:
        print('0 -> ', end='')
    elif termos >= 2:
        print('0 -> 1 -> ', end='')

n = 2
anterior = soma = 0
while n < termos:
    n += 1
    anterior += 1
    soma += anterior
    print(f'{soma} -> ', end='')
print('FIM')
