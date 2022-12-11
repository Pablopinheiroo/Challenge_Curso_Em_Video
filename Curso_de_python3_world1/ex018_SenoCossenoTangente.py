""" Desafio 018
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""

from math import cos, sin, tan, radians

msg = 'Identificando o Seno, Cosseno e Tangente'
m = len(msg)
print('-' * m)
print('{}'.format(msg))
print('-' * m)

agl = float(input('Digite o ângulo que você deseja: '))

# Convertendo o ângulo para radianos com a função radians()
agl1 = radians(agl)

# Calculando o Seno, Cosseno e Tangente com as funções da biblioteca math
seno = sin(agl1)
cos = cos(agl1)
tan = tan(agl1)


print('O Ângulo de {} tem o SENO de {:.2f}'.format(agl, seno))
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(agl, cos))
print('O Ângulo de {} tem a TANGENTE de {:.2f}'.format(agl, tan))
