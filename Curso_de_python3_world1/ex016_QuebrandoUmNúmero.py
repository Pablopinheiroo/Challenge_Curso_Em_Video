""" Desafio 016
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
Ex: Digite um número: 6.127 --> O número 6.127 tem a parte Inteira 6. """

from math import trunc
msg = 'Identificador da Porção Inteira'
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

n1 = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}.'.format(n1, trunc(n1)))
