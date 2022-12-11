""" Desafio 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa."""

from math import hypot

msg = 'Cálculo da Hipotenusa'
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

co = float(input('Comprimento do Cateto oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))

print('A hipotenusa vai medir {:.2f}'.format(hypot(co, ca)))
